# [Claude docs changes for February 22nd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/64ec774a8b671038a675e588b8ddd97f17a30cf6) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/64ec774a8b671038a675e588b8ddd97f17a30cf6)]

## Executive Summary
- Two new hook events (`WorktreeCreate` and `WorktreeRemove`) enable worktree lifecycle customization and support for non-git version control systems (SVN, Perforce, Mercurial) in isolated sessions
- Subagents can now use worktree isolation via `isolation: worktree` in their frontmatter, allowing parallel work without conflicts
- New `claude agents` CLI command lists all configured subagents grouped by source without starting an interactive session
- New `CLAUDE_CODE_DISABLE_1M_CONTEXT` environment variable allows disabling 1M context window support in enterprise environments

-----

## Claude Code changes

### Changed documents

#### [CLI Reference](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* New `claude agents` command added that lists all configured subagents, grouped by source. [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/cli-reference.md?plain=1#L13)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-commands)]

#### [Common Workflows](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* New "Subagent worktrees" section: subagents can now use worktree isolation to work in parallel without conflicts by adding `isolation: worktree` to the agent's frontmatter. Each subagent gets its own worktree that is automatically cleaned up when done. [[lines 1006-1009](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/common-workflows.md?plain=1#L1006-L1009)] [[Source](https://code.claude.com/docs/en/common-workflows#subagent-worktrees)]
* New "Non-git version control" section: worktree isolation can now support non-git VCS (SVN, Perforce, Mercurial) via `WorktreeCreate` and `WorktreeRemove` hooks that replace the default git behavior. [[lines 1049-1052](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/common-workflows.md?plain=1#L1049-L1052)] [[Source](https://code.claude.com/docs/en/common-workflows#manage-worktrees-manually)]

#### [Hooks Guide](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Two new hook events documented: `WorktreeCreate` (fires when a worktree is being created, replaces default git behavior) and `WorktreeRemove` (fires when a worktree is being removed). [[lines 369-370](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/hooks-guide.md?plain=1#L369-L370)] [[Source](https://code.claude.com/docs/en/hooks-guide#how-hooks-work)]
* `SessionStart` hook source now includes `clear` as a valid value in addition to `startup`, `resume`, and `compact`. [[line 402](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/hooks-guide.md?plain=1#L402)] [[Source](https://code.claude.com/docs/en/hooks-guide#hook-input)]
* `ConfigChange` event now documented as supporting matchers on configuration source (`user_settings`, `project_settings`, `local_settings`, `policy_settings`, `skills`). [[line 501](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/hooks-guide.md?plain=1#L501)] [[Source](https://code.claude.com/docs/en/hooks-guide#filter-hooks-with-matchers)]
* Updated list of hook types supported per event: clarified which events support `command`, `prompt`, and `agent` hooks vs. command-only hooks. [[lines 505-525](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/hooks-guide.md?plain=1#L505-L525)] [[Source](https://code.claude.com/docs/en/hooks-guide#filter-hooks-with-matchers)]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Two new hook events added to the events table: `WorktreeCreate` and `WorktreeRemove`, with full documentation including input/output schemas and examples. [[lines 29-30](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/hooks.md?plain=1#L29-L30)] [[Source](https://code.claude.com/docs/en/hooks#hook-lifecycle)]
* `WorktreeCreate` hook must print the absolute path to the created worktree directory on stdout; non-zero exit causes creation to fail. `WorktreeRemove` hook failures are only logged in debug mode. [[lines 503-504](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/hooks.md?plain=1#L503-L504)] [[Source](https://code.claude.com/docs/en/hooks#exit-code-2-behavior-per-event)]
* `WorktreeCreate` and `WorktreeRemove` added to the no-matcher list (always fire on every occurrence). [[line 187](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/hooks.md?plain=1#L187)] [[Source](https://code.claude.com/docs/en/hooks#matcher-patterns)]
* `ConfigChange` added to the block decision model events (using `"block"` decision value). [[line 557](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/hooks.md?plain=1#L557)] [[Source](https://code.claude.com/docs/en/hooks#decision-control)]
* Full new sections for `WorktreeCreate` and `WorktreeRemove` hook events with input schemas and usage examples for non-git VCS (SVN example). [[lines 1511-1622](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/hooks.md?plain=1#L1511-L1622)] [[Source](https://code.claude.com/docs/en/hooks#configchange-decision-control)]
* Updated prompt-based hooks section to clearly delineate which events support all three hook types (`command`, `prompt`, `agent`) vs. command-only events. [[lines 1692-1715](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/hooks.md?plain=1#L1692-L1715)] [[Source](https://code.claude.com/docs/en/hooks#prompt-based-hooks)]

#### [Model Config](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* New `CLAUDE_CODE_DISABLE_1M_CONTEXT` environment variable documented: setting it to `1` disables 1M context window support and removes 1M model variants from the model picker. [[line 166](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/model-config.md?plain=1#L166)] [[Source](https://code.claude.com/docs/en/model-config#extended-context)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New `CLAUDE_CODE_DISABLE_1M_CONTEXT` environment variable added: disables 1M context window support; useful for enterprise environments with compliance requirements. [[line 894](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/settings.md?plain=1#L894)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Documented that `claude agents` CLI command lists all configured subagents from the command line (grouped by source, showing overrides) without requiring an interactive session. [[line 160](https://github.com/gpambrozio/ClaudeDocs/blob/64ec774a8b671038a675e588b8ddd97f17a30cf6/docs-md/claude-code/sub-agents.md?plain=1#L160)] [[Source](https://code.claude.com/docs/en/sub-agents#use-the-/agents-command)]
