# Parallel

Use for objective-shaped primary web excerpts (especially financial, legal, and healthcare docs), clean PDF/JS page extraction, specialized vertical lookups, image search, or permitted research and batch enrichment.

## Connection surface

- **ChatGPT app vs. direct hosted MCP (`https://mcp.parallel.ai/mcp`):** Tool lists differ by connection. The ChatGPT app may expose dedicated flight/product tools without dataset tools; the direct hosted MCP typically exposes `web_search`, `web_fetch`, `web_decisions`, `image_search`, `find_verticals`, and `search_vertical` keyless, plus `web_research` when authenticated. Always inspect the live tool list.

## Search, Fetch, and Images

- **`web_search`:** Supply one self-contained goal-style `objective` plus 1–3 short keyword `search_queries` (3–6 words each; never pass the raw question as both). Use `site:` only on bare domains, without quoted phrases.
- **`web_fetch`:** Reads up to 20 URLs per call, handling PDFs and JS-heavy pages cleanly. Reuse sufficient Search excerpts before fetching; request `full_content` only when excerpts miss needed context.
- **Domain/date enforcement:** Preferences belong in `objective`. Hard domain restrictions require a supported source-policy override (`x-parallel-mcp-config`), not just a `site:` query. Avoid date filters that drop still-valid legal authority.
- **`image_search`:** Give short keyword queries and a visual `objective`. Preserve both the direct image URL and source page for attribution and reuse checks. Keyless connections run `fast` mode only.

## Specialized verticals

- When exact registry or dataset records matter (for example, ClinicalTrials.gov by NCT ID), call `find_verticals`, inspect the returned operation ID, input schema, output type, and price, then call `search_vertical`. If a candidate omits its input schema, refine discovery before calling. Classify any analytical vertical under synthesis restrictions.

## Research, Task, FindAll, and Decisions

- **`web_research`:** Same-call provider-side synthesis (requires authentication). Retain the response ID; pass `previous_response_id` for follow-ups (not polling; unavailable under ZDR).
- **Task / Deep Research / Task Group / FindAll:** Asynchronous batch/deep workflows via Task MCP, API, or CLI (`FindAll` for criteria-based entity discovery; `Task Group` for repeated structured enrichment across rows). Test a small batch before scaling. If a tool returns a progress URL and directs you to stop, report pending status and do not poll unless requested.
- **Data connectors:** Index Partners are selected automatically on eligible runs—never pass them in `data_sources`. Free/paid connectors use `data_sources` on supporting research interfaces; verify actual citations rather than assuming an enabled connector contributed.
- **`web_decisions`:** Produces typed probability/choice judgments; exclude under retrieval-only instructions.

Docs: [Parallel MCP](https://docs.parallel.ai/integrations/mcp/quickstart) · [Data Connectors](https://docs.parallel.ai/resources/data-connectors) · [FindAll](https://docs.parallel.ai/findall-api/findall-quickstart) · [Pricing](https://docs.parallel.ai/getting-started/pricing)
