# [Claude docs changes for June 25th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/20eab6114bea019654f3948b42c556470cfd43a2) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/20eab6114bea019654f3948b42c556470cfd43a2)]

## Executive Summary
- LLM gateway docs were completely reorganized into three focused guides: a developer connect guide, an admin rollout guide, and a protocol reference — replacing the old monolithic configuration page
- New `sandbox.credentials` setting lets admins explicitly block credential files and secret environment variables from sandboxed Bash commands (requires v2.1.187)
- `availableModels` enforcement was significantly expanded: it now covers skills, commands, the advisor, background agents, and sessions restored from `/resume`, with a new surface-coverage table showing how delivery differs across CLI, Desktop, and cloud sessions
- v2.1.191 added `/rewind` support for resuming conversations from before `/clear` was run, fixed hooks with comma-separated matchers silently never firing, and reduced CPU usage during streaming by ~37%
- Organization admins can now restrict models via the Claude Console toggle (v2.1.187), enforced server-side for Anthropic API sessions independently from the `availableModels` settings key

## New Claude Code versions

### [2.1.190](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/versions/2.1.190.md)

#### Major bug fixes

* Bug fixes and reliability improvements

### [2.1.191](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/versions/2.1.191.md)

#### New features

* Added `/rewind` support for resuming a conversation from before `/clear` was run

#### Existing feature improvements

* Sandbox network permission dialog now remembers hosts you allow with "Yes" for the rest of the current session, so later connections to the same host do not re-prompt
* MCP server capability discovery (`tools/list`, `prompts/list`, `resources/list`) now retries transient network errors with short backoff
* MCP OAuth discovery and token requests now retry once after transient network errors, and headless environments (SSH, no display) skip the browser popup and go straight to paste-the-URL prompt
* MCP error messages now show the URL and point to MCP config on HTTP 404 errors
* Vim mode prompt-history search (NORMAL `/`) now hints how to reach slash commands
* Reduced CPU usage during streaming responses by ~37% by coalescing text updates to 100ms
* Reduced long-session memory growth from terminal output cache

#### Major bug fixes

* Fixed scroll position jumping to the bottom while reading earlier output during a streaming response
* Fixed background agents resurrecting after being stopped — stopping an agent from the tasks panel is now permanent
* Fixed `/voice` showing a generic "not available" message when disabled by an organization's policy — it now explains the restriction
* Fixed `/login` URL opening truncated in Windows Terminal when it wraps across lines
* Fixed Cmd+click on links in fullscreen mode for Ghostty over ssh/tmux
* Fixed `claude agents` sending builtin slash commands like `/usage` to background sessions as prompt text instead of showing a hint
* Fixed `claude agents` job rows showing full filesystem paths for pasted images instead of the `[Image #N]` placeholder
* Fixed hooks with comma-separated matchers (e.g. `"Bash,PowerShell"`) silently never firing
* Fixed `/permissions` Recently-denied tab: approving a denial now persists on close instead of being silently discarded
* Fixed the agent panel jumping by one row when scrolling the roster past the overflow cap
* Fixed the welcome splash art overflowing the default 80×24 macOS Terminal window
* Fixed managed settings `forceRemoteSettingsRefresh` not taking effect when set via MDM or file policy, and the fetch now sends `Cache-Control: no-cache` to prevent proxies from serving stale responses

-----

## Claude Code changes

### New Documents

#### [Connect Claude Code to an LLM gateway](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/llm-gateway-connect.md) [[Source](https://code.claude.com/docs/en/llm-gateway-connect)]

New developer guide for connecting to an organization-managed LLM gateway. Covers checking whether an administrator already distributed the configuration, and how to configure the gateway address and credentials manually using `ANTHROPIC_BASE_URL` and auth variables. Includes guidance on rotating credentials with `apiKeyHelper` and verifying the connection with `/status`.

#### [LLM gateway protocol reference](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/llm-gateway-protocol.md) [[Source](https://code.claude.com/docs/en/llm-gateway-protocol)]

New technical reference for organizations building or configuring a gateway product. Covers supported API formats (Anthropic Messages, Bedrock InvokeModel, Vertex rawPredict), which request headers must be forwarded for features to work, gateway model discovery via `/v1/models`, and what happens when the gateway does not forward beta headers.

#### [Roll out an LLM gateway](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/llm-gateway-rollout.md) [[Source](https://code.claude.com/docs/en/llm-gateway-rollout)]

New admin guide for deploying and distributing an LLM gateway to an organization. Walks through deploying the gateway, issuing per-developer credentials, distributing configuration through managed settings files, and verifying each developer's connection. Includes configuration examples for distributing the base URL and credential via `env` in managed settings.

### Changed documents

#### [Admin setup](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

* Added `availableModels` and `enforceAvailableModels` to the enforcement options table, with a note linking to the surface coverage documentation. [[line 65](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/admin-setup.md?plain=1#L65)] [[Source](https://code.claude.com/docs/en/admin-setup#decide-what-to-enforce)]
* Clarified that `fallbackModel` and `availableModels` are exceptions to the general array-merge rule — the managed value replaces lower layers rather than merging. [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/admin-setup.md?plain=1#L47)] [[Source](https://code.claude.com/docs/en/admin-setup#decide-how-settings-reach-devices)]

#### [Advisor](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/advisor.md) [[Source](https://code.claude.com/docs/en/advisor)]

* If the saved `advisorModel` is excluded by `availableModels`, the advisor is not invoked until you pick an allowed model with `/advisor`. [[line 34](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/advisor.md?plain=1#L34)] [[Source](https://code.claude.com/docs/en/advisor#use-the-/advisor-command)]
* The `--advisor` flag now exits with an error if the requested model is excluded by `availableModels`, in addition to when the main model doesn't support the advisor. [[line 54](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/advisor.md?plain=1#L54)] [[Source](https://code.claude.com/docs/en/advisor#use-the-advisor-flag)]

#### [Agent SDK — Claude Code features](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/agent-sdk/claude-code-features.md) [[Source](https://code.claude.com/docs/en/agent-sdk/claude-code-features)]

* Clarified that managed policy settings include both endpoint-managed (MDM/file) and server-managed settings, with distinct descriptions of when each applies and how to disable each. [[line 54](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/agent-sdk/claude-code-features.md?plain=1#L54)] [[Source](https://code.claude.com/docs/en/agent-sdk/claude-code-features#what-settingsources-does-not-control)]
* Added note that server-managed settings are fetched even in SDK deployments when authenticating with an org credential, and that filesystem isolation doesn't remove them. [[line 58](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/agent-sdk/claude-code-features.md?plain=1#L58)] [[Source](https://code.claude.com/docs/en/agent-sdk/claude-code-features#what-settingsources-does-not-control)]

#### [Agent SDK — Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* Updated matcher documentation to include comma (`,`) as an accepted list separator alongside `|`, with optional surrounding whitespace. [[line 153](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L153)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#matchers)]

#### [Agent SDK — Python](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* Clarified `setting_sources` behavior: endpoint-managed policy always loads; server-managed settings are fetched only when authenticating with an org credential on an eligible configuration. [[line 804](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/agent-sdk/python.md?plain=1#L804)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#claudeagentoptions)]

#### [Agent SDK — TypeScript](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Clarified `settingSources` and `resolveSettings` documentation to distinguish endpoint-managed policy (always loaded) from server-managed settings (fetched on eligible org-authenticated configurations, from on-disk cache in SDK). [[lines 345-346](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L345-L346)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#parameters-10)]

#### [Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Updated Mantle model ID example in `availableModels` to use version prefixes (`claude-haiku-4-5`) rather than bare aliases, because adding a Mantle ID removes the bare alias from the picker per the new merge behavior. [[line 344](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/amazon-bedrock.md?plain=1#L344)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#run-mantle-alongside-the-invoke-api)]

#### [Authentication](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/authentication.md) [[Source](https://code.claude.com/docs/en/authentication)]

* Clarified that `apiKeyHelper`, `ANTHROPIC_API_KEY`, and `ANTHROPIC_AUTH_TOKEN` apply to the CLI and CLI-wrapping surfaces (VS Code extension, Agent SDK, GitHub Actions), not just "terminal CLI sessions". [[line 131](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/authentication.md?plain=1#L131)] [[Source](https://code.claude.com/docs/en/authentication#credential-management)]

#### [Checkpointing](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/checkpointing.md) [[Source](https://code.claude.com/docs/en/checkpointing)]

* New section: the rewind menu now shows an entry to resume the session that was active before `/clear` ran, available until you exit Claude Code or resume a different session. Requires v2.1.191. [[lines 35-38](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/checkpointing.md?plain=1#L35-L38)] [[Source](https://code.claude.com/docs/en/checkpointing#rewind-past-a-cleared-conversation)]

#### [Claude Code on the web](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* Cloud sessions now receive server-managed settings fetched from Anthropic's servers at session start, documented in the availability table and availability notes. [[lines 54-62](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L54-L62)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#what’s-available-in-cloud-sessions)]
* Clarified that hooks in cloud sessions come from the repo and from server-managed settings (not just the repo). [[line 194](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L194)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#setup-scripts-vs-sessionstart-hooks)]

#### [Costs](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* Updated guidance for cost tracking on Bedrock/Vertex/Foundry: replaced LiteLLM-specific recommendation with general note that organizations routing through an LLM gateway can track spend there. [[line 32](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/costs.md?plain=1#L32)] [[Source](https://code.claude.com/docs/en/costs#managing-costs-for-teams)]

#### [Desktop](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Replaced the blanket statement that admin-console settings only reach CLI/IDE with a per-session-type breakdown: local sessions get both file-based and server-managed settings; cloud sessions get server-managed only; SSH sessions read managed settings from the remote host. [[lines 543-549](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/desktop.md?plain=1#L543-L549)] [[Source](https://code.claude.com/docs/en/desktop#managed-settings)]
* Added note that `managedMcpServers` must be delivered through the managed settings file or MDM in third-party deployments, since those don't receive admin-console settings. [[line 545](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/desktop.md?plain=1#L545)] [[Source](https://code.claude.com/docs/en/desktop#managed-settings)]

#### [Discover plugins](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* New "Not used recently" group appears in the Installed tab for marketplace plugins not invoked in at least two weeks over at least 10 sessions; detail view also shows a "Last used" timestamp. Requires v2.1.187. [[lines 278-280](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/discover-plugins.md?plain=1#L278-L280)] [[Source](https://code.claude.com/docs/en/discover-plugins#manage-installed-plugins)]

#### [Environment variables](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New variable: `CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT` — idle timeout in milliseconds for remote MCP tool calls (default 300000 / 5 min); set to `0` to disable. Requires v2.1.187. [[line 212](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/env-vars.md?plain=1#L212)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* Updated `CLAUDE_CODE_SKIP_FOUNDRY_AUTH` description: for gateways, use `ANTHROPIC_FOUNDRY_API_KEY` instead; without an API key, the variable leaves the Foundry client unable to send requests. [[line 251](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/env-vars.md?plain=1#L251)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* Updated `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY` to note that `availableModels` delivery for gateway configurations must use MDM or managed settings files (server-managed delivery is not available on gateway configurations). [[line 185](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/env-vars.md?plain=1#L185)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [Errors](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New error entry: `Model ... is restricted by your organization's settings` — covers both Console-disabled models and `availableModels` exclusions, with guidance on what to do. [[lines 609-622](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/errors.md?plain=1#L609-L622)] [[Source](https://code.claude.com/docs/en/errors#claude-opus-is-not-available-with-the-claude-pro-plan)]
* New auto mode error variant: when a separate API safety check blocked the classifier request because of earlier conversation content, the error now explains this and advises switching permission modes or starting a fresh conversation. [[lines 141-150](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/errors.md?plain=1#L141-L150)] [[Source](https://code.claude.com/docs/en/errors#auto-mode-cannot-determine-the-safety-of-an-action)]

#### [Fast mode](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Added exception: if a session is already running on an allowed Opus model that supports fast mode, `/fast` enables fast mode on the current model instead of refusing. [[line 88](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/fast-mode.md?plain=1#L88)] [[Source](https://code.claude.com/docs/en/fast-mode#requirements)]

#### [Fullscreen rendering](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* Click to choose an option in select menus (permission prompts, `/model`, `/config`, etc.) is now supported in fullscreen mode. Requires v2.1.187. [[line 40](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/fullscreen.md?plain=1#L40)] [[Source](https://code.claude.com/docs/en/fullscreen#use-the-mouse)]

#### [GitHub Actions](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/github-actions.md) [[Source](https://code.claude.com/docs/en/github-actions)]

* Updated `/install-github-app` description: the command installs the Claude GitHub App first, then optionally sets up GitHub Actions workflows. As of v2.1.187 you can skip the Actions setup and return to it later. [[lines 28-29](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/github-actions.md?plain=1#L28-L29)] [[Source](https://code.claude.com/docs/en/github-actions#quick-setup)]

#### [Glossary](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/glossary.md) [[Source](https://code.claude.com/docs/en/glossary)]

* Updated "Managed settings" definition to cover both server-delivered (admin console) and device-deployed (OS-level file) forms, with a note on eligibility requirements for server-managed delivery. [[lines 128-129](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/glossary.md?plain=1#L128-L129)] [[Source](https://code.claude.com/docs/en/glossary#managed-settings)]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Matchers now accept comma (`,`) as a list separator in addition to `|`, with optional surrounding whitespace. `FileChanged` and `StopFailure` events only accept `|`; all other events accept both. Requires v2.1.191. [[lines 178-180](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/hooks.md?plain=1#L178-L180)] [[Source](https://code.claude.com/docs/en/hooks#matcher-patterns)]

#### [Interactive mode](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Vim mode `/` (reverse history search) now shows a hint to press Esc then `i` then `/` to open the command menu instead (v2.1.191). [[line 136](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/interactive-mode.md?plain=1#L136)] [[Source](https://code.claude.com/docs/en/interactive-mode#navigation-normal-mode)]
* History search now loads the 100 most recent unique prompts, with duplicates collapsed to the newest occurrence. [[line 220](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/interactive-mode.md?plain=1#L220)] [[Source](https://code.claude.com/docs/en/interactive-mode#reverse-search-with-ctrl+r)]
* `/btw` overlay now supports Left/Right to step between earlier `/btw` answers from the session. Requires v2.1.187. [[line 310](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/interactive-mode.md?plain=1#L310)] [[Source](https://code.claude.com/docs/en/interactive-mode#side-questions-with-/btw)]

#### [LLM gateways](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/llm-gateway.md) [[Source](https://code.claude.com/docs/en/llm-gateway)]

* Major rewrite: the page is now a high-level overview of what gateways provide, how routing and credentials work, and the steps to roll one out. The detailed configuration content (LiteLLM setup, auth methods, provider pass-through examples) has moved to three new dedicated pages: `llm-gateway-connect.md`, `llm-gateway-protocol.md`, and `llm-gateway-rollout.md`. [[full file](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/llm-gateway.md)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Capability discovery requests (`tools/list`, `prompts/list`, `resources/list`) now retry transient errors up to three times with short backoff after a successful connection (v2.1.191). [[line 152](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/mcp.md?plain=1#L152)] [[Source](https://code.claude.com/docs/en/mcp#automatic-reconnection)]
* Remote MCP tool calls that send no response and no progress notification for 5 minutes now abort with an error; configurable with `CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT` (v2.1.187). [[line 170](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/mcp.md?plain=1#L170)] [[Source](https://code.claude.com/docs/en/mcp#push-messages-with-channels)]
* MCP OAuth (`claude mcp login`) now auto-detects when no local browser is available (SSH sessions, Linux without display server) and prints the authorization URL instead of trying to open a browser. `--no-browser` forces the URL prompt even when a browser is detected (v2.1.191). [[line 484](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/mcp.md?plain=1#L484)] [[Source](https://code.claude.com/docs/en/mcp#authenticate-from-the-command-line)]

#### [Model configuration](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* `availableModels` enforcement expanded: now also applies to skill/command model frontmatter, the advisor model, the `--advisor` flag, background agent model selection, and models restored when resuming a session. [[lines 93-98](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/model-config.md?plain=1#L93-L98)] [[Source](https://code.claude.com/docs/en/model-config#restrict-model-selection)]
* New surface coverage table showing which delivery mechanism (server-managed vs endpoint-managed) reaches CLI/IDE, Desktop, cloud sessions, Agent SDK, and Cowork. [[lines 110-122](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/model-config.md?plain=1#L110-L122)] [[Source](https://code.claude.com/docs/en/model-config#restrict-model-selection)]
* New section: Organization model restrictions — admins can disable models via the Claude Console, enforced server-side independently from `availableModels`. Requires v2.1.187. [[lines 151-156](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/model-config.md?plain=1#L151-L156)] [[Source](https://code.claude.com/docs/en/model-config#control-the-model-users-run-on)]
* New dedicated section for `enforceAvailableModels` with a code example and explanation of how Default resolves when the account-type default is excluded. [[lines 128-143](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/model-config.md?plain=1#L128-L143)] [[Source](https://code.claude.com/docs/en/model-config#surface-coverage)]
* Fable 5 content-safety fallback target is now checked against `availableModels`; when blocked, no fallback occurs and the request ends with a refusal. [[lines 248-252](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/model-config.md?plain=1#L248-L252)] [[Source](https://code.claude.com/docs/en/model-config#automatic-model-fallback)]
* Merge behavior clarified: a specific version entry in `availableModels` disables that family's wildcard (e.g. `["sonnet", "claude-sonnet-4-5"]` allows only 4.5 versions, not all Sonnet). [[line 170](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/model-config.md?plain=1#L170)] [[Source](https://code.claude.com/docs/en/model-config#control-the-model-users-run-on)]

#### [Monitoring usage](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Clarified retry exhaustion `attempt` count: it equals one more than the effective retry limit when all retries are exhausted (11 by default, never more than 16). [[line 967](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/monitoring-usage.md?plain=1#L967)] [[Source](https://code.claude.com/docs/en/monitoring-usage#detect-retry-exhaustion)]

#### [Sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* New section: `sandbox.credentials` — declare credential files (`~/.aws/credentials`, `~/.ssh`) and secret environment variables (`GITHUB_TOKEN`, `NPM_TOKEN`) to block from sandboxed Bash commands. Requires v2.1.187. [[lines 164-192](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/sandboxing.md?plain=1#L164-L192)] [[Source](https://code.claude.com/docs/en/sandboxing#protect-credentials)]
* Sandbox network permissions: "Yes" at the approval prompt now remembers the host for the rest of the session (v2.1.191). [[line 208](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/sandboxing.md?plain=1#L208)] [[Source](https://code.claude.com/docs/en/sandboxing#network-isolation)]

#### [Server-managed settings](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* Delivery now explicitly requires an organization OAuth login or directly configured API key — keys returned by `apiKeyHelper` do not trigger the server-managed settings fetch. [[line 186](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/server-managed-settings.md?plain=1#L186)] [[Source](https://code.claude.com/docs/en/server-managed-settings#platform-availability)]
* Added Claude Platform on AWS to the list of providers where server-managed settings are not available. [[line 191](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/server-managed-settings.md?plain=1#L191)] [[Source](https://code.claude.com/docs/en/server-managed-settings#platform-availability)]
* `forceRemoteSettingsRefresh` is now honored when set in any managed source (v2.1.191), including MDM — an MDM-delivered value is not ignored when server-managed settings are also present. The settings fetch also sends `Cache-Control: no-cache`. [[line 169](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/server-managed-settings.md?plain=1#L169)] [[Source](https://code.claude.com/docs/en/server-managed-settings#enforce-fail-closed-startup)]
* Clarified that the HKCU (user-writable) Windows registry fallback does not count as an admin-deployed source for `parentSettingsBehavior` purposes. [[line 187](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/server-managed-settings.md?plain=1#L187)] [[Source](https://code.claude.com/docs/en/server-managed-settings#platform-availability)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Managed settings scope description now clarifies that server-managed delivery applies to all organization members, while plist/HKLM/file delivery applies to all users on a machine, and HKCU registry applies only to the current user. [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/settings.md?plain=1#L13)] [[Source](https://code.claude.com/docs/en/settings#available-scopes)]
* New `sandbox.credentials` settings: `credentials.files` (credential files to block from sandboxed commands) and `credentials.envVars` (environment variables to unset before sandboxed commands run). Requires v2.1.187. [[lines 358-359](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/settings.md?plain=1#L358-L359)] [[Source](https://code.claude.com/docs/en/settings#sandbox-settings)]
* `sandbox.credentials` entries in managed settings that are individually invalid are stripped with a warning; a wholly invalid `credentials` value is dropped while the rest of `sandbox` still applies (v2.1.191). [[line 160](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/settings.md?plain=1#L160)] [[Source](https://code.claude.com/docs/en/settings#invalid-entries-in-managed-settings)]
* `availableModels` now also restricts [skills](skills.md). [[line 197](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/settings.md?plain=1#L197)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* `enforceAvailableModels` description updated: it constrains the Default model to the first allowlisted entry and has no effect when `availableModels` is unset or empty. [[line 224](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/settings.md?plain=1#L224)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* `apiKeyHelper` description updated to note it uses the system shell (`cmd` on Windows) not just `/bin/sh`. [[line 200](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/settings.md?plain=1#L200)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Array-merge note now lists two exceptions — `fallbackModel` and `availableModels` — separately with clear explanations. [[lines 600-604](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/settings.md?plain=1#L600-L604)] [[Source](https://code.claude.com/docs/en/settings#settings-precedence)]

#### [Skills](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Skill `model` frontmatter: a value excluded by `availableModels` is not used and the session keeps its current model. [[line 208](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/skills.md?plain=1#L208)] [[Source](https://code.claude.com/docs/en/skills#frontmatter-reference)]

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* `availableModels` allowlist now also checks the per-invocation model parameter, environment variable, and frontmatter values for subagents; excluded values fall back to the inherited model. [[line 281](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/sub-agents.md?plain=1#L281)] [[Source](https://code.claude.com/docs/en/sub-agents#choose-a-model)]
* Background subagent depth is now fixed at spawn time (v2.1.187): resuming a background subagent from a shallower context does not change its depth or allow additional nesting levels. [[line 741](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/sub-agents.md?plain=1#L741)] [[Source](https://code.claude.com/docs/en/sub-agents#spawn-nested-subagents)]

#### [Third-party integrations](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/third-party-integrations.md) [[Source](https://code.claude.com/docs/en/third-party-integrations)]

* Foundry LLM gateway example updated: replaced `CLAUDE_CODE_SKIP_FOUNDRY_AUTH=1` with `ANTHROPIC_FOUNDRY_API_KEY=your-gateway-key` as the correct way to authenticate a gateway. [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/third-party-integrations.md?plain=1#L95)] [[Source](https://code.claude.com/docs/en/third-party-integrations#microsoft-foundry)]
* Vertex AI LLM gateway example now includes `ANTHROPIC_VERTEX_PROJECT_ID` and `CLOUD_ML_REGION` in the configuration. [[lines 127-128](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/claude-code/third-party-integrations.md?plain=1#L127-L128)] [[Source](https://code.claude.com/docs/en/third-party-integrations#google-vertex-ai)]

-----

## API changes

### Changed documents

#### [Adaptive thinking](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* Minor: updated obfuscated email link for contacting Anthropic sales about full thinking output.

#### [Extended thinking](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Minor: updated obfuscated email link for contacting Anthropic sales about full thinking output.

#### [Files](https://github.com/gpambrozio/ClaudeDocs/blob/20eab6114bea019654f3948b42c556470cfd43a2/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Minor: updated obfuscated contact link for requesting higher rate limits during the beta period.
