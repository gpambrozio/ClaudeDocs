# [Claude docs changes for March 12th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/6ec3b00b7dc11e6a450733e438dc209e449cfefc) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/6ec3b00b7dc11e6a450733e438dc209e449cfefc)]

## Executive Summary
- New `modelOverrides` setting (2.1.73) lets enterprise admins map individual model versions to provider-specific IDs such as Bedrock inference profile ARNs, enabling per-version routing and governance
- New `autoMemoryDirectory` setting (2.1.74) allows configuring a custom directory for auto-memory storage; `/context` command gains actionable optimization tips
- API Tier 4 monthly spend threshold raised dramatically from $5,000 to $200,000
- `/output-style` command deprecated in favor of `/config`; output style is now locked at session start to enable prompt caching
- 1-hour prompt caching now supported on Google Cloud's Vertex AI (previously only Claude API and Microsoft Foundry)

## New Claude Code versions

### [2.1.73](https://github.com/gpambrozio/ClaudeDocs/blob/6ec3b00b7dc11e6a450733e438dc209e449cfefc/versions/2.1.73.md)

#### New features

* Added `modelOverrides` setting to map model picker entries to custom provider model IDs (e.g., Bedrock inference profile ARNs), enabling per-version routing for enterprise environments
* Added actionable guidance when OAuth login or connectivity checks fail due to SSL certificate errors (corporate proxies, `NODE_EXTRA_CA_CERTS`)

#### Existing feature improvements

* Changed default Opus model on Bedrock, Vertex, and Microsoft Foundry to Opus 4.6 (was Opus 4.1)
* Deprecated `/output-style` command — use `/config` instead; output style is now fixed at session start for better prompt caching
* Improved Up arrow after interrupting Claude — now restores the interrupted prompt and rewinds the conversation in one step
* Improved `/effort` to work while Claude is responding, matching `/model` behavior
* Improved IDE detection speed at startup and clipboard image pasting performance on macOS
* Improved voice mode to automatically retry transient connection failures during rapid push-to-talk re-press

#### Major bug fixes

* Fixed freezes and 100% CPU loops triggered by permission prompts for complex bash commands
* Fixed a deadlock that could freeze Claude Code when many skill files changed at once (e.g., during `git pull` in a repo with a large `.claude/skills/` directory)
* Fixed Bash tool output being lost when running multiple Claude Code sessions in the same project directory
* Fixed subagents with `model: opus`/`sonnet`/`haiku` being silently downgraded to older model versions on Bedrock, Vertex, and Microsoft Foundry
* Fixed SessionStart hooks firing twice when resuming a session via `--resume` or `--continue`
* Fixed JSON-output hooks injecting no-op system-reminder messages into the model's context on every turn
* Fixed Linux sandbox failing to start with "ripgrep (rg) not found" on native builds
* Fixed Linux native modules not loading on Amazon Linux 2 and other glibc 2.26 systems
* VSCode: Fixed HTTP 400 errors for users behind proxies or on Bedrock/Vertex with Claude 4.5 models

### [2.1.74](https://github.com/gpambrozio/ClaudeDocs/blob/6ec3b00b7dc11e6a450733e438dc209e449cfefc/versions/2.1.74.md)

#### New features

* Added actionable suggestions to `/context` command — identifies context-heavy tools, memory bloat, and capacity warnings with specific optimization tips
* Added `autoMemoryDirectory` setting to configure a custom directory for auto-memory storage

#### Existing feature improvements

* Changed `--plugin-dir` so local dev copies now override installed marketplace plugins with the same name (unless force-enabled by managed settings)

#### Major bug fixes

* Fixed memory leak where streaming API response buffers were not released when the generator was terminated early, causing unbounded RSS growth on the Node.js/npm code path
* Fixed managed policy `ask` rules being bypassed by user `allow` rules or skill `allowed-tools`
* Fixed full model IDs (e.g., `claude-opus-4-5`) being silently ignored in agent frontmatter `model:` field and `--agents` JSON config
* Fixed MCP OAuth authentication hanging when the callback port is already in use
* Fixed MCP OAuth refresh never prompting for re-auth after the refresh token expires for OAuth servers that return errors with HTTP 200 (e.g., Slack)
* Fixed `SessionEnd` hooks being killed after 1.5s on exit regardless of `hook.timeout` — now configurable via `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS`
* Fixed Hebrew, Arabic, and other RTL text not rendering correctly in Windows Terminal, conhost, and VS Code integrated terminal
* Fixed LSP servers not working on Windows due to malformed file URIs
* VSCode: Fixed delete button not working for Untitled sessions

-----

## Claude Code changes

### Changed documents

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/6ec3b00b7dc11e6a450733e438dc209e449cfefc/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* New section added explaining how to use `modelOverrides` to map multiple model versions within the same family to distinct Bedrock inference profile ARNs. [[lines 209-230](https://github.com/gpambrozio/ClaudeDocs/blob/6ec3b00b7dc11e6a450733e438dc209e449cfefc/docs-md/claude-code/amazon-bedrock.md?plain=1#L209-L230)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#map-each-model-version-to-an-inference-profile)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/6ec3b00b7dc11e6a450733e438dc209e449cfefc/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Updated `/config` command description to clarify it adjusts theme, model, output style, and other preferences. [[line 85](https://github.com/gpambrozio/ClaudeDocs/blob/6ec3b00b7dc11e6a450733e438dc209e449cfefc/docs-md/claude-code/interactive-mode.md?plain=1#L85)] [[Source](https://code.claude.com/docs/en/interactive-mode#built-in-commands)]
* Removed `/output-style` from the slash commands table (deprecated in favor of `/config`).

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/6ec3b00b7dc11e6a450733e438dc209e449cfefc/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* New section "Override model IDs per version" documenting the `modelOverrides` setting, which maps individual Anthropic model IDs to provider-specific strings for per-version routing on Bedrock, Vertex, and Foundry. [[lines 227-252](https://github.com/gpambrozio/ClaudeDocs/blob/6ec3b00b7dc11e6a450733e438dc209e449cfefc/docs-md/claude-code/model-config.md?plain=1#L227-L252)] [[Source](https://code.claude.com/docs/en/model-config#override-model-ids-per-version)]

#### [output-styles](https://github.com/gpambrozio/ClaudeDocs/blob/6ec3b00b7dc11e6a450733e438dc209e449cfefc/docs-md/claude-code/output-styles.md) [[Source](https://code.claude.com/docs/en/output-styles)]

* Instructions for changing output style updated: now uses `/config` menu instead of the deprecated `/output-style` command. [[lines 35-58](https://github.com/gpambrozio/ClaudeDocs/blob/6ec3b00b7dc11e6a450733e438dc209e449cfefc/docs-md/claude-code/output-styles.md?plain=1#L35-L58)] [[Source](https://code.claude.com/docs/en/output-styles#change-your-output-style)]
* Added note that output style is fixed at session start so the system prompt stays stable, enabling prompt caching to reduce latency and cost. [[lines 55-58](https://github.com/gpambrozio/ClaudeDocs/blob/6ec3b00b7dc11e6a450733e438dc209e449cfefc/docs-md/claude-code/output-styles.md?plain=1#L55-L58)] [[Source](https://code.claude.com/docs/en/output-styles#change-your-output-style)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/6ec3b00b7dc11e6a450733e438dc209e449cfefc/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `modelOverrides` to the settings reference table, describing how to map Anthropic model IDs to provider-specific model IDs such as Bedrock inference profile ARNs. [[line 158](https://github.com/gpambrozio/ClaudeDocs/blob/6ec3b00b7dc11e6a450733e438dc209e449cfefc/docs-md/claude-code/settings.md?plain=1#L158)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

-----

## API changes

### Changed documents

#### [build-with-claude/overview](https://github.com/gpambrozio/ClaudeDocs/blob/6ec3b00b7dc11e6a450733e438dc209e449cfefc/docs-md/api/build-with-claude/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

* Google Cloud's Vertex AI added to the list of platforms supporting 1-hour prompt caching (previously only Claude API and Microsoft Foundry). [[line 75](https://github.com/gpambrozio/ClaudeDocs/blob/6ec3b00b7dc11e6a450733e438dc209e449cfefc/docs-md/api/build-with-claude/overview.md?plain=1#L75)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

#### [api/rate-limits](https://github.com/gpambrozio/ClaudeDocs/blob/6ec3b00b7dc11e6a450733e438dc209e449cfefc/docs-md/api/api/rate-limits.md) [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

* Tier 4 monthly spend threshold increased from $5,000 to $200,000. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/6ec3b00b7dc11e6a450733e438dc209e449cfefc/docs-md/api/api/rate-limits.md?plain=1#L38)] [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

#### [test-and-evaluate/strengthen-guardrails/handle-streaming-refusals](https://github.com/gpambrozio/ClaudeDocs/blob/6ec3b00b7dc11e6a450733e438dc209e449cfefc/docs-md/api/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)]

* Removed the special test string (`ANTHROPIC_MAGIC_STRING_TRIGGER_REFUSAL_...`) that could be used to trigger refusals in testing.
