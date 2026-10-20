#!/usr/bin/env python3
"""Read-only structural and declared-state checks for a Jimeng video plan."""

from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path
from typing import Any


SCOPE = "structural_and_declared_state_only"
TIME_TOLERANCE = 1e-6
RATIO_PATTERN = re.compile(r"^[1-9][0-9]*:[1-9][0-9]*$")
ASSET_FILE_ERRORS = {"ASSET_FILE_MISSING", "ASSET_NOT_REGULAR_FILE"}
INCOMING_TYPES = {"continuous", "cut", "ellipsis"}


def _is_finite_number(value: Any) -> bool:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    try:
        return math.isfinite(value)
    except OverflowError:
        return False


def _base_result() -> dict[str, Any]:
    return {
        "structural_valid": False,
        "asset_ready": False,
        "errors": [],
        "warnings": [],
        "pending_assets": [],
        "scope": SCOPE,
        "visual_or_video_quality_verified": False,
    }


def _add_issue(
    result: dict[str, Any],
    bucket: str,
    code: str,
    message: str,
    shot: str | None = None,
) -> None:
    issue: dict[str, str] = {"code": code, "message": message}
    if shot is not None:
        issue["shot"] = shot
    result[bucket].append(issue)


def check_plan(plan: Any, plan_dir: Path) -> dict[str, Any]:
    """Validate plan structure, timeline, declared continuity, and asset paths."""
    result = _base_result()
    errors = result["errors"]
    warnings = result["warnings"]
    asset_ready = True

    if not isinstance(plan, dict):
        _add_issue(result, "errors", "PLAN_ROOT_TYPE", "计划根节点必须是 JSON 对象。")
        return result

    required_root_fields = ("duration_s", "ratio", "locked_state_keys", "assets", "shots")
    for field in required_root_fields:
        if field not in plan:
            _add_issue(result, "errors", "FIELD_REQUIRED", f"缺少根字段 {field}。")

    duration = plan.get("duration_s")
    duration_valid = _is_finite_number(duration) and duration > 0
    if "duration_s" in plan:
        if isinstance(duration, bool) or not isinstance(duration, (int, float)):
            _add_issue(result, "errors", "DURATION_TYPE", "duration_s 必须是有限数值，不能是布尔值。")
        elif not _is_finite_number(duration):
            _add_issue(result, "errors", "NUMBER_NOT_FINITE", "duration_s 必须是有限数值。")
        elif duration <= 0:
            _add_issue(result, "errors", "DURATION_NOT_POSITIVE", "duration_s 必须大于 0。")

    ratio = plan.get("ratio")
    if "ratio" in plan:
        if not isinstance(ratio, str) or RATIO_PATTERN.fullmatch(ratio) is None:
            _add_issue(result, "errors", "RATIO_INVALID", "ratio 必须是两个正整数组成的 A:B。")

    locked_keys = plan.get("locked_state_keys")
    if "locked_state_keys" in plan:
        if not isinstance(locked_keys, list) or any(not isinstance(key, str) or not key for key in locked_keys):
            _add_issue(result, "errors", "LOCKED_KEYS_TYPE", "locked_state_keys 必须是非空字符串组成的数组。")
            locked_keys = []
        else:
            seen_locked_keys: set[str] = set()
            for key in locked_keys:
                if key in seen_locked_keys:
                    _add_issue(result, "warnings", "LOCKED_KEY_DUPLICATE", f"锁定键 {key} 重复声明。")
                seen_locked_keys.add(key)

    raw_assets = plan.get("assets")
    assets: list[Any]
    if isinstance(raw_assets, list):
        assets = raw_assets
    else:
        assets = []
        asset_ready = False
        if "assets" in plan:
            _add_issue(result, "errors", "ASSETS_TYPE", "assets 必须是数组。")

    asset_by_id: dict[str, dict[str, Any]] = {}
    valid_asset_records: list[tuple[dict[str, Any], str | None]] = []
    for index, asset in enumerate(assets):
        if not isinstance(asset, dict):
            _add_issue(result, "errors", "ASSET_TYPE", f"assets[{index}] 必须是对象。")
            asset_ready = False
            continue

        for field in ("id", "path", "status", "role", "preserve", "exclude"):
            if field not in asset:
                _add_issue(result, "errors", "ASSET_FIELD_REQUIRED", f"素材项 {index} 缺少字段 {field}。")

        asset_id = asset.get("id")
        valid_id = isinstance(asset_id, str) and bool(asset_id.strip())
        if "id" in asset and not valid_id:
            _add_issue(result, "errors", "ASSET_ID_INVALID", f"素材项 {index} 的 id 必须是非空字符串。")
        if valid_id:
            if asset_id in asset_by_id:
                _add_issue(result, "errors", "DUPLICATE_ASSET_ID", f"素材 id {asset_id} 重复。")
                asset_ready = False
            else:
                asset_by_id[asset_id] = asset

        path_value = asset.get("path")
        path_valid = isinstance(path_value, str) and bool(path_value.strip())
        if "path" in asset and not path_valid:
            _add_issue(result, "errors", "ASSET_PATH_INVALID", f"素材 {asset_id or index} 的 path 必须是非空字符串。")

        status = asset.get("status")
        status_valid = status in {"available", "planned"} if isinstance(status, str) else False
        if "status" in asset and not status_valid:
            _add_issue(result, "errors", "ASSET_STATUS_INVALID", f"素材 {asset_id or index} 的 status 必须是 available 或 planned。")
            asset_ready = False

        for field in ("role",):
            if field in asset and (not isinstance(asset[field], str) or not asset[field].strip()):
                _add_issue(result, "errors", "ASSET_FIELD_TYPE", f"素材 {asset_id or index} 的 {field} 必须是非空字符串。")
        for field in ("preserve", "exclude"):
            if field in asset and (
                not isinstance(asset[field], list)
                or any(not isinstance(item, str) for item in asset[field])
            ):
                _add_issue(result, "errors", "ASSET_FIELD_TYPE", f"素材 {asset_id or index} 的 {field} 必须是字符串数组。")

        resolved_path: str | None = None
        if path_valid and status_valid:
            candidate = Path(path_value)
            if not candidate.is_absolute():
                candidate = plan_dir / candidate
            try:
                resolved_path = str(candidate.resolve(strict=False))
            except (OSError, RuntimeError):
                resolved_path = str(candidate)

            if status == "planned":
                asset_ready = False
                if valid_id:
                    result["pending_assets"].append(asset_id)
                _add_issue(result, "warnings", "ASSET_PLANNED", f"素材 {asset_id or index} 标记为待制作。")
            elif status == "available":
                try:
                    is_regular_file = candidate.is_file()
                    exists = candidate.exists()
                except OSError:
                    is_regular_file = False
                    exists = False
                if not exists:
                    asset_ready = False
                    _add_issue(result, "errors", "ASSET_FILE_MISSING", f"素材 {asset_id or index} 标记为 available，但文件不存在：{path_value}。")
                elif not is_regular_file:
                    asset_ready = False
                    _add_issue(result, "errors", "ASSET_NOT_REGULAR_FILE", f"素材 {asset_id or index} 标记为 available，但路径不是普通文件：{path_value}。")
        elif not status_valid or not path_valid:
            asset_ready = False

        if valid_id:
            valid_asset_records.append((asset, resolved_path))

    raw_shots = plan.get("shots")
    if isinstance(raw_shots, list):
        shots = raw_shots
    else:
        shots = []
        if "shots" in plan:
            _add_issue(result, "errors", "SHOTS_TYPE", "shots 必须是数组。")

    if not shots and isinstance(raw_shots, list):
        _add_issue(result, "errors", "SHOTS_EMPTY", "shots 至少需要包含一个镜头。")

    normalized_shots: list[dict[str, Any]] = []
    seen_shot_ids: set[str] = set()
    for index, shot in enumerate(shots):
        if not isinstance(shot, dict):
            _add_issue(result, "errors", "SHOT_TYPE", f"shots[{index}] 必须是对象。")
            normalized_shots.append({"id": None, "start": None, "end": None, "start_state": {}, "end_state": {}, "incoming_type": None})
            continue

        for field in ("id", "start_s", "end_s", "asset_ids"):
            if field not in shot:
                _add_issue(result, "errors", "SHOT_FIELD_REQUIRED", f"镜头 {index} 缺少字段 {field}。")

        shot_id = shot.get("id")
        if not isinstance(shot_id, str) or not shot_id.strip():
            if "id" in shot:
                _add_issue(result, "errors", "SHOT_ID_INVALID", f"镜头 {index} 的 id 必须是非空字符串。")
            shot_id = None
        elif shot_id in seen_shot_ids:
            _add_issue(result, "errors", "DUPLICATE_SHOT_ID", f"镜头 id {shot_id} 重复。", shot_id)
        else:
            seen_shot_ids.add(shot_id)

        times: dict[str, int | float | None] = {"start_s": None, "end_s": None}
        for field in ("start_s", "end_s"):
            value = shot.get(field)
            if field not in shot:
                continue
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                _add_issue(result, "errors", "SHOT_TIME_TYPE", f"镜头 {shot_id or index} 的 {field} 必须是有限数值，不能是布尔值。", shot_id)
            elif not _is_finite_number(value):
                _add_issue(result, "errors", "NUMBER_NOT_FINITE", f"镜头 {shot_id or index} 的 {field} 必须是有限数值。", shot_id)
            else:
                times[field] = value
        start = times["start_s"]
        end = times["end_s"]
        if start is not None and end is not None and end <= start:
            _add_issue(result, "errors", "SHOT_DURATION_INVALID", f"镜头 {shot_id or index} 的 end_s 必须大于 start_s。", shot_id)

        asset_ids = shot.get("asset_ids")
        if "asset_ids" in shot:
            if not isinstance(asset_ids, list) or any(not isinstance(ref, str) for ref in asset_ids):
                _add_issue(result, "errors", "SHOT_ASSET_IDS_TYPE", f"镜头 {shot_id or index} 的 asset_ids 必须是字符串数组。", shot_id)
                asset_ready = False
            else:
                seen_refs: set[str] = set()
                for ref in asset_ids:
                    if ref in seen_refs:
                        _add_issue(result, "warnings", "ASSET_REFERENCE_DUPLICATE", f"镜头重复引用素材 {ref}。", shot_id)
                    seen_refs.add(ref)
                    if ref not in asset_by_id:
                        asset_ready = False
                        _add_issue(result, "errors", "ASSET_REFERENCE_UNKNOWN", f"镜头引用了未声明的素材 id {ref}。", shot_id)

        states: dict[str, dict[str, Any]] = {}
        for field in ("start_state", "end_state"):
            state = shot.get(field)
            if field not in shot:
                _add_issue(result, "warnings", "SHOT_STATE_MISSING", f"镜头 {shot_id or index} 未声明 {field}。", shot_id)
                states[field] = {}
            elif not isinstance(state, dict):
                _add_issue(result, "errors", "SHOT_STATE_TYPE", f"镜头 {shot_id or index} 的 {field} 必须是对象。", shot_id)
                states[field] = {}
            else:
                states[field] = state
                if not state:
                    _add_issue(result, "warnings", "SHOT_STATE_MISSING", f"镜头 {shot_id or index} 的 {field} 未声明具体状态。", shot_id)

        incoming_type: str | None = None
        incoming = shot.get("incoming")
        if index > 0 and "incoming" not in shot:
            _add_issue(result, "errors", "SHOT_INCOMING_REQUIRED", f"镜头 {shot_id or index} 缺少 incoming.type。", shot_id)
        elif "incoming" in shot:
            if not isinstance(incoming, dict):
                _add_issue(result, "errors", "SHOT_INCOMING_TYPE", f"镜头 {shot_id or index} 的 incoming 必须是对象。", shot_id)
            else:
                incoming_type_value = incoming.get("type")
                if index > 0 and "type" not in incoming:
                    _add_issue(result, "errors", "SHOT_INCOMING_REQUIRED", f"镜头 {shot_id or index} 缺少 incoming.type。", shot_id)
                elif "type" in incoming:
                    if not isinstance(incoming_type_value, str) or incoming_type_value not in INCOMING_TYPES:
                        _add_issue(result, "errors", "SHOT_INCOMING_TYPE", f"镜头 {shot_id or index} 的 incoming.type 必须是 continuous、cut 或 ellipsis。", shot_id)
                    else:
                        incoming_type = incoming_type_value
                if incoming_type in {"cut", "ellipsis"}:
                    reason = incoming.get("reason")
                    if not isinstance(reason, str) or not reason.strip():
                        _add_issue(result, "errors", "SHOT_INCOMING_REASON_REQUIRED", f"镜头 {shot_id or index} 的 {incoming_type} 必须说明接法或省略内容。", shot_id)
                elif "reason" in incoming and not isinstance(incoming["reason"], str):
                    _add_issue(result, "errors", "SHOT_INCOMING_REASON_TYPE", f"镜头 {shot_id or index} 的 incoming.reason 必须是字符串。", shot_id)

        normalized_shots.append(
            {
                "id": shot_id,
                "start": start,
                "end": end,
                "start_state": states["start_state"],
                "end_state": states["end_state"],
                "incoming_type": incoming_type,
            }
        )

    # Check the declared timeline in the supplied order. Small floating-point
    # differences up to the documented tolerance are accepted.
    previous_end: int | float | None = None
    for index, shot in enumerate(normalized_shots):
        start = shot["start"]
        end = shot["end"]
        shot_id = shot["id"]
        if start is None or end is None:
            previous_end = end if end is not None else previous_end
            continue
        if duration_valid and (start < -TIME_TOLERANCE or end > duration + TIME_TOLERANCE):
            _add_issue(result, "errors", "SHOT_OUT_OF_BOUNDS", f"镜头 {shot_id or index} 超出 0 到 duration_s 的范围。", shot_id)
        expected_start = 0 if index == 0 else previous_end
        if expected_start is not None:
            delta = start - expected_start
            if delta > TIME_TOLERANCE:
                _add_issue(result, "errors", "SHOT_TIMELINE_GAP", f"镜头 {shot_id or index} 与前一时间点之间有空隙。", shot_id)
            elif delta < -TIME_TOLERANCE:
                _add_issue(result, "errors", "SHOT_TIMELINE_OVERLAP", f"镜头 {shot_id or index} 与前一时间点重叠。", shot_id)
        previous_end = end

    if normalized_shots and duration_valid:
        final_end = normalized_shots[-1]["end"]
        if final_end is not None:
            delta = duration - final_end
            if delta > TIME_TOLERANCE:
                _add_issue(result, "errors", "SHOT_TIMELINE_GAP", "最后一个镜头结束早于 duration_s。")
            elif delta < -TIME_TOLERANCE:
                _add_issue(result, "errors", "SHOT_TIMELINE_OVERLAP", "最后一个镜头结束晚于 duration_s。")

    # Continuous boundaries compare only fields explicitly declared on both
    # sides. Missing comparisons remain warnings; they are not physical proof.
    for index in range(1, len(normalized_shots)):
        current = normalized_shots[index]
        previous = normalized_shots[index - 1]
        if current["incoming_type"] != "continuous":
            continue
        shared_keys = set(previous["end_state"]) & set(current["start_state"])
        if not shared_keys:
            _add_issue(result, "warnings", "CONTINUITY_UNSPECIFIED", "连续镜头两侧没有共同声明的状态键，无法核对状态衔接。", current["id"])
        for key in sorted(shared_keys):
            if previous["end_state"][key] != current["start_state"][key]:
                _add_issue(result, "errors", "CONTINUITY_STATE_CONFLICT", f"连续镜头边界的状态键 {key} 前后不一致。", current["id"])

    if isinstance(locked_keys, list):
        for key in locked_keys:
            declared_values: list[tuple[Any, str | None]] = []
            for shot in normalized_shots:
                for state_name in ("start_state", "end_state"):
                    state = shot[state_name]
                    if key in state:
                        declared_values.append((state[key], shot["id"]))
            if not declared_values:
                _add_issue(result, "warnings", "LOCKED_STATE_UNDECLARED", f"全片没有明确声明锁定键 {key} 的值。")
                continue
            first_value = declared_values[0][0]
            for value, shot_id in declared_values[1:]:
                if value != first_value:
                    _add_issue(result, "errors", "LOCKED_STATE_CONFLICT", f"锁定键 {key} 在全片出现不同的已声明值。", shot_id)
                    break

    result["structural_valid"] = not any(issue["code"] not in ASSET_FILE_ERRORS for issue in errors)
    result["asset_ready"] = asset_ready
    return result


def _reject_nonstandard_constant(value: str) -> None:
    raise ValueError(f"非标准 JSON 数值常量：{value}")


def load_and_check(plan_path: Path) -> dict[str, Any]:
    try:
        text = plan_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        result = _base_result()
        _add_issue(result, "errors", "PLAN_READ_ERROR", f"无法读取计划文件：{exc}。")
        return result

    try:
        plan = json.loads(text, parse_constant=_reject_nonstandard_constant)
    except (json.JSONDecodeError, ValueError) as exc:
        result = _base_result()
        _add_issue(result, "errors", "PLAN_JSON_INVALID", f"计划文件不是合法 JSON：{exc}。")
        return result

    return check_plan(plan, plan_path.parent)


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        result = _base_result()
        _add_issue(result, "errors", "CLI_ARGUMENTS", "用法：python3 check_plan.py PLAN.json。")
    else:
        result = load_and_check(Path(args[0]))

    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
