# [Claude docs changes for Oct, 1st 2026](https://github.com/gpambrozio/ClaudeDocs/tree/381c857d9d1ab747ba2e6c7aee40585a6cd072ec) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/381c857d9d1ab747ba2e6c7aee40585a6cd072ec)]

## Executive Summary
- New `allowedProviders` managed setting lets admins restrict which API providers (Anthropic, Bedrock, Vertex, Foundry, gateways...) a machine may use
- New Plugins API (beta) for inventorying, publishing, versioning, sharing and validating plugins and marketplaces in a Claude Enterprise organization
- Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`) is deprecated, with retirement on November 30, 2026 (replacement: `claude-sonnet-5-5`)
- Claude Code 2.1.286 improves permission prompts and fullscreen lists, retries on the previous model when a model is refused, and adds VS Code bookmarks
- Claude apps gateway can now call Bedrock in another AWS account via `assume_role`; Managed Agents examples now use limited networking

## New Claude Code versions

### [2.1.286](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/versions/2.1.286.md)

#### New features

* Permission prompts show a count such as "2 of 5" when several requests stack up
* Mouse support for the "N more" rows of lists in fullscreen mode
* [VSCode] Bookmarks: save Claude's responses and keep them in a Bookmarks side panel
* [VSCode] Question cards now show option previews, and answered questions appear in the conversation
* [VSCode] Rows under a message open the terminal output, browser tab and selected code sent with it
* [Claude Tag] Add channel button on the spend limits page to set a limit on any channel

#### Existing feature improvements

* Commit guidance: if a project or user skill named `verify` exists, Claude runs it right before committing (except docs-only and tests-only commits)
* Bash, PowerShell, Monitor, fetch, skill, file read and other permission prompts now match the look of file edit prompts
* Ctrl+G external editor opens on the cursor's line; slash command suggestions are more responsive and match by word prefix
* `/hooks` opens on one list of hooks grouped by event; theme and output style pickers redesigned (number keys no longer pick)
* List screens align details in one column, and scrollbars have clickable arrows
* Send now (ctrl+enter) moves the running command of a subagent or skill to the background
* Plugin installs refuse npm sources that are git repositories or folders, and install dependencies only from registry packages
* Failed API requests: one retry limit now covers a whole model call (at most 14 requests with defaults)
* `--bare` connects only MCP servers named on the command line, sends no system reminders and starts no background tasks
* The `claude-api` skill's Managed Agents examples now use limited networking
* [VSCode] Stop and Escape end only the current turn; background agents keep running

#### Major bug fixes

* When the API refuses the model a default or alias resolves to, Claude Code retries once on the previous model of the same tier; `--fallback-model` retries run at standard speed
* Fixed `claude --resume`/`--continue` losing turns after parallel tool calls in a crashed session
* Fixed API 400 errors after a tool or hook returned a non-text value
* Fixed multiple processes opening login browsers when gcpAuthRefresh/awsAuthRefresh credentials expire
* Fixed Remote Control sessions staying connected after org policy turns it off
* Fixed secret redaction gaps in logs, transcripts and MCP errors (Bearer/Basic tokens, URL passwords, zero-width characters)
* Fixed `/compact`, `/clear` and `/rewind` silently acting on the main conversation while viewing a background agent
* Fixed the Claude apps gateway spend meter mispricing 1-hour cache writes and undercounting streamed server-tool turns
* Fixed `claude auth status` reporting a Console API key sign-in as `claude.ai`
* Fixed several subagent issues (duplicate messages, missing task tools, double CLAUDE.md loading, Workflow subagents restarting)

-----

## Claude Code changes

### New Documents

None.

### Changed documents

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* Added `ClaudeSDKClient.get_context_usage()`, returning the same breakdown `/context` shows, plus the `ContextUsageResponse` type. [[lines 437-461](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/agent-sdk/python.md?plain=1#L437-L461), [lines 1409-1439](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/agent-sdk/python.md?plain=1#L1409-L1439)]
* `query()` accepts an async iterable of user message dicts, including content blocks such as images. [[line 526](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/agent-sdk/python.md?plain=1#L526)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#example-streaming-input-with-claudesdkclient)]
* Tool output schemas (Edit, Read, Bash timeout semantics) documented in detail. [[lines 2665-2745](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/agent-sdk/python.md?plain=1#L2665-L2745)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#edit)]

#### [authentication](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/authentication.md) [[Source](https://code.claude.com/docs/en/authentication)]

* New section on restricting which API providers a machine may use with `allowedProviders`, paired with `forceLoginMethod`/`forceLoginOrgUUID`. [[lines 171-188](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/authentication.md?plain=1#L171-L188)] [[Source](https://code.claude.com/docs/en/authentication#restrict-which-api-providers-a-machine-may-use)]

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* New "Bedrock in another AWS account" section: `assume_role` upstream setting (`role_arn`, `external_id`, `session_name`), trust policy example, requires gateway v2.1.281+. [[lines 308-388](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L308-L388)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#apply-an-amazon-bedrock-guardrail)]
* Clarified which status codes trigger upstream failover and that `bedrock:ApplyGuardrail` must be granted. [[line 157](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L157), [line 300](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L300)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* `claude mcp add` success output and `claude mcp list` health statuses explained. [[lines 206-238](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/mcp.md?plain=1#L206-L238)] [[Source](https://code.claude.com/docs/en/mcp#from-an-mcpservers-json-block)]
* Reserved built-in server names; OAuth credentials sent only to HTTPS or localhost token endpoints. [[line 280](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/mcp.md?plain=1#L280), [line 326](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/mcp.md?plain=1#L326)]
* Transient first-connection failures retry up to three times; long MCP calls move to a background task visible in `/tasks`. [[lines 360-411](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/mcp.md?plain=1#L360-L411)] [[Source](https://code.claude.com/docs/en/mcp#failed-first-connections)]
* Connector tools set to `blocked` are filtered before Claude sees them. [[line 1144](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/mcp.md?plain=1#L1144)] [[Source](https://code.claude.com/docs/en/mcp#organization-controls-on-connector-tools)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Fallback model behavior when the primary is overloaded or unavailable. [[line 470](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/model-config.md?plain=1#L470)] [[Source](https://code.claude.com/docs/en/model-config#fallback-model-chains)]
* Context window behind an LLM gateway: recognized models, including Sonnet 5.5 and Sonnet 5, get the same window as on the Anthropic API; native 1M models auto-compact at about 967K tokens. [[lines 698-761](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/model-config.md?plain=1#L698-L761)] [[Source](https://code.claude.com/docs/en/model-config#extended-context)]

#### [sessions](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/sessions.md) [[Source](https://code.claude.com/docs/en/sessions)]

* Resuming a still-running background session now attaches to it (`claude --resume` runs `claude attach`; `/resume` moves the current conversation to the background), with the cases where this is skipped. [[lines 26-43](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/sessions.md?plain=1#L26-L43)] [[Source](https://code.claude.com/docs/en/sessions#resume-a-session)]
* Resumed-session permission mode depends on how you resume. [[line 62](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/sessions.md?plain=1#L62)] [[Source](https://code.claude.com/docs/en/sessions#permission-mode-on-resume)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* New managed `allowedProviders` setting (`anthropic`, `bedrock`, `vertex`, `foundry`, `anthropicAws`, `mantle`, `customEndpoint`, `gateway`) and the endpoint pins required in managed `env`. [[lines 5354-5394](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/settings-reference.md?plain=1#L5354-L5394)] [[Source](https://code.claude.com/docs/en/settings-reference#allowedproviders)]
* Custom spinner tips can be added or replace built-ins (v2.1.247+). [[lines 3360-3368](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/settings-reference.md?plain=1#L3360-L3368)] [[Source](https://code.claude.com/docs/en/settings-reference#spinnertipsoverride)]
* Strict plugin marketplace setting also rejects `--plugin-dir`, `--plugin-url`, `--agents`, `--mcp-config`; notes on desktop-managed plugins. [[lines 5790-5810](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/settings-reference.md?plain=1#L5790-L5810)] [[Source](https://code.claude.com/docs/en/settings-reference#disablesideloadflags)]
* Artifact tool disable behavior and merge rules for restriction allowlists clarified. [[line 5150](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/settings-reference.md?plain=1#L5150), [line 5861](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/settings-reference.md?plain=1#L5861)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Skill shell commands run under the Bash tool's 2-minute default timeout. [[line 679](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/skills.md?plain=1#L679)] [[Source](https://code.claude.com/docs/en/skills#how-injected-commands-run)]
* Table showing what `Skill(...)` deny rules also block (aliases, nested skills, claude.ai-synced skills). [[lines 787-801](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/skills.md?plain=1#L787-L801)] [[Source](https://code.claude.com/docs/en/skills#restrict-claudes-skill-access)]

#### Other updated documents

Smaller updates across [errors](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/errors.md), [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/tools-reference.md), [slash-commands](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/slash-commands.md), [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/vs-code.md), [plugins/troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/plugins/troubleshooting.md), [claude-apps-gateway-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/claude-apps-gateway-on-aws.md) and [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/claude-code/desktop-changelog.md) reflect the 2.1.286 changes.

-----

## API changes

### New Documents

#### [manage-claude/plugins-api](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/manage-claude/plugins-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/plugins-api)]

New guide to the Plugins API (beta header `ce-plugins-2026-09-01`) for Claude Enterprise organizations: inventory plugins, upload plugins and versions from your own pipelines, choose the version members are served, control who can use each plugin, download plugin files for review, and validate a Git marketplace before connecting it. Includes error responses and a pointer to the Analytics APIs for usage reporting.

#### [api/beta/organization/plugins and plugin_marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/api/beta/organization/plugins.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/plugins)]

New API reference pages for plugin CRUD, versions (create, list, retrieve, download), installation settings, shares, and marketplaces (list, retrieve, update, validate archive/repository).

#### [api/organization](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/api/organization.md) [[Source](https://platform.claude.com/docs/en/api/organization)]

New non-beta Admin API reference tree covering API keys, compliance settings, external keys, federation issuers and rules, invites, rate limits, service accounts, users, and workspaces (including members, rate limits and service accounts).

### Changed documents

#### [about-claude/model-deprecations](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/about-claude/model-deprecations.md) [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]

* Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`) marked Deprecated on September 30, 2026, retiring November 30, 2026; recommended replacement `claude-sonnet-5-5`. [[lines 69-98](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/about-claude/model-deprecations.md?plain=1#L69-L98)] [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations#model-status)]

#### [manage-claude/cmek](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/manage-claude/cmek.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

* Feature support table replaced with inline coverage lists (Batch, Skills, and tool data at rest); Managed Agents and Claude Science marked beta. [[lines 61-73](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/manage-claude/cmek.md?plain=1#L61-L73)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek#encrypted-with-cmek-key)]
* Structured outputs unavailable for Fable/Mythos models in CMEK orgs; artifacts can only be shared within the org; Design/Slides/Docs and routines unavailable. [[lines 85-97](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/manage-claude/cmek.md?plain=1#L85-L97)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek#disabled-or-modified)]

#### [manage-claude/compliance-org-data](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/manage-claude/compliance-org-data.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-org-data)]

* New section: Compliance Access Keys with `read:compliance_org_data` can call the Plugins API's read endpoints; writes require an Admin API key with `write:plugins`. [[lines 270-282](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/manage-claude/compliance-org-data.md?plain=1#L270-L282)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-org-data#read-plugins-and-plugin-marketplaces)]

#### [managed-agents/migration](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/managed-agents/migration.md) [[Source](https://platform.claude.com/docs/en/managed-agents/migration)]

* Environment examples in all SDKs switched from unrestricted to `limited` networking with `allow_package_managers`. [[line 709](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/managed-agents/migration.md?plain=1#L709)] [[Source](https://platform.claude.com/docs/en/managed-agents/migration#code-comparison)]

#### [managed-agents/quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/managed-agents/quickstart.md) [[Source](https://platform.claude.com/docs/en/managed-agents/quickstart)]

* Quickstart environment now uses `limited` networking with package managers allowed, in every language example. [[line 351](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/managed-agents/quickstart.md?plain=1#L351)] [[Source](https://platform.claude.com/docs/en/managed-agents/quickstart#create-your-first-session)]

#### [api/beta and api/cli/beta](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* Large expansions of the beta API and CLI reference, including organization, sessions, events and threads types; cost/usage analytics pages updated.

#### Other updated documents

Smaller updates to [claude-in-microsoft-foundry](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/build-with-claude/claude-in-microsoft-foundry.md), [claude-on-vertex-ai](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/build-with-claude/claude-on-vertex-ai.md), [claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/build-with-claude/claude-platform-on-aws.md), [api-and-data-retention](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/manage-claude/api-and-data-retention.md), [wif-reference](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/manage-claude/wif-reference.md), [sonnet-4-5/overview](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/models/sonnet-4-5/overview.md) and [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/381c857d9d1ab747ba2e6c7aee40585a6cd072ec/docs-md/api/release-notes/overview.md).
