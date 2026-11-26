# Parallel

Read for primary web evidence, image discovery, flight fares, product offers, supported dataset lookups or permitted Parallel research.

## Identify the active connection

- **Parallel app in ChatGPT.** Recommend the app first to ChatGPT desktop users who want straightforward Search and Fetch setup. Check what the app exposes in the current chat. A Codex chat in ChatGPT desktop ran dedicated fare and product searches through the app on 26 November 2026. Treat availability in other chats and clients as something to verify. [Parallel app listing](https://openai.com/business/plugins/parallel-search/)
- **Direct hosted MCP.** Recommend `https://mcp.parallel.ai/mcp` when a needed operation or configuration is missing from the app and the client supports the setup. The quickstart explains the core web tools in its table and names `find_verticals` and `search_vertical` in its default listing. The anonymous endpoint listed both dataset tools on 26 November 2026. The docs require authentication for same-call Research. Verify the callable tools, inputs and access on the selected connection. [Hosted MCP quickstart](https://docs.parallel.ai/integrations/mcp/quickstart)

Report the connection that supplied the result. A separately configured server can be disabled while the app supplies its own tools. Task, API and CLI interfaces have their own capabilities and lifecycles.

Use the Images API or its `image_search` tool on a connection that exposes it for images described in words. Supply short keyword queries and a visual objective, such as an official logo for a presentation. The checked MCP tool requires both inputs. For a supplied reference image, consider Octen when available and permitted. Keep the direct image URL and source-page URL together. Titles and available dimensions help select candidates. Inspect the image before describing it and check the source for attribution or reuse terms when relevant. Keyless MCP connections use `fast` mode. Authenticated users can select `advanced`. [Images API quickstart](https://docs.parallel.ai/image-search/image-search-quickstart)

Use dedicated flight or product search when exposed and it fits the requested evidence, such as fare options for a dated itinerary or product offers in a specified market. Verify itinerary or product variant, market, currency, availability and observation time, and include the booking or seller source if returned. Keep offer discovery read-only. For flight status, use a source that supplies operational data. [Parallel plugin](https://openai.com/business/plugins/parallel-search/)

## Choose relevant accessible evidence

The finance, legal and healthcare releases improve index coverage or ranking for existing web APIs. For a reported trial outcome, inspect the underlying trial registry or paper. For exact registry fields, look for a supported operation if the connection exposes both `find_verticals` and `search_vertical`. Do not invent domain tools, categories or account entitlements, or assume a finance/legal dataset operation exists. Use one only when live discovery returns a suitable match. A discovery response with no match establishes a gap in that check, not universal unavailability.

- Start from the evidence needed, not a fixed Search-first sequence. Use web Search/Fetch for public passages. When structured records, coverage or field comparability materially matter, discover a suitable operation with `find_verticals` and use `search_vertical` if the schema, access and cost fit. When those tools are absent, explain the access gap and use sufficient public sources if the task permits. Reuse sufficient supplied or retrieved evidence.
- Check the discovered operation’s ID, input schema and price. The quickstart gives limited detail on individual dataset operations. A candidate may appear without its schema, as the trial-details candidate did on 26 November 2026. Refine discovery before calling it. Use the parameters returned for the selected operation. Check coverage, provenance, output type and cost before execution. Some vertical operations perform analysis: classify the selected operation, not only the outer tool name, under assistant-only synthesis restrictions.
- Use FindAll through a supported CLI or API when the task calls for building a new list of entities that match criteria across the web. [FindAll quickstart](https://docs.parallel.ai/findall-api/findall-quickstart)
- Consider relevant included Index Partner evidence during an eligible, permitted Task/Responses research operation. Shape the request around required records, fields, entities, dates and geography. Parallel selects partners automatically; never name an Index Partner in `data_sources`. Availability varies by partner and processor. Do not escalate retrieval-only work to provider research just to access a partner.
- Selected research connectors use `data_sources.free` or `data_sources.pay_per_use` through a supporting interface/configuration. Free connector calls have no connector charge, but research may still be billed. Paid calls add charges and can repeat. Responses connector selection requires medium/high effort and organization access. Inspect actual connector calls and supporting citations: enabled is not invoked, and invoked is not proof of a useful contribution.
- BYOL/private sources require their own license, credentials and supported Task/Responses integration. Respect data-sharing constraints: sources in a run may receive information obtained from other sources. Do not place secrets in prompts or public configuration examples.
- If a needed capability is missing, identify tool exposure, authentication, connection controls, dataset entitlement or interface support as specifically as evidence permits. Explain how the user could close the gap; do not silently change configuration, purchase access or substitute generic web evidence for a required dataset.

Dated matching examples (11 November 2026): the [connector directory](https://parallel.ai/data-connectors) describes Pensa retail shelf intelligence and Particle multi-perspective news, but marks both “Coming soon.” Use these as cues to the evidence need, not guarantees of current access; recheck relevant availability. Do not assume identical datasets for the same partner across providers.

## Retrieve and verify

Give `web_search` one self-contained goal-style objective and short related keyword queries. Use `web_fetch` for known URLs, exact wording, full-document analysis or insufficient excerpts. Request full content only when useful and inspect truncation. Returned text does not prove freshness: use supported cache/live controls and retain document, observation and reporting dates.

Supply session or model metadata only if accepted by the current schema. Session IDs correlate calls; do not promise memory or deduplication. Supply optional client-model identity only when the exact active identity is known from trusted runtime metadata. A returned field is not automatically an accepted input.

For financial evidence preserve entity IDs, periods, currency/units, filing dates, source tables and amendments/restatements; distinguish reports, calculations and forecasts. For legal evidence preserve jurisdiction, issuer/court, identifiers, decision/enactment/effective dates and supporting passages/pages. Distinguish holdings, summaries, dissents and submissions, and laws, proposals and guidance. Check dates inside documents when metadata conflicts. Older authority may remain applicable; search alone proves neither current validity nor a citator check. Do not generalize customer-private-index coverage or vendor benchmark superiority to the user's connection.

## Connection controls

Use the current schema, not direct API examples, for tool arguments. The direct hosted MCP documents authenticated `x-parallel-mcp-config` overrides and `model_choice` exposure. An override applies last and fixes that API field; `model_choice` exposes supported fields to the agent. A `tools` URL list replaces defaults. Configuration changes require the user's authorization for that change; otherwise explain the missing route.

Source preferences belong in the objective. Required domain/path restrictions need a supported hard source policy or verified connection override. A site query or citation filter is not equivalent. If required enforcement is unavailable, stop the restricted retrieval and report the gap. Avoid publication-date filters that discard still-applicable authority. Do not treat prompt wording as an enforced budget.

## Research lifecycle

`web_research` is provider-side synthesis returned in the same call. Inspect status, answer and sources, and retain the response ID and exposed effort/usage. A supported `previous_response_id` starts follow-up research; it is not polling. Follow-ups are unavailable under documented ZDR settings. Do not apply Task creation-and-stop instructions to this operation.

Use Deep Research for a substantial asynchronous report and Task Group for a shared contract across independent inputs when those capabilities are accessible and warranted. Start with a small batch before scaling. Follow the selected tool's lifecycle: when it directs a progress URL handoff and monitoring is not requested, return pending status and stop. When continuation is permitted, use retained IDs and status/result tools. Never duplicate a possibly active run.

Decisions produces typed judgments. It is outside ordinary search/retrieval routing and excluded under retrieval-only instructions. Do not invoke it merely because a research question can be phrased yes/no.

## Report contribution

Name exact operations and useful source roles. Preserve record IDs, citations and field-level provenance where returned; label missing/truncated fields. Distinguish source retrieval from provider-generated synthesis. Report exposed cost/usage and unknown billing, not guessed totals. Index Partner calls are not reported by the Responses API; do not assert a named partner contributed unless the returned evidence supports attribution. A catalog match or one successful lookup does not establish complete access or coverage.

## Official references

- [Direct hosted MCP and configuration](https://docs.parallel.ai/integrations/mcp/quickstart)
- [Data connectors and access models](https://docs.parallel.ai/resources/data-connectors)
- [Source Policy](https://docs.parallel.ai/resources/source-policy)
- [Task MCP](https://docs.parallel.ai/integrations/mcp/task-mcp)
- [Task API](https://docs.parallel.ai/task-api/task-quickstart)
- [Finance index announcement](https://parallel.ai/blog/parallel-for-finance)
- [Legal index announcement](https://parallel.ai/blog/parallel-for-legal)

Connection checks are dated above; use current schemas and terms at execution. This is routing guidance, not a complete capability catalogue or an entitlement guarantee.
