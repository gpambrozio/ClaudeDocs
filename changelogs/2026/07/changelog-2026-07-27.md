# [Claude docs changes for July 27th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/b699ba47962ef731af7fb9932e80971a8adbc85e) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/b699ba47962ef731af7fb9932e80971a8adbc85e)]

## Executive Summary
- Subagent nesting is on by default again: subagents can now spawn subagents of their own up to three layers deep (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` default raised from 1 to 3 as of v2.1.219), reversing the v2.1.217 change that turned nesting off by default.
- The `workflowSizeGuideline` setting's default changed from `unrestricted` to `medium` (fewer than 15 agents), and as of v2.1.219 it can be set directly in any settings file, taking precedence over the `/config` **Dynamic workflow size** row.
- Usage-policy-refusal and cybersecurity-safeguard error messages were shortened and now name the specific model that flagged the request; non-interactive mode drops the `/feedback` mention in favor of a plain "Learn more:" link.

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/subagents](https://github.com/gpambrozio/ClaudeDocs/blob/b699ba47962ef731af7fb9932e80971a8adbc85e/docs-md/claude-code/agent-sdk/subagents.md) [[Source](https://code.claude.com/docs/en/agent-sdk/subagents)]

* Subagents can now spawn subagents of their own by default, up to three layers below the main conversation; `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` still controls the limit, with `1` turning nesting off. Documents the intermediate default of `1` used in v2.1.217-v2.1.218 before v2.1.219 raised it to `3`. [[lines 174-177](https://github.com/gpambrozio/ClaudeDocs/blob/b699ba47962ef731af7fb9932e80971a8adbc85e/docs-md/claude-code/agent-sdk/subagents.md?plain=1#L174-L177)] [[Source](https://code.claude.com/docs/en/agent-sdk/subagents#agentdefinition-configuration)]

#### [claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/b699ba47962ef731af7fb9932e80971a8adbc85e/docs-md/claude-code/claude-platform-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

* Removed the enterprise sales/pricing banner ("Deploying Claude Code across your organization?") from the top of the page. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/b699ba47962ef731af7fb9932e80971a8adbc85e/docs-md/claude-code/claude-platform-on-aws.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/b699ba47962ef731af7fb9932e80971a8adbc85e/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` default changed from `1` to `3`, matching the new default-on nesting behavior; set `1` to turn nesting off again. [[line 246](https://github.com/gpambrozio/ClaudeDocs/blob/b699ba47962ef731af7fb9932e80971a8adbc85e/docs-md/claude-code/env-vars.md?plain=1#L246)] [[Source](https://code.claude.com/docs/en/env-vars#agent-and-subagent-configuration)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/b699ba47962ef731af7fb9932e80971a8adbc85e/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Usage policy refusal message shortened to `<model> can't help with this. Start a new session to continue.`, naming the specific model (or `Claude` when none is recorded); non-interactive mode now ends with `Learn more:` and a link instead of mentioning `/feedback`. Documents the prior wording used before v2.1.219. [[lines 998-1004](https://github.com/gpambrozio/ClaudeDocs/blob/b699ba47962ef731af7fb9932e80971a8adbc85e/docs-md/claude-code/errors.md?plain=1#L998-L1004)] [[Source](https://code.claude.com/docs/en/errors#usage-policy-refusal)]
* Cybersecurity safeguard message shortened to `<model>'s safeguards flagged this message`, pointing to the Cyber Verification Program; non-interactive mode now ends with `Learn more:` and a link instead of dropping the `/feedback` sentence. Adds a version history of the three message wordings used since before v2.1.203. [[lines 1015-1030](https://github.com/gpambrozio/ClaudeDocs/blob/b699ba47962ef731af7fb9932e80971a8adbc85e/docs-md/claude-code/errors.md?plain=1#L1015-L1030)] [[Source](https://code.claude.com/docs/en/errors#safety-measures-flagged-a-cybersecurity-topic)]
* "Matched no tools in this session" and the zero-tools refusal now describe the `Agent` tool being withheld because a subagent is at the nesting depth limit, rather than because nesting is off entirely — consistent with nesting now being on by default. [[lines 1264 and 1279](https://github.com/gpambrozio/ClaudeDocs/blob/b699ba47962ef731af7fb9932e80971a8adbc85e/docs-md/claude-code/errors.md?plain=1#L1264)] [[Source](https://code.claude.com/docs/en/errors#tools-list-matched-no-tools)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/b699ba47962ef731af7fb9932e80971a8adbc85e/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* `workflowSizeGuideline` moved out of the global-config-only table and into the main settings table: its default changed from `unrestricted` to `medium`, it can now be set directly in any settings file as of v2.1.219 (taking precedence over `/config`, which hides the row once a settings file sets the key), and on v2.1.202-v2.1.218 it must still be set via `/config`. [[line 314](https://github.com/gpambrozio/ClaudeDocs/blob/b699ba47962ef731af7fb9932e80971a8adbc85e/docs-md/claude-code/settings.md?plain=1#L314)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/b699ba47962ef731af7fb9932e80971a8adbc85e/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* "Let subagents spawn their own subagents" rewritten: nesting is on by default up to three layers, `Agent` is withheld only once a subagent hits the depth limit, and `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1` turns nesting off rather than being the default. Adds a version history table for the v2.1.172-v2.1.216 (5 layers, unconfigurable) and v2.1.217-v2.1.218 (default 1) eras. [[lines 757-779](https://github.com/gpambrozio/ClaudeDocs/blob/b699ba47962ef731af7fb9932e80971a8adbc85e/docs-md/claude-code/sub-agents.md?plain=1#L757-L779)] [[Source](https://code.claude.com/docs/en/sub-agents#let-subagents-spawn-their-own-subagents)]

#### [workflows](https://github.com/gpambrozio/ClaudeDocs/blob/b699ba47962ef731af7fb9932e80971a8adbc85e/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* "Set a size guideline" rewritten: the default is now `medium` (previously `unrestricted`), `/config` shows `medium (default)` until a value is chosen, and as of v2.1.219 the `workflowSizeGuideline` settings-file key takes precedence over `/config` and hides that row. The `Large workflow` warning threshold still follows only a guideline you explicitly set. [[lines 306-333](https://github.com/gpambrozio/ClaudeDocs/blob/b699ba47962ef731af7fb9932e80971a8adbc85e/docs-md/claude-code/workflows.md?plain=1#L306-L333)] [[Source](https://code.claude.com/docs/en/workflows#set-a-size-guideline)]

-----

## API changes

No significant documentation changes today; only Cloudflare email-obfuscation link updates in `build-with-claude/files` and `build-with-claude/thinking`.
