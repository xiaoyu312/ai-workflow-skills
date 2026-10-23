[简体中文](README.md) · [English](README.en.md) · [日本語](README.ja.md)

# 短视频结构迁移


作者的项目：[FateClear](https://fateclear.com) · [X 项目更新](https://x.com/liu_xiaoyu27334)

为内容策划提取参考片的功能结构，以用户合法提供的产品事实和素材重建原创分镜。

状态：公开源码实验版；具体测试边界见下文。

## 先看交付示例

[合成收纳盒案例](examples/demo.json)只给出可折叠、带盖两项事实，沿用“问题—演示—行动”的功能结构。价格、承重与优惠缺失，交付状态仍为“补信息后可拍”，不会补造卖点。

**最短入口：**让能读取 Markdown 的助手先读本目录的 [SKILL.md](SKILL.md)，再提交案例或自己的授权输入。完整目录与安装条件见下文。

本页提供三语介绍；操作指令、模板和部分示例仍以中文为主。可在请求中指定输出语言，但未验证跨宿主调用或日文生成效果。

## 安装与使用

这是指令型 Skill，不是托管服务。将本目录完整复制到支持 Skills 的环境所指定的技能目录；目录名采用 `benchmark-script-adapter`。也可直接让助手读取本目录的 `SKILL.md`，再提交任务。安装位置和调用方式由宿主环境决定；不要执行陌生安装脚本。

调用示例：`用 $benchmark-script-adapter，按 examples 中的合成输入演示流程；缺失事实标为待确认。`

不需要 API 密钥或环境变量，因此没有虚构的 `.env.example`。需要模型或平台操作时，使用宿主已授权能力；本包不会自动调用付费服务、上传素材或改写业务源表。

## 合成示例与本地检查

样例明确标注“模拟数据 DEMO”，由固定种子产生；不是从真实业务快照匿名化。只用 Python 3 标准库，无需安装依赖。

```sh
python3 -B scripts/generate_demo.py
python3 -B -m unittest discover -s tests -p "test_*.py"
```

该通用版不附视频下载器、转写器、产品事实库、历史成片、参考帧或自动抽图脚本。输入为用户提供且有权使用的描述／媒体；未看到的素材不得声称已分析。

## 成熟度与限制

公开源码准备阶段的检查覆盖结构、引用、合成样例和随包测试。本次文档整理未重新运行随包测试。上述检查不代表模型输出质量、真实平台参数、用户业务效果或媒体成片验收通过。本包不是托管服务；集合根目录 README 说明本仓库的收录范围。

## 许可与来源

自写部分采用 MIT，见 [LICENSE](LICENSE)。来源与排除范围见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)；具体边界见 [LICENSE-STATUS.md](LICENSE-STATUS.md)。请勿把客户材料、媒体、密钥或真实报表加入公开版本。

欢迎试试 [FateClear](https://fateclear.com) 的免费生日排盘与解读，也可以在 [X](https://x.com/liu_xiaoyu27334) 关注我的新项目和后续更新。
