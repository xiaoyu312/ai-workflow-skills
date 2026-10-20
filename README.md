# AI Workflow Skills

[English](README.en.md)

面向内容创作、AI 视频制作和电商运营的可复用工作流。这里仅包含已完成本地来源、隐私和文件检查的通用版本；不是全部私有 Skills 的完整镜像。

| Skill | 能力与公开范围 |
| --- | --- |
| [中文写作轻改](skills/wang-xiaobo-writing/README.md) | 保留事实和个人口气；精简版不含书籍章节映射、文风机制归纳或个人资料 |
| [即梦视频导演](skills/jimeng-video-director/README.md) | 镜头计划、参考分工、连续性和回片检查；保留 MIT 上游归属 |
| [天猫万相台周复盘](skills/tmall-wanxiang-weekly-review/README.md) | 口径、复算、证据分层与行动方案；不含连接器、业务数据或私有报告生成器 |
| [参考视频结构迁移](skills/benchmark-script-adapter/README.md) | 通用拆解流程和空白输出模板；不含品牌事实库、成片语料或素材 |
| [经营看板设计系统](skills/operations-dashboard-design/README.md) | CSS tokens、设计约束和独立合成预览；不含原品牌看板或数据 |

## 使用

将所需 `skills/<name>/` 目录完整复制到宿主支持的 Skill 目录，或直接要求助手读取该目录中的 `SKILL.md`。安装路径与调用方式以宿主为准。各包 README 提供合成输入和检查命令。

不需要为这个仓库创建 API 密钥；本仓库不附连接器，也不会自动发布内容或使用付费服务。实际任务的输入和工具权限由使用者提供。

## 验证边界

本地结构、引用和合成用例已检查。视频导演 13 项、周复盘/结构迁移/设计系统各 4 项测试通过；写作包检查了精确文件清单、14 个引用和 2 个合成样例。未验证模型行为质量、真实平台、真实业务效果或浏览器视觉效果。静态检查不保证所有模型均能正确执行流程。

所有示例都是独立合成数据。可用 `python3 -B scripts/generate_public_examples.py` 重现公开示例；不会读取业务文件或联网。

## 许可

自写部分采用 [MIT](LICENSE)。逐包的 `LICENSE-STATUS.md` 和 `THIRD_PARTY_NOTICES.md` 说明范围；即梦视频导演保留上游 MIT 全文。MIT 不覆盖第三方品牌、书籍、课程、媒体或用户输入的内容。

授权未清的课程/书籍衍生 Skills 和镜头导演旧版没有收录；不要把本仓库视为这些材料的再分发授权。
