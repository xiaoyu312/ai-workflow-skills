# Operations Dashboard Design

[中文](README.md)

More from the author: [FateClear](https://fateclear.com) · [Project updates on X](https://x.com/liu_xiaoyu27334)

A reusable design workflow and CSS token set for Chinese-language operations dashboards, with semantic colors, typography, layout, data-state and accessibility conventions. No private business inputs or media are included.

Status: **Experimental public source edition**.

## Install and use

Copy this entire folder into the skill directory designated by your host, using `operations-dashboard-design` as the folder name. Alternatively, ask your assistant to read `SKILL.md` directly before performing a task. No installer is included. Host-specific invocation and model behavior have not been verified.

Example: `Use $operations-dashboard-design with the synthetic examples and clearly mark missing facts.`

No API keys or environment variables are required, so no unused `.env.example` is supplied. Platform operations require the host's existing authorized capabilities. This package does not automatically submit paid jobs, upload assets, or edit source business records.

## Delivered scope

The original wrapper that loaded a private business dashboard is excluded. The standalone examples/index.html uses only synthetic rows and system fonts. No dashboard data connector or OpenDesign viewer is bundled. CSS-reference tests passed; browser rendering, responsive appearance and assistive-technology behavior were not tested.

## Synthetic demo and checks

Examples are generated from a fixed seed and labeled “模拟数据 DEMO”. They are constructed examples, not anonymized business records. Python 3 standard library only:

```sh
python3 -B scripts/generate_demo.py
python3 -B -m unittest discover -s tests -p "test_*.py"
```

These checks cover file structure, references and declared example constraints. They do not verify model quality, current platform capabilities, business impact, or generated media. This package is not a hosted service. The collection root README describes the scope of this repository.

## License

MIT covers the user's authored instructions and code. See [LICENSE](LICENSE), [LICENSE-STATUS.md](LICENSE-STATUS.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Retained third-party notices remain applicable.

Try [FateClear](https://fateclear.com) for free birthday charting and interpretation, or follow [me on X](https://x.com/liu_xiaoyu27334) for new projects and updates.
