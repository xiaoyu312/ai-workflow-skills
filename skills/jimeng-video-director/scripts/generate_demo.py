from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
PAYLOAD = {'classification': 'synthetic_demo', 'label': '模拟数据 DEMO', 'seed': 'jimeng-video-director-demo-v1', 'duration_s': 4, 'ratio': '16:9', 'locked_state_keys': ['object_id'], 'assets': [{'id': 'BOX', 'path': 'planned/box-reference.png', 'status': 'planned', 'role': 'object', 'preserve': ['geometry'], 'exclude': ['background']}], 'shots': [{'id': 'S1', 'start_s': 0, 'end_s': 2, 'asset_ids': ['BOX'], 'start_state': {'object_id': 'DEMO-BOX', 'lid': 'closed'}, 'end_state': {'object_id': 'DEMO-BOX', 'lid': 'closed'}}, {'id': 'S2', 'start_s': 2, 'end_s': 4, 'asset_ids': ['BOX'], 'incoming': {'type': 'cut', 'reason': 'synthetic view change'}, 'start_state': {'object_id': 'DEMO-BOX', 'lid': 'closed'}, 'end_state': {'object_id': 'DEMO-BOX', 'lid': 'closed'}}]}

REGRESSION_CASES = [{'id': 'synthetic-pending', 'input': '计划结构通过，盒子参考图仍为 planned。是否已完成视频验收？', 'expected': '仅结构有效；素材待制作；视频质量未验证。'}, {'id': 'synthetic-state-conflict', 'input': '上一镜盒盖关闭，下一连续镜头突然开启，未注明操作或省略。', 'expected': '指出声明状态不连续，补动作或明确剪辑省略。'}]

def main():
    destination = ROOT / "examples" / 'demo.json'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "examples/regression-cases.json").write_text(json.dumps(REGRESSION_CASES, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
