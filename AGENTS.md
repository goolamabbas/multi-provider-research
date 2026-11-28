# Repository Instructions (`multi-provider-research`)

Standing maintenance and release rules for anyone (human or AI agent) updating this optional routing skill.

## Packaging & Context Budget
- **Shipped files only in `skills/multi-provider-research/`:** `scripts/package-release.py` packs tracked files under `skills/multi-provider-research/` plus `LICENSE` into the installable release ZIP.
- **Keep maintainer evals out of the skill ZIP:** Put evaluation fixtures in `evals/behavioral-evaluations.md` and historical logs in `VERIFICATION.md`—never inside `skills/multi-provider-research/references/`.
- **Stay lean:** Keep `SKILL.md` plus `references/*.md` under ~3,000 words total. Keep only durable routing judgment, positive task-to-provider guidance, and non-obvious operational gotchas—do not duplicate live MCP schemas or dated probe logs.

## Provider Neutrality & Accuracy
- **No provider rankings:** Cover **Exa, Parallel, Keenable, Octen, Perplexity**, and authenticated **X** fairly by capability and evidence need.
- **Verify live docs first:** Check current official MCP docs before changing tool names, auth boundaries, fetch/freshness parameters, or cost-gate warnings. Keep companion links in `README.md` aligned with live anchors on `https://goolamabbas.github.io/separate-intelligence-and-search/`.

## Release & Verification Workflow
1. Bump `metadata.version` in `skills/multi-provider-research/SKILL.md`, prepend an entry in `CHANGELOG.md`, and update version/download links in `README.md`.
2. Test packaging locally:
   ```bash
   python3 scripts/package-release.py --output /tmp/mpr-release-test
   unzip -l /tmp/mpr-release-test/multi-provider-research-v*.zip
   (cd /tmp/mpr-release-test && shasum -a 256 -c SHA256SUMS)
   ```
   Confirm `evals/behavioral-evaluations.md` and `AGENTS.md` are excluded from the ZIP.
3. Because `install.md` installs from the latest **published GitHub release** (not `main`), merging a version bump requires tagging `vX.Y.Z` on `main` and publishing the GitHub release with both the verified ZIP and `SHA256SUMS`.
