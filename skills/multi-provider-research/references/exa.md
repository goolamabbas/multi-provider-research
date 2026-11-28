# Exa

Use for semantic web discovery, structured company/people/paper/podcast records in Exa Library, or permitted Exa Agent and Connect workflows.

## Search and Fetch

- Write a descriptive query naming the ideal source type, entity, and qualifying details rather than terse keywords. Use regular Search by default; use Advanced Search only when explicit domain, date, category, or freshness controls matter.
- **Auto vs. Lite:** `auto` is the default. Choose `lite` only when cost/latency matter and cached content suffices—Lite never fetches live and rejects freshness (`maxAgeHours`) and subpage parameters. Prefer `lite` over legacy `fast` / `instant`.
- Ignore deprecated `startCrawlDate`, `endCrawlDate`, and `github` category even if still exposed; inspect returned `warnings` for ignored or relaxed filters.
- **Built-in structured indexes (Search, no Agent needed):** Use `category:company` or `category:people` (or supported `company` / `people` / `news` / `publication` / `financial report` categories) for structured records in ordinary Search. Library fields are not equivalent to a named Connect partner's data; check dates and provenance.
- **Podcast transcripts:** Ordinary Search/Fetch can retrieve indexed Library transcripts (`includeDomains: ["exa.ai/library/podcast"]` where supported; do not invent a `podcast` category). Library coverage is strongest on recent episodes, so a miss is not proof an episode doesn't exist. Preserve speaker, date, and timestamps.
- **Places quirk:** Request content during Search where supported—Exa documents that later Fetch on Places records is unreliable.
- Reuse sufficient Search highlights; call Fetch only for known URLs or missing context.

## Agent, Ultra, and Connect

Treat `agent_run` (including Connect) as provider-side synthesis and usage-based billing.

- **Lifecycle:** Retain `runId` and resume active runs after timeouts; timeouts do not cancel provider work. Use `previousRunId` only to start a new billable follow-up from a completed run, with `input.data` for rows to enrich and `input.exclusion` for entities already found.
- **Ultra effort:** Reserve `effort: "ultra"` for comprehensive list-building or hard multi-source research where completeness outweighs latency and cost. Inspect whether the live schema exposes budget/stop controls before starting—a dollar limit in prompt text is not an enforced cap (default Ultra cap is $20). Check `stopReason` separately from `status: completed` (`budget_reached` / `time_limit_reached` means partial coverage).
- **Connect partners (inspect live `dataSources` enum before calling):**
  - `fiber` (B2B firmographics/people), `similarweb` (web traffic/competitors), `financial_datasets` (US public-company financials/SEC), `baselayer` (US business verification/KYB), `particle` (podcast analytics/sentiment), `polymarket` (prediction-market odds/history), `affiliate` (product/merchant offers), `jinko` (travel/airfare).
  - Verify completed output for actual partner contribution and provenance; never fill missing partner fields with generic web guesses.

Docs: [Exa MCP](https://exa.ai/docs/reference/exa-mcp) · [Search](https://exa.ai/docs/search/quickstart) · [Library](https://exa.ai/library) · [Agent](https://exa.ai/docs/agent/quickstart) · [Connect](https://exa.ai/docs/agent/connect/overview)
