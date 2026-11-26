# X-native routing

Use this reference only when the requested evidence is native to X, including posts, X Articles, accounts, timelines, bookmarks, engagement, search, counts, or trends.

## Portable capability preflight

- Treat live callable commands and tool schemas as the source of truth. A configured client, documented endpoint, or documentation MCP does not prove authenticated X data access.
- When using the official X MCP for research, prefer an already configured read-only connection if it covers the required fields and scopes. For setup advice, X documents `https://api.x.com/mcp?read_only=true`, which hides write tools and rejects write calls. Read scopes still apply. [X MCP documentation](https://docs.x.com/tools/mcp)
- Use xurl as the default read interface when installed and authenticated and no suitable read-only MCP route is already configured.
- Prefer an authenticated X API MCP when its dedicated structured tool better fits the request, such as archive search, user or news search, counts, trends, or bookmark folders, or when xurl is unavailable.
- Capability names and coverage vary across harnesses. Select by task semantics and inspected schema rather than hard-coded tool names.
- Treat xurl and an X API MCP as alternative interfaces, not independent sources. Use both for the same query only when the user requests cross-validation or the second interface can materially verify or complete the first.

## Retrieval and evidence

- Use authenticated X interfaces for X-native content. When the request permits broader evidence, general web or browser material may be labeled as non-X corroboration, but it cannot replace unavailable X API data.
- Preserve the material query, operators, endpoint or search type, requested and returned date range, result limit, pagination, and archive or account-visibility constraints.
- Request the fields needed to substantiate the answer. For long-form X Articles, retrieve the article body field exposed by the live API schema; a post preview or link is not the article body.
- Distinguish retrieved X data from inference, quoted third-party discussion, and non-X corroboration.
- If X access is missing, unauthenticated, rate-limited, or lacks the needed archive or account scope, report that limitation without silently changing evidence sources.

## Read-only and credential safety

- Research is read-only. Do not post, reply, like, repost, follow, bookmark, message, delete, or perform another mutation without separate explicit user authorization.
- Never read or expose xurl credential stores, print access tokens, enable verbose output that may reveal headers, or pass credentials through prompts, command arguments, logs, or tool results.
- Use only safe authentication-status checks available in the current harness. If authentication requires credentials or an interactive flow, ask the user to complete it outside the agent context.
