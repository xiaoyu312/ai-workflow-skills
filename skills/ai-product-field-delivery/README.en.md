# AI Product Field Delivery

[中文](README.md) · [FateClear — free birthday charting and interpretation](https://fateclear.com) · [Follow project updates on X](https://x.com/liu_xiaoyu27334)

Turn an AI tool, retrieval, agent, or automation request into a delivery document people can review and verify. This public edition offers four entry points: a delivery brief, an evaluation plan, a release plan, and an operations review.

It is intended for developers, product managers, and delivery owners who need to define scope, verification, and human handoff. A small personal utility can use only the relevant template.

## Use

Copy this entire directory into a local Skills location supported by your assistant. The host must be able to read `SKILL.md` and its relative resources; the installation location depends on the host. No dependencies, API keys, or network service are required by this package.

Example request:

> Use ai-product-field-delivery to design an evaluation for an inventory question-answering assistant that can only read CSV files. We have no real query logs. Do not deploy anything or assume that cost savings have already been achieved.

Start with [SKILL.md](SKILL.md), which routes to the relevant template. The instructions and templates are in Chinese; they can be used to produce the language requested by the user. The [synthetic exercise](examples/synthetic-request.md) helps check whether a response distinguishes a plan, its evidence, and actions actually performed.

## Scope and limits

- Retains the practical purpose: define scope and a baseline, plan acceptance, arrange human handoff and failure handling, and review observed results.
- The public edition uses newly prepared general instructions and blank forms. It does not directly reuse the private edition's chapter map, reference files, or eight-stage organization.
- It includes no book text, chapter summaries, third-party cases, customer material, logs, secrets, or original execution history.
- It does not claim to reproduce the private edition or any source author's complete method or results. Package checks and synthetic exercises are not real-world delivery validation.
- Technical, business, and professional decisions still depend on project evidence and the responsible people.

## Provenance and license

The private edition was partly inspired by Fan Bing (XDash)'s FDE book. This public edition retains that historical attribution without bundling the work or relicensing it under MIT. It is not endorsed by the source author. See [third-party and provenance notices](THIRD_PARTY_NOTICES.md).

[MIT](LICENSE) applies only to the package author's own instructions, templates, and documentation.

---

The author also builds [FateClear](https://fateclear.com), a free birthday charting and interpretation website. Follow new projects and development notes on [X](https://x.com/liu_xiaoyu27334).
