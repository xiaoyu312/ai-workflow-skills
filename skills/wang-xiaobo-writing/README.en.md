[简体中文](README.md) · [English](README.en.md)

# Voice-First Chinese Editing


More from the author: FateClear · Project updates on X

A Chinese writing skill for improving drafts while preserving the writer's voice, facts, and scope. It supports short posts, essays, spoken scripts, and requested local critiques.

Status: **Experimental public source edition**. This reduced package is distributed with the scope and validation limits below.

## Preview the handoff

The [existing synthetic case](examples/synthetic-cases.json) tests a reminder tool three times, with one reminder two minutes late. A light edit must keep both facts, without claiming reliable timing or major time savings. The input and illustrative edit appear below.

**Shortest entry:** ask a Markdown-capable assistant to read this folder's [SKILL.md](SKILL.md), then supply an example or your own authorized input. Keep the whole folder; setup details follow below.

The collection provides three-language introductions. Use its root index for the Japanese introduction at `docs/ja/wang-xiaobo-writing/README.md`. Operational instructions, templates and some examples remain primarily Chinese. You may request an output language, but cross-host invocation and Japanese generation quality have not been validated.

## Scope of this public edition

- Retains the original workflow: preserve facts and the writer's existing expression, then make necessary edits.
- Preserves numbers, conditions, scope, and causal strength. It does not invent experiences, dialogue, or negative factual claims.
- Includes platform guidance, checks for empty phrasing, and original synthetic teaching examples.
- Does not add jokes, grand conclusions, or multiple versions by default. Formal notices can remain formal.

The identifier `wang-xiaobo-writing` is retained for compatibility. The original project studied Wang Xiaobo's *The Silent Majority*. This edition omits book sample mappings, chapter content anchors, and the technique summaries derived from those samples. It does not include the full style-distillation functionality of the private edition and is not endorsed by the author or rights holders.

See [LICENSE-STATUS.md](LICENSE-STATUS.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for retained provenance and licensing scope.

## Use

No scripts, network connection, API keys, source book, or additional dependencies are required to read the skill. The package provides instructions, not a model.

1. Keep this directory intact in an AI assistant environment that can read Markdown instructions.
2. Ask the assistant to read `SKILL.md` before editing your draft. Preserve its relative reference files.
3. In a host that supports installed skills by name, invoke `$wang-xiaobo-writing`. Installation locations and discovery are host-specific; this package does not install itself.

Example request:

> Read this directory's SKILL.md first. Lightly edit the following Chinese draft. Preserve the facts and my voice, keep it concise and natural, and return only the edited text.

The skill does not publish posts, send messages, or modify external services.

## Synthetic demonstration

The following case was constructed for this package. It is not a real business record or an anonymized snapshot.

Input:

> 我今天试了一个提醒工具。只试了 3 次，其中 1 次提醒晚了 2 分钟。先继续试试。

Acceptable light edit:

> 今天试了个提醒工具，试了 3 次，其中 1 次晚了 2 分钟。先继续试试。

The result must not become a claim that the tool is reliably on time or has saved substantial time. See [examples/synthetic-cases.json](examples/synthetic-cases.json) for fixed synthetic cases and constraints, and [references/before-after.md](references/before-after.md) for original teaching examples.

## Validation and maturity

Run:

```sh
python3 -B tests/check_package.py
```

Documentation layout: the existing checker requires a fixed file set and accepts only package-local links. This package therefore retains Chinese/English switching. Its Japanese introduction lives at repository path `docs/ja/wang-xiaobo-writing/README.md`, linked from the collection index. Author links to FateClear and X are also provided at repository level. The checker source is unchanged.

The check requires Python 3.9+ and uses only the standard library to verify the explicit file set, metadata, local references, path boundaries, absence of symlinks, synthetic example constraints, and selected sensitive-content patterns. It does not call a model, use the network, read the source project, or write user configuration.

The private project has historical behavior evaluations. This edition removes functionality, so those results are not claimed as validation of the public edition. Model generation and installation across hosts have not been tested. There are no guarantees about subjective style, engagement, or AI-detector outcomes. A passing static scan is not a complete security audit.

## Files

- `SKILL.md`: workflow.
- `agents/openai.yaml`: optional interface metadata.
- `references/before-after.md`: original synthetic teaching examples.
- `examples/synthetic-cases.json`: fixed synthetic cases.
- `tests/check_package.py`: dependency-free local checks.

The user-owned retained instructions, original examples, and new documentation/tests are licensed under MIT, copyright `2026 xiaoyu312`. The license does not cover excluded books or other third-party works.

Try FateClear for free birthday charting and interpretation, or follow me on X for new projects and updates.
