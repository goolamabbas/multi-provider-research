# Parallel

Read for objective-shaped web evidence, financial/legal sources, specialized records or permitted Parallel research. Inspect the relevant live tools; the unified MCP can expose retrieval, vertical discovery/querying and authenticated same-call research. Task/API/CLI workflows have separate capabilities and lifecycles.

## Choose relevant accessible evidence

- Start from the evidence needed, not a fixed Search-first sequence. Use web Search/Fetch for public passages. When structured records, coverage or field comparability materially matter, use `find_verticals`, inspect a matching operation, then `search_vertical`. Reuse sufficient supplied or retrieved evidence.
- Discovery returns IDs, prices and schemas for best matches. If a relevant ID lacks its input schema, refine discovery. Use the returned contract rather than inventing parameters. Check coverage, provenance, output type and cost before execution. Some vertical operations perform analysis: classify the selected operation, not only the outer tool name, under assistant-only synthesis restrictions.
- Consider relevant included Index Partner evidence during an eligible, permitted Task/Responses research operation. Shape the request around required records, fields, entities, dates and geography. Parallel selects partners automatically; never name an Index Partner in `data_sources`. Availability varies by partner and processor. Do not escalate retrieval-only work to provider research just to access a partner.
- Selected research connectors use `data_sources.free` or `data_sources.pay_per_use` through a supporting interface/configuration. Free connector calls have no connector charge, but research may still be billed. Paid calls add charges and can repeat. Responses connector selection requires medium/high effort and organization access. Inspect actual connector calls and supporting citations: enabled is not invoked, and invoked is not proof of a useful contribution.
- BYOL/private sources require their own license, credentials and supported Task/Responses integration. Respect data-sharing constraints: sources in a run may receive information obtained from other sources. Do not place secrets in prompts or public configuration examples.
- If a needed capability is missing, identify tool exposure, authentication, connection controls, dataset entitlement or interface support as specifically as evidence permits. Explain how the user could close the gap; do not silently change configuration, purchase access or substitute generic web evidence for a required dataset.

Dated matching examples (11 November 2026): the [connector directory](https://parallel.ai/data-connectors) describes Pensa retail shelf intelligence and Particle multi-perspective news, but marks both “Coming soon.” Use these as cues to the evidence need, not guarantees of current access; recheck relevant availability. Do not assume identical datasets for the same partner across providers.

## Retrieve and verify

Give `web_search` one self-contained goal-style objective and short related keyword queries. Use `web_fetch` for known URLs, exact wording, full-document analysis or insufficient excerpts. Request full content only when useful and inspect truncation. Returned text does not prove freshness: use supported cache/live controls and retain document, observation and reporting dates.

Supply session or model metadata only if accepted by the current schema. Session IDs correlate calls; do not promise memory or deduplication. Supply optional client-model identity only when the exact active identity is known from trusted runtime metadata. A returned field is not automatically an accepted input.

Finance/Legal releases upgrade the index and ranking behind existing APIs; do not invent domain tools, categories or account entitlements. For financial evidence preserve entity IDs, periods, currency/units, filing dates, source tables and amendments/restatements; distinguish reports, calculations and forecasts. For legal evidence preserve jurisdiction, issuer/court, identifiers, decision/enactment/effective dates and supporting passages/pages. Distinguish holdings, summaries, dissents and submissions, and laws, proposals and guidance. Check dates inside documents when metadata conflicts. Older authority may remain applicable; search alone proves neither current validity nor a citator check. Do not generalize customer-private-index coverage or vendor benchmark superiority to the user's connection.

## Connection controls

Use the current schema, not direct API examples, for tool arguments. The unified MCP documents authenticated `x-parallel-mcp-config` overrides and `model_choice` exposure. An override applies last and fixes that API field; `model_choice` exposes supported fields to the agent. A `tools` URL list replaces defaults. Configuration changes require the user's authorization for that change; otherwise explain the missing route.

Source preferences belong in the objective. Required domain/path restrictions need a supported hard source policy or verified connection override. A site query or citation filter is not equivalent. If required enforcement is unavailable, stop the restricted retrieval and report the gap. Avoid publication-date filters that discard still-applicable authority. Do not treat prompt wording as an enforced budget.

## Research lifecycle

`web_research` is provider-side synthesis returned in the same call. Inspect status, answer and sources, and retain the response ID and exposed effort/usage. A supported `previous_response_id` starts follow-up research; it is not polling. Follow-ups are unavailable under documented ZDR settings. Do not apply Task creation-and-stop instructions to this operation.

Use Deep Research for a substantial asynchronous report and Task Group for a shared contract across independent inputs when those capabilities are accessible and warranted. Start with a small batch before scaling. Follow the selected tool's lifecycle: when it directs a progress URL handoff and monitoring is not requested, return pending status and stop. When continuation is permitted, use retained IDs and status/result tools. Never duplicate a possibly active run.

Decisions produces typed judgments. It is outside ordinary search/retrieval routing and excluded under retrieval-only instructions. Do not invoke it merely because a research question can be phrased yes/no.

## Report contribution

Name exact operations and useful source roles. Preserve record IDs, citations and field-level provenance where returned; label missing/truncated fields. Distinguish source retrieval from provider-generated synthesis. Report exposed cost/usage and unknown billing, not guessed totals. Index Partner calls are not reported by the Responses API; do not assert a named partner contributed unless the returned evidence supports attribution. A catalog match or one successful lookup does not establish complete access or coverage.

## Official references

- [Unified MCP and configuration](https://docs.parallel.ai/integrations/mcp/quickstart)
- [Data connectors and access models](https://docs.parallel.ai/resources/data-connectors)
- [Source Policy](https://docs.parallel.ai/resources/source-policy)
- [Task MCP](https://docs.parallel.ai/integrations/mcp/task-mcp)
- [Task API](https://docs.parallel.ai/task-api/task-quickstart)
- [Finance index announcement](https://parallel.ai/blog/parallel-for-finance)
- [Legal index announcement](https://parallel.ai/blog/parallel-for-legal)

Docs and selected schemas checked 11 November 2026; use current schemas and terms at execution. This is routing guidance, not a complete capability catalogue or an entitlement guarantee.
