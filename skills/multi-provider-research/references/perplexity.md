# Perplexity

Read when Perplexity is required or selected.

- Use the operation that fits each evidence need. Combine Search for discovery and Context for missing source passages when both are permitted.
- Use Search for ranked URLs, facts, or recent-news leads without a provider-generated narrative answer.
- After selecting Perplexity Search for the task, prefer `search_type: "fast"` for routine lookups, repeated agent searches, or latency-sensitive retrieval when the live interface exposes it. This is a skill preference; omitting the parameter uses the API's standard `"web"` default. It does not make Perplexity the default provider.
- Choose `search_type: "web"` directly for rare, difficult, or ambiguous questions, or for a targeted follow-up when Fast Search leaves a material evidence gap. Do not automatically run both types for every query; honor an explicitly requested type.
- Never pass `search_type` to an interface that does not expose it. If an explicitly requested type is unavailable, disclose the gap and follow the user's fallback boundary.
- Both Search types retrieve ranked sources without a generated narrative answer. Fast Search is distinct from Ask's Agent API `fast` preset.
- Use Ask for a focused factual answer or concise cited explanation.
- Use Reason for comparison or decision analysis against explicit criteria using current web evidence.
- Use Research only for genuinely deep, comprehensive multi-source investigation whose added latency is justified.
- Inspect the selected tool's live schema; do not assume that Search, Context, Ask, Reason, and Research expose the same controls.
- Treat Ask, Reason, and Research as provider-side synthesis. Preserve their cited URLs and inspect the underlying source content before using material claims. Report exposed model or preset metadata without guessing missing details.

## Context for known URLs

Use `perplexity_context` for supplied URLs or to fill material gaps in a Search excerpt. Check the callable tool and batch limit. Respect explicit Search-only or reader restrictions. Use Markdown or query-focused source highlights. For assistant-only synthesis omit `criteria`, which adds provider-side scoring and input-token charges.

Inspect status and metadata for each URL. Reuse successful reads and retry only recoverable gaps within scope. A `not_modified` result carries no new page body. Reuse the previously inspected copy if available and sufficient. The default allows stored copies up to two days old. Use `max_age_seconds: 0` when current evidence requires a live read.

For point-in-time work, use `snapshot_as_of` only where exposed. Use the same timestamp for historical Search discovery and Context reading if both accept it. Context snapshots require an archived copy and never fetch live. If it is missing, use another permitted archive with the same cutoff or report the gap. Publication-date filters and live reads cannot reproduce an older page body. [Context quickstart](https://docs.perplexity.ai/docs/context/quickstart) · [Time Machine](https://docs.perplexity.ai/docs/search/time-machine)

Report the exact mode, selected search type when relevant, material query/domain/recency/country/context controls, inspected underlying sources, and exposed provider model or preset when material. Never infer that the current assistant performs provider-side synthesis.

See the [official Fast Search documentation](https://docs.perplexity.ai/docs/search/fast-search) for current usage and pricing. A successful request establishes execution, not independently measured latency or billed cost.
