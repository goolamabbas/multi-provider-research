# X-native routing

Use only when the evidence is native to X: posts, threads, X Articles, user profiles, timelines, bookmarks, counts, or trends.

- **Interface choice:** Prefer an already-configured read-only X MCP (`https://api.x.com/mcp?read_only=true`, which omits write tools) or authenticated `xurl`. Treat them as alternative routes to the same data—do not run the same query through both unless cross-checking a failure.
- **No silent web substitution:** Web search cannot replace unavailable authenticated X data. If X access is missing, unauthenticated, or lacks archive scope, report the gap cleanly (label any permitted web context as non-X corroboration).
- **Evidence details:** Preserve author handle, timestamp, direct post link, query/date window, and result limits. For X Articles, fetch the full article body field exposed by the live schema rather than citing a truncated post preview.
- **Read-only & credential safety:** Never post, reply, like, repost, follow, bookmark, or message without separate explicit authorization. Never print or inspect `xurl` credential stores, access tokens, or verbose auth headers.

Docs: [X MCP](https://docs.x.com/tools/mcp) · [xurl](https://github.com/xdevplatform/xurl)
