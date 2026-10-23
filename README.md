[简体中文](README.md) · [English](README.en.md) · [日本語](README.ja.md)

# AI Workflow Skills

作者的项目：[FateClear](https://fateclear.com) · [X 项目更新](https://x.com/liu_xiaoyu27334)

11 个面向内容创作、AI 视频、电商运营、产品交付和决策支持的可复用工作流。每个目录包含 `SKILL.md` 指令、必要模板及使用说明，供兼容宿主读取。公开版按逐项来源和隐私边界整理；具体能力与原私有版本的差异见各包 README。

## 从一个具体任务开始

先选一项工作流，完整保留该目录，让能读取 Markdown 的助手先读其中的 `SKILL.md`，再提供自己的授权输入。宿主安装与调用方式不同；本仓库不提供模型或一键安装器。

| 想交付什么 | 可先查看的合成输入或样稿 |
| --- | --- |
| 有事实依据的产品介绍 | [品牌文案：虚构三格收纳盒](skills/brand-copywriting/examples/synthetic-product.md) |
| 拍摄前的镜头计划 | [镜头简报：4 秒纸盒打开](skills/jimeng-shot-director/examples/brief.json) |
| 指标与证据分层的复盘 | [广告周报：合成金额与 ROI 复算](skills/tmall-wanxiang-weekly-review/examples/demo.json) |
| 能验收的 AI 交付方案 | [只读库存问答：评测与权限边界](skills/ai-product-field-delivery/examples/synthetic-request.md) |

这些是仓库已有的独立合成文本或数据，不是客户案例、运行截图或效果成绩。操作指令、模板和部分示例仍以中文为主；三语 README 不代表已完成工作流日文化或验证日文生成质量。

## 选择工作流

| Skill | 能力与公开范围 |
| --- | --- |
| [中文写作轻改](skills/wang-xiaobo-writing/README.md) · [日本語](docs/ja/wang-xiaobo-writing/README.md) | 保留事实和个人口气；精简版不含书籍章节映射、文风机制归纳或个人资料 |
| [即梦视频导演](skills/jimeng-video-director/README.md) | 镜头计划、参考分工、连续性和回片检查；保留 MIT 上游归属 |
| [天猫万相台周复盘](skills/tmall-wanxiang-weekly-review/README.md) | 口径、复算、证据分层与行动方案；不含连接器、业务数据或私有报告生成器 |
| [参考视频结构迁移](skills/benchmark-script-adapter/README.md) | 通用拆解流程和空白输出模板；不含品牌事实库、成片语料或素材 |
| [经营看板设计系统](skills/operations-dashboard-design/README.md) | CSS tokens、设计约束和独立合成预览；不含原品牌看板或数据 |
| [镜头设计与回片检查](skills/jimeng-shot-director/README.md) | 参考职责、镜头动作与相机关系、连续性、镜头卡与回片诊断；不附案例媒体或提示词语料 |
| [千川短视频脚本](skills/qianchuan-script-creator/README.md) | 商品事实核对、脚本分流、分镜和单变量迭代；不依赖课程知识库 |
| [品牌文案工作台](skills/brand-copywriting/README.md) | 需求简报、证据与卖点、原创交付模板和校对；不附课程摘录 |
| [AI 产品现场交付](skills/ai-product-field-delivery/README.md) | 任务界定、评测设计、发布计划与运行复盘；使用独立表单，不附书稿框架摘要 |
| [职场沟通与行动](skills/gandepiaoliang-career-coach/README.md) | 目标、角色、决策权、沟通方案与阶段成果；不附书籍章节和攻略映射 |
| [个人决策与复盘](skills/laoyu-life-coach/README.md) | 选项、风险、小步试验与复盘；不附课程地图、转写或语料 |

## 使用

将所需 `skills/<name>/` 目录完整复制到宿主支持的 Skill 目录，或直接要求助手读取该目录中的 `SKILL.md`。安装路径与调用方式以宿主为准。各包 README 提供合成输入和检查命令。

不需要为这个仓库创建 API 密钥；本仓库不附连接器，也不会自动发布内容或使用付费服务。实际任务的输入和工具权限由使用者提供。

## 验证边界

源码公开准备阶段记录了本地结构、引用和合成用例检查。视频导演 13 项、周复盘/结构迁移/设计系统各 4 项测试通过；写作包检查了精确文件清单、14 个引用和 2 个合成样例。未验证模型行为质量、真实平台、真实业务效果或浏览器视觉效果。静态检查不保证所有模型均能正确执行流程。

新增六包还接受独立合成任务检查；具体检查范围和未验证事项见各包 README。未承诺完整保留私有版本的方法体系或效果。

本次三语文档整理未重新运行上述功能测试。写作包的静态检查要求固定文件清单、只接受包内链接；因此该包日文介绍放在仓库级 `docs/ja/`，由本索引提供入口，包内只保留中英互链。作者外链由仓库级文档承接，测试源码未改。

所有示例都是独立合成数据。可用 `python3 -B scripts/generate_all_examples.py` 重现公开示例；不会读取业务文件或联网。

## 许可

自写部分采用 [MIT](LICENSE)。逐包的 `LICENSE-STATUS.md` 和 `THIRD_PARTY_NOTICES.md` 说明范围；即梦视频导演保留上游 MIT 全文。MIT 不覆盖第三方品牌、书籍、课程、媒体或用户输入的内容。

新增六包保留可确认自写的流程，或补充独立编写的通用模板。历史来源按各包说明署名；受限原材料未收录，署名与本仓库 MIT 均不授予这些材料的再分发权。旧目录名仅用于兼容，不代表原作者或平台的官方版本。

欢迎试试 [FateClear](https://fateclear.com) 的免费生日排盘与解读，也可以在 [X](https://x.com/liu_xiaoyu27334) 关注我的新项目和后续更新。
