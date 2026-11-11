# Keenable

## Choose Keenable

Use for general web discovery, query-relevant passages from long documents, publication/index-date filtering, or reading supplied and selected web pages. Benchmarks are dated evaluation evidence, not a universal routing rule. Do not replace explicitly required providers or materially matched specialist datasets merely because Keenable is available.

The MCP normally exposes `search_web_pages` and `fetch_page_content`; SDK/API names and options differ. Inspect the callable schema. Some public MCP endpoints omit `mode`. Do not invent unsupported parameters, operator `_meta` overrides or experimental API tools.

## Search and source boundaries

Describe the page and evidence that would answer the question. Use a focused query; split genuinely independent aspects when necessary, with bounded concurrency and no duplicate reads. Start with a modest result count and adequate snippet context; expand for material evidence gaps, not provider coverage.

Use `pro` for ordinary depth-oriented research when selectable; choose `realtime` when latency is the priority. Inspect the returned mode when available because operator/account defaults can differ. Realtime does not guarantee fresher source content. Do not claim a requested mode executed when the interface cannot select or report it.

For source-only or assistant-only synthesis, set `disable_cards: true`. Keenable can otherwise return generated cards at `cards.keenable.ai/w/`; these are provider-written results with URLs documented to expire after one day. If cards are allowed, distinguish them from source pages and inspect underlying evidence for material claims. If a required control is unavailable, disclose the limitation rather than silently relaxing the user's boundary.

Ordinary snippets select source passages using machine learning; they are not a guarantee of complete context. Reuse sufficient returned passages. Fetch when the URL was supplied, the user needs full-document analysis, or snippets omit qualifications, conflict, lack context or are stale. Do not automatically fetch every search result.

`max_results` and `snippet_max_length` control results and characters per result, not a token budget. Documentation currently specifies 1–50 results and 180–10,000 snippet characters; live validation governs. Short caps can remove necessary evidence. Read `snippet`; the deprecated `description` field may be empty. Prefer JSON output when structured dates and returned mode matter.

## Dates and domains

Use `published_after` / `published_before` for publication windows. Publication filters omit records with unknown publication dates; preserve that coverage limitation. `acquired_after` / `acquired_before` concern when Keenable indexed a page, not when its underlying event occurred.

Use `query_time` only for a point-in-time index query. `query_time: "7d"` means as of seven days ago, not the last seven days. For a past interval, use explicit dates/timestamps: relative filters still count back from request time. A date-only `query_time` resolves to midnight UTC; date-only ordinary before bounds cover the full UTC day. Do not promise historical page-body reconstruction from an ordinary Fetch or claim a complete record of what was publicly knowable.

`site` restricts one site; supported query operators may target several. `exclude_domains` uses host names, including their subdomains, not paths, suffixes or wildcards. Check results against actual user restrictions; a filter is not a source-quality guarantee.

## Fetch

Omit `prompt` for source-only work. With `prompt`, an LLM reads the page and returns its answer instead of full source text. Use that option only when the user's synthesis restrictions permit it, disclose provider-generated output and do not guess the model.

Default Fetch uses indexed content; a URL with no indexed copy can trigger live retrieval. Request `live: true` when current source content matters and the interface supports it. Preserve source and retrieval dates separately. Successful live fetching is not proof of completeness, truth or publication freshness.

Check truncation against `max_chars` (documented default 50,000). This is a content cap, not query-targeted extraction. Retrieve enough context for the task or explicitly state what remains unread; do not call a truncated response the full document.

## Cost, limits and completion

Search and Fetch are separate operations. Check current account terms and exposed usage rather than assuming every connection is free. Authenticated MCP may return `_meta["keenable/usage"]` with SKU, credits and paid/free-allowance status; some harnesses do not expose it. Missing metadata is not proof of zero cost. Do not embed changing dollar prices in routing rules; link the official pricing and credit documentation.

On rate limiting, follow exposed retry timing within the task's limits. On insufficient credits, stop repeated paid attempts and report the access gap; do not purchase credits or enable auto-top-up without authorization. Do not disable native tools or configure other clients as a side effect of research.

An optional `session_id` groups calls in a run; it does not promise memory or deduplication. Report meaningful evidence contributions, failures, substitutions, truncation, generated output and freshness/cost limitations proportionally. Distinguish executed checks from documented features.

## Official references

- [Search and parameters](https://docs.keenable.ai/products/search)
- [Fetch and prompted extraction](https://docs.keenable.ai/products/fetch)
- [MCP endpoints, schemas and metadata](https://docs.keenable.ai/mcp-server)
- [Best practices](https://docs.keenable.ai/best-practices)
- [Pricing](https://keenable.ai/pricing), [credits](https://docs.keenable.ai/credits), [rate limits](https://docs.keenable.ai/rate-limits)
