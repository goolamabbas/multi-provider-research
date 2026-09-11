---
name: multi-provider-research
description: "Route provider-aware research across Octen, Exa Search/Agent/Connect, Perplexity, Parallel, Firecrawl, TinyFish, and X-native interfaces. Use when the user names one of these providers, requests X-native evidence, or needs specialized provider-backed data, batch web enrichment, site mapping or crawling, structured webpage extraction, or browser interaction. Do not use for explicitly native-search-only work."
---

# Multi-provider research

Use the minimum set of available providers that gives each research subproblem a distinct, task-appropriate evidence lane. Preserve the user's intent, constraints, model boundary, and named-provider choices.

## Workflow

1. **Set the boundaries.** Apply this precedence: explicit provider inclusions or exclusions, then named-provider requests, then a materially matched specialized dataset, then a generic discovery default. Naming a provider requires its contribution to the requested evidence lane; it does not by itself mean exclusivity. Honor “only,” “exactly,” and equivalent restrictions. Complementary providers may fill a distinct need within the authorized scope; do not silently replace a required provider or materially expand the task.
2. **Preflight only relevant capabilities.** Inspect exact callable tools and live schemas. Distinguish configuration or visibility, authentication and reachability, successful execution, and useful returned evidence. If a tool description conflicts with runtime argument validation, follow the runtime validation and report the mismatch.
3. **Set the model boundary.** Apply any explicit synthesis restriction. Otherwise default ordinary lookups to retrieval and harness synthesis; select provider-generated research or enrichment when the requested outcome warrants it. Ask only when an unresolved boundary would materially affect scope, cost, or data handling. An MCP or provider call does not imply that the provider uses the harness-selected model.
4. **Decompose and route.** Split the request into evidence subproblems, assign one provider role to each, and choose the minimum sufficient set. Do not repeat the same query or fetch the same URL across providers without a user-requested comparison or material verification reason.
5. **Execute and verify.** Preserve provider-appropriate query semantics, reuse asynchronous run IDs, inspect actual provider contribution, and inspect the underlying source content for material claims.
6. **Report proportionally.** Answer from verified evidence and state provider contributions, material controls, failures, substitutions, and gaps at the level warranted by the work.

An explicit harness-native-only instruction overrides this skill. If the skill was loaded automatically, stop external-provider routing and use only the permitted native tools. The skill works with any callable subset of supported providers, including one provider.

If a named or task-matched provider is unavailable, disclose the gap before a materially different fallback. Use a fallback only when the request permits it, label the different evidence class, and never imply that generic web evidence came from Connect or an X API.

When provider-side inference is permitted, identify the exact provider tool and its exposed model or preset. If the user requires harness-model-only synthesis, limit providers to retrieval, extraction, and page reading; do not use Perplexity Ask, Reason, or Research; Exa Agent; Parallel Deep Research or Task Group; Firecrawl Agent; or another provider-side answer or agent operation.

Classify the selected operation and output options, not just the tool name. A fetch or scrape tool may offer generated summaries or freeform answers; those modes are provider-side synthesis too. Under harness-only synthesis, choose source-content or faithful extraction modes and avoid options that generate conclusions. Retrieval, ranking, and extraction may still use internal machine learning; this boundary does not guarantee model-free processing.

For changing facts, inspect cache and freshness controls before retrieval and use a live fetch or an appropriate maximum cache age when supported. Distinguish retrieval time from publication, reporting-period, and observation dates. A successful fetch alone does not establish currentness; report material freshness uncertainty.

## Route the work

### Octen

- Use plain Search for a focused web lookup and its news topic when current news is the evidence lane.
- Use Broad Search for multi-angle discovery. Pass the original question unchanged because Broad Search performs its own query expansion.
- Use Extract for known URLs unique to Octen or when Octen is the requested reading surface.
- Use the separate image or video search capability only when the request requires visual or video discovery and that capability is callable and authorized.

### Exa Search and Fetch

- Translate terse input into an intent-preserving description of the ideal sources because Exa retrieval is semantic.
- Use regular Search for ordinary semantic discovery and independent cross-checking.
- When the evidence matches a specialized index, use the current People, Company, Code/GitHub, News, or other vertical only when exposed by the live schema. Treat search verticals as distinct from Exa Connect providers.
- Use Advanced Search only when precise domain, date, category, freshness, text, location, or subpage controls matter.
- Use Fetch for known URLs or when search content is insufficient.

### Exa Agent and Connect

- Treat Agent as provider-side agentic inference. Use it for genuine multi-step research, enrichment, structured list-building, or a materially matched Connect dataset.
- Inspect the live `dataSources` enum and select only providers needed for the requested fields. A simple lookup can warrant one Connect provider.
- Name the provider and provider-backed fields in the query and `outputSchema`; use bounded arrays and source, timestamp, or evidence fields where supported.
- Retain and resume the same run ID until a terminal state. Do not start a duplicate while a run may still be active.
- Inspect the completed result for actual provider contribution, field provenance, errors, and partial coverage. Requested `dataSources` alone do not prove use.
- Separate provider-backed data, Agent inference, and ordinary web evidence.

When Connect may apply, read [references/provider-routing.md](references/provider-routing.md).

### Perplexity

- Use Perplexity selectively and use one mode per subproblem by default.
- Use Search for ranked URLs, facts, or recent-news leads without a provider-generated narrative answer.
- Use Ask for a focused factual answer or concise cited explanation.
- Use Reason for comparison or decision analysis against explicit criteria using current web evidence.
- Use Research only for genuinely deep, comprehensive multi-source investigation whose added latency is justified.
- Inspect the selected tool's live schema; do not assume that Search, Ask, Reason, and Research expose the same controls.
- Treat Ask, Reason, and Research as provider-side synthesis. Preserve their cited URLs and inspect the underlying source content before using material claims. Report exposed model or preset metadata without guessing missing details.

### Parallel

- Treat the Search MCP and Task MCP as distinct surfaces. Use `web_search` for current web discovery and answer-ready excerpts; use `web_fetch` only for a known URL, exact wording, full-page analysis, or insufficient search excerpts.
- Give Search a self-contained objective plus concise related keyword queries. Reuse the same session ID across related Search and Fetch calls. Pass `model_name` only when the exact active model slug is known from trusted runtime metadata; it is analytics metadata, not a search-quality control.
- Use `createDeepResearch` for a genuinely deep single-topic, provider-generated report. Use `createTaskGroup` for applying the same requested fields or output to a list of items; test a small batch before scaling when the user authorizes a larger run.
- Treat Deep Research and Task Group output as provider-side research or enrichment. Follow the live asynchronous lifecycle: do not poll automatically or start duplicates when the tool instructs the agent to return a progress URL and wait for a later user request.
- Prefer Parallel Task over duplicate general research only when asynchronous depth or consistent batch enrichment is the distinct requirement. Exa Connect remains the specialized provider-backed-data lane.

### Firecrawl

- Match the operation to the evidence job: Search discovers results; Scrape retrieves one supplied page; Map inventories site URLs without page bodies; Crawl collects a bounded multi-page section; Parse handles supported document files.
- Use structured JSON extraction when the requested fields are known; use Markdown when readable page content is genuinely needed. Keep crawl limits, paths, depth, subdomains, and external-link scope conservative unless broader coverage is requested.
- Use Firecrawl Agent only for requested asynchronous multi-source research and resume it through the corresponding status tool. Do not start a duplicate while a job may still be active.
- Use Developer Search for programming questions and the dedicated research tools for literature lookup when those indexed sources fit. Do not confuse the general Search `research` category with the paper-search surface.
- Treat Interact and Monitor as separate authorization boundaries. Interact can cause persistent website actions, and Monitor creates recurring external checks; use them only when the user explicitly requests the corresponding interaction or monitoring outcome.
- Prefer Firecrawl over ordinary fetchers when the distinct need is URL inventory, site-scale crawling, document parsing, or schema-driven webpage extraction. Prefer TinyFish for a focused browser-rendered read or user-directed interactive task when site-scale extraction is not required.

### TinyFish

- Inspect the live TinyFish surface because Search, Fetch Content, and Web Automation may be exposed separately.
- Use Search for compact general-web, news, or research-paper discovery when it is the chosen discovery lane and no provider restriction excludes it.
- Use Fetch Content for known URLs or browser-rendered batch extraction, including JavaScript-heavy pages. Prefer it over automation when reading alone is sufficient.
- Use Web Automation only when a user-directed task requires navigation, clicks, forms, login, or interactive page state. Follow its live lifecycle instructions and do not duplicate a run that may still be active.

### X-native evidence

- Use xurl as the default read interface when it is callable and authenticated.
- Use an authenticated X API MCP instead when a dedicated structured tool better fits the task or xurl is unavailable. Inspect live schemas rather than assuming fixed tool names or coverage.
- Treat xurl and X API MCP as alternative interfaces to the same evidence, not independent sources.
- Generic web or browser evidence may supplement the answer only when the request permits it and must be labeled non-X corroboration; it cannot replace missing X-native data.
- Keep research read-only unless the user separately and explicitly authorizes a mutation.

For X-native work, read [references/x-routing.md](references/x-routing.md).

## Evidence and reporting

- Prefer original, official, regulatory, filing, repository, or primary-research evidence for material claims. Treat search snippets and provider-generated prose as leads when underlying evidence is available.
- Cite only inspected source content or provider-backed results that directly substantiate the claim. Full source text returned by search counts as inspected content; a separate fetch is unnecessary when the returned text provides sufficient context. Treat short or ambiguous snippets and generated answers as leads; retrieve the underlying content before relying on material claims. Preserve material dates, speakers, timestamps, entities, and field-level provenance.
- Public professional fields may be collected when the user requests them. Do not seek private contact details, sensitive personal attributes, or data-broker-style enrichment.
- For ordinary single-provider retrieval, a one-sentence provider note is sufficient. For multi-provider work, Connect, asynchronous provider work, provider-side synthesis, interactive or recurring operations, or X-native evidence, use [references/reporting-checklist.md](references/reporting-checklist.md) as an internal check. Report exact tools, distinct contributions, and material limitations; expand the ledger only when coverage, provenance, reproducibility, or an audit request warrants it. A simple X lookup or two-provider task need not receive a long report.

## Maintenance validation

When revising routing behavior, use [references/behavioral-evaluations.md](references/behavioral-evaluations.md). These cases are for maintenance, not a checklist to run during ordinary research.
