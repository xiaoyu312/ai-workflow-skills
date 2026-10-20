# E-commerce Ads Weekly Review

[中文](README.md)

A workflow for e-commerce advertising reviews: establish source versions and comparable periods, recompute metrics, separate observed facts from hypotheses, and propose reversible actions. No private business inputs or media are included.

Status: **Experimental public source edition**.

## Install and use

Copy this entire folder into the skill directory designated by your host, using `tmall-wanxiang-weekly-review` as the folder name. Alternatively, ask your assistant to read `SKILL.md` directly before performing a task. No installer is included. Host-specific invocation and model behavior have not been verified.

Example: `Use $tmall-wanxiang-weekly-review with the synthetic examples and clearly mark missing facts.`

No API keys or environment variables are required, so no unused `.env.example` is supplied. Platform operations require the host's existing authorized capabilities. This package does not automatically submit paid jobs, upload assets, or edit source business records.

## Delivered scope

This package contains methodology and reporting contracts only. The original private report generator and data connectors are not included. The synthetic example covers arithmetic and scene reconciliation; it is not a complete production-report snapshot. An assistant can apply the workflow to authorized user inputs, or an independently reviewed generator may consume the contract.

## Synthetic demo and checks

Examples are generated from a fixed seed and labeled “模拟数据 DEMO”. They are constructed examples, not anonymized business records. Python 3 standard library only:

```sh
python3 -B scripts/generate_demo.py
python3 -B -m unittest discover -s tests -p "test_*.py"
```

These checks cover file structure, references and declared example constraints. They do not verify model quality, current platform capabilities, business impact, or generated media. This package is not a hosted service. The collection root README describes the scope of this repository.

## License

MIT covers the user's authored instructions and code. See [LICENSE](LICENSE), [LICENSE-STATUS.md](LICENSE-STATUS.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Retained third-party notices remain applicable.
