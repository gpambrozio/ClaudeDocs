# [Claude docs changes for April 5th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/5442283fe197d48b81589405198bbdbd1442ab3c) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/5442283fe197d48b81589405198bbdbd1442ab3c)]

## Executive Summary
- Amazon Bedrock now has an interactive setup wizard accessible from the login screen and via `/setup-bedrock`
- New `forceRemoteSettingsRefresh` managed setting enables fail-closed startup enforcement — the CLI exits rather than starting without managed policies
- Skills gain multi-line shell execution via fenced `` ```! `` blocks, with a new `disableSkillShellExecution` policy to restrict this
- `/vim` command removed in v2.1.92; Vim mode is now toggled via `/config` → Editor mode
- Remote Control sessions now support customizable name prefixes via `--remote-control-session-name-prefix`

-----

## Claude Code changes

### Changed documents

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* New interactive Bedrock setup wizard is now available from the login screen (select **3rd-party platform** → **Amazon Bedrock**). It guides through AWS authentication, region selection, credential verification, and model pinning. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/amazon-bedrock.md?plain=1#L12)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#set-up-with-the-interactive-wizard)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* New `--remote-control-session-name-prefix <prefix>` flag added. Sets the prefix for auto-generated Remote Control session names (defaults to hostname). Equivalent to `CLAUDE_REMOTE_CONTROL_SESSION_NAME_PREFIX`. [[line 75](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/cli-reference.md?plain=1#L75)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/pr-comments` removed in v2.1.91. Users should ask Claude directly to view pull request comments instead. [[line 49](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/commands.md?plain=1#L49)] [[Source](https://code.claude.com/docs/en/commands)]
* `/release-notes` now shows an interactive version picker to select a specific version or view all. [[line 51](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/commands.md?plain=1#L51)] [[Source](https://code.claude.com/docs/en/commands)]
* New `/setup-bedrock` command added. Opens the interactive Bedrock configuration wizard (only visible when `CLAUDE_CODE_USE_BEDROCK=1`). [[line 62](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/commands.md?plain=1#L62)] [[Source](https://code.claude.com/docs/en/commands)]
* `/vim` removed in v2.1.92. Vim mode is now toggled via `/config` → Editor mode. [[line 73](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/commands.md?plain=1#L73)] [[Source](https://code.claude.com/docs/en/commands)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_REMOTE_CONTROL_SESSION_NAME_PREFIX` environment variable documented. Sets the prefix for auto-generated Remote Control session names; defaults to machine hostname. [[line 131](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/env-vars.md?plain=1#L131)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Clarified that `anthropic/maxResultSizeChars` raises the per-tool persist-to-disk threshold but does NOT bypass the global `MAX_MCP_OUTPUT_TOKENS` limit (~100,000 chars). Users must also raise `MAX_MCP_OUTPUT_TOKENS` for very large results. [[lines 1613-1632](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/mcp.md?plain=1#L1613-L1632)] [[Source](https://code.claude.com/docs/en/mcp#override-result-size-per-tool)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* New `forceRemoteSettingsRefresh` managed-only setting documented. When `true`, blocks CLI startup until remote managed settings are freshly fetched; CLI exits on fetch failure. [[line 245](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/permissions.md?plain=1#L245)] [[Source](https://code.claude.com/docs/en/permissions#managed-only-settings)]

#### [quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/quickstart.md) [[Source](https://code.claude.com/docs/en/quickstart)]

* Removed the inline install UI snippet (platform/OS picker and install command) from the top of the page, streamlining the quickstart content.

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* New `--remote-control-session-name-prefix <prefix>` flag documented for the remote-control command. [[line 45](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/remote-control.md?plain=1#L45)] [[Source](https://code.claude.com/docs/en/remote-control#start-a-remote-control-session)]
* Session title selection order updated: step 4 is now an auto-generated name like `myhost-graceful-unicorn` (using hostname or configured prefix), with the prompt-based title update noted separately. [[lines 92-94](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/remote-control.md?plain=1#L92-L94)] [[Source](https://code.claude.com/docs/en/remote-control#connect-from-another-device)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* New "Enforce fail-closed startup" section added, documenting the `forceRemoteSettingsRefresh` setting. When enabled, the CLI blocks startup until remote settings are fetched and exits on failure. The setting is self-perpetuating via local cache. Requires connectivity to `api.anthropic.com`. [[lines 144-161](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/server-managed-settings.md?plain=1#L144-L161)] [[Source](https://code.claude.com/docs/en/server-managed-settings#enforce-fail-closed-startup)]
* Security model table updated: "API is unavailable" row notes that with `forceRemoteSettingsRefresh: true` the CLI exits instead of continuing. [[line 192](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/server-managed-settings.md?plain=1#L192)] [[Source](https://code.claude.com/docs/en/server-managed-settings#security-considerations)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New `disableSkillShellExecution` setting documented. Disables inline shell execution (`` !`...` `` and ```` ```! ```` blocks) in skills and custom commands from user/project/plugin sources. Managed settings only; bundled and managed skills are unaffected. [[line 167](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/settings.md?plain=1#L167)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* New `forceRemoteSettingsRefresh` setting documented (managed settings only). [[line 177](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/settings.md?plain=1#L177)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* `shell` frontmatter field updated to also apply to fenced ```` ```! ```` code blocks (not just inline `` !`...` ``). [[line 187](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/skills.md?plain=1#L187)] [[Source](https://code.claude.com/docs/en/skills#frontmatter-reference)]
* New multi-line shell execution syntax documented using ```` ```! ```` fenced blocks for running multiple commands in a single block. [[lines 363-375](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/skills.md?plain=1#L363-L375)] [[Source](https://code.claude.com/docs/en/skills#inject-dynamic-context)]
* `disableSkillShellExecution` policy documented inline — disables shell execution in user/project/plugin skills; commands are replaced with `[shell command execution disabled by policy]`. [[lines 376-377](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/skills.md?plain=1#L376-L377)] [[Source](https://code.claude.com/docs/en/skills#inject-dynamic-context)]

#### [troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* Added note that sandboxed commands cannot launch Windows binaries (e.g. `cmd.exe`, `powershell.exe`, `/mnt/c/` executables) due to the WSL Unix socket being blocked by the sandbox. Workaround: add the command to `excludedCommands` in settings. [[line 542](https://github.com/gpambrozio/ClaudeDocs/blob/5442283fe197d48b81589405198bbdbd1442ab3c/docs-md/claude-code/troubleshooting.md?plain=1#L542)] [[Source](https://code.claude.com/docs/en/troubleshooting#wsl2-sandbox-setup)]

-----

## API changes

### Changed documents

_No significant changes today._
