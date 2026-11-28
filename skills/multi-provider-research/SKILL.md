---
name: multi-provider-research
description: "Route research using Exa, Parallel, Keenable, Octen, Perplexity, or X-native tools. Use for research through a named provider, specialized datasets, batch enrichment, or external source retrieval. Skip native-only research and tasks that merely mention a provider."
metadata:
  version: "0.12.0"
---

# Multi-provider research

Maintained routing for Exa, Parallel, Keenable, Octen, Perplexity, and authenticated X interfaces. Works with any available subset, including a single provider. For providers outside this set, follow their own instructions when explicitly requested rather than substituting a maintained provider.

Use the smallest sufficient set of available providers. Give each a distinct role; one provider is often enough.

## Choose by evidence need

Read only the provider references relevant to the task and active connections.

| Evidence need | Best fit when connected | Reference |
| --- | --- | --- |
| Semantic discovery, company/people profiles, papers, podcast transcripts, or Connect partner datasets | **Exa** | [references/exa.md](references/exa.md) |
| Primary financial/legal/healthcare excerpts, PDF or JS-heavy page fetch, structured registries, or batch list enrichment | **Parallel** | [references/parallel.md](references/parallel.md) |
| High-recall general web passages, date windows, point-in-time index search (`query_time`), or web monitors | **Keenable** | [references/keenable.md](references/keenable.md) |
| Fast official-URL lookup (`Pulse`), broad multi-angle discovery, current news, local places, business cards, or image search | **Octen** | [references/octen.md](references/octen.md) |
| Fast ranked search, archived URL snapshots (`Context`), or permitted cited synthesis (`Ask` / `Reason` / `Research`) | **Perplexity** | [references/perplexity.md](references/perplexity.md) |
| Original X posts, threads, X Articles, trends, counts, or saved bookmarks | **Authenticated X** | [references/x-routing.md](references/x-routing.md) |

## Routing boundaries and defaults

- **Precedence:** Explicit user inclusions/exclusions and native-only instructions always win (even if this skill loaded automatically). Naming a provider requires its contribution to that role; `"only"` or `"exactly"` makes the permitted set exclusive.
- **Native tools:** Allowed when useful and not excluded, but never use native search/fetch to bypass a required provider, exclusive list, or X-native requirement.
- **Retrieval first, synthesis deliberately:** Default ordinary lookups to source retrieval (search and fetch) and let the current assistant write the answer. Use provider-generated research or paid enrichment (Exa Agent/Connect, Parallel `web_research`/Deep Research/`FindAll`, Perplexity Ask/Reason/Research) only when the task genuinely needs it and restrictions/budget permit.
- **Strict assistant-only synthesis (when requested):** Exclude provider answer/agent endpoints and disable default generated output (Octen News storylines, Keenable generated cards and prompted Fetch, Perplexity `criteria` scoring). Never imply provider-generated prose came from the current assistant's model.
- **Live schema governs:** Inspect callable tool schemas before first use; never invent parameters from direct-API docs. Do not run a separate probe call solely to test access when the first useful lookup establishes it.
- **Avoid duplicate work and duplicate paid runs:** Do not repeat the same query or fetch the same URL across providers unless cross-coverage or conflict verification warrants it. For asynchronous runs (Exa Agent, Parallel Task/`FindAll`), retain and resume the same run ID instead of launching duplicates.
- **Fallbacks:** If a required provider is unavailable, report the gap without silent substitution and finish independent permitted work. For unrestricted tasks, switch to another suitable permitted provider and note the substitution briefly.
- **Read-only by default:** Never post, reply, create recurring monitors, purchase credits, or change client configuration without explicit authorization.

## Evidence and reporting

- Prefer primary and official sources (filings, official docs, original transcripts, repositories). Reuse returned excerpts when they already contain the needed facts and caveats; fetch full pages when context is truncated, ambiguous, or conflicting.
- For changing facts, check freshness/cache controls and keep publication, reporting-period, and retrieval dates distinct.
- When a tool translates list criteria into filters, verify it did not add or drop a constraint.
- Collect public professional fields when requested; do not seek private contact details or sensitive personal data.
- Keep reporting proportional: cite primary links and note real gaps or tool limits concisely. Do not bury simple answers in mechanical ledgers; consult [references/reporting-checklist.md](references/reporting-checklist.md) only when provenance, async runs, or an audit requires detail.
