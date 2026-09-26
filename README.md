# Multi-provider research

A portable research-routing skill for AI agents. It selects the smallest useful set of available research providers, respects provider and synthesis restrictions, verifies source evidence, and reports material gaps.

The skill covers Octen, Exa Search/Agent/Connect, Perplexity, Parallel, Firecrawl, TinyFish, and authenticated X interfaces. It works with any available subset, including one provider. Provider access, authentication, billing, and available operations depend on your environment.

## Install

1. Download this repository as a ZIP, or clone it.
2. Inside the download, locate `skills/multi-provider-research/`.
3. Copy that entire folder into the personal skills directory supported by your application. Preserve its `references/` and `agents/` subfolders. Consult your application's current instructions for its skills directory and discovery behavior.
4. Start a fresh task or reload skills as your application requires.
5. Connect and test at least one suitable research provider separately.

Install the inner `multi-provider-research` folder containing `SKILL.md`. The root routes to provider references as needed; preserve the complete package.

`agents/openai.yaml` supplies optional OpenAI-specific interface metadata. Its invocation syntax is environment-specific; the plain-language example below is the portable entry point.

If another version is already installed, compare or back it up before replacing it.

## Use

```text
Use the multi-provider-research skill.

Research question: [YOUR QUESTION]
```

State any required or excluded providers and whether provider-generated analysis is permitted. Naming a provider requires its contribution; “only” or “exactly” restricts the permitted set.

Firecrawl Alexandria is an optional route to structured provider data. The skill discovers current capabilities when the task benefits from them, checks coverage and published prices, and reuses sufficient search or page evidence instead of adding paid enrichment. Catalog discovery is free; execution and ordinary Firecrawl web operations have their own charges. See the [guide and generic prompt](https://goolamabbas.github.io/separate-intelligence-and-search/guide/research-prompts/#firecrawl-with-optional-alexandria-data).

Exa Agent Ultra is an optional effort for comprehensive list-building and difficult multi-source research. The skill checks available budget controls, preserves run IDs, and distinguishes limited findings from exhaustive coverage. It does not make Ultra the default or claim independently measured superiority. See [when to use Ultra](https://goolamabbas.github.io/separate-intelligence-and-search/guide/choosing-providers/#when-agent-ultra-is-worth-it) and the [budgeted research example](https://goolamabbas.github.io/separate-intelligence-and-search/guide/research-prompts/#exa-agent-ultra-for-comprehensive-discovery).

The skill supplies instructions. It does not install providers, supply API keys, enforce permissions, or guarantee that a named operation is available.

[Read the skill](skills/multi-provider-research/SKILL.md) for the complete routing rules.

## Guide

[Choosing External Research Tools for AI Agents](https://goolamabbas.github.io/separate-intelligence-and-search/guide/) — the detailed companion guide, provider reference, connection guidance, and copyable research prompts.

## License

[MIT](LICENSE). External provider services retain their own terms.
