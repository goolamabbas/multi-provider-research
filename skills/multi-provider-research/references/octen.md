# Octen

Read for Octen discovery or page reading. Inspect the selected interface's current schema; MCP and direct HTTP arguments can differ.

- Use Search for a focused lookup and its news topic for current-news discovery. Use separate image/video search only when that evidence is requested and the capability is callable and permitted.
- Use Broad Search when several distinct angles justify its fan-out. Submit one self-contained question that preserves intent, resolves conversational references, and fits the live input limit. Let the tool expand it; use targeted follow-ups for remaining gaps rather than repeating broad discovery. A simple comparison may need only targeted searches.
- When source context is needed, explicitly request full content using the interface's controls and inspect the returned text. The MCP Search and Broad Search schemas inspected on 2026-09-13 expose top-level `full_content: {enable: true}` and an optional `max_tokens`. Full content is optional; do not request every page body when sufficient evidence is already returned.
- Use Extract for supplied URLs or missing, truncated, unusable, or stale content. Reuse sufficient search content. Leave Extract's `query` unset when the full body is needed: the inspected schema describes query mode as relevance-ranked highlights instead of the full body.
- Inspect cache-age validation when freshness matters; do not assume that zero is accepted. Preserve source dates and report any remaining freshness gap.

A paired MCP Search check on 2026-09-13 returned highlights with full-content controls omitted and page content with explicit enablement. Extract also returned the requested article with `max_age_seconds: 300`. Broad Search execution, direct HTTP behavior, billing, and official Octen skill execution were not tested in that check. These observations are not guarantees of complete or fresh content on every page.

Report material query transformations, content-depth or freshness limitations, and any failed or partial extraction.
