---
name: multi-provider-research
description: "Route research using Octen, Exa, Perplexity, Parallel, Firecrawl, TinyFish, or X-native tools. Use for research through a named provider, specialized datasets, batch enrichment, site extraction, or browser-based evidence gathering. Skip native-only research and tasks that merely mention a provider."
---

# Multi-provider research

Use the minimum sufficient set of available providers. Give each a distinct evidence role within the user's requested outcome; a single provider can be enough.

## Shared boundaries

- Apply explicit provider inclusions or exclusions, then named-provider requests, then a materially matched specialized dataset, then a generic discovery default. Naming a provider requires its contribution to the requested role, not exclusivity. Honor “only,” “exactly,” and equivalent restrictions. Explicit native-only instructions override external routing even if this skill was loaded automatically.
- Default ordinary lookups to retrieval and synthesis by the current assistant. Use provider-generated research or enrichment when the requested outcome warrants it and restrictions permit it. Ask only when an unresolved boundary materially affects scope, cost, or data handling; existing authorization continues to apply.
- Classify operations and output options, not just tool names. Under assistant-only synthesis, avoid provider-generated answers, summaries, reasoning, and agent operations, including Connect through Exa Agent. Source retrieval, ranking, and faithful extraction may use internal machine learning; this restriction does not guarantee model-free processing. A provider call does not imply use of the assistant's selected model.
- Research is read-only unless the user explicitly authorizes the corresponding action. Persistent website actions and recurring checks require authorization for those outcomes. Provider installation or availability alone is not authorization.

## Choose and execute

Read only the references relevant to the requested evidence and selected providers. Decompose multi-part work when useful; a focused lookup needs no elaborate routing plan.

| Evidence need or required provider | Reference |
| --- | --- |
| Focused web/news discovery or multi-angle discovery with Octen | [Octen](references/octen.md) |
| Semantic discovery, People/Company/Code/News verticals, or Exa Agent enrichment | [Exa](references/exa.md) |
| Specialized fields: podcast statements, company or professional signals, traffic estimates, comparable financial fields, business verification, product offers, airfare, prediction-market data | [Exa Connect matching](references/exa.md#connect-provider-map) — check even without a provider name; a supplied authoritative document may already suffice |
| Perplexity retrieval or permitted cited analysis | [Perplexity](references/perplexity.md) |
| Parallel discovery, source excerpts, deep reports, or repeated batch fields | [Parallel](references/parallel.md) |
| Site URL inventory, bounded crawling, document parsing, or structured webpage extraction | [Firecrawl](references/firecrawl.md) |
| Focused browser-rendered reading or user-directed browser interaction | [TinyFish](references/tinyfish.md) |
| X posts, Articles, accounts, timelines, bookmarks, engagement, search, counts, or trends | [X-native routing](references/x-routing.md) |

Inspect the selected operation's callable schema before first use; reuse that knowledge unless the surface changes or validation fails. Distinguish visibility/configuration, authentication/reachability, successful execution, and useful evidence. The first useful read can establish live usability; do not make a separate probe solely to demonstrate availability. Runtime validation governs accepted arguments when descriptions disagree; report material mismatches.

Avoid repeating successful queries or fetching the same URL across providers without a requested comparison or material verification reason. If a required or task-matched provider is unavailable, disclose the gap before a materially different fallback. Proceed with a distinct fallback when already permitted, label its evidence class, and never attribute web evidence to Connect or an X API. Do not silently replace a required provider or materially expand scope.

Retain asynchronous identifiers and follow the selected tool's lifecycle. Do not duplicate a run that may still be active. A provider-specific instruction to return a progress URL is a pending handoff, not completed research.

## Evidence and completion

Prefer original, official, regulatory, filing, repository, or primary-research evidence for material claims. Cite inspected source content or provider-backed results that directly support the claim and retain necessary context. Sufficient source excerpts or full text returned by search need no duplicate fetch. Retrieve more context when excerpts are ambiguous, incomplete, conflicting, or omit material qualifications. Generated answers are synthesis, not underlying source evidence; separate inference from source facts.

For changing facts, inspect relevant cache/freshness controls and use an appropriate live fetch or cache age when supported. Distinguish retrieval time from publication, reporting-period, and observation dates. A successful fetch alone does not establish currentness. Preserve material speakers, timestamps, entities, and field-level provenance; report remaining uncertainty.

Public professional fields may be collected when requested. Do not seek private contact details, sensitive personal attributes, or data-broker-style enrichment.

Continue permitted research until the requested deliverable has sufficient inspected evidence, or remaining gaps are blocked by access, explicit restrictions, budget, or the tool's lifecycle. Pursue material gaps without repeating successful work. If one evidence lane is blocked, complete independent permitted work and report the limitation.

Report exact tools, distinct contributions, material failures, substitutions, and gaps proportionally. Identify provider-side synthesis and its exposed model or preset without guessing. A short provider note can suffice for a simple lookup. Use [the reporting checklist](references/reporting-checklist.md) when coverage, provenance, asynchronous work, or an audit warrants more detail; do not print an exhaustive ledger by default.

## Maintenance

When changing routing behavior, use [behavioral evaluations](references/behavioral-evaluations.md). These are maintenance cases, not steps to run during ordinary research.
