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

Record whether validation was a manual walkthrough, mocked execution, or independent agent run. Note failures and untested live behavior; passing these cases does not prove provider authentication or production reliability.
