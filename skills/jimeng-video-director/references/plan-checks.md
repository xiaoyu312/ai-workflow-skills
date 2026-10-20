# 本地计划检查

仅在批量或复杂连续性计划需要机器检查时采用此格式。简单提示词、纯诊断或单镜不必转换 JSON。

一份计划对应一支影片或一个连续片段。两个独立方案分别检查，不把 D/G 不同服装强锁进同一条时间轴。

## 命令

```bash
python3 scripts/check_plan.py /absolute/path/plan.json
```

仅使用 Python 3 标准库；读取计划与参考路径，不上传、不联网、不改输入、不生成媒体。相对素材路径以计划文件所在目录为起点；绝对路径也可用。

## 数据字段

| 字段 | 内容 |
|---|---|
| `duration_s` | 本次检查时间轴的总秒数，有限正数。明确它是成片区间还是某生成段；不要混用。 |
| `ratio` | 正整数比例，例如 `9:16` 或 `16:9`。检查格式，不验证图片像素。 |
| `locked_state_keys` | 全片确实不变的状态键，例如人物 ID、包材几何版本。持物手、构图等需要改变的字段不要无条件锁死。可以为空数组。 |
| `assets` | 每项有唯一 `id`、`path`、`status`、`role`、字符串数组 `preserve` 与 `exclude`。 |
| `status` | `available` 表示文件应存在；`planned` 表示待制作，即使将来路径已有文件，也不能直接视为已核对可用。 |
| `shots` | 按实际时间顺序列出，不自动重新排序。每项含 `id`、`start_s`、`end_s`、`asset_ids`。 |
| `start_state`／`end_state` | 可选的状态对象，例如 `held_by`、`contact`、`person_id`、`product_geometry`。未看见的状态不要编成已知值；缺项产生提醒。 |
| `incoming` | 第二镜起必须写 `type`：`continuous`、`cut` 或 `ellipsis`；后两者还须 `reason`。 |

同一影片内 ID 唯一；时间从 0 连续覆盖到总时长，允许 `1e-6` 秒数值误差。连续接法比较两端共同明确的状态键；普通切镜／省略允许非锁定状态变化，但仍检查全片锁定键。

示例见 [demo.json](../examples/demo.json)。其中参考图明确为待制作，所以预期结构通过、素材未齐备；它不是已完成的生成包。

## 返回结果怎么读

- `structural_valid`：结构、时间轴、引用与声明状态是否存在错误。文件缺失单独反映在 `asset_ready` 及错误列表，因此二者都要看。
- `asset_ready`：声明素材是否全部存在且无待制作项；仅检查文件路径，不识别图片内容、分辨率、修订版本或真实可上传性。
- `errors`：结构、时间、引用、缺文件或显式状态冲突。命令退出码为 1。
- `warnings`／`pending_assets`：未声明状态、重复引用或待制作素材等。没有错误时退出码为 0，即使素材仍未齐备。
- `visual_or_video_quality_verified` 始终为 `false`。任何返回组合都不能替代人工图像检查、平台预检或用户验收。

检查器不解析自然语言来判定肌肤接触或空间是否真实；`contact:false` 写在 JSON 中也不能证明图片里没有接触。它能阻止前后声明冲突，不能证明声明与图片相符。

## 维护时验证

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

这些测试检验检查器实际拒绝错位时间、漏素材、错误手位和锁定身份变化等行为。它们不是视频效果测试。

Skill 行为回归问题见 [synthetic regression cases](../examples/regression-cases.json)。独立前向试用时只给评估者请求、Skill 和最少原始资料，先收集实际输出，再用期望项评价，不先泄露答案。需付费生成的效果测试另行遵循用户授权；文字试用不能宣称视频提升。
