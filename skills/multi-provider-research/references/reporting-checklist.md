# Reporting checklist

Use this internal checklist for multi-provider research, any Exa Connect run, provider-generated synthesis, asynchronous tasks, interactive or recurring operations, or X-native evidence.

## Evidence

- Provider status distinguishes visibility or configuration, authentication and reachability, successful execution, and useful returned evidence.
- Claims are supported by inspected primary-source content or explicit provider-backed results. Full source text supplied in search can satisfy this check without another fetch; short snippets and generated answers do not substitute for underlying evidence.
- For changing facts, cache controls and source observation dates support the requested freshness, or the limitation is disclosed.
- Synthesis classification accounts for selected output options, including generated answers inside retrieval tools.
- Speaker, timestamp, publication date, reporting period, or observation time is retained when material.
- Search snippets are not presented as transcript, filing, traffic, price, or verification evidence.
- Perplexity Ask, Reason, and Research responses are identified as generated synthesis; material claims are attributed to their inspected underlying sources rather than to the generated answer alone.
- Inferences are labeled separately from source facts.

## Provider ledger

Report exact tools, distinct contributions, and material limitations. Use the details below only when they affect interpretation, coverage, reproducibility, or a requested audit; do not mechanically print every field or list unused capabilities. Simple X or two-provider lookups may need only a short note.

Details to include when material:

- providers requested or semantically matched;
- exact callable tools used;
- query transformations, filters, date ranges, or output constraints that materially affected coverage;
- Connect `dataSources` requested and providers confirmed in the completed result;
- for TinyFish, whether Search, Fetch Content, or Web Automation was used and any lifecycle, interaction, or page-access limitation that affected coverage;
- for Perplexity, the exact mode used, material query, domain, recency, country, context-size, or result controls, which underlying cited sources were inspected, whether the output was discovery or generated synthesis, and the provider-side model or preset when exposed by the completed result;
- for Parallel, whether Search, Fetch, Deep Research, or Task Group was used; the stable session or task/group identifier when material; whether the output was retrieval, provider-side research, or batch enrichment; and whether an asynchronous result remains pending;
- for Firecrawl, whether Search, Scrape, Map, Crawl, Parse, Agent, a specialized index, Interact, or Monitor was used; the URL and scope limits; requested output format; cache/freshness behavior when material; and any asynchronous, interaction, or recurring side effect;
- any provider-side answer, reasoning, research, or Agent operation, clearly separated from work performed by the harness-selected model;
- for X-native work, the interface used, material query operators, search or endpoint type, date range, pagination or result limits, and any authentication or archive-coverage constraint;
- distinct contribution of each provider;
- failed calls, unavailable providers, partial results, and substitutions;
- material evidence gaps and any untested capabilities.

Do not claim a provider, mode, or interface was used merely because it was configured, visible in documentation, included in `dataSources`, or available through a generic Agent surface.
