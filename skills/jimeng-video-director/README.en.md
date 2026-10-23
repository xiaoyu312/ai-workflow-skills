[简体中文](README.md) · [English](README.en.md) · [日本語](README.ja.md)

# AI Video Direction Workflow


More from the author: [FateClear](https://fateclear.com) · [Project updates on X](https://x.com/liu_xiaoyu27334)

A workflow for AI video creators covering scripts, shot planning, reference roles, continuity, prompt revisions, and returned-video review. It includes a standard-library Python checker for timelines, asset references and declared state. No private business inputs or media are included.

Status: **Experimental public source edition**.

## Preview the handoff

Start with the [synthetic shot plan](examples/demo.json): reference assets are deliberately marked `planned`. A valid structure does not mean the assets are ready or that acceptable video has been generated. The workflow keeps these states separate while planning shots and reviewing footage.

**Shortest entry:** ask a Markdown-capable assistant to read this folder's [SKILL.md](SKILL.md), then supply an example or your own authorized input. Keep the whole folder; setup details follow below.

This README is available in three languages. Operational instructions, templates and some examples remain primarily Chinese. You may request an output language, but cross-host invocation and Japanese generation quality have not been validated.

## Install and use

Copy this entire folder into the skill directory designated by your host, using `jimeng-video-director` as the folder name. Alternatively, ask your assistant to read `SKILL.md` directly before performing a task. No installer is included. Host-specific invocation and model behavior have not been verified.

Example: `Use $jimeng-video-director with the synthetic examples and clearly mark missing facts.`

No API keys or environment variables are required, so no unused `.env.example` is supplied. Platform operations require the host's existing authorized capabilities. This package does not automatically submit paid jobs, upload assets, or edit source business records.

## Synthetic demo and checks

Examples are generated from a fixed seed and labeled “模拟数据 DEMO”. They are constructed examples, not anonymized business records. Python 3 standard library only:

```sh
python3 -B scripts/generate_demo.py
python3 -B -m unittest discover -s tests -p "test_*.py"
```

Run `python3 -B scripts/check_plan.py examples/demo.json` to inspect the synthetic plan. Its reference files are deliberately marked `planned`: the expected result is structurally valid, assets not ready, and video quality unverified.

Checks recorded during public source preparation covered file structure, references and declared example constraints. The bundled tests were not rerun for this documentation update. They do not verify model quality, current platform capabilities, business impact, or generated media. This package is not a hosted service. The collection root README describes the scope of this repository.

## License

MIT covers the user's authored instructions and code. See [LICENSE](LICENSE), [LICENSE-STATUS.md](LICENSE-STATUS.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Retained third-party notices remain applicable.

Try [FateClear](https://fateclear.com) for free birthday charting and interpretation, or follow [me on X](https://x.com/liu_xiaoyu27334) for new projects and updates.
