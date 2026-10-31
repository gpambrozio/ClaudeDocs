# [Claude docs changes for October 31st, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/4a031a86788e1182b0a203ee0b93fdc01842e01b) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/4a031a86788e1182b0a203ee0b93fdc01842e01b)]

## Executive Summary
- Claude Code 2.1.316 deprecates fast mode for Opus 4.8 (removal on November 30, 2026, with no fallback to standard Opus 4.8), so users should migrate to Opus 5.5. The API docs say the same.
- A new **Ultra** subscription plan now appears throughout the Claude Code and API docs, including plan eligibility, API credits ($200/month), ultrareview (3 free runs) and fast mode.
- New Claude Tag organization admin API reference (beta) for bundles, bundle targets, Slack channels and Slack workspaces, plus a new `experimental-claude-tag-2026-10-21` beta header across the SDK references.
- The Claude apps gateway gets pooled group budgets, a layered policy mode and Bedrock guardrail input tagging. New env vars `CLAUDE_CODE_DISABLE_ULTRATHINK` and `CLAUDE_CODE_SUBAGENT_EFFORT` are also added.
- The citations guide gains a section on getting structured data with citations.

## New Claude Code versions

### [2.1.316](https://github.com/gpambrozio/ClaudeDocs/blob/4a031a86788e1182b0a203ee0b93fdc01842e01b/versions/2.1.316.md)

#### New features

* Added `CLAUDE_CODE_DISABLE_ULTRATHINK` to turn the `ultrathink` keyword off
* Added `CLAUDE_CODE_SUBAGENT_EFFORT` to set the default effort level of subagents instead of inheriting the session's
* Claude apps gateway: pooled group budgets (`pooled_budget` on the spend limits admin API), `managed.policy_mode: layered` (all matching policies apply, merged), and `guardrail.input_tagging` for Amazon Bedrock guardrail upstreams
* Added `CLAUDE_CODE_DISABLE_LOOPED_CROSS_CERT_DROP` to keep looped system cross-certificates for servers whose private CA needs one
* Deprecated fast mode for Opus 4.8 (removed November 30, 2026); migrate to Opus 5.5
* VS Code: sign in to a Claude apps gateway from the chat panel; `ultrathink` now runs at `xhigh` effort
* Cloud sessions: form card for MCP server forms, a "Catching up…" indicator, and Enterprise members can add and delete network secrets
* Code Review analytics: new findings-by-severity card

#### Existing feature improvements

* `/code-review` from Desktop or web shows the findings card in cloud and `claude remote-control` sessions
* `/diff` on large repositories runs fewer git commands and spaces out refreshes
* Clearer messages when no GitHub remote is found for `/ultrareview`, cloud sessions or cloud agents
* SSL certificate errors now name likely causes (such as a missing intermediate certificate) and fixes
* Server-managed settings for Team and Enterprise logins apply without an approval prompt, and unverifiable stored copies are refused
* Auto mode: an `autoMode.allow` list without `"$defaults"` no longer removes the built-in rule on scheduled-task prompts
* Claude Tag: Slack channel "Respond automatically" switch became a "How Claude participates" choice

#### Major bug fixes

* Shell commands are no longer left running on macOS/Linux when Claude Code exits by itself
* The Claude apps gateway now checks every model a request names against `availableModels`, `deniedModels` and `models`
* `--restricted` sessions no longer upload files outside the working directories
* PowerShell hooks now block on exit code 2 for commands that begin with a type cast, `param`, `using` or an attribute
* Fixed bash alias/function loss in the Bash tool, and scripts stopping after the first command when `SHELLOPTS` is exported
* Fixed `sonnet`/`opus`/`haiku` aliases erroring mid-session on Vertex AI and Bedrock when the newest model is unavailable
* Fixed `claude auth login` refusing to run where managed settings require a Claude apps gateway
* Fixed Grep and Glob hanging on Windows when the search process is killed but does not exit

-----

## Claude Code changes

### Changed documents

#### [Many pages: Ultra plan](https://github.com/gpambrozio/ClaudeDocs/blob/4a031a86788e1182b0a203ee0b93fdc01842e01b/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* "Ultra" was added as a subscription plan next to Pro and Max in plan requirements, authentication, `/usage`, `/privacy-settings`, `/restart`, bypass permissions, Dispatch, routines/scheduled tasks, network secrets, Slack, Projects, artifacts, data usage and legal pages.

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/4a031a86788e1182b0a203ee0b93fdc01842e01b/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Ultra added to eligible plans and usage-credits instructions. [[lines 19-20](https://github.com/gpambrozio/ClaudeDocs/blob/4a031a86788e1182b0a203ee0b93fdc01842e01b/docs-md/claude-code/fast-mode.md?plain=1#L19-L20)] [[Source](https://code.claude.com/docs/en/fast-mode#speed-up-responses-with-fast-mode)]

#### [glossary](https://github.com/gpambrozio/ClaudeDocs/blob/4a031a86788e1182b0a203ee0b93fdc01842e01b/docs-md/claude-code/glossary.md) [[Source](https://code.claude.com/docs/en/glossary)]

* Auto mode entry now separates behavior by version: v2.1.283+ makes it the built-in starting mode, while earlier versions do so only on Pro, Max, Ultra and Team. [[line 53](https://github.com/gpambrozio/ClaudeDocs/blob/4a031a86788e1182b0a203ee0b93fdc01842e01b/docs-md/claude-code/glossary.md?plain=1#L53)] [[Source](https://code.claude.com/docs/en/glossary#auto-mode)]

#### [ultrareview](https://github.com/gpambrozio/ClaudeDocs/blob/4a031a86788e1182b0a203ee0b93fdc01842e01b/docs-md/claude-code/ultrareview.md) [[Source](https://code.claude.com/docs/en/ultrareview)]

* The pricing table adds the Ultra plan: 3 free runs, then billed as usage credits. [[line 119](https://github.com/gpambrozio/ClaudeDocs/blob/4a031a86788e1182b0a203ee0b93fdc01842e01b/docs-md/claude-code/ultrareview.md?plain=1#L119)] [[Source](https://code.claude.com/docs/en/ultrareview#pricing-and-free-runs)]

#### [slack](https://github.com/gpambrozio/ClaudeDocs/blob/4a031a86788e1182b0a203ee0b93fdc01842e01b/docs-md/claude-code/slack.md) [[Source](https://code.claude.com/docs/en/slack)]

* Clarified that the earlier Claude Code in Slack answers only Pro, Max and Ultra accounts in workspaces not connected to Claude Tag.

#### Formatting-only changes

* Many pages (for example hooks, hooks-guide, setup, settings-example, troubleshoot-install, features-overview) changed mostly because platform and language tabs are now rendered as `> [tab]` blockquotes and link cards as `> [card]`, with no substantive content change.

-----

## API changes

### New Documents

#### [claude_tag](https://github.com/gpambrozio/ClaudeDocs/blob/4a031a86788e1182b0a203ee0b93fdc01842e01b/docs-md/api/api/beta/organization/claude_tag.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/claude_tag)]

New beta Claude Tag organization admin API reference. It defines domain types such as guest policies (`allow`, `restrict`, `channel_only`) and setting sources. Sub-pages cover:

* `claude_tag/bundles` (list, retrieve) and `bundles/targets` (create, delete, list, retrieve)
* `claude_tag/slack_channels` (create, delete, list, retrieve, update)
* `claude_tag/slack_workspaces` (list, retrieve, update)

### Changed documents

#### [api-credits-for-subscribers](https://github.com/gpambrozio/ClaudeDocs/blob/4a031a86788e1182b0a203ee0b93fdc01842e01b/docs-md/api/about-claude/api-credits-for-subscribers.md) [[Source](https://platform.claude.com/docs/en/about-claude/api-credits-for-subscribers)]

* Retitled to "API credits for Max, Ultra, and Team plans". Max 5x/20x tiers are replaced by Max ($100) and Ultra ($200), and upgrade paths were updated.

#### [citations](https://github.com/gpambrozio/ClaudeDocs/blob/4a031a86788e1182b0a203ee0b93fdc01842e01b/docs-md/api/build-with-claude/citations.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/citations)]

* New "Get structured data with citations" section: prompt for one `field: value` line per field and parse it yourself. Avoid JSON-only prompts, which can return few or no citations. [[lines 403-460](https://github.com/gpambrozio/ClaudeDocs/blob/4a031a86788e1182b0a203ee0b93fdc01842e01b/docs-md/api/build-with-claude/citations.md?plain=1#L403-L460)] [[Source](https://platform.claude.com/docs/en/build-with-claude/citations#get-structured-data-with-citations)]
* Feature status labels changed from `ga` to `stable` (also on other feature pages such as fast-mode).

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/4a031a86788e1182b0a203ee0b93fdc01842e01b/docs-md/api/build-with-claude/fast-mode.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

* Fast mode on Claude Opus 4.8 is deprecated and will be removed on November 30, 2026. After that, `claude-opus-4-8` requests with `speed: "fast"` return an error. Migrate to Opus 5.5. [[lines 683-685](https://github.com/gpambrozio/ClaudeDocs/blob/4a031a86788e1182b0a203ee0b93fdc01842e01b/docs-md/api/build-with-claude/fast-mode.md?plain=1#L683-L685)] [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode#api-support)]

#### [SDK references (beta deployments, etc.)](https://github.com/gpambrozio/ClaudeDocs/blob/4a031a86788e1182b0a203ee0b93fdc01842e01b/docs-md/api/api/csharp/beta/deployments.md) [[Source](https://platform.claude.com/docs/en/api/csharp/beta/deployments)]

* New `experimental-claude-tag-2026-10-21` beta header value added to Deployments endpoints and mirrored across the per-language SDK references (C#, CLI, etc.).
* The CLI and C# `beta` references and the compliance API references were substantially expanded.
