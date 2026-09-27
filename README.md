# Multi-provider research

Version **0.4.2** · [Changelog](CHANGELOG.md) · [Historical verification log](VERIFICATION.md)

A portable research-routing skill for AI agents. It selects the smallest useful set of available research providers, respects provider and synthesis restrictions, verifies source evidence, and reports material gaps.

The skill covers Octen, Exa Search/Agent/Connect, Perplexity, Parallel, Firecrawl, TinyFish, and authenticated X interfaces. It works with any available subset, including one provider. Provider access, authentication, billing, and available operations depend on your environment.

## Install

1. Download [multi-provider-research-v0.4.2.zip](https://github.com/goolamabbas/multi-provider-research/releases/download/v0.4.2/multi-provider-research-v0.4.2.zip) from the [release](https://github.com/goolamabbas/multi-provider-research/releases/tag/v0.4.2). The release also includes `SHA256SUMS` for integrity checking.
2. Extract the ZIP. Its single top-level folder is `multi-provider-research/`, containing `SKILL.md`, `references/`, and `agents/`.
3. Copy that entire folder into the personal skills directory supported by your application. Consult your application's current instructions for its skills directory and discovery behavior.
4. Start a fresh task or reload skills as your application requires.
5. Connect and test at least one suitable research provider separately.

If another version is installed, back up the complete existing folder, then replace it with the complete new folder rather than merging files. Preserve local customizations separately and review them before reapplying.

The dedicated release ZIP is ready to copy. GitHub's automatically generated source ZIP instead contains the repository: install only its inner `skills/multi-provider-research/` folder. Cloning the repository uses that same inner folder.

`agents/openai.yaml` supplies optional OpenAI-specific interface metadata. Its invocation syntax is environment-specific; the plain-language example below is the portable entry point. The installed version is recorded in `SKILL.md` under `metadata.version`.

## Use

```text
Use the multi-provider-research skill.

Research question: [YOUR QUESTION]
```

State any required or excluded providers and whether provider-generated analysis is permitted. Naming a provider requires its contribution; “only” or “exactly” restricts the permitted set.

By default, ordinary lookups use source retrieval and analysis by the current assistant. Native search and page reading may help within your restrictions. If a required provider or reader is unavailable, the skill reports the gap and continues other permitted work; replacement requires an already-permitted fallback. For unrestricted tasks, it can choose another suitable tool and disclose the substitution.

Firecrawl Alexandria is an optional route to structured provider data. The skill discovers current capabilities when the task benefits from them, checks coverage and published prices, and reuses sufficient search or page evidence instead of adding paid enrichment. Catalog discovery is free; execution and ordinary Firecrawl web operations have their own charges. See the [guide and generic prompt](https://goolamabbas.github.io/separate-intelligence-and-search/guide/research-prompts/#firecrawl-with-optional-alexandria-data).

Exa Agent Ultra is an optional effort for comprehensive list-building and difficult multi-source research. The skill checks available budget controls, preserves run IDs, and distinguishes limited findings from exhaustive coverage. It does not make Ultra the default or claim independently measured superiority. See [when to use Ultra](https://goolamabbas.github.io/separate-intelligence-and-search/guide/choosing-providers/#when-agent-ultra-is-worth-it) and the [budgeted research example](https://goolamabbas.github.io/separate-intelligence-and-search/guide/research-prompts/#exa-agent-ultra-for-comprehensive-discovery).

The skill supplies instructions. It does not install providers, supply API keys, enforce permissions, or guarantee that a named operation is available.

[Read the skill](skills/multi-provider-research/SKILL.md) for the complete routing rules.

## Guide

[Choosing External Research Tools for AI Agents](https://goolamabbas.github.io/separate-intelligence-and-search/guide/) — the detailed companion guide, provider reference, connection guidance, and copyable research prompts.

## License

[MIT](LICENSE). External provider services retain their own terms.

## Maintainer packaging

Run `python3 scripts/package-release.py --output /path/to/release-directory` from the repository root. The script reads the version from `SKILL.md`, packages tracked skill files plus the MIT license under one `multi-provider-research/` folder, and writes the ZIP and `SHA256SUMS`. Commit the reviewed changes before tagging and publishing the matching release. Changelog and historical verification notes remain repository documentation rather than research-time references.
