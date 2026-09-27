# Perplexity

Read when Perplexity is required or selected.

- Use Perplexity selectively and use one mode per subproblem by default.
- Use Search for ranked URLs, facts, or recent-news leads without a provider-generated narrative answer.
- After selecting Perplexity Search for the task, prefer `search_type: "fast"` for routine lookups, repeated agent searches, or latency-sensitive retrieval when the live interface exposes it. This is a skill preference; omitting the parameter uses the API's standard `"web"` default. It does not make Perplexity the default provider.
- Choose `search_type: "web"` directly for rare, difficult, or ambiguous questions, or for a targeted follow-up when Fast Search leaves a material evidence gap. Do not automatically run both types for every query; honor an explicitly requested type.
- Never pass `search_type` to an interface that does not expose it. If an explicitly requested type is unavailable, disclose the gap and follow the user's fallback boundary.
- Both Search types retrieve ranked sources without a generated narrative answer. Fast Search is distinct from Ask's Agent API `fast` preset.
- Use Ask for a focused factual answer or concise cited explanation.
- Use Reason for comparison or decision analysis against explicit criteria using current web evidence.
- Use Research only for genuinely deep, comprehensive multi-source investigation whose added latency is justified.
- Inspect the selected tool's live schema; do not assume that Search, Ask, Reason, and Research expose the same controls.
- Treat Ask, Reason, and Research as provider-side synthesis. Preserve their cited URLs and inspect the underlying source content before using material claims. Report exposed model or preset metadata without guessing missing details.

Report the exact mode, selected search type when relevant, material query/domain/recency/country/context controls, inspected underlying sources, and exposed provider model or preset when material. Never infer that the current assistant performs provider-side synthesis.

See the [official Fast Search documentation](https://docs.perplexity.ai/docs/search/fast-search) for current usage and pricing. A successful request establishes execution, not independently measured latency or billed cost.
