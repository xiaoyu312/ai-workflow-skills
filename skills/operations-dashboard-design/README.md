# 经营看板设计系统

[English](README.en.md)

作者的项目：[FateClear](https://fateclear.com) · [X 项目更新](https://x.com/liu_xiaoyu27334)

为中文经营看板提供语义色、排版、布局、状态和可访问性约束，不含业务数据或数据接口。

状态：公开源码实验版；具体测试边界见下文。

## 安装与使用

这是指令型 Skill，不是托管服务。将本目录完整复制到支持 Skills 的环境所指定的技能目录；目录名采用 `operations-dashboard-design`。也可直接让助手读取本目录的 `SKILL.md`，再提交任务。安装位置和调用方式由宿主环境决定；不要执行陌生安装脚本。

调用示例：`用 $operations-dashboard-design，按 examples 中的合成输入演示流程；缺失事实标为待确认。`

不需要 API 密钥或环境变量，因此没有虚构的 `.env.example`。需要模型或平台操作时，使用宿主已授权能力；本包不会自动调用付费服务、上传素材或改写业务源表。

## 合成示例与本地检查

样例明确标注“模拟数据 DEMO”，由固定种子产生；不是从真实业务快照匿名化。只用 Python 3 标准库，无需安装依赖。

```sh
python3 -B scripts/generate_demo.py
python3 -B -m unittest discover -s tests -p "test_*.py"
```

原 UI kit 会加载私有预览，已完全排除。公开版只提供 CSS tokens、通用指令和合成 HTML 样例；未做浏览器截图或视觉验收。

## 成熟度与限制

本轮检查结构、引用、合成样例和随包测试；不代表模型输出质量、真实平台参数、用户业务效果或媒体成片验收通过。本包不是托管服务；集合根目录 README 说明本仓库的收录范围。

## 许可与来源

自写部分采用 MIT，见 [LICENSE](LICENSE)。来源与排除范围见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)；具体边界见 [LICENSE-STATUS.md](LICENSE-STATUS.md)。请勿把客户材料、媒体、密钥或真实报表加入公开版本。

欢迎试试 [FateClear](https://fateclear.com) 的免费生日排盘与解读，也可以在 [X](https://x.com/liu_xiaoyu27334) 关注我的新项目和后续更新。
