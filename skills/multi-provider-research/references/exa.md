# Exa

Read for semantic discovery, specialized fields, or permitted Agent research. Search verticals and Connect providers are different surfaces.

## Search and Fetch

- Translate terse input into an intent-preserving description of the ideal sources because Exa retrieval is semantic.
- Use regular Search for ordinary semantic discovery and independent cross-checking.
- When the evidence matches a specialized index, use the current People, Company, Code/GitHub, News, or other vertical only when exposed by the live schema. Treat search verticals as distinct from Exa Connect providers.
- Use Advanced Search only when precise domain, date, category, freshness, text, location, or subpage controls matter.
- Use Fetch for known URLs or when search content is insufficient.

## Agent and Connect

Treat Agent as provider-side inference, including when a simple lookup uses Connect. Use it for multi-step research, enrichment, structured list-building, or a materially matched dataset when synthesis restrictions permit it.

Inspect the current `dataSources` enum, select only providers needed for the requested fields, and name them in the query. Request those fields plus source, timestamp, or evidence fields in `outputSchema`. Match array limits to the requested scope; do not silently turn a comprehensive-list request into a small sample. Allow unknown fields rather than forcing unsupported values.

Retain and resume the same run ID until a terminal state or genuine stopping condition. An interrupted call or polling timeout is not cancellation; do not start a duplicate while a run may still be active. `previousRunId` starts a new follow-up using a completed run as context; it is not how to poll an active run. Use `input.data` for rows to process or enrich and `input.exclusion` for entities already found when expanding a list. Further runs incur their own costs and must remain within the authorized scope and budget.

Inspect the completed result for actual provider contribution, field provenance, errors, and partial coverage. Requested `dataSources` alone do not prove use. Separate provider-backed fields, Agent inference, and ordinary web evidence; label contribution unverified when it cannot be confirmed.

### Effort and Agent Ultra

Choose the smallest sufficient supported effort. Ultra is an optional Agent effort, not a separate provider or Connect dataset. Use it for large list-building, deep multi-source research, or hard-to-verify criteria when completeness matters more than latency or cost and provider-side synthesis is permitted. Ordinary lookups and supplied-page reading should stay on retrieval routes. A clearly suitable Ultra task does not require a preliminary lower-effort run.

Inspect the callable effort enum, budget fields, and lifecycle controls. A connector may expose `effort: "ultra"` without exposing the direct API's budget or stop controls. Do not pass unsupported fields or describe a natural-language spending instruction as an enforced limit. If a required limit cannot be expressed, resolve the interface or budget boundary before starting; do not silently accept a higher default cap or switch interfaces. Existing sufficient authorization does not require another confirmation.

As checked on September 26, 2026, Exa documents Ultra as metered usage with a default $20 run cap, not a fixed $20 charge. The direct API accepts `budget.maxCostDollars` from $1 to $100 for `auto` and `ultra`; `budget.maxDurationSeconds` from 300 to 10,800 is a soft duration ceiling for Ultra only. Exa describes complex runs as typically about 30 minutes, potentially three hours. These are dated provider terms, not measured performance; recheck applicable pricing and Connect charges before a material expenditure. Prefer fixed effort when predictable per-request pricing meets the task.

Inspect `stopReason` separately from terminal status. `budget_reached`, `time_limit_reached`, or `stopped` returns what was found within that limit; qualify coverage accordingly. `schema_satisfied` reports task completion, not independent proof that every qualifying entity exists in the results. Report returned cost, effort, evidence gaps, and material limits; disclose unavailable usage metadata instead of substituting the cap for actual cost. Distinguish the provider's graceful stop operation, which retains findings, from cancellation, and use only exposed controls under the user's stopping instructions.

Official references: [Ultra](https://exa.ai/docs/agent/agent-ultra.md), [Agent request and response schema](https://exa.ai/docs/reference/agent-api/create-a-run.md), and [pricing](https://exa.ai/docs/reference/pricing.md). Vendor benchmark claims do not establish superiority for the current task.

## Connect provider map

The provider IDs below were exposed in the callable schema on 2026-09-13. Field descriptions remain routing hints from the 2026-09-03 catalog; no Connect run or commercial/access validation was performed in the September 13 audit. Reinspect the live enum before use. Documented partners, including [additional partners](https://exa.ai/docs/reference/agent-api/connect/additional-partners), are not guaranteed account access.

| Provider ID | Use when the requested evidence concerns | Prefer provider-backed fields such as |
| --- | --- | --- |
| `particle` | Podcasts, guests, hosts, spoken commentary, narrative or sentiment monitoring | show, episode, air date, speaker, speaker role, timestamp, transcript window, stance |
| `fiber` | B2B companies, people, jobs, professional profiles, headcount, funding, or job-change signals | entity identity, domain, role, employer, employee count, funding stage, dated signal |
| `financial_datasets` | U.S. public-company prices, fundamentals, statements, earnings, ownership, SEC filings, or screening | ticker, reporting date, price timestamp, metrics, filing form and date, direct filing link |
| `similarweb` | Website traffic, rankings, engagement, digital footprint, or competitor discovery | domain, estimated visits, period, rank, engagement measure, competitor domain |
| `baselayer` | U.S. business verification, registrations, entity structure, officers, KYB, or risk checks | legal name, jurisdiction, registration status, officers, verification status, risk result |
| `affiliate` | Product discovery, merchant catalogs, prices, brands, or shopping comparisons | product, brand, price and currency, merchant, offer URL, observation time |
| `jinko` | Travel destination discovery or live airfare comparisons | origin, destination, dates, cabin, fare and currency, itinerary, observation time |
| `polymarket` | Prediction markets, market-implied probabilities, price history, order books, or public trader positions | market and event, outcome, implied probability, observation time, volume or liquidity, price history, market URL |

Documentation:

- Particle: https://exa.ai/docs/reference/agent-api/connect/particle
- Fiber.ai: https://exa.ai/docs/reference/agent-api/connect/fiber
- Financial Datasets: https://exa.ai/docs/reference/agent-api/connect/financialdatasets
- Similarweb: https://exa.ai/docs/reference/agent-api/connect/similarweb
- Baselayer: https://exa.ai/docs/reference/agent-api/connect/baselayer
- Affiliate.com: https://exa.ai/docs/reference/agent-api/connect/affiliatecom
- Jinko: https://exa.ai/docs/reference/agent-api/connect/jinko
- Polymarket: https://exa.ai/docs/reference/agent-api/connect/polymarket

## Matching examples

Match the requested fields and coverage, not just the topic. Prefer a specialized dataset when it materially supplies the needed evidence; an authoritative supplied document may already satisfy a document-reading request. Explicit provider requirements and synthesis restrictions still apply.

- A request about what podcast speakers said should trigger a Particle availability check even if it says only “use Exa.”
- A request for company traffic estimates should trigger Similarweb, not generic web estimates.
- A request to screen companies using comparable financial or ownership fields should trigger a Financial Datasets availability check. Reading one supplied official filing can be satisfied directly without an enrichment run. Never present ordinary web evidence as structured provider data.
- A request for current prediction-market odds or their history should trigger a Polymarket availability check rather than treating commentary about the odds as market data.
- A company research task may justify more than one provider only when the output requires distinct fields, such as Fiber firmographics plus Similarweb traffic. Avoid automatic multi-provider enrichment.

Report requested versus confirmed providers, material field provenance and missing coverage, and exposed Agent model or preset metadata.
