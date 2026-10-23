[简体中文](README.md) · [English](README.en.md) · [日本語](README.ja.md)

# Video Structure Adaptation


More from the author: [FateClear](https://fateclear.com) · [Project updates on X](https://x.com/liu_xiaoyu27334)

A workflow for content planners to extract a reference video's functional structure and rebuild an original, shootable script using authorized product facts. No private business inputs or media are included.

Status: **Experimental public source edition**.

## Preview the handoff

The [synthetic storage-box case](examples/demo.json) supplies only two facts: foldable and lidded. It follows a problem–demonstration–action structure. Price, load capacity and promotions are missing, so the result remains “补信息后可拍” (shootable after missing information is supplied), without invented claims.

**Shortest entry:** ask a Markdown-capable assistant to read this folder's [SKILL.md](SKILL.md), then supply an example or your own authorized input. Keep the whole folder; setup details follow below.

This README is available in three languages. Operational instructions, templates and some examples remain primarily Chinese. You may request an output language, but cross-host invocation and Japanese generation quality have not been validated.

## Install and use

Copy this entire folder into the skill directory designated by your host, using `benchmark-script-adapter` as the folder name. Alternatively, ask your assistant to read `SKILL.md` directly before performing a task. No installer is included. Host-specific invocation and model behavior have not been verified.

Example: `Use $benchmark-script-adapter with the synthetic examples and clearly mark missing facts.`

No API keys or environment variables are required, so no unused `.env.example` is supplied. Platform operations require the host's existing authorized capabilities. This package does not automatically submit paid jobs, upload assets, or edit source business records.

## Delivered scope

The brand-specific product corpus, historical-video analysis, footage, reference frames, download/transcription tools and extraction scripts have been removed. Users provide their own authorized inputs. The synthetic example deliberately lacks price and performance claims, so its result remains pending information rather than ready to shoot.

## Synthetic demo and checks

Examples are generated from a fixed seed and labeled “模拟数据 DEMO”. They are constructed examples, not anonymized business records. Python 3 standard library only:

```sh
python3 -B scripts/generate_demo.py
python3 -B -m unittest discover -s tests -p "test_*.py"
```

Checks recorded during public source preparation covered file structure, references and declared example constraints. The bundled tests were not rerun for this documentation update. They do not verify model quality, current platform capabilities, business impact, or generated media. This package is not a hosted service. The collection root README describes the scope of this repository.

## License

MIT covers the user's authored instructions and code. See [LICENSE](LICENSE), [LICENSE-STATUS.md](LICENSE-STATUS.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Retained third-party notices remain applicable.

Try [FateClear](https://fateclear.com) for free birthday charting and interpretation, or follow [me on X](https://x.com/liu_xiaoyu27334) for new projects and updates.
