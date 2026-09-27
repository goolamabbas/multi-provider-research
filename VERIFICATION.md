# Historical verification log

These observations were moved from provider references in v0.4.2. They are historical records, not current availability, pricing, or performance guarantees. This packaging release did not repeat the provider checks. Operational decisions use the live schema and applicable current terms.

## Exa Ultra — 26 September 2026

As checked on September 26, 2026, Exa documents Ultra as metered usage with a default $20 run cap, not a fixed $20 charge. The direct API accepts `budget.maxCostDollars` from $1 to $100 for `auto` and `ultra`; `budget.maxDurationSeconds` from 300 to 10,800 is a soft duration ceiling for Ultra only. Exa describes complex runs as typically about 30 minutes, potentially three hours. These are dated provider terms, not measured performance; recheck applicable pricing and Connect charges before a material expenditure. Prefer fixed effort when predictable per-request pricing meets the task.

## Exa Connect — 3 and 13 September 2026

The provider IDs below were exposed in the callable schema on 2026-09-13. Field descriptions remain routing hints from the 2026-09-03 catalog; no Connect run or commercial/access validation was performed in the September 13 audit. Reinspect the live enum before use. Documented partners, including [additional partners](https://exa.ai/docs/reference/agent-api/connect/additional-partners), are not guaranteed account access.

## Octen — 13 September 2026

A paired MCP Search check on 2026-09-13 returned highlights with full-content controls omitted and page content with explicit enablement. Extract also returned the requested article with `max_age_seconds: 300`. Broad Search execution, direct HTTP behavior, billing, and official Octen skill execution were not tested in that check. These observations are not guarantees of complete or fresh content on every page.

## TinyFish — 13 September 2026

These are routing hints, not guaranteed exposed tools; TinyFish was absent from the registry inspected on 2026-09-13.

## Parallel — 13 September 2026

Use the current status/result tools with retained identifiers when continuation is permitted. The createDeepResearch description inspected on 2026-09-13 still directs sharing the URL and stopping unless otherwise instructed. This is a lifecycle rule for that surface, not a universal polling rule. No Task run was launched in that audit.

## Scope

The Octen schema snapshot exposed top-level `full_content: {enable: true}` and optional `max_tokens` for Search and Broad Search. Execution coverage is limited as recorded above. The published [ChatGPT + TinyFish beginner walkthrough](https://goolamabbas.github.io/separate-intelligence-and-search/guide/tinyfish-beginner/) records a later, separate Search/Fetch run; the earlier absence observation is not a current availability claim.
