[简体中文](README.md) · [English](README.en.md) · [日本語](README.ja.md)

# AI Workflow Skills

More from the author: [FateClear](https://fateclear.com) · [Project updates on X](https://x.com/liu_xiaoyu27334)

11 reusable workflows for content, AI video, e-commerce operations, product delivery and decision support. Each folder contains `SKILL.md` instructions, relevant templates and usage notes for a compatible host to read. Public editions follow file-level provenance and privacy boundaries; individual READMEs describe differences from the private editions.

## Start with a concrete task

Choose one workflow, keep its folder intact, and ask a Markdown-capable assistant to read its `SKILL.md` before supplying your authorized input. Setup and invocation depend on the host. This repository supplies neither a model nor a one-click installer.

| Desired handoff | Existing synthetic input or illustrative output |
| --- | --- |
| A product description grounded in facts | [Brand copy: a fictional three-compartment organizer](skills/brand-copywriting/examples/synthetic-product.md) |
| A shot plan before production | [Shot brief: a cardboard box opening in four seconds](skills/jimeng-shot-director/examples/brief.json) |
| A review separating metrics and evidence | [Ad review: synthetic spend and ROI reconciliation](skills/tmall-wanxiang-weekly-review/examples/demo.json) |
| An AI delivery plan with acceptance criteria | [Read-only inventory questions: evaluation and authority](skills/ai-product-field-delivery/examples/synthetic-request.md) |

These are existing, independently constructed texts and data, not client cases, runtime screenshots or measured outcomes. Operational instructions, templates and some examples remain primarily Chinese. Three-language READMEs do not mean the workflows have been localized or Japanese generation quality has been validated.

## Choose a workflow

| Skill | Public scope |
| --- | --- |
| [Voice-preserving Chinese editing](skills/wang-xiaobo-writing/README.en.md) · [日本語](docs/ja/wang-xiaobo-writing/README.md) | A reduced factual editing workflow; no book mappings, literary mechanisms or personal records |
| [AI video direction](skills/jimeng-video-director/README.en.md) | Shot planning, reference roles, continuity and output review; upstream MIT attribution retained |
| [Weekly advertising review](skills/tmall-wanxiang-weekly-review/README.en.md) | Metric definitions, reconciliation, evidence and actions; no connector, business data or private report generator |
| [Reference-video structure adaptation](skills/benchmark-script-adapter/README.en.md) | General analysis workflow and blank templates; no brand facts, historical-video corpus or media |
| [Operations dashboard design](skills/operations-dashboard-design/README.en.md) | CSS tokens, design constraints and a standalone synthetic preview; no original business dashboard |
| [Shot planning and output review](skills/jimeng-shot-director/README.en.md) | Reference roles, shot actions, camera relationships, continuity and review; no case-study media or prompt corpus |
| [Short-video commerce scripts](skills/qianchuan-script-creator/README.en.md) | Product evidence, task routing, shot tables and single-variable iterations; no course knowledge-base dependency |
| [Brand copywriting workbench](skills/brand-copywriting/README.en.md) | Briefs, evidence, selling points, original delivery templates and editing; no course excerpts |
| [AI product field delivery](skills/ai-product-field-delivery/README.en.md) | Task scope, evaluation design, release planning and operational review with independent forms |
| [Workplace communication and action](skills/gandepiaoliang-career-coach/README.en.md) | Goals, roles, decision authority, communication and observable progress; no book chapter/playbook mapping |
| [Personal decisions and review](skills/laoyu-life-coach/README.en.md) | Options, risks, small experiments and review; no course maps, transcripts or corpus |

## Use

Copy an entire `skills/<name>/` folder into a Skill directory supported by your host, or ask an assistant to read its `SKILL.md`. Installation paths and invocation depend on the host. Individual READMEs include synthetic examples and check commands.

No API key is needed for this repository. It includes no connector and does not automatically publish content or call paid services. Users provide authorized inputs and tool access.

## Validation limits

The source-release preparation recorded checks of local structure, links and synthetic fixtures. Video direction passed 13 tests; weekly review, reference adaptation and dashboard design passed 4 each. The writing package checked exact membership, 14 links and 2 synthetic cases. Model quality, live platforms, business outcomes and browser visuals remain unverified.

The six additions also receive independent synthetic-task checks; individual READMEs state their scope and unverified behavior. They do not promise the complete method or outcomes of private editions.

This multilingual documentation update did not rerun those functional tests. The writing checker requires a fixed file list and package-local links. Its Japanese introduction therefore lives under repository-level `docs/ja/` and is linked from this index; the package retains Chinese/English switching. Author links are provided at repository level, and the checker source is unchanged.

All examples are independently synthetic. `python3 -B scripts/generate_all_examples.py` reproduces the public examples without reading business files or accessing a network.

## License

User-authored portions are [MIT](LICENSE). Each package contains license-scope and third-party notices; video direction retains the upstream MIT text. This grant does not cover third-party brands, books, courses, media or user inputs.

The six additions retain confirmed user-authored instructions or add independently written general templates. Package notices credit historical sources. Restricted source materials are excluded; neither attribution nor this MIT grant licenses their redistribution. Legacy folder names provide compatibility and do not imply an official author or platform edition.

Try [FateClear](https://fateclear.com) for free birthday charting and interpretation, or follow [me on X](https://x.com/liu_xiaoyu27334) for new projects and updates.
