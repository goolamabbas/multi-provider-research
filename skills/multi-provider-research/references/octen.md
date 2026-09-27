# Octen

Read for Octen discovery or page reading. Inspect the selected interface's current schema; MCP and direct HTTP arguments can differ.

- Use Search for a focused lookup and its news topic for current-news discovery. Use separate image/video search only when that evidence is requested and the capability is callable and permitted.
- Use Broad Search when several distinct angles justify its fan-out. Submit one self-contained question that preserves intent, resolves conversational references, and fits the live input limit. Let the tool expand it; use targeted follow-ups for remaining gaps rather than repeating broad discovery. A simple comparison may need only targeted searches.
- When source context is needed, explicitly request full content using the interface's controls and inspect the returned text. Where exposed by the live MCP schema, use top-level `full_content: {enable: true}` and optional `max_tokens`. Full content is optional; do not request every page body when sufficient evidence is already returned.
- Use Extract for supplied URLs or missing, truncated, unusable, or stale content. Reuse sufficient search content. Leave Extract's `query` unset when the full body is needed: the inspected schema describes query mode as relevance-ranked highlights instead of the full body.
- Inspect cache-age validation when freshness matters; do not assume that zero is accepted. Preserve source dates and report any remaining freshness gap.

Returned content is not guaranteed to be complete or fresh; inspect it for the requested evidence.

Report material query transformations, content-depth or freshness limitations, and any failed or partial extraction.
