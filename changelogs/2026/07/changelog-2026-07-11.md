# [Claude docs changes for July 11th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4)]

## Executive Summary
- Claude Code 2.1.207 makes auto mode available on Bedrock, Vertex AI, and Foundry without the `CLAUDE_CODE_ENABLE_AUTO_MODE` opt-in, closes a plugin shell-injection vector, and fixes a security-consent dialog bypass on non-interactive runs plus terminal freezing during long streamed responses.
- A new `agent-memory-2026-07-22` beta header rolls out across the Managed Agents / Memory Store API reference, replacing `managed-agents-2026-04-01` for memory endpoints, with clearer `depth`/`limit`/pagination docs for listing memories.
- The Advisor tool docs are restructured to support Claude Fable 5 and Mythos 5 as advisor models, which return an encrypted `advisor_redacted_result` instead of plaintext advice; the quick start now pairs `claude-sonnet-5` with `claude-fable-5`.
- Access Transparency adds a `cmek_preserve` content-preservation event that can now be triggered by automated safety processing (not only human review), with two new reason codes for policy-violation and CSAE investigations.
- Two new Claude Code weekly digests land: Week 27 (Claude Sonnet 5 as the new subscription default, Claude in Chrome GA, background subagents, Claude Desktop on Linux beta, `/radio`) and Week 28 (in-app desktop browser, `/doctor` as a full setup checkup); Bedrock, Google Cloud's Agent Platform, and Claude Platform on AWS now default `opus` to Opus 4.8.

-----

## New Claude Code versions

### [2.1.207](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/versions/2.1.207.md)

#### New features

* Auto mode is now available without `CLAUDE_CODE_ENABLE_AUTO_MODE` opt-in on Bedrock, Vertex AI, and Foundry; disable via `disableAutoMode` in settings

#### Existing feature improvements

* Bedrock, Vertex, and Claude Platform on AWS now default to Claude Opus 4.8
* Auto mode config no longer reads `autoMode` from repo-resident `.claude/settings.local.json`; use `~/.claude/settings.json` instead
* Agent view: pasting the same text again now expands the existing `[Pasted text #N]` placeholder instead of adding a duplicate
* Agent view: blocked session peeks lead with the question and show a worded staleness clock (`waiting 3m`) instead of a duplicate timestamp
* Plugin hooks/monitors/MCP headersHelper: `${user_config.*}` in shell-form commands is now rejected, closing a shell-injection vector; use exec-form `args` or `$CLAUDE_PLUGIN_OPTION_<KEY>` instead
* Plugin option values (`pluginConfigs`) are no longer read from project-level `.claude/settings.json`; only user, `--settings`, and managed settings are honored

#### Major bug fixes

* Fixed the terminal freezing and keystrokes lagging while streaming responses containing very long lists, tables, paragraphs, or code blocks
* Fixed remote managed settings from a non-interactive run (`claude -p`, the SDK) being permanently recorded as consented without ever showing the security consent dialog
* Fixed spurious prompt-injection warnings triggered by benign system-generated conversation updates
* Fixed the auto-updater overwriting a custom launcher script or symlink at `~/.local/bin/claude` on every release; `/doctor` now reports an externally managed launcher
* Fixed a crash loop in agent teams where a malformed teammate mailbox message caused repeated errors every second until the mailbox file was manually deleted
* Fixed `extensions.worktreeConfig` being left in the repo's `.git/config` after the last `worktree.sparsePaths` worktree was removed, which broke go-git tools like `tea`
* Fixed malformed bracket patterns in rules globs, skill paths, `.ignore`, and `.worktreeinclude` breaking file reads, file suggestions, and worktree creation
* Fixed Remote Control task status updates being lost when the connection recovered from a network interruption or credential refresh
* Fixed Remote Control sessions hosted by the desktop app not showing background agent and workflow progress on mobile and web
* Fixed Bedrock repeatedly requesting fresh AWS SSO credentials from IAM Identity Center on every API request
* Fixed an indefinite hang on Windows when AWS credential resolution stalls (e.g. a stuck `credential_process`); a 60-second stall guard now fires instead of waiting forever
* Fixed `/usage-credits` amount inputs silently stripping malformed values (e.g. a pasted timestamp) to digits instead of rejecting them; amounts over $1,000 now require a typed confirmation

-----

## Claude Code changes

### New Documents

#### [whats-new/2026-w27](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/whats-new/2026-w27.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w27)]

Weekly dev digest for releases v2.1.195–v2.1.201 (June 29 – July 3, 2026): Claude Sonnet 5 becomes the default model for Pro, Team Standard, and Enterprise subscription seats (1M-token context, adaptive thinking on by default); Claude in Chrome reaches general availability; subagents run in the background by default instead of pausing the conversation; Claude Desktop launches in beta on Ubuntu/Debian; and `/radio` streams Claude FM lo-fi radio. Also notes Artifacts reaching Pro/Max, an org default model setting, stacked skill invocations (up to 5), and automatic retry of transient rate-limit errors.

#### [whats-new/2026-w28](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/whats-new/2026-w28.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w28)]

Weekly dev digest for releases v2.1.202–v2.1.206 (July 6–10, 2026): Claude Code desktop gets a built-in, sandboxed browser for external sites; `/doctor` (alias `/checkup`) becomes a full setup checkup that diagnoses and fixes issues instead of just reporting them. Also notes auto mode blocking transcript tampering and unresolved `rm -rf` targets, `/cd` path suggestions, and agent view state/headline improvements.

### Changed documents

#### [whats-new](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/whats-new.md) [[Source](https://code.claude.com/docs/en/whats-new)]

* Added the Week 27 and Week 28 digest summaries linking to the two new pages above. [[lines 5-24](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/whats-new.md?plain=1#L5-L24)] [[Source](https://code.claude.com/docs/en/whats-new)]

#### [Agent SDK for Python](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* New `SystemPromptFile` option (`{"type": "file", "path": "..."}`) loads a large system prompt from disk instead of passing it as a string, avoiding OS argv length limits (~128 KB on Linux, ~32 KB on Windows) that fail process spawn with the string form. [[lines 864-879](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/agent-sdk/python.md?plain=1#L864-L879)] [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

#### [Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/amazon-bedrock.md), [Google Cloud's Agent Platform](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/google-vertex-ai.md), [Claude Platform on AWS](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/claude-platform-on-aws.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Without pinning env vars, the `opus` alias now resolves to Opus 4.8 on all three providers (previously Opus 4.6 on Bedrock/Vertex, 4.7 on Claude Platform on AWS); Bedrock and Vertex's unpinned primary model default also moves from Sonnet 4.5 to Opus 4.8. [[lines 166-181](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/amazon-bedrock.md?plain=1#L166-L181)] [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

#### [Model configuration](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Provider default-model table split out per provider: Claude Platform on AWS's `default` mode now resolves to Opus 4.8 (was 4.7), and Bedrock/Google Cloud's Agent Platform now default to Opus 4.8 while Microsoft Foundry stays on Sonnet 4.5/Opus 4.6. [[lines 28-40](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/model-config.md?plain=1#L28-L40)] [[lines 262-268](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/model-config.md?plain=1#L262-L268)] [[Source](https://code.claude.com/docs/en/model-config)]
* Fable 5's automated content-safety fallback now always re-runs on Opus 4.8 (dropping the separate Opus 4.7 fallback previously used on Claude Platform on AWS). [[line 315](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/model-config.md?plain=1#L315)] [[Source](https://code.claude.com/docs/en/model-config)]

#### [Permission modes](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/permission-modes.md), [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/permissions.md), [Glossary](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/glossary.md), [Desktop application](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/desktop.md), [How Claude Code works](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/how-claude-code-works.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Auto mode is no longer labeled a "research preview" in any of these docs — it's now described as generally available, though still not a safety guarantee. [[line 139](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/permission-modes.md?plain=1#L139)] [[Source](https://code.claude.com/docs/en/permission-modes)]

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/permissions.md), [Security](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/security.md), [Communications kit](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/communications-kit.md), [VS Code](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/vs-code.md), [Tools reference](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Read-only file tools (Read, Grep, Glob) now document that they prompt for paths outside the working directory and `additionalDirectories`, not just edits/shell commands; Manual mode's description changes from "asks before each action" to "asks before file edits and most shell commands." [[lines 8-10](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/permissions.md?plain=1#L8-L10)] [[Source](https://code.claude.com/docs/en/permissions)]
* A built-in set of read-only Bash commands (e.g. `ls`, `cat`, `git status`) runs without prompting regardless of mode; restrict it with sandbox `denyRead` rules. [[lines 7-17](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/security.md?plain=1#L7-L17)] [[Source](https://code.claude.com/docs/en/security)]
* New Tools reference paragraph explains the "Permission required" column: tools marked No can still prompt for out-of-directory paths, and `Bash` is marked Yes despite its built-in read-only command allowlist. [[line 5](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/tools-reference.md?plain=1#L5)] [[Source](https://code.claude.com/docs/en/tools-reference)]

#### [Errors reference](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Anchor links with apostrophes now use plain ASCII IDs (e.g. `#youve-hit-your-session-limit` instead of the URL-encoded curly-quote form), fixing links that previously failed to jump to the right section in some renderers. [[lines 23-35](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/errors.md?plain=1#L23-L35)] [[Source](https://code.claude.com/docs/en/errors)]

#### [Claude Desktop on Linux](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/desktop-linux.md) [[Source](https://code.claude.com/docs/en/desktop-linux)]

* New "Troubleshoot" section covers `E: Unable to locate package claude-desktop`: check the repository file was written, that `dpkg --print-architecture` reports `amd64`/`arm64`, and `apt update` output for reachability/key errors before falling back to a downloaded install. [[lines 97-108](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/claude-code/desktop-linux.md?plain=1#L97-L108)] [[Source](https://code.claude.com/docs/en/desktop-linux)]

### Minor edits (not itemized individually)

* `index.md` and `overview.md` reworded "environment" to "surface" in a couple of places, with no new information beyond what's covered above.

-----

## API changes

### Changed documents

#### [Access Transparency](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/manage-claude/access-transparency.md) [[Source](https://platform.claude.com/docs/en/manage-claude/access-transparency)]

* A `cmek_preserve` preservation event can now be written whether preservation was initiated by human review or an automated safety pipeline; previously the docs stated preservation always followed a human `anthropic_access` event. [[lines 24-25](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/manage-claude/access-transparency.md?plain=1#L24-L25)] [[lines 115-155](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/manage-claude/access-transparency.md?plain=1#L115-L155)] [[Source](https://platform.claude.com/docs/en/manage-claude/access-transparency)]
* Two new reason codes documented: `policy_violation_investigation` and `csae_report`, both used for preservation events rather than access events. [[lines 161-167](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/manage-claude/access-transparency.md?plain=1#L161-L167)] [[Source](https://platform.claude.com/docs/en/manage-claude/access-transparency)]

#### [Advisor tool](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/agents-and-tools/tool-use/advisor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

* Claude Fable 5 and Mythos 5 can now be advisor models; their result comes back as an encrypted `advisor_redacted_result` (server-side only), while Opus 4.8 still returns the plaintext `advisor_result` shown in earlier examples. [[lines 64-65](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L64-L65)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]
* Quick start now pairs `claude-sonnet-5` as executor with `claude-fable-5` as advisor (previously `claude-sonnet-4-6`/`claude-opus-4-8`); "Model compatibility" and "Platform availability" sections are reordered after "Cost control." [[lines 40-65](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L40-L65)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

#### [Beta headers](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/api/beta.md), [Create Agent](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/api/beta/agents/create.md), [Create Skill](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/api/beta/skills/create.md), [Create Skill Version](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/api/beta/skills/versions/create.md), [List memories](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/api/beta/memory_stores/memories/list.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* New `agent-memory-2026-07-22` beta header added to the `anthropic-beta` enum (also reflected across the Python, TypeScript, Java, and Go reference pages). [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/api/beta.md?plain=1#L82)] [[Source](https://platform.claude.com/docs/en/api/beta)]
* List memories: `depth`, `limit`, `path_prefix`, and `view` get precise semantics (e.g. `path_prefix` must end with `/`; `view=full` caps `limit` at 20), and the `order`/`order_by` params are removed in favor of a stable server-defined order. [[lines 20-60](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/api/beta/memory_stores/memories/list.md?plain=1#L20-L60)] [[Source](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list)]
* Custom tool `description` limit is now documented as 1-4096 characters (up from 1-1024) on this reference set. [[line 573](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/api/beta/agents/create.md?plain=1#L573)] [[Source](https://platform.claude.com/docs/en/api/beta/agents/create)]
* Create Skill / Create Skill Version: `files` is now a required parameter (was optional), and the request example switches to `Content-Type: multipart/form-data` with a sample `-F files=` upload. [[lines 88-96](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/api/beta/skills/create.md?plain=1#L88-L96)] [[lines 168-176](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/api/beta/skills/versions/create.md?plain=1#L168-L176)] [[Source](https://platform.claude.com/docs/en/api/beta/skills/create)]

#### [Webhooks](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/api/beta/webhooks.md), [Work](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/api/beta/environments/work.md) [[Source](https://platform.claude.com/docs/en/api/beta/webhooks)]

* The `environment.*` and `memory_store.*` webhook event types and their event-data schemas are removed from the reference (default, Python, TypeScript, Java, and Go pages). [[line 850](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/api/beta/webhooks.md?plain=1#L850)] [[Source](https://platform.claude.com/docs/en/api/beta/webhooks)]
* The `secret` credential field on `BetaSelfHostedWork` is removed from every work endpoint's schema, including polling (default, Python, TypeScript, Java, and Go pages). [[line 93](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/api/beta/environments/work.md?plain=1#L93)] [[Source](https://platform.claude.com/docs/en/api/beta/environments/work)]

#### [Fallback credit](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/build-with-claude/fallback-credit.md), [Refusals and fallback](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/build-with-claude/refusals-and-fallback.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)]

* The refusal-fallback SDK middleware is now documented as available in every Anthropic SDK, including Ruby and PHP, which previously required the manual detect-and-retry pattern. [[lines 89-91](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/build-with-claude/refusals-and-fallback.md?plain=1#L89-L91)] [[lines 258-259](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/build-with-claude/refusals-and-fallback.md?plain=1#L258-L259)] [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)]
* Fallback credit's manual-retry guidance now scopes to "raw HTTP or custom retry logic" only, since Ruby and PHP get the SDK middleware. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/3a567ebbf1d64e6a0aeb4fea901c6f728087a8f4/docs-md/api/build-with-claude/fallback-credit.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/build-with-claude/fallback-credit)]

### Minor edits (not itemized individually)

* Dozens of per-language (default/Python/TypeScript/Java/Go) API reference pages under `docs-md/api/api/**` picked up only the `agent-memory-2026-07-22` beta header addition and the bumped "N more" beta-header count described above, with no other new information.
