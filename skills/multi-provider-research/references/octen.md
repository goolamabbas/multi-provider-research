# Octen

Use for fast official-URL discovery (`Pulse`), focused or broad multi-angle web search, current news, company/person cards, local places, visual/reference-image search, or page extraction. Inspect the live MCP schema—exposed operations vary by plan and version (including newer Premier and Design search tools).

## Operation selection

- **Pulse:** Fast lookup for likely official homepages or docs URLs (candidates only, not page-content evidence). Use Search or News for actual evidence and freshness.
- **Search / Premier Search:** Focused general-web lookup. Explicitly request full content (`full_content: {enable: true}` when exposed) if you need page bodies, to avoid separate Extract calls.
- **Broad Search:** Pass one self-contained question (resolve pronouns from prior context) and let Octen expand sub-queries. Bound sub-queries/results—each sub-query can be billable—and deduplicate repeated URLs.
- **News Search:** Current reporting. Set `subjects.enable: false` under assistant-only synthesis (storylines are provider summaries on by default, and domain filters apply to articles, not storylines).
- **Business Search:** Company/person entity cards plus ranked sources. Cards do not inherit domain/date/language filters, and default `entities.count` is 2 (set explicitly for 3+ entities). Corroborate key card figures in underlying sources; set `entities.enable: false` if strict source-only provenance is required.
- **Place Search:** Local venues, reported hours, ratings, and optional reviews. Requires a named area or paired coordinates (radius requires coordinates). Verify live hours on the venue's official page when timing matters.
- **Image / Video Search:** Image Search accepts text `query` **or** one reference image (`image_url` / `image_data`), never both. Preserve source-page links for attribution/rights. Video Search requires early-access entitlement; skip if known unavailable.
- **Extract:** For supplied URLs or missing/incomplete Search text. Leave `query` unset for the full page body (setting `query` returns highlights). Inspect `page_structure` (e.g. `No Main Content`) to spot login walls or empty shells; retry with `advanced` mode only on failed or skeletal pages.

Docs: [Octen MCP](https://docs.octen.ai/integrations/octen-mcp-server) · [Pricing](https://docs.octen.ai/overview/pricing)
