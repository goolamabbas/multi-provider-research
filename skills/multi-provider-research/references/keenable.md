# Keenable

Use for high-recall general web discovery, relevant passages from long documents (Dynamic Snippets), date/point-in-time index queries, clean Markdown page reads, and optional authenticated Monitors.

## Privacy note

Keenable uses standard-tier search trajectories (queries, returned snippets, and fetched URLs) to improve retrieval. Keep queries to public facts unless the connection is on a zero-data-retention plan.

## Search (`search_web_pages`)

- Describe the page and evidence sought rather than stuffing keywords. Reuse returned snippets when they already contain the facts and caveats.
- **Modes:** Prefer `pro` for research depth when exposed; use `realtime` only when latency matters most (`realtime` does not guarantee fresher content). Public keyless endpoints (`/mcp-public`) may omit `mode`.
- **Assistant-only synthesis:** Set `disable_cards: true` so Keenable returns ordinary web sources instead of provider-written cards (whose URLs expire after one day).
- **Dates & point-in-time search:**
  - `published_after` / `published_before` filter publication date (pages without a known date may be omitted).
  - `acquired_after` / `acquired_before` filter when Keenable indexed the page.
  - `query_time` searches the index *as it stood* at a past instant (`query_time: "7d"` means as of 7 days ago, not the last 7 days). For a past window, pair `query_time` with explicit dates because relative deltas still count back from now.
- **Domains:** `site` targets one domain; `exclude_domains` excludes hosts and subdomains. Inspect live validation if excluding a public suffix like `.gov` (some MCP versions reject bare suffixes).

## Fetch (`fetch_page_content`) and Monitors

- Returns clean Markdown for up to 20 URLs (keyless tier accepts 1 URL per call). By default returns Keenable's indexed copy and falls back to live fetch for unindexed URLs.
- Use `max_age_hours: 0` when you need a guaranteed live read, or `-1` for strictly index-only reads. Check truncation against `max_chars` (default 20,000 total split across URLs).
- Omit `prompt` for source-only reading; setting `prompt` runs an LLM over the page and returns an answer instead of source text.
- Authenticated connections may also expose `get_billing` (read-only) and Monitors tools (`create_monitor`, `list_monitors`, `get_monitor_results`, `delete_monitor`). Create or delete monitors only with explicit user authorization.

Docs: [Keenable MCP](https://docs.keenable.ai/mcp-server) · [Pricing](https://keenable.ai/pricing) · [Search Trajectories](https://keenable.ai/blog/trajectories-in-improvements-out)
