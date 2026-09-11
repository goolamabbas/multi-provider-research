# Provider routing

Use this reference only when selecting among research providers or considering Exa Connect.

## Dynamic selection rule

The live callable tool schema is the availability source of truth. The catalog below is a maintenance snapshot last inspected on **2026-09-03**, not guaranteed access. Inspect the current Exa Agent `dataSources` enum before execution. If documentation and the callable schema disagree, follow the schema and report the discrepancy.

Apply provider constraints in this order: explicit inclusions or exclusions, named-provider requests, materially matched specialized data, then a generic default. A named provider is required for its requested role, but is exclusive only when the request says so. Follow the entrypoint boundary rules before adding a complementary provider.

## Parallel boundaries

The live schema inspected on **2026-09-03** exposed two separate MCP surfaces:

- **Search MCP:** `web_search` returns ranked sources and LLM-oriented excerpts; `web_fetch` retrieves relevant excerpts or optional full content from up to 20 supplied URLs. Use one stable session ID across related calls.
- **Task MCP:** `createDeepResearch` starts a single-topic analyst-style report, while `createTaskGroup` applies a consistent text or JSON output request to a list. `getStatus` and `getResultMarkdown` resume an existing task or group.

Search and Fetch are retrieval. Deep Research and Task Groups perform provider-side research or enrichment. Follow the live Task MCP stopping rule: after starting a task, return its progress URL and do not poll unless the user asked for monitoring or later requests the result.

Parallel overlaps ordinary discovery providers. Route to it when the user names it or when its answer-ready excerpts, shared search/fetch session, asynchronous deep research, or consistent batch enrichment is a distinct requirement. Do not add it merely to duplicate an already successful search.

## Firecrawl boundaries

The live schema inspected on **2026-09-03** exposed these main evidence lanes:

| Operation | Distinct result |
| --- | --- |
| Search | Ranked web, news, image, developer, or research-site results; page content only when scrape options are requested |
| Scrape | Content or schema-driven fields from one supplied URL |
| Map | URL inventory for a site, without retrieving every page body |
| Crawl | Bounded multi-page collection with path, depth, sitemap, subdomain, and external-link controls |
| Parse | Parsed content or structured fields from a supported document |
| Agent | Asynchronous multi-source provider-side research |
| Developer and research tools | Indexed programming evidence or scientific-paper records and passages |
| Interact and Monitor | Live browser actions or recurring external checks that require their own authorization |

Use Firecrawl when site topology, bounded crawling, document parsing, or structured extraction is the reason for the provider choice. For a single dynamic page, prefer Scrape before Interact. For ordinary static reading, use an already selected provider's fetcher rather than adding Firecrawl without a distinct role.

## Exa Connect self-serve provider map

At the snapshot date, the live `dataSources` enum and Exa's current Connect documentation expose the eight self-serve providers below. Exa also documents [additional Connect partners](https://exa.ai/docs/reference/agent-api/connect/additional-partners) that require account enablement. Treat any provider as unavailable until it appears in the current callable schema, and do not infer successful contribution or commercial terms from the catalog alone.

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

## Connect execution checks

1. Confirm the provider ID exists in the current `dataSources` enum.
2. Pass only the relevant provider IDs.
3. Describe the provider-specific evidence in the Agent query.
4. Require those fields, plus evidence or timestamps, in `outputSchema`.
5. Poll the same run ID until completion or a genuine stopping condition.
6. Inspect nested result metadata, provider usage, errors, and missing fields.
7. If provider contribution cannot be confirmed, label it unverified and do not attribute the data to that provider.
