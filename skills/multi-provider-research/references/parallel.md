# Parallel

Read for Parallel Search/Fetch or Task workflows.

- Treat the Search MCP and Task MCP as distinct surfaces. Use `web_search` for current web discovery and answer-ready excerpts; use `web_fetch` only for a known URL, exact wording, full-page analysis, or insufficient search excerpts.
- Give Search a self-contained objective plus concise related keyword queries. Reuse the same session ID across related Search and Fetch calls. Pass `model_name` only when the exact active model slug is known from trusted runtime metadata; it is analytics metadata, not a search-quality control.
- Use `createDeepResearch` for a genuinely deep single-topic, provider-generated report. Use `createTaskGroup` for applying the same requested fields or output to a list of items; test a small batch before scaling when the user authorizes a larger run.
- Treat Deep Research and Task Group output as provider-side research or enrichment. Follow the live asynchronous lifecycle: do not poll automatically or start duplicates when the tool instructs the agent to return a progress URL and wait for a later user request.
- Prefer Parallel Task over duplicate general research only when asynchronous depth or consistent batch enrichment is the distinct requirement. Exa Connect remains the specialized provider-backed-data lane.

Use the current status/result tools with retained identifiers when continuation is permitted. The createDeepResearch description inspected on 2026-09-13 still directs sharing the URL and stopping unless otherwise instructed. This is a lifecycle rule for that surface, not a universal polling rule. No Task run was launched in that audit.

Report Search/Fetch versus Deep Research/Task Group, material session or task identifiers, retrieval versus provider-side research, exposed processor metadata, and pending status or limitations.
