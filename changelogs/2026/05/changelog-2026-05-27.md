# [Claude docs changes for May 27th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1)]

## Executive Summary
- New `security-guidance` plugin documentation: automatically reviews Claude's code changes for vulnerabilities (injection, unsafe deserialization, DOM injection, etc.) and fixes them in the same session, at three layers: per-edit pattern match, end-of-turn diff review, and commit/push review
- New comprehensive guide for monorepos and large codebases covering per-directory CLAUDE.md files, sparse worktrees, code intelligence plugins, and centralized convention management
- Version 2.1.152 adds a `MessageDisplay` hook for transforming assistant message text, `SessionStart` enhancements (session title setting, skill reloading), and `disallowed-tools` frontmatter for skills/commands
- Version 2.1.152: auto mode no longer requires opt-in consent, and `/code-review --fix` now applies findings directly to the working tree
- Corrected documentation across Bedrock, Vertex AI, and Microsoft Foundry: only `/logout` is unavailable when using cloud provider credentials (not `/login`)

## New Claude Code versions

### [2.1.152](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/versions/2.1.152.md)

#### New features

* `/code-review --fix` now applies review findings to the working tree after the review; `/simplify` now invokes `/code-review --fix`
* Skills and slash commands can now set `disallowed-tools` in frontmatter to remove tools from the model while the skill or command is active
* Added `/reload-skills` command to re-scan skill directories without restarting the session
* `SessionStart` hooks can now return `reloadSkills: true` to re-scan skill directories, making skills installed by the hook available in the same session
* `SessionStart` hooks can now set the session title via `hookSpecificOutput.sessionTitle` on startup and resume
* Added a `MessageDisplay` hook event that lets hooks transform or hide assistant message text as it is displayed
* Added `pluginSuggestionMarketplaces` managed setting: admins can allowlist org marketplaces whose plugins may be suggested via context-aware tips
* `claude plugin marketplace remove` now accepts `--scope user|project|local` for symmetry with other marketplace commands
* Auto mode no longer requires opt-in consent
* Vim mode: `/` in NORMAL mode now opens reverse history search (like Ctrl+R), matching bash/zsh vi-mode

#### Existing feature improvements

* Claude Code now switches to the configured `--fallback-model` for the rest of the session when the primary model is not found, instead of failing every request
* The `/usage` breakdown now includes large session files; files are scanned with a streaming read so memory usage stays flat
* Thinking summaries in the collapsed group now stay readable for at least 3 seconds, render as markdown, and cap at 10 lines (`Ctrl+O` shows full thinking)
* In fullscreen mode, the "Thinking for Ns" indicator now counts up live while the model is thinking and keeps its value if you interrupt mid-thought
* Simplified the Workflow tool's inline progress display — live agent counts now show only in the persistent workflow status row
* The post-response timer now shows "Waiting for N background agents/workflows to finish" when backgrounded work is still running, and reports cumulative time once results are processed
* Added the session entrypoint as an OpenTelemetry metric attribute (`app.entrypoint`, opt-in via `OTEL_METRICS_INCLUDE_ENTRYPOINT=true`)

#### Major bug fixes

* Fixed terminal styling degrading in very long sessions by recycling the renderer's style pool
* Fixed sessions getting stuck after a model or login switch left stale thinking-block signatures in history
* Fixed `cache_creation_input_tokens` reporting as 0 in transcript and result usage when the API reports cache writes only via the nested `cache_creation` breakdown
* Fixed remote MCP servers failing to connect in Claude Code Remote sessions when the egress proxy is enabled
* Fixed plugin MCP servers with the same command but different environment variables being incorrectly deduplicated
* Fixed plugins that track a git branch silently no longer receiving updates after the plugin registry was rebuilt

-----

## Claude Code changes

### New Documents

#### [Large codebases](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/large-codebases.md) [[Source](https://code.claude.com/docs/en/large-codebases)]

New guide: "Set up Claude Code in a monorepo or large codebase." Covers layering per-directory CLAUDE.md files, excluding irrelevant CLAUDE.md files with `claudeMdExcludes`, blocking reads of generated/vendored code with `Read` deny rules, using code intelligence plugins to replace file scans, configuring `worktree.sparsePaths` for lightweight worktrees, granting cross-package access with `additionalDirectories`, adding per-directory skills, and centralizing conventions via plugins when directory-level layering stops scaling.

#### [Security guidance](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/security-guidance.md) [[Source](https://code.claude.com/docs/en/security-guidance)]

New guide for the `security-guidance` plugin, which reviews Claude's own code changes for common vulnerabilities and fixes them in the same session. Describes three review layers: per-edit pattern match (no model call), end-of-turn diff review by a separate Claude instance, and an agentic commit/push review with surrounding code context. Covers custom rules via `.claude/claude-security-guidance.md` and `.claude/security-patterns.yaml`, usage costs, how to disable individual layers, and how the plugin fits alongside `/security-review` and PR-time code review.

### Changed documents

#### [Admin setup](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

* Added link to the new monorepo/large codebase guide for organizations deploying into a monorepo. [[line 123](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/admin-setup.md?plain=1#L123)] [[Source](https://code.claude.com/docs/en/admin-setup#next-steps)]

#### [Agent SDK - Overview](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/agent-sdk/overview.md) [[Source](https://code.claude.com/docs/en/agent-sdk/overview)]

* Commands (formerly "Slash commands") are now described as the legacy format; the description explicitly says to use skills for new custom commands. [[line 321](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/agent-sdk/overview.md?plain=1#L321)] [[Source](https://code.claude.com/docs/en/agent-sdk/overview#claude-code-features)]
* Plugins description updated to "Extend with skills, agents, hooks, and MCP servers" (removed "custom commands"). [[line 323](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/agent-sdk/overview.md?plain=1#L323)] [[Source](https://code.claude.com/docs/en/agent-sdk/overview#claude-code-features)]

#### [Agent SDK - Plugins](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/agent-sdk/plugins.md) [[Source](https://code.claude.com/docs/en/agent-sdk/plugins)]

* The SDK init message now includes a `skills` field listing available plugin skills (separate from `slash_commands`); the code example is updated to show both. [[line 143](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/agent-sdk/plugins.md?plain=1#L143)] [[Source](https://code.claude.com/docs/en/agent-sdk/plugins#complete-example)]
* Troubleshooting now says to verify that a skill appears in the `skills` list (not `slash_commands`) when debugging plugin skill invocation. [[line 225](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/agent-sdk/plugins.md?plain=1#L225)] [[Source](https://code.claude.com/docs/en/agent-sdk/plugins#skills-not-appearing)]

#### [Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Corrected: when using Bedrock, only the `/logout` command is unavailable — `/login` is still available. [[line 158](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/amazon-bedrock.md?plain=1#L158)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#3-configure-claude-code)]

#### [Best practices](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Added guidance to have Claude show evidence of success (test output, command result, screenshot) rather than asserting it — reviewing evidence is faster than re-running verification. [[line 37](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/best-practices.md?plain=1#L37)] [[Source](https://code.claude.com/docs/en/best-practices#give-claude-a-way-to-verify-its-work)]
* Added tip that the most useful specs are self-contained: they name files and interfaces involved, state what is out of scope, and end with an end-to-end verification step. [[line 338](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/best-practices.md?plain=1#L338)] [[Source](https://code.claude.com/docs/en/best-practices#let-claude-interview-you)]
* Corrected non-interactive streaming example: `--output-format stream-json` now requires `--verbose`. [[line 415](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/best-practices.md?plain=1#L415)] [[Source](https://code.claude.com/docs/en/best-practices#run-non-interactive-mode)]
* New "Add an adversarial review step" section: guidance on using a subagent in fresh context to review diffs against the plan before treating a task as done, including how to use `/code-review` and how to avoid over-engineering from reviewer findings. [[line 499](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/best-practices.md?plain=1#L499)] [[Source](https://code.claude.com/docs/en/best-practices#add-an-adversarial-review-step)]

#### [CLI reference](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Updated usage examples for `--include-hook-events`, `--include-partial-messages`, and `--replay-user-messages` to include `--verbose`, which is now required alongside `--output-format stream-json`. [[lines 78-79](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/cli-reference.md?plain=1#L78-L79), [line 99](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/cli-reference.md?plain=1#L99)]

#### [Common workflows](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Added reference to the new monorepo/large codebase guide in the "Understand new codebases" section. [[line 25](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/common-workflows.md?plain=1#L25)] [[Source](https://code.claude.com/docs/en/common-workflows#understand-new-codebases)]

#### [Discover plugins](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Added new "Automatic security review" section listing the `security-guidance` plugin, which reviews each change Claude makes for common vulnerabilities and instructs Claude to fix them in the same session. [[line 90](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/discover-plugins.md?plain=1#L90)] [[Source](https://code.claude.com/docs/en/discover-plugins#automatic-security-review)]

#### [Google Vertex AI](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/google-vertex-ai.md) [[Source](https://code.claude.com/docs/en/google-vertex-ai)]

* Corrected: when using Vertex AI, only the `/logout` command is unavailable — `/login` is still available. [[line 130](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/google-vertex-ai.md?plain=1#L130)] [[Source](https://code.claude.com/docs/en/google-vertex-ai#4-configure-claude-code)]

#### [Hooks guide](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Added reference to the `security-guidance` plugin as a production example of hooks that run a separate model review and feed findings back into the session. [[line 93](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/hooks-guide.md?plain=1#L93)] [[Source](https://code.claude.com/docs/en/hooks-guide#what-you-can-automate)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Clarified scope precedence behavior: when the same server is defined in multiple scopes, the entire server entry from the highest-precedence source is used — fields are not merged across scopes. [[line 304](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/mcp.md?plain=1#L304)] [[Source](https://code.claude.com/docs/en/mcp#scope-hierarchy-and-precedence)]

#### [Memory](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Added note that to block an action regardless of what Claude decides, use a `PreToolUse` hook rather than CLAUDE.md instructions. [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/memory.md?plain=1#L23)] [[Source](https://code.claude.com/docs/en/memory#claude-md-vs-auto-memory)]
* Corrected the maximum import recursion depth for `@path` imports in CLAUDE.md from five to four hops. [[line 87](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/memory.md?plain=1#L87)] [[Source](https://code.claude.com/docs/en/memory#import-additional-files)]
* Added reference to the new monorepo/large codebase guide for CLAUDE.md layout and per-directory rules. [[line 137](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/memory.md?plain=1#L137)] [[Source](https://code.claude.com/docs/en/memory#how-claude-md-files-load)]

#### [Microsoft Foundry](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/microsoft-foundry.md) [[Source](https://code.claude.com/docs/en/microsoft-foundry)]

* Corrected: when using Microsoft Foundry, only the `/logout` command is unavailable — `/login` is still available. [[line 59](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/microsoft-foundry.md?plain=1#L59)] [[Source](https://code.claude.com/docs/en/microsoft-foundry#2-configure-azure-credentials)]

#### [Security](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/security.md) [[Source](https://code.claude.com/docs/en/security)]

* Added link to the security guidance plugin in the related resources section. [[line 132](https://github.com/gpambrozio/ClaudeDocs/blob/9fa050cf9ba45b6d6adc67ecef0f2146d4cd1ce1/docs-md/claude-code/security.md?plain=1#L132)] [[Source](https://code.claude.com/docs/en/security#related-resources)]

-----

## API changes

No significant API documentation changes today.
