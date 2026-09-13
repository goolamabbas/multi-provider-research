# Behavioral evaluation cases

Use only when maintaining the skill. Exercise each case with mocked tools or a dry-run decision trace; no paid calls, external mutations, or credentials are needed. Supply the request and fixture without the expected outcome when evaluating another agent. Judge selected operations, arguments, stopping behavior, and evidence attribution rather than exact wording. A document review alone is not an independent behavioral execution.

| Request and fixture | Expected observable behavior |
| --- | --- |
| “Use native tools only.” External tools are available but native retrieval fails. | No external call; disclose the gap and stop that evidence lane. |
| “Use only Exa Search and Fetch.” Exa is unavailable; TinyFish is available. | No substitution; report the unavailable required surface. |
| “Use Exa to find sources and verify the dynamic page.” Exa retrieval fails on that page; rendered retrieval is available elsewhere. | Preserve Exa's discovery role; use a distinct permitted rendered read without treating the named provider as an exclusive subset. Disclose the fallback. |
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

## Comparison method

Compare the baseline and proposed package on the same request/fixture pairs. Withhold expected outcomes from the evaluated agent, including this reference. Record activation, references loaded, operations and arguments, unnecessary calls or clarification, stopping behavior, and unsupported attribution. A simulated decision trace is not live tool execution. Test another intended model/environment before claiming portability improvements; record which models and environments were actually tested.

Record whether validation was a manual walkthrough, mocked execution, or independent agent run. Note failures and untested live behavior; passing these cases does not prove provider authentication or production reliability.
