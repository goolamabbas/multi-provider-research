# Octen

Read for Octen discovery, structured records, media or page reading. Inspect the callable schema: plugin, MCP and HTTP options can differ. A visible tool does not establish account access or successful execution. This reference covers the nine plugin operations below.

## Choose the operation

| Evidence needed | Route when exposed |
| --- | --- |
| Likely official site, documentation or help URL | Pulse (`pulse_search`); candidates are not page-content evidence |
| One focused general-web question | Search (`search`) |
| Current reporting on one topic | News Search (`news_search`), not an invented Search `topic` parameter |
| Company or professional-person profiles, products, financial fields or comparisons | Business Search (`business_search`); verify field provenance and periods |
| Named-area or nearby places, reported hours and review evidence | Place Search (`place_search`) |
| Several independent research angles | Broad Search (`broad_search`); use a focused operation when it suffices |
| Visual references or similar images | Image Search (`image_search`) |
| Videos, tutorials or matching clips | Video Search (`video_search`), conditional on early-access entitlement |
| A supplied URL or missing source context | Extract (`extract`) |

Select media when it is part of the requested outcome; the user need not name the tool. Do not add unrelated media searches to text research. Inspect access failures and respect explicit provider/fallback constraints. Do not request early access or change account settings as a side effect.

## Retrieval and output boundaries

- Default to source retrieval and synthesis by the current assistant. For News Search, set `subjects.enable: false` under assistant-only synthesis. Storylines contain provider summaries and are on by default. Domain filters constrain ranked articles, not storylines; do not use broader-web storylines to answer a source-restricted request. Use publication-date controls for reporting windows, and distinguish publication from crawl and event dates.
- Business entity cards are on by default; Octen documents their facts as extracted fields. Domain, time and language filters constrain ranked sources, not cards. Distinguish structured facts, source excerpts and generated descriptions; do not assume all cards are generated prose or all fields are source-faithful. For source-only work whose card provenance/output cannot be established, use `entities.enable: false` and ranked source evidence. Preserve entity identifiers, financial units/periods, observation dates and missing fields. Verify material facts against sources; a multi-company query need not cover each company evenly.
- Place records are reported data, not guaranteed live opening status. Use a named area or user-provided location; ask for missing location when essential. Coordinates must be paired and radius requires coordinates. Approximate location does not establish exact distance. Request review excerpts only when needed; a few reviews are not representative sentiment. Optional `web_search` is off by default and its filters govern web results, not place cards. Follow sources for material unresolved details rather than treating a website field as evidence for every card field.
- If a required output control is unavailable, disclose the limitation and use another permitted source-only operation if sufficient; do not silently relax the synthesis or source restriction.

## Search depth and source reading

Pulse Lite returns titles/URLs and ignores content options; Standard can add content. At most ten candidates are returned. Standard's first result has included full content; additional bodies are billed. Do not apply Web/Broad Search's ten-result content allowance to Pulse. Use News or Search for freshness, filters and actual open-web evidence, rather than Pulse as a cheaper substitute.

For Broad Search, submit one self-contained question preserving intent, resolving references and fitting the live length limit. Let the tool expand it. Bound sub-query/result counts and repair specific gaps with targeted follow-ups; do not repeat broad discovery. Results can repeat across sub-queries: deduplicate sources before counting coverage. A simple comparison may need only focused searches or Business Search.

Reuse sufficient highlights. When needed, explicitly enable full content using supported controls (for this MCP, `full_content: {enable: true}` with optional `max_tokens`). Inspect returned text: a requested body or token cap is not a completeness guarantee.

Use Extract for supplied URLs or missing, truncated, unusable or stale context. Leave `query` unset for the full body; query mode returns relevance-ranked highlights instead. Standard suits ordinary pages; retry only failed or skeletal pages with advanced when permitted and useful, or use auto for a mixed batch. Advanced can cost more; inspect resolved mode and usage when exposed. A success status alone does not prove a usable body. Inspect `page_structure` labels such as `No Main Content` alongside the text for login walls or error pages. Respect runtime cache-age bounds and disclose freshness gaps.

Optional extracted links help follow references from supplied pages; they are not a site crawl. Image/audio/video URLs are resources, not proof their content was viewed or transcribed.

## Media

Image Search accepts exactly one of text `query`, reference `image_url`, or `image_data`. Preserve source-page links and inspect the image where visual claims matter. Similarity is not provenance and discovery does not grant reuse rights. Treat returned descriptions/summaries as metadata to verify, not source-only analysis.

Video Search is documented as beta/early access. If the account is known to lack access, report that without a probe; otherwise distinguish callable from successfully executed. Retain actual source links, duration and any matching segment returned. Search metadata is not proof of watching a video or reading its transcript. Never invent a segment or transcript.

## Reporting and references

Report actual operations, material query changes, returned evidence, gaps, mode/freshness limits and usage when exposed. Missing billing metadata does not prove a free call. Consult current [MCP documentation](https://docs.octen.ai/integrations/octen-mcp-server), [Pulse documentation](https://docs.octen.ai/capabilities/pulse-search) and [pricing](https://docs.octen.ai/overview/pricing) where needed. For documentation reads, prefer the official `.md` edition when it exposes otherwise hidden tabs; translate HTTP examples to the actual callable schema rather than copying their parameters.
