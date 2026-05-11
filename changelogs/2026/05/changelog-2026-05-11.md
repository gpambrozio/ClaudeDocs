# [Claude docs changes for May 11th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/7f381d936cf0469d9ac776918d0654e9657a84a9) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/7f381d936cf0469d9ac776918d0654e9657a84a9)]

## Executive Summary
- Hook events now expose an `effort` field with the active effort level (`low`/`medium`/`high`/`xhigh`/`max`), also available as `$CLAUDE_EFFORT` env var
- `--worktree` can now branch directly from a PR number (`#1234`) or full GitHub PR URL
- New `worktree.baseRef` setting (`"fresh"` or `"head"`) replaces manual git remote commands for controlling worktree base branch
- `--resume` now automatically restores the permission mode from the prior session (except `plan` and `bypassPermissions`)

-----

## Claude Code changes

### Changed documents

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/7f381d936cf0469d9ac776918d0654e9657a84a9/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* A new `effort` field was added to the hook event JSON payload. It contains a `level` property with the active [effort level](https://github.com/gpambrozio/ClaudeDocs/blob/7f381d936cf0469d9ac776918d0654e9657a84a9/docs-md/claude-code/model-config.md) for the turn (`"low"`, `"medium"`, `"high"`, `"xhigh"`, or `"max"`). If the requested effort exceeds what the current model supports, the field reflects the downgraded level actually used. Present for events like `PreToolUse`, `PostToolUse`, `Stop`, and `SubagentStop`. The level is also exposed as the `$CLAUDE_EFFORT` environment variable. [[line 504](https://github.com/gpambrozio/ClaudeDocs/blob/7f381d936cf0469d9ac776918d0654e9657a84a9/docs-md/claude-code/hooks.md?plain=1#L504)] [[Source](https://code.claude.com/docs/en/hooks#common-input-fields)]
* `--resume` now automatically restores the permission mode that was active when a tool was deferred — you no longer need to pass `--permission-mode` again on resume. The exceptions are `plan` and `bypassPermissions`, which are never carried over. Passing `--permission-mode` explicitly on resume overrides the restored value. [[line 1170](https://github.com/gpambrozio/ClaudeDocs/blob/7f381d936cf0469d9ac776918d0654e9657a84a9/docs-md/claude-code/hooks.md?plain=1#L1170)] [[Source](https://code.claude.com/docs/en/hooks#defer-a-tool-call-for-later)]

#### [Sessions](https://github.com/gpambrozio/ClaudeDocs/blob/7f381d936cf0469d9ac776918d0654e9657a84a9/docs-md/claude-code/sessions.md) [[Source](https://code.claude.com/docs/en/sessions)]

* Clarified that the `/branch` confirmation now prints two session IDs: the new branch you are now in and the original, making it easier to return to the original session. [[line 91](https://github.com/gpambrozio/ClaudeDocs/blob/7f381d936cf0469d9ac776918d0654e9657a84a9/docs-md/claude-code/sessions.md?plain=1#L91)] [[Source](https://code.claude.com/docs/en/sessions#branch-a-session)]

#### [Worktrees](https://github.com/gpambrozio/ClaudeDocs/blob/7f381d936cf0469d9ac776918d0654e9657a84a9/docs-md/claude-code/worktrees.md) [[Source](https://code.claude.com/docs/en/worktrees)]

* New requirement: before using `--worktree` in a directory for the first time, you must accept the workspace trust dialog by running `claude` once in that directory. If trust has not been accepted, `--worktree` exits with an error. [[line 45](https://github.com/gpambrozio/ClaudeDocs/blob/7f381d936cf0469d9ac776918d0654e9657a84a9/docs-md/claude-code/worktrees.md?plain=1#L45)] [[Source](https://code.claude.com/docs/en/worktrees#start-claude-in-a-worktree)]
* The base branch for worktrees is now configured via a new `worktree.baseRef` setting in settings.json, accepting `"fresh"` (default, branches from `origin/HEAD`) or `"head"` (branches from local `HEAD`, useful for subagents needing in-progress work). The previous approach of using `git remote set-head` commands has been replaced. [[line 51](https://github.com/gpambrozio/ClaudeDocs/blob/7f381d936cf0469d9ac776918d0654e9657a84a9/docs-md/claude-code/worktrees.md?plain=1#L51)] [[Source](https://code.claude.com/docs/en/worktrees#choose-the-base-branch)]
* New feature: `--worktree` now accepts a PR number prefixed with `#` (e.g. `claude --worktree "#1234"`) or a full GitHub PR URL to create a worktree branching from that pull request. Claude Code fetches `pull/<number>/head` from `origin` and creates the worktree at `.claude/worktrees/pr-<number>`. [[line 61](https://github.com/gpambrozio/ClaudeDocs/blob/7f381d936cf0469d9ac776918d0654e9657a84a9/docs-md/claude-code/worktrees.md?plain=1#L61)] [[Source](https://code.claude.com/docs/en/worktrees#choose-the-base-branch)]
