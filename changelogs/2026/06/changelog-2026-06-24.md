# [Claude docs changes for June 24th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/eae0226a) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/eae0226a)]

## Executive Summary
- Claude Code 2.1.187 adds a new `sandbox.credentials` setting to block credential file access in sandboxes, organization-wide model restrictions in the model picker, and mouse click support in fullscreen select menus
- Agent view gains in-session `/model` switching with a temporary `(session)` override, plus major documentation on how background sessions handle authentication and provider credentials (changed in v2.1.174)
- Claude Code in Slack is being replaced by "Claude Tag" for Team and Enterprise workspaces, with no reinstall required
- The Java SDK beta messages API reference pages now have full content (they previously showed a loading error)
- AWS Lambda MicroVMs added as a supported platform for self-hosted agent sandboxes

## New Claude Code versions

### [2.1.187](https://github.com/gpambrozio/ClaudeDocs/blob/eae0226a/versions/2.1.187.md)

#### New features

* Added `sandbox.credentials` setting to block sandboxed commands from reading credential files and secret environment variables
* Added org-configured model restrictions to the model picker, `--model`, `/model`, and `ANTHROPIC_MODEL`, with a "restricted by your organization's settings" message when a restricted model is selected
* Added mouse click support to select menus (permission prompts, `/model`, `/config`, etc.) in fullscreen mode

#### Existing feature improvements

* Improved `/install-github-app`: GitHub Actions workflow setup is now optional — you can install just the GitHub App and skip the workflow/secret steps
* Improved `/btw` with ←/→ arrow navigation to step through earlier answers
* Improved `/plugin` to surface plugins you haven't used recently so you can clean them up

#### Major bug fixes

* Fixed `--resume` failing with "No conversation found" when the original `-p` run produced no model turns
* Fixed `--json-schema` and workflow `agent({schema})` structured output: the model can no longer re-call `StructuredOutput` indefinitely after a successful call, and follow-up turns now reliably return structured output
* Fixed remote MCP tool calls that hang with no response for 5 minutes — they now abort with an error instead of blocking indefinitely (override with `CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT`)
* Fixed background jobs in the agents view getting stuck in "working" indefinitely when the agent ended a turn without producing structured output
* Fixed channel connections dropping after navigating to the agents view and back, and after `/bg`, `/tui`, or `/update`
* Fixed subagent depth tracking: resumed subagents now restore their original spawn depth, and forked subagents now count toward the depth cap
* Fixed leaked agent worktree registrations: locked `.git/worktrees/` entries from killed agents are now cleaned up automatically
* Fixed pasted Korean/CJK text turning into mojibake in terminals that deliver paste as per-byte extended-key events
* Fixed `claude --help` not listing the `--bg`/`--background` flag
* [VSCode] Fixed extension becoming unresponsive when resuming a large session

-----

## Claude Code changes

### Changed documents

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/eae0226a/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* Clarified which commands run in agent view itself vs. dispatching to sessions: `/model` now also runs in-view to set the dispatch model; skills, user commands, and prompt-expanding built-ins like `/init` go to new sessions; other built-ins show an "attach to a session to run it" hint. [[line 227](https://github.com/gpambrozio/ClaudeDocs/blob/eae0226a/docs-md/claude-code/agent-view.md?plain=1#L227)] [[Source](https://code.claude.com/docs/en/agent-view#from-agent-view)]
* New section documenting how to change the dispatch model from inside agent view with `/model <name>` — sets a temporary `(session)` override without writing to settings, cleared with `/model default`, requires v2.1.172+. [[lines 333-342](https://github.com/gpambrozio/ClaudeDocs/blob/eae0226a/docs-md/claude-code/agent-view.md?plain=1#L333-L342)] [[Source](https://code.claude.com/docs/en/agent-view#set-the-model)]
* Background sessions now inherit `env` values from project settings (including `ANTHROPIC_MODEL`); cloud provider selection vars like `CLAUDE_CODE_USE_BEDROCK` follow the dispatching shell; gateway endpoint vars like `ANTHROPIC_BASE_URL` do not propagate from the shell. [[lines 347-349](https://github.com/gpambrozio/ClaudeDocs/blob/eae0226a/docs-md/claude-code/agent-view.md?plain=1#L347-L349)] [[Source](https://code.claude.com/docs/en/agent-view#set-the-model)]
* Documented the pre-warmed worker process: the supervisor keeps one worker ready to eliminate cold-start latency, assigns it on dispatch, then starts a replacement. [[lines 417-420](https://github.com/gpambrozio/ClaudeDocs/blob/eae0226a/docs-md/claude-code/agent-view.md?plain=1#L417-L420)] [[Source](https://code.claude.com/docs/en/agent-view#the-supervisor-process)]
* Clarified that background sessions use stored credentials (not shell env vars) for gateway endpoints; explains the behavior change introduced in v2.1.174 and how to configure gateway endpoints via project `settings.json` `env` block instead. [[lines 420-424](https://github.com/gpambrozio/ClaudeDocs/blob/eae0226a/docs-md/claude-code/agent-view.md?plain=1#L420-L424)] [[Source](https://code.claude.com/docs/en/agent-view#the-supervisor-process)]
* New troubleshooting section for "Could not resolve authentication method" on background dispatch, with steps to recover via `claude daemon stop --any --keep-workers`. [[lines 480-492](https://github.com/gpambrozio/ClaudeDocs/blob/eae0226a/docs-md/claude-code/agent-view.md?plain=1#L480-L492)] [[Source](https://code.claude.com/docs/en/agent-view#agent-view-says-the-background-service-did-not-respond)]

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/eae0226a/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* Added a link to Claude Tag in the related resources section, describing it as an organization-managed @Claude in Slack that runs on the same cloud environment. [[line 765](https://github.com/gpambrozio/ClaudeDocs/blob/eae0226a/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L765)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#related-resources)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/eae0226a/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Added a note that project skills committed to a repo also load when that repo is used in a Claude Tag channel, with a link to the Claude Tag skills repo docs. [[line 792](https://github.com/gpambrozio/ClaudeDocs/blob/eae0226a/docs-md/claude-code/skills.md?plain=1#L792)] [[Source](https://code.claude.com/docs/en/skills#related-resources)]

#### [slack](https://github.com/gpambrozio/ClaudeDocs/blob/eae0226a/docs-md/claude-code/slack.md) [[Source](https://code.claude.com/docs/en/slack)]

* New intro paragraph announcing that Claude Code in Slack is being replaced by Claude Tag for Team and Enterprise workspaces — no reinstall needed, existing setups continue to work during the transition. [[lines 3-4](https://github.com/gpambrozio/ClaudeDocs/blob/eae0226a/docs-md/claude-code/slack.md?plain=1#L3-L4)] [[Source](https://code.claude.com/docs/en/slack)]
* Added clarification that each Slack session runs under the user's own Claude account, using their connected repositories and plan limits. [[line 8](https://github.com/gpambrozio/ClaudeDocs/blob/eae0226a/docs-md/claude-code/slack.md?plain=1#L8)] [[Source](https://code.claude.com/docs/en/slack#use-cases)]
* New troubleshooting section for the "Claude Code is not enabled for your account" error: sign in at claude.ai/code once to create the cloud environment; each user must do this individually. [[lines 172-177](https://github.com/gpambrozio/ClaudeDocs/blob/eae0226a/docs-md/claude-code/slack.md?plain=1#L172-L177)] [[Source](https://code.claude.com/docs/en/slack#troubleshooting)]
* Added a Claude Tag link card in the related resources section. [[lines 222-224](https://github.com/gpambrozio/ClaudeDocs/blob/eae0226a/docs-md/claude-code/slack.md?plain=1#L222-L224)] [[Source](https://code.claude.com/docs/en/slack#related-resources)]

-----

## API changes

### Changed documents

#### [Java beta Messages](https://github.com/gpambrozio/ClaudeDocs/blob/eae0226a/docs-md/api/api/java/beta/messages.md) [[Source](https://platform.claude.com/docs/en/api/java/beta/messages)]

* Page was previously showing a loading error ("Something went wrong / Loading chunk failed") and is now populated with the full Java SDK beta messages API reference, including `BetaMessage`, `BetaMessageTokensCount`, all model type definitions, and available model constants (including `claude-fable-5`).

#### [Java beta Messages - Create a Message](https://github.com/gpambrozio/ClaudeDocs/blob/eae0226a/docs-md/api/api/java/beta/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/java/beta/messages/create)]

* Page was previously a stub titled "Create" with minimal content and is now the complete "Create a Message" reference, documenting all `MessageCreateParams` fields, beta header options, response types, and streaming variants for the Java SDK.

#### [self-hosted-sandboxes](https://github.com/gpambrozio/ClaudeDocs/blob/eae0226a/docs-md/api/managed-agents/self-hosted-sandboxes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

* Added AWS Lambda MicroVMs to the list of platform-specific guides for self-hosted agent sandboxes. [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/eae0226a/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L33)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]
