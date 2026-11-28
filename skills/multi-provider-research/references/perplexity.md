# Perplexity

Use for fast ranked web search (`perplexity_search`), clean known-URL reading with optional historical snapshots (`perplexity_context`), or permitted provider-generated synthesis (`perplexity_ask`, `perplexity_reason`, `perplexity_research`).

## Retrieval (`Search` and `Context`)

- **`perplexity_search`:** Returns ranked results without an AI-written answer. When the live schema exposes `search_type`, prefer `"fast"` ($1/1k) for routine lookups and `"web"` ($5/1k) directly for difficult or ambiguous questions. Never invent `search_type` if omitted, and do not confuse Search's `"fast"` mode with `perplexity_ask`'s `fast` preset.
- **`perplexity_context`:** Reads supplied or selected URLs as Markdown or query-focused highlights. Default permits cached copies up to two days old; set `max_age_seconds: 0` for a live fetch. Omit `criteria` under assistant-only synthesis (scoring adds model/token charges). A `not_modified` status carries no body—reuse the prior copy.
- **Historical snapshots:** Use `snapshot_as_of` on Context (and Search where exposed) to retrieve archived copies as of a past cutoff date. Snapshots never fetch live; report missing archived copies rather than substituting current pages.

## Provider-side synthesis (`Ask`, `Reason`, `Research`)

- Choose at most one synthesis mode per sub-question when synthesis is permitted: **Ask** (`fast` preset, quick cited answer), **Reason** (`medium` preset, criteria-based comparison/trade-offs), or **Research** (`high` preset, deep multi-source report).
- Treat output as provider synthesis using Perplexity's own presets, not the current assistant's model. Inspect primary sources for material claims and report the tool/preset used without guessing the underlying model.

Docs: [Perplexity MCP](https://docs.perplexity.ai/docs/getting-started/integrations/mcp-server) · [Fast Search](https://docs.perplexity.ai/docs/search/fast-search) · [Context](https://docs.perplexity.ai/docs/context/quickstart) · [Pricing](https://docs.perplexity.ai/docs/getting-started/pricing)
