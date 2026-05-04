# [Claude docs changes for May 4th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/232b2a65f72b363c30b15fe1ed45beb12aa9fdc1) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/232b2a65f72b363c30b15fe1ed45beb12aa9fdc1)]

## Executive Summary
- LLM hooks now have clarified `ok: false` behavior: for `Stop`/`SubagentStop` hooks, Claude keeps working using the reason as its next instruction; for all other events, the turn ends and the reason appears as a chat warning that Claude does not see
- `autoMemoryDirectory` security restriction tightened — now rejected from both project and local settings (not just project settings), since either file in a cloned repo could redirect memory writes to sensitive paths
- npm update command for Claude Code corrected from `npm update -g` to `npm install -g @anthropic-ai/claude-code@latest`

## New Claude Code versions

None

-----

## Claude Code changes

### Changed documents

#### [Discover plugins](https://github.com/gpambrozio/ClaudeDocs/blob/232b2a65f72b363c30b15fe1ed45beb12aa9fdc1/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* The npm command to update Claude Code was corrected to `npm install -g @anthropic-ai/claude-code@latest` (previously `npm update -g @anthropic-ai/claude-code`). [[line 389](https://github.com/gpambrozio/ClaudeDocs/blob/232b2a65f72b363c30b15fe1ed45beb12aa9fdc1/docs-md/claude-code/discover-plugins.md?plain=1#L389)] [[Source](https://code.claude.com/docs/en/discover-plugins#/plugin-command-not-recognized)]

#### [Hooks guide](https://github.com/gpambrozio/ClaudeDocs/blob/232b2a65f72b363c30b15fe1ed45beb12aa9fdc1/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Clarified that `ok: false` behavior differs by hook type: for `Stop` and `SubagentStop` hooks the reason is fed back to Claude and the turn continues; for all other events the turn ends and the reason appears in chat as a warning line that Claude does not see. [[line 701](https://github.com/gpambrozio/ClaudeDocs/blob/232b2a65f72b363c30b15fe1ed45beb12aa9fdc1/docs-md/claude-code/hooks-guide.md?plain=1#L701)] [[Source](https://code.claude.com/docs/en/hooks-guide#prompt-based-hooks)]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/232b2a65f72b363c30b15fe1ed45beb12aa9fdc1/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Added explanation of the LLM hook `ok: false` semantics: for `Stop` and `SubagentStop` the reason is returned to Claude as its next instruction and the turn continues; for all other supported events, the turn ends and the reason appears as a chat warning line. Also notes this is equivalent to `"continue": false` from a command hook, and points to command hook fields for alternative blocking semantics. [[lines 2318-2320](https://github.com/gpambrozio/ClaudeDocs/blob/232b2a65f72b363c30b15fe1ed45beb12aa9fdc1/docs-md/claude-code/hooks.md?plain=1#L2318-L2320)] [[Source](https://code.claude.com/docs/en/hooks#response-schema)]

#### [Memory](https://github.com/gpambrozio/ClaudeDocs/blob/232b2a65f72b363c30b15fe1ed45beb12aa9fdc1/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Clarified that `autoMemoryDirectory` must be set in user settings at `~/.claude/settings.json` specifically. [[line 298](https://github.com/gpambrozio/ClaudeDocs/blob/232b2a65f72b363c30b15fe1ed45beb12aa9fdc1/docs-md/claude-code/memory.md?plain=1#L298)] [[Source](https://code.claude.com/docs/en/memory#storage-location)]
* The value must now be documented as requiring an absolute path or a `~/`-prefixed path. Security restriction expanded: the setting is now rejected from both project and local settings (previously only project settings), since a cloned repository could supply either file to redirect auto memory writes to sensitive locations. The `--settings` flag is explicitly listed as an accepted source. [[lines 301-303](https://github.com/gpambrozio/ClaudeDocs/blob/232b2a65f72b363c30b15fe1ed45beb12aa9fdc1/docs-md/claude-code/memory.md?plain=1#L301-L303)] [[Source](https://code.claude.com/docs/en/memory#storage-location)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/232b2a65f72b363c30b15fe1ed45beb12aa9fdc1/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Updated `autoMemoryDirectory` description to reflect the expanded security restriction: now accepted from policy and user settings, and from the `--settings` flag; rejected from project or local settings to prevent cloned repos from redirecting memory writes to sensitive locations. [[line 159](https://github.com/gpambrozio/ClaudeDocs/blob/232b2a65f72b363c30b15fe1ed45beb12aa9fdc1/docs-md/claude-code/settings.md?plain=1#L159)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

-----

## API changes

### Changed documents

No significant changes. (Only obfuscated contact email link updates in `adaptive-thinking.md`, `extended-thinking.md`, and `files.md`.)
