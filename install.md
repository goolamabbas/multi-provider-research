# Install multi-provider-research

Instructions for the agent receiving the installation request.

Install the latest stable release from https://github.com/goolamabbas/multi-provider-research into this application's supported skills directory. This installs research instructions only, not provider connections, accounts, credentials, or paid services.

## Choose the destination

Honor the scope requested by the user or project instructions. For project-only installation, use `<project>/.agents/skills/multi-provider-research` in Codex or `<project>/.claude/skills/multi-provider-research` in Claude Code. Do not write a personal installation when project scope is requested. Treat “for all my projects” as a request for personal installation for the current application, not installation into every application. For personal installation, consult current application documentation/configuration; do not assume one shared directory works in every application. If scope is unspecified, prefer project scope inside a project and report that choice. Ask only if the application, project root, or supported destination cannot be established.

If scope is unspecified and there is no project, ask whether to install personally. An inaccessible location is not evidence that no installation exists.

If a sandbox blocks the intended directory, use the application’s normal permission request for that specific directory. Do not disable sandbox protections, switch scope, or change global settings to evade the restriction. Diagnose the actual command error before attributing it to permissions.

## Obtain and install the complete release

1. Resolve the latest stable published GitHub release (exclude draft/prerelease releases). Obtain its dedicated `multi-provider-research-v<VERSION>.zip` and `SHA256SUMS`; do not install a lone SKILL.md or an untagged main checkout. GitHub CLI, the GitHub API, or ordinary HTTPS downloads are suitable.
2. Download to a temporary directory and verify the ZIP's SHA-256 against the matching checksum entry. Stop on missing assets, a mismatch, or an inaccessible release; do not claim success or silently switch sources.
3. Inspect archive paths before extraction: reject absolute paths, traversal, and symlinks escaping the package. The dedicated ZIP contains one `multi-provider-research/` folder. Confirm it contains `LICENSE`, `SKILL.md`, `agents/`, and `references/`, and that its metadata version matches the release.
4. Check the destination before changing it, including symlinks. For an existing installation, make a complete backup outside the active skill-discovery directories. Compare it with its recorded published version where possible. Preserve local customizations and ask before overwriting uncertain or customized content. If it already matches the requested release, report that without replacing it.
5. Install the complete verified folder. For an approved update, replace the folder rather than overlay-merging, so removed files do not survive. Never change another installation scope or application configuration to make installation succeed.
6. Compare every installed file and the full file inventory with the extracted release. Report version, exact destination, checksum verification, and any backup.

## Check discovery separately

Use the application's skill listing or a fresh session to confirm the installed path is discovered. Check for same-named skills in other scopes; do not mistake a personal copy for the project installation. If a reload/fresh task is needed, explain it. File equality proves installation, not discovery or successful provider execution. Do not launch research or paid tool calls merely to test installation.

If local filesystem access or skill loading is unsupported, state the limitation and give the manual release link. Do not claim a chat-only environment has installed a skill.
