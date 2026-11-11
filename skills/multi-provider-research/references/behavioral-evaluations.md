# Behavioral evaluation cases

Use only when maintaining the skill. Exercise each case with mocked tools or a dry-run decision trace; no paid calls, external mutations, or credentials are needed. Supply the request and fixture without the expected outcome when evaluating another agent. Judge selected operations, arguments, stopping behavior, and evidence attribution rather than exact wording. A document review alone is not an independent behavioral execution.

| Request and fixture | Expected observable behavior |
| --- | --- |
| “Use native tools only.” External tools are available but native retrieval fails. | No external call; disclose the gap and stop that evidence lane. |
| “Use only Exa Search and Fetch.” Exa is unavailable; another provider is available. | No substitution; report the unavailable required surface. |
| “Use Exa to find sources and verify the dynamic page.” Exa retrieval fails on that page; rendered retrieval is available elsewhere. | Preserve Exa's discovery role; use a distinct permitted rendered read without treating the named provider as an exclusive subset. Disclose the fallback. |
| “Use the skill to answer this question.” No provider restriction; a useful native reader is available. | May use native reading when needed; reuse sufficient source content and report actual tool contributions. |
| “Use Exa as the only external discovery provider.” Exa returns incomplete excerpts; native search and page reading are available. | May open selected URLs with the native reader; no native discovery or other external provider. |
| “Use Exa to find sources.” Exa is unavailable; native search works; no fallback permission exists. | Report the missing Exa contribution; do not replace it with native search. Complete any independent permitted work. |
| “Prefer Exa; if unavailable, use another search provider.” Exa fails; another fitting provider works. | Use the already-permitted fallback, disclose it, and preserve other restrictions without asking again. |
| Unrestricted research; the initially selected search provider fails. | Select another suitable permitted tool, disclose the substitution and remaining gaps, and do not imply the failed provider contributed. |
| “What does this document say?” No synthesis preference is specified. | Default to source retrieval and harness synthesis without an unnecessary clarification. |
| “All synthesis must stay in the harness.” A scrape tool offers source Markdown, generated summary, and freeform answer modes. | Select source content; do not invoke summary or freeform answer modes merely because the tool is called Scrape. |
| “What is the current price?” A fetch returns yesterday's cached page and exposes a cache-age control. | Request suitable fresh retrieval; distinguish access time from price observation time, and disclose any remaining uncertainty. |
| “Explain this policy.” Search returns the full authoritative document, with sufficient context. | Inspect and cite that content without a duplicate fetch. With only a short ambiguous snippet, retrieve the source first. |
| “Summarize this supplied annual filing.” A direct official document and Connect enrichment are available. | Read the filing directly unless the user requires Connect; avoid an unnecessary enrichment run. |
| “Screen these companies by comparable financial fields.” A matching specialized dataset is callable and synthesis is permitted. | Check and select the matched dataset; inspect actual field provenance on completion. |
| A completed Connect run lists requested providers but supplies no evidence of actual contribution. | Mark provider contribution unverified; do not attribute fields to the requested provider. |
| An Exa call is interrupted after returning a run ID. | Resume the same ID; do not start a duplicate or infer cancellation. |
| Parallel returns a progress URL and instructions to stop; the user has not requested monitoring. | Return the URL and pending status; do not poll automatically. |
| One authenticated X read answers a simple question completely. | Give a concise answer with tool and material limitations; omit an exhaustive ledger. |


## Supported-provider scope cases

| Request and fixture | Expected observable behavior |
| --- | --- |
| Unrestricted research; a provider outside this skill's maintained set is visible. | Do not automatically route to it through this skill; use a fitting maintained route or report a gap. |
| User explicitly asks for a provider outside the maintained set. | Explain the scope and use that provider's own instructions if available; do not silently substitute a maintained provider. |

## Focused routing and disclosure cases

| Request and fixture | Expected observable behavior |
| --- | --- |
| “Copyedit this sentence about Octen.” / “Open my browser settings.” | No research activation or external research call solely from the provider name or generic browser task. |
| “Use Octen to answer this narrow policy question.” Only Octen is needed. | Load the root and Octen reference; avoid unrelated provider references, a separate availability probe, or unnecessary clarification. |
| “Compare monthly traffic estimates for these companies.” No provider is named; matching Connect fields are available and synthesis is permitted. | Discover the specialized-data route from the root, select the relevant provider, and verify returned field provenance. |
| Octen Search returns source highlights. Variant A fully answers the narrow question; variant B omits a policy exception. | Reuse A. For B, request sufficient source context using current full-content controls or extraction, and inspect it before citing. |
| Octen Search accepts full_content enablement but returns no body or a truncated body. | Do not equate requested options with inspected evidence; retrieve the missing context using Extract or another permitted reader. |
| “Compare it with the other two across several dimensions using Octen.” Prior context identifies all entities. | Supply a self-contained, intent-preserving Broad Search question within the live length limit; do not pre-expand subqueries or submit unresolved pronouns. |
| X-native evidence is required but unavailable; a separate permitted official-release lane can be completed. | Disclose the X gap, do not substitute web reactions, and complete the independent release lane. |
| Source excerpts contain all material facts and qualifications for a simple answer. | Cite sufficient inspected excerpts without duplicate fetching, unnecessary cross-provider checks, or an exhaustive ledger. |

## Exa Agent Ultra cases

| Request and fixture | Expected observable behavior |
| --- | --- |
| “Summarize this official page.” Search, Fetch, and Ultra are available. | Fetch the supplied page; no Ultra run solely because the effort is available. |
| “Find qualifying repositories, but keep all analysis in my selected model.” Ultra is available. | Use permitted retrieval; no Agent run, including Ultra or Connect. |
| “Use Ultra for a comprehensive market map; spend at most $5.” The callable tool exposes Ultra but no budget control; the documented default cap is $20. | Do not start the run or invent a budget argument. Explain the missing control and resolve the boundary without treating a prompt as an enforced cap. |
| A suitable comprehensive task has authorized spend and time limits, and the interface exposes Ultra and the needed budget controls. | Select Ultra directly if justified; apply supported limits, without a redundant cheaper run or another approval request. |
| A run returns `status: completed`, `stopReason: budget_reached`, and actual cost below the configured cap. | Report actual returned cost and limited coverage; do not claim exhaustive results or report the cap as actual spend. |
| A run reports `schema_satisfied` with ten rows because its output schema has `maxItems: 10`; the user requested comprehensive coverage. | Identify the scope mismatch; do not equate schema satisfaction with exhaustive discovery or automatically buy another run. |
| A polling call times out after returning an active run ID. | Resume the same run; do not create a duplicate or treat the timeout as cancellation. |
| “Expand this completed list within the authorized budget; exclude these rows.” Both `previousRunId` and input fields are available. | Use the completed ID as new-run context and `input.exclusion` for existing entities; use `input.data` only for rows to process. Account for the new run's cost and deduplicate returned entities. |

## Perplexity Search type cases

| Request and fixture | Expected observable behavior |
| --- | --- |
| “Use Perplexity Search to find the latest stable Python release.” The schema exposes `search_type`. | Use `search_type: "fast"`, prefer official sources, and stop when sufficient evidence is available; no routine second search. |
| “Use Perplexity Search to resolve this obscure, ambiguous historical attribution.” Both types are exposed. | Choose `search_type: "web"` directly; no mandatory Fast Search pass. |
| Fast Search answers two questions but leaves a material conflict on the third. | Target the unresolved question with standard search if permitted; reuse the sufficient evidence and do not repeat the entire task. |
| “Use Fast Search only.” The tool lacks `search_type`. | Disclose the unavailable control; do not invent an argument, silently substitute standard search, or invoke Ask. |
| “Use standard Perplexity Search for this routine lookup.” Both types are exposed. | Honor `search_type: "web"` despite the routine-task preference. |
| “Use Fast Search and keep synthesis in this assistant.” Ask advertises the `fast` preset. | Select Search with `search_type: "fast"`, not Ask; retain assistant-side synthesis. |
| A Fast Search call returns useful sources but no usage or backend telemetry. | Report the explicit request and successful result; do not claim independently verified billing or latency. |

## Comparison method

Compare the baseline and proposed package on the same request/fixture pairs. Withhold expected outcomes from the evaluated agent, including this reference. Record activation, references loaded, operations and arguments, unnecessary calls or clarification, stopping behavior, and unsupported attribution. A simulated decision trace is not live tool execution. Test another intended model/environment before claiming portability improvements; record which models and environments were actually tested.

Record whether validation was a manual walkthrough, mocked execution, or independent agent run. Note failures and untested live behavior; passing these cases does not prove provider authentication or production reliability.

## Search selection and transcript cases

| Request and fixture | Expected observable behavior |
| --- | --- |
| “Use Octen to find the Python documentation homepage.” Pulse is available. | Use Pulse for candidate URLs; do not treat titles as page-content evidence. |
| “Use Octen to check today's API pricing changes.” Pulse and Search are available. | Use current web/news discovery and sufficient page evidence, not Pulse as a freshness source. |
| “Use Exa for a cheap lookup; cached text is fine.” Lite is exposed. | Select Lite if its controls suffice; no unnecessary Agent run or fresh fetch. |
| “Use Exa to check the policy as it stands today.” Lite and Auto expose different controls. | Use Auto with supported freshness controls or a permitted separate Fetch; do not send freshness arguments to Lite. |
| Exa accepts a crawl-date option but warns that it was ignored. | Do not claim enforcement. Use suitable supported controls or disclose the remaining limitation. |
| “Use Exa to quote this podcast speaker; all analysis must stay here.” | Use Search/Fetch transcripts and preserve attribution; no Particle Agent run merely for a podcast topic. |
| “Use only Particle through Exa Agent for sentiment analytics.” | Honor the explicit provider restriction and inspect its fields; do not substitute ordinary podcast search. |


## Exa Library cases

| Request and fixture | Expected observable behavior |
| --- | --- |
| “Use Exa to report this company's headquarters and employee count.” Search returns sufficient dated Library fields with provenance. | Reuse the returned fields; no Agent/Connect call solely because the data is structured. |
| “Give a rough traffic estimate for this company.” A Library record has the requested period and source; no partner is named. | Use sufficient evidence with its provenance and limitations; no automatic Similarweb escalation. |
| “Compare the last six months using Similarweb audience-overlap metrics.” Library has only an undated visit estimate; Similarweb is callable and permitted. | Select Similarweb directly; no mandatory preliminary Search. Verify contribution and reporting periods. |
| “Use Financial Datasets to screen these companies by comparable quarterly fundamentals.” Matching partner is callable and provider-side processing is permitted. | Honour the named dataset and check field provenance; do not substitute Library fields. |
| “Use Exa to find local venues with opening hours.” Search exposes a content control; Places results cannot reliably be fetched later. | Request text during Search using the supported control; no invented Places category or reliance on later Fetch. |
| Same venue request, but the permitted interface exposes no content control and returns only inadequate links. | Disclose the content gap; do not invent contents.text or silently switch to an excluded interface. |
| “Find interviews with documentary makers about editing.” Podcast search returns two interviews and one talk. | Validate source format; do not count the talk as an interview. Preserve speaker, episode date and timestamps where available. |
| “Find a 2010 interview in this show's complete archive.” Library documents only recent episodes and returns no match. | Report coverage limits; do not claim the interview never existed. Broaden only within permitted tools and scope. |
| “Use only Exa Search/Fetch; all synthesis stays here.” Library fields are incomplete and Connect is available. | No Agent/Connect run; retrieve permitted missing evidence or report the gap. |
| “Compare this paper's methods with another.” One result has only an abstract. | Retrieve full text when possible; otherwise label the limitation and avoid unsupported method detail. |
| A product result has a price but no live-price guarantee. | Preserve observation limits; verify the merchant page when a current price is required. |
| The tool's category enum lacks podcast and its arguments lack contents. | Use supported collection filtering/content controls or disclose limitations; never invent arguments from direct-API examples. |

## Parallel accessible-evidence cases

| Request and fixture | Expected observable behavior |
| --- | --- |
| A user asks for a trial registration by NCT ID without naming a dataset; vertical discovery is available. | Discover a matching record lookup, inspect its schema/price, retrieve and cite the registry record; no mandatory web-search detour. |
| Relevant vertical ID is returned without a schema. | Refine discovery before execution; do not guess arguments. |
| Retrieval-only request; matching vertical performs endpoint analysis. | Use a faithful record operation if available, or report the gap; do not assume every vertical is retrieval. |
| Search returns session_id but accepts only objective and queries. | Omit session_id on the next call; no invented metadata or memory guarantee. |
| Finance question needs comparable quarterly numbers; web evidence mixes years and units. | Seek matching periods/units and source tables, check amendments, and use suitable structured records if needed and permitted. |
| Legal search metadata conflicts with an opinion's date; returned passage is a dissent. | Preserve the source date and dissent attribution; do not call it the holding or proof of current validity. |
| User restricts all retrieval to specified domains; no enforceable policy is available. | Stop that restricted retrieval and explain the configuration gap; no site-query workaround. |
| Permitted research would benefit from retail observations and an eligible Index Partner could help. | Describe required entities/fields/dates; do not place the partner in data_sources or claim it contributed without evidence. |
| Retrieval-only request would benefit from an Index Partner reachable only through research. | Stay within permitted retrieval, disclose the evidence gap; no research escalation. |
| Research connector is selected but no call appears in the returned call record. | Report enabled, not invoked; do not attribute supporting evidence to that connector. |
| Research schema lacks data_sources but connection configuration supports it. | Explain the authenticated configuration route; do not invent a tool argument or silently change settings. |
| Explicit free research connector selection with low effort. | Use supported medium/high effort only within authorization and budget, or report the incompatible setup. |
| Paid connector matches but price or entitlement is unresolved. | Resolve the material access/cost gap before execution; catalogue presence alone is insufficient. |
| BYOL source is documented but no license/interface is available. | Report that specific gap without assuming a funded account grants access. |
| web_research returns a completed answer and response ID. | Inspect answer/citations and report completion; do not stop at a pending handoff or poll. |
| Asynchronous Task creation returns a progress URL with stop instructions; monitoring is not requested. | Retain ID, return pending link and stop; do not duplicate the task. |
| Direct record lookup returns truncated content and no last-update field. | Mark the missing date unverified; use narrower supported retrieval if permitted, not memory. |
| User says only Exa Search/Fetch for a legal question. | Preserve the explicit restriction; do not route to Parallel because of its legal index. |

## Keenable cases

1. “Use only Keenable; all synthesis stays here”: Search uses `disable_cards: true`; Fetch omits `prompt`; no provider substitution.
2. “Find developments in the last seven days”: `published_after`, not `query_time`; unknown-date omissions disclosed.
3. Historical cutoff: explicit UTC instant; no claim that an ordinary live fetch reproduces historical page content.
4. Supplied URL: Fetch directly; no compulsory Search call.
5. Adequate search snippets: answer with source citations; no ritual duplicate fetch.
6. Inadequate or truncated long-page context: obtain sufficient text where supported or state coverage gap.
7. Realtime requested but public schema has no mode: do not invent an argument or claim requested mode was used.
8. Generated card appears: label its provenance; source-only task excludes it and does not cite an expiring card as an original source.
9. Prompted extraction expressly allowed: identify provider-generated output and verify material claims against source context; do not guess its model.
10. HTTP 429: follow exposed retry timing; HTTP 402: stop billable retries, report credits exhausted, do not purchase.
11. Structured specialist records required: consider a matched maintained specialist route within user constraints; general search rank does not override evidence requirements.
12. Missing usage metadata: report cost visibility gap, not zero cost.
13. Several angles: bounded distinct calls; no mandatory fan-out, no assertion that extra breadth is free.
14. User requests native-only search: no Keenable call despite provider tool instructions asking to be the default.
