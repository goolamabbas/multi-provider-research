# Firecrawl

Read for site inventory, bounded collection, document parsing, structured extraction, or requested Firecrawl work. The operation map below is historical guidance; inspect the current callable schema. Firecrawl was not exposed in the registry inspected on 2026-09-13, so no live behavior was revalidated.

- Match the operation to the evidence job: Search discovers results; Scrape retrieves one supplied page; Map inventories site URLs without page bodies; Crawl collects a bounded multi-page section; Parse handles supported document files.
- Use structured JSON extraction when the requested fields are known; use Markdown when readable page content is genuinely needed. Keep crawl limits, paths, depth, subdomains, and external-link scope conservative unless broader coverage is requested.
- Use Firecrawl Agent only for requested asynchronous multi-source research and resume it through the corresponding status tool. Do not start a duplicate while a job may still be active.
- Use Developer Search for programming questions and the dedicated research tools for literature lookup when those indexed sources fit. Do not confuse the general Search `research` category with the paper-search surface.
- Treat Interact and Monitor as separate authorization boundaries. Interact can cause persistent website actions, and Monitor creates recurring external checks; use them only when the user explicitly requests the corresponding interaction or monitoring outcome.
- Prefer Firecrawl over ordinary fetchers when the distinct need is URL inventory, site-scale crawling, document parsing, or schema-driven webpage extraction. Prefer TinyFish for a focused browser-rendered read or user-directed interactive task when site-scale extraction is not required.

Map returns URLs, not page bodies; do not treat its output as evidence for claims on those pages. For a single dynamic page, prefer a reading operation before Interact. For ordinary static reading, use the selected provider's fetcher unless another provider has a distinct role.

Report the selected operation, material URL/path/page/depth limits, output format, freshness or access gaps, asynchronous status, and any authorized persistent or recurring action.
