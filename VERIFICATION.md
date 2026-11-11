# Historical verification log

These observations were moved from provider references in v0.4.2. They are historical records, not current availability, pricing, or performance guarantees. This packaging release did not repeat the provider checks. Operational decisions use the live schema and applicable current terms.

## Exa Ultra — 26 September 2026

As checked on September 26, 2026, Exa documents Ultra as metered usage with a default $20 run cap, not a fixed $20 charge. The direct API accepts `budget.maxCostDollars` from $1 to $100 for `auto` and `ultra`; `budget.maxDurationSeconds` from 300 to 10,800 is a soft duration ceiling for Ultra only. Exa describes complex runs as typically about 30 minutes, potentially three hours. These are dated provider terms, not measured performance; recheck applicable pricing and Connect charges before a material expenditure. Prefer fixed effort when predictable per-request pricing meets the task.

## Exa Connect — 3 and 13 September 2026

The provider IDs listed in the [Connect provider map](skills/multi-provider-research/references/exa.md#connect-provider-map) were exposed in the callable schema on 2026-09-13. Field descriptions remain routing hints from the 2026-09-03 catalog; no Connect run or commercial/access validation was performed in the September 13 audit. Reinspect the live enum before use. Documented partners, including [additional partners](https://exa.ai/docs/reference/agent-api/connect/additional-partners), are not guaranteed account access.

## Octen — 13 September 2026

A paired MCP Search check on 2026-09-13 returned highlights with full-content controls omitted and page content with explicit enablement. Extract also returned the requested article with `max_age_seconds: 300`. Broad Search execution, direct HTTP behavior, billing, and official Octen skill execution were not tested in that check. These observations are not guarantees of complete or fresh content on every page.

## TinyFish — 13 September 2026

TinyFish support has been removed in the current draft; this observation is retained only as history. TinyFish was absent from the registry inspected on 2026-09-13.

## Parallel — 13 September 2026

Use the current status/result tools with retained identifiers when continuation is permitted. The createDeepResearch description inspected on 2026-09-13 still directs sharing the URL and stopping unless otherwise instructed. This is a lifecycle rule for that surface, not a universal polling rule. No Task run was launched in that audit.

## Scope

The Octen schema snapshot exposed top-level `full_content: {enable: true}` and optional `max_tokens` for Search and Broad Search. Execution coverage is limited as recorded above. The archived [ChatGPT + TinyFish beginner walkthrough](https://github.com/goolamabbas/separate-intelligence-and-search/tree/main/archive/tinyfish-beginner) records a later, separate Search/Fetch run; the earlier absence observation is not a current availability claim.

## Exa Library — 10 November 2026 (0.6.0)

Structural validation passed with the skill-creator validator in an isolated PyYAML environment. Local reference destinations were checked. Twelve new Library cases received manual dry-run decision traces; no independent agent evaluation or live execution of those fixtures was performed. Existing provider restrictions and Agent budget/lifecycle guidance were retained.

The preceding documentation review executed one podcast-scoped Exa Advanced Search and one episode Fetch, returning episode pages and a timestamped, speaker-labelled transcript excerpt. This demonstrates that path only, not improved retrieval quality or performance of the revised skill. No Places, partner-data or Agent scenario was executed. The Library homepage failed in Exa Fetch; Parallel supplied it, and direct HTTPS checks confirmed key Places and podcast limitations. Sources: https://exa.ai/library ; https://exa.ai/library/place ; https://exa.ai/library/podcast .

No release or personal installation was performed. Version metadata remains at the existing release pending approval.

## Parallel coordinated draft — 11 November 2026

Current unified MCP and Data Connectors docs were retrieved through Parallel Fetch; Search supplied the official Finance announcement. Earlier same-day legal review retrieved the Legal announcement and tested primary-source discovery. Callable Search/Fetch, Research and vertical schemas were inspected. Search/Fetch did not accept session or client-model fields; Research did not expose data_sources.

find_verticals returned clinical_trials.get_trial_details with a required nct_id and $0 price. One search_vertical lookup for NCT04280705 returned the identifier, title, completed status and official registry citation, with cost_usd 0. The response was truncated: last-update date and completeness were not verified. This tests one direct-record path, not all verticals or research connectors.

No configuration changes, paid research, Task jobs, BYOL calls or Index Partner attribution tests were performed. Connector overrides and entitlement behavior are documented, not executed. Manual behavioral cases are consistency checks, not independent model evaluations. Benchmark claims were not reproduced. These checks preceded the authorized v0.7.0 publication and personal installation.


## Parallel distinction clarification — 11 November 2026 (v0.7.1)

Targeted wording update based on the previously reviewed discovery evidence. Only the Parallel reference changes operational guidance; skill version and release documentation are updated for packaging. Structural validation and release integrity are checked during publication. No new provider availability test or benchmark was run.


## Provider scope removal — 11 November 2026 (v0.8.0)

Removed Firecrawl and TinyFish from maintained routing and the installable references. Structural validation passed; the coordinated guide build, internal links, prompt payloads and starter filtering passed. No new live provider execution or independent behavioral evaluation was performed for this scope reduction. Historical observations above do not imply continued support. Release and installed file integrity are verified during publication.


## Keenable local draft — 11 November 2026

Added scoped Search/Fetch guidance. Six practical calls (four Pro searches, two live fetches without prompt) checked dated announcement discovery, one long HTML methodology and a multi-angle access/cost comparison. All returned results. Search required a targeted follow-up for an omitted provider and produced HTML/Markdown duplicates; announcement metadata and printed date differed. No billing metadata was exposed. Realtime, point-in-time, public-endpoint connection, cards, prompted Fetch and error recovery remain unexecuted. Manual review of 14 routing cases is not an independent behavioral evaluation. Structural validation and local reference checks passed. Guide build, 626 internal links, 71 copy payloads and four-starter/four-Keenable indexing checks passed. Release v0.9.0 approved for publication and personal installation; release integrity and installation are verified separately during delivery.


## Octen expanded routing — local draft, 11 November 2026

Five bounded direct tool checks completed: Pulse, source-only News, source-only Business, Places and text Image Search. No Video execution because account early access is absent. Uneven company coverage, older source/image dates and unverified place hours are recorded in the local review. Thirteen manual decision cases added; these are not independent agent evaluations. Skill structural validation and guide build, internal links and source-to-rendered prompt checks passed. Release v0.10.0 approved for publication and personal installation; package and installed-file integrity are verified during delivery.
