# [Claude docs changes for April 18th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/cb1b0d8) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/cb1b0d8)]

## Executive Summary
- Claude Code CLI now spawns a native platform binary instead of bundled JavaScript; `npm install` delivers the same binary via per-platform optional dependencies
- Claude in Amazon Bedrock is now GA and open to all customers — Claude Opus 4.7 and Haiku 4.5 available self-serve in 27 AWS regions with global and regional endpoints
- All Anthropic SDKs (Python, TypeScript, Go, Java, Ruby, C#) now expose a new `BedrockMantle` client class targeting the Messages API endpoint on Bedrock, recommended for all new projects
- New `sandbox.network.deniedDomains` setting lets you block specific domains even when a broader wildcard `allowedDomains` rule would otherwise permit them
- Three security improvements to the permission system: macOS dangerous-path detection, exec-wrapper bypass prevention, and `find -exec`/`-delete` auto-approval removed

## New Claude Code versions

### [2.1.113](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/versions/2.1.113.md)

#### New features

* CLI now spawns a native platform binary (via per-platform optional dependency) instead of bundled JavaScript
* Added `sandbox.network.deniedDomains` setting to block specific domains even when a broader `allowedDomains` wildcard would otherwise permit them
* `/extra-usage` now works from Remote Control (mobile/web) clients
* Remote Control clients can now query `@`-file autocomplete suggestions

#### Existing feature improvements

* Fullscreen mode: Shift+↑/↓ now scrolls the viewport when extending a selection past the visible edge
* `Ctrl+A` and `Ctrl+E` now move to the start/end of the current logical line in multiline input (readline behavior)
* Windows: `Ctrl+Backspace` now deletes the previous word
* Long URLs in responses and bash output stay clickable when wrapping across lines (in terminals with OSC 8 hyperlinks)
* Improved `/loop`: pressing Esc cancels pending wakeups; wakeups display as "Claude resuming /loop wakeup" for clarity
* Improved `/ultrareview`: faster launch with parallelized checks, diffstat in the launch dialog, and animated launching state
* Subagents that stall mid-stream now fail with a clear error after 10 minutes instead of hanging silently
* Bash tool: multi-line commands whose first line is a comment now show the full command in the transcript, closing a UI-spoofing vector
* Running `cd <current-directory> && git …` no longer triggers a permission prompt when the `cd` is a no-op
* Security: on macOS, `/private/{etc,var,tmp,home}` paths are treated as dangerous removal targets under `Bash(rm:*)` allow rules
* Security: Bash deny rules now match commands wrapped in `env`/`sudo`/`watch`/`ionice`/`setsid` and similar exec wrappers
* Security: `Bash(find:*)` allow rules no longer auto-approve `find -exec`/`-delete`

#### Major bug fixes

* Fixed MCP concurrent-call timeout handling where a message for one tool call could silently disarm another call's watchdog
* Fixed Bash `dangerouslyDisableSandbox` running commands outside the sandbox without a permission prompt
* Fixed messages typed while viewing a running subagent being hidden from its transcript and misattributed to the parent AI
* Fixed Remote Control sessions not streaming subagent transcripts
* Fixed Remote Control sessions not being archived when Claude Code exits
* Fixed `thinking.type.enabled is not supported` 400 error when using Opus 4.7 via a Bedrock Application Inference Profile ARN
* Fixed compacting a resumed long-context session failing with "Extra usage is required for long context requests"
* Fixed Cmd-backspace / `Ctrl+U` to once again delete from the cursor to the start of the line
* Fixed markdown tables breaking when a cell contains an inline code span with a pipe character
* Fixed `/insights` crashing with `EBUSY` on Windows

### [2.1.114](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/versions/2.1.114.md)

#### Major bug fixes

* Fixed a crash in the permission dialog when an agent teams teammate requested tool permission

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/hosting](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/agent-sdk/hosting.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hosting)]

* Updated runtime dependencies note: both SDK packages now bundle a native Claude Code binary for the host platform; no separate Claude Code or Node.js install is needed for the spawned CLI. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/agent-sdk/hosting.md?plain=1#L19)] [[Source](https://code.claude.com/docs/en/agent-sdk/hosting#system-requirements)]

#### [agent-sdk/overview](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/agent-sdk/overview.md) [[Source](https://code.claude.com/docs/en/agent-sdk/overview)]

* Added note that the TypeScript SDK bundles a native Claude Code binary as an optional dependency — no separate Claude Code install required. [[line 53](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/agent-sdk/overview.md?plain=1#L53)] [[Source](https://code.claude.com/docs/en/agent-sdk/overview#get-started)]

#### [agent-sdk/quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/agent-sdk/quickstart.md) [[Source](https://code.claude.com/docs/en/agent-sdk/quickstart)]

* Added note that the TypeScript SDK bundles a native Claude Code binary as an optional dependency. [[line 55](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/agent-sdk/quickstart.md?plain=1#L55)] [[Source](https://code.claude.com/docs/en/agent-sdk/quickstart#setup)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Added note that the SDK bundles a native Claude Code binary via optional dependency; `pathToClaudeCodeExecutable` is only needed if optional dependencies were skipped or the platform is unsupported. [[lines 10-11](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L10-L11)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#installation)]
* Clarified `pathToClaudeCodeExecutable` option description — auto-resolved from bundled native binary by default. [[line 340](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L340)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#options)]

#### [agent-sdk/typescript-v2-preview](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/agent-sdk/typescript-v2-preview.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview)]

* Added note that the SDK bundles a native Claude Code binary as an optional dependency. [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/agent-sdk/typescript-v2-preview.md?plain=1#L18)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#installation)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Clarified the `once` field: it is only honored for hooks declared in skill frontmatter; it is ignored in settings files and agent frontmatter. [[line 283](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/hooks.md?plain=1#L283)] [[Source](https://code.claude.com/docs/en/hooks#common-fields)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Added clarification that the `opusplan` model alias uses the standard 200K context window during the plan-mode Opus phase; the automatic 1M upgrade for the `opus` setting does not extend to `opusplan`. [[line 136](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/model-config.md?plain=1#L136)] [[Source](https://code.claude.com/docs/en/model-config#opusplan-model-setting)]

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* Removed the "From fork" PR filter option from the routine filter table and its associated example. [[line 232](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/routines.md?plain=1#L232)] [[Source](https://code.claude.com/docs/en/routines#filter-pull-requests)]

#### [setup](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* npm installation is no longer marked as deprecated; the section now explains that `npm install -g @anthropic-ai/claude-code` installs the same native binary as the standalone installer via per-platform optional dependencies. [[lines 265-278](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/setup.md?plain=1#L265-L278)] [[Source](https://code.claude.com/docs/en/setup#install-a-specific-version)]
* Listed the eight supported npm install platforms. [[line 276](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/setup.md?plain=1#L276)] [[Source](https://code.claude.com/docs/en/setup#install-with-npm)]

#### [troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* New troubleshooting section "Native binary not found after npm install" covering three causes: optional dependencies disabled, unsupported platform, and corporate npm mirror missing platform packages. Also notes that `--ignore-scripts` skips the postinstall link step and causes a slower fallback. [[lines 587-598](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/claude-code/troubleshooting.md?plain=1#L587-L598)] [[Source](https://code.claude.com/docs/en/troubleshooting#native-binary-not-found-after-npm-install)]

-----

## API changes

### Changed documents

#### [about-claude/models/overview](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/about-claude/models/overview.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]

* Updated footnote: Claude Opus 4.7 on AWS is now available through the full Claude in Amazon Bedrock endpoint (no longer a research preview). [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/about-claude/models/overview.md?plain=1#L36)] [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]

#### [about-claude/pricing](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* Updated AWS Bedrock links to point to the new `claude-in-amazon-bedrock` doc; added distinction between the new Messages-API endpoint (Opus 4.7, Haiku 4.5, newer models) and the legacy integration. [[lines 35-54](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/about-claude/pricing.md?plain=1#L35-L54)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

#### [api/sdks/csharp](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/api/sdks/csharp.md) [[Source](https://platform.claude.com/docs/en/api/sdks/csharp)]

* Added `AnthropicBedrockMantleClient` for the Messages-API Bedrock endpoint; `AnthropicBedrockClient` (legacy `InvokeModel` path) remains available. Recommended to use `AnthropicBedrockMantleClient` for new projects. [[lines 415-418](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/api/sdks/csharp.md?plain=1#L415-L418)] [[Source](https://platform.claude.com/docs/en/api/sdks/csharp)]

#### [api/sdks/go](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/api/sdks/go.md) [[Source](https://platform.claude.com/docs/en/api/sdks/go)]

* Added `bedrock.NewMantleClient` for the Messages-API Bedrock endpoint (SSE streaming); legacy `WithLoadDefaultConfig`/`WithConfig` remain for `InvokeModel` apps. Recommended to use `NewMantleClient` for new projects. [[lines 534-537](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/api/sdks/go.md?plain=1#L534-L537)] [[Source](https://platform.claude.com/docs/en/api/sdks/go)]

#### [api/sdks/java](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/api/sdks/java.md) [[Source](https://platform.claude.com/docs/en/api/sdks/java)]

* Added `BedrockMantleBackend.fromEnv()` for the Messages-API Bedrock endpoint; `BedrockBackend` remains for legacy `InvokeModel` apps. [[lines 1072-1076](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/api/sdks/java.md?plain=1#L1072-L1076)] [[Source](https://platform.claude.com/docs/en/api/sdks/java)]

#### [api/sdks/python](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/api/sdks/python.md) [[Source](https://platform.claude.com/docs/en/api/sdks/python)]

* Added `AnthropicBedrockMantle` client for the Messages-API Bedrock endpoint; `AnthropicBedrock` remains for legacy `InvokeModel` apps. Updated client table from three to four clients. [[lines 724-729](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/api/sdks/python.md?plain=1#L724-L729)] [[Source](https://platform.claude.com/docs/en/api/sdks/python)]

#### [api/sdks/ruby](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/api/sdks/ruby.md) [[Source](https://platform.claude.com/docs/en/api/sdks/ruby)]

* Added `Anthropic::BedrockMantleClient` (requires `aws-sdk-core` gem) for the Messages-API Bedrock endpoint; `Anthropic::BedrockClient` (requires `aws-sdk-bedrockruntime`) remains for legacy `InvokeModel` apps. [[lines 381-384](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/api/sdks/ruby.md?plain=1#L381-L384)] [[Source](https://platform.claude.com/docs/en/api/sdks/ruby)]

#### [api/sdks/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/api/sdks/typescript.md) [[Source](https://platform.claude.com/docs/en/api/sdks/typescript)]

* Added `AnthropicBedrockMantle` client from `@anthropic-ai/bedrock-sdk` for the Messages-API Bedrock endpoint; `AnthropicBedrock` remains for legacy `InvokeModel` apps. [[lines 771-775](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/api/sdks/typescript.md?plain=1#L771-L775)] [[Source](https://platform.claude.com/docs/en/api/sdks/typescript)]

#### [build-with-claude/claude-in-amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/build-with-claude/claude-in-amazon-bedrock.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)]

* GA announcement: Claude in Amazon Bedrock is now open to all customers (was research preview). Claude Opus 4.7 and Haiku 4.5 are self-serve; Claude Mythos Preview remains invitation-only. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/build-with-claude/claude-in-amazon-bedrock.md?plain=1#L11)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)]
* Prerequisites updated: now only requires standard Bedrock model access, not a dedicated allowlisted account (except for Mythos Preview). [[lines 17-23](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/build-with-claude/claude-in-amazon-bedrock.md?plain=1#L17-L23)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)]
* Added supported model table with model IDs and access levels. [[lines 169-173](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/build-with-claude/claude-in-amazon-bedrock.md?plain=1#L169-L173)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)]
* Added comprehensive region availability table covering 27 AWS regions with global, regional, and inference-profile endpoint types. [[lines 197-232](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/build-with-claude/claude-in-amazon-bedrock.md?plain=1#L197-L232)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)]
* Data retention section updated: now governed by Amazon Bedrock (AWS); ZDR is available by contacting AWS support. [[lines 238-241](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/build-with-claude/claude-in-amazon-bedrock.md?plain=1#L238-L241)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)]

#### [build-with-claude/claude-on-amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/build-with-claude/claude-on-amazon-bedrock.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock)]

* Page renamed to "Claude on Amazon Bedrock (legacy)" and intro updated to clarify it covers the `InvokeModel`/`Converse` APIs with ARN-versioned model IDs; new endpoint documented in `claude-in-amazon-bedrock`. [[lines 1-7](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/build-with-claude/claude-on-amazon-bedrock.md?plain=1#L1-L7)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock)]
* Added note that Claude Opus 4.7 is reachable via `InvokeModel` on `bedrock-runtime` but lacks an ARN-versioned model ID; full feature parity requires the new Bedrock endpoint. [[lines 68-76](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/build-with-claude/claude-on-amazon-bedrock.md?plain=1#L68-L76)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock)]

#### [build-with-claude/structured-outputs](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* Updated platform availability: Claude Opus 4.7 and Claude Mythos Preview are now available for structured outputs through the Claude in Amazon Bedrock Messages-API endpoint (previously only in research preview). [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Added April 18, 2026 entry: Claude in Amazon Bedrock is now GA and open to all customers, with Claude Opus 4.7 and Haiku 4.5 available self-serve in 27 AWS regions. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/cb1b0d8/docs-md/api/release-notes/overview.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]
