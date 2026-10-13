# [Claude docs changes for October 13th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/9ff2088a6786598a14eaf59f5ec7b42f43262c0b) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/9ff2088a6786598a14eaf59f5ec7b42f43262c0b)]

## Executive Summary
- The Browser/Computer use SDK guide was restructured around ready-made provider drivers, so an agent now takes only a few lines of code. Writing your own driver is documented as an advanced case.
- Managed Agents docs gained PHP examples for event deltas and event listing, plus a new `ant apply` example for clearing agent fields. The self-hosted sandbox quickstart now checks `workers_polling` in every SDK language.
- Data retention docs now point to the new Console **Data retention** page for enabling 30-day standard retention, and for encryption keys.
- Claude Code docs reword model-version references, for example "Opus 4.7, Sonnet 4.6, Haiku 4.5, and earlier models" for task-tool availability. The adaptive-reasoning docs now name Opus 4.6, Sonnet 4.6, Haiku 5.5 and Fable 5.
- Many SDK reference pages and code samples were reformatted, with no behavior changes: PHP `\` namespace prefixes, braces on JS `if` statements, and table line breaks.

## New Claude Code versions

No new Claude Code versions today.

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* Task-tool availability is reworded: the tools are on by default for Opus 4.7, Sonnet 4.6, Haiku 4.5 and earlier models. [[line 3074](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/agent-sdk/python.md?plain=1#L3074)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#todowrite)]

#### [agent-sdk/todo-tracking](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/agent-sdk/todo-tracking.md) [[Source](https://code.claude.com/docs/en/agent-sdk/todo-tracking)]

* Same task-tool availability rewording. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/agent-sdk/todo-tracking.md?plain=1#L11)] [[Source](https://code.claude.com/docs/en/agent-sdk/todo-tracking#model-availability)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Same task-tool availability rewording, in two places. [[line 3295](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L3295)] [[line 4245](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L4245)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#todowrite)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Model naming was updated in the `CLAUDE_CODE_DISABLE_LEGACY_MODEL_REMAP` and `VERTEX_REGION_CLAUDE_*` descriptions, for example "Opus 4 and Opus 4.1". [[line 253](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/env-vars.md?plain=1#L253)] [[lines 506-508](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/env-vars.md?plain=1#L506-L508)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [feature-availability](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/feature-availability.md) [[Source](https://code.claude.com/docs/en/feature-availability)]

* On Google Cloud's Agent Platform, web search is now described as available for Opus 4, Sonnet 4, Haiku 4.5 and later. Tool search is not supported on models earlier than Opus 4.5, Sonnet 4.5 and Haiku 4.5. [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/feature-availability.md?plain=1#L33)] [[line 208](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/feature-availability.md?plain=1#L208)] [[line 254](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/feature-availability.md?plain=1#L254)] [[Source](https://code.claude.com/docs/en/feature-availability#features-available-on-every-provider)]

#### [google-vertex-ai](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/google-vertex-ai.md) [[Source](https://code.claude.com/docs/en/google-vertex-ai)]

* The "Claude 3.x" reference was removed from the note on MCP tool definitions loading upfront on earlier models. [[line 191](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/google-vertex-ai.md?plain=1#L191)] [[Source](https://code.claude.com/docs/en/google-vertex-ai#4-configure-claude-code)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* The task list's default model availability is reworded to "Opus 4.7, Sonnet 4.6, Haiku 4.5, and earlier models". [[line 631](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/interactive-mode.md?plain=1#L631)] [[Source](https://code.claude.com/docs/en/interactive-mode#task-list)]

#### [llm-gateway-connect](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/llm-gateway-connect.md) [[Source](https://code.claude.com/docs/en/llm-gateway-connect)]

* The adaptive-reasoning `400` troubleshooting row now says Claude Code requests adaptive reasoning for Opus 4.6, Sonnet 4.6, Haiku 5.5, Fable 5 and later. [[line 509](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/llm-gateway-connect.md?plain=1#L509)] [[Source](https://code.claude.com/docs/en/llm-gateway-connect#troubleshoot-gateway-errors)]

#### [llm-gateway-protocol](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/llm-gateway-protocol.md) [[Source](https://code.claude.com/docs/en/llm-gateway-protocol)]

* The same model list applies to when Claude Code sends `thinking: {"type": "adaptive"}`. [[line 210](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/llm-gateway-protocol.md?plain=1#L210)] [[Source](https://code.claude.com/docs/en/llm-gateway-protocol#feature-pass-through)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Models without tool search on Google Cloud's Agent Platform are now named as earlier than Opus 4.5, Sonnet 4.5 and Haiku 4.5. [[line 292](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/mcp.md?plain=1#L292)] [[Source](https://code.claude.com/docs/en/mcp#tool-availability)]

#### [prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/prompt-caching.md) [[Source](https://code.claude.com/docs/en/prompt-caching)]

* Same model-naming update for tool search availability. [[line 108](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/prompt-caching.md?plain=1#L108)] [[Source](https://code.claude.com/docs/en/prompt-caching#connecting-or-removing-an-mcp-server)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* Task-tool availability and WebSearch support on Google Cloud's Agent Platform use the new model naming. [[line 577](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/tools-reference.md?plain=1#L577)] [[line 646](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/claude-code/tools-reference.md?plain=1#L646)] [[Source](https://code.claude.com/docs/en/tools-reference#task-tool-availability)]

-----

## API changes

### Changed documents

#### [agents-and-tools/tool-use/browser-use-sdk](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/agents-and-tools/tool-use/browser-use-sdk.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-sdk)]

* The intro was rewritten around building agents that work in a browser or on a desktop. The SDK runs your configured checks (URL policy, approval callback) and sends passing calls to your driver. [[lines 9-15](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/agents-and-tools/tool-use/browser-use-sdk.md?plain=1#L9-L15)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-sdk#a-mybrowser-that-also-implements-read_console)]
* A new "Use a driver from a provider" section replaces the long hand-written driver quick start. With a provider driver, an agent takes a few lines of code. [[line 21](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/agents-and-tools/tool-use/browser-use-sdk.md?plain=1#L21)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-sdk#use-a-driver-from-a-provider)]
* Writing your own driver is now presented as an advanced case under "Implement a driver". [[line 17](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/agents-and-tools/tool-use/browser-use-sdk.md?plain=1#L17)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-sdk#a-mybrowser-that-also-implements-read_console)]

#### [agents-and-tools/tool-use/tool-reference](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/agents-and-tools/tool-use/tool-reference.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)]

* The tools tables were reformatted, with no change in content. [[lines 15-27](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/agents-and-tools/tool-use/tool-reference.md?plain=1#L15-L27)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference#anthropic-provided-tools)]

#### [build-with-claude/claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/build-with-claude/claude-platform-on-aws.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)]

* The Console "Encryption keys" entry is now described as a section of the Data retention page instead of **Settings → Encryption keys**. [[line 777](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/build-with-claude/claude-platform-on-aws.md?plain=1#L777)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#available-pages)]

#### [manage-claude/api-and-data-retention](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/manage-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

* The steps for enabling 30-day retention changed. Go to the Console **Data retention** page, choose the workspace, select **Standard data retention**, click **Save**, then accept the terms in the confirmation dialog. [[lines 138-144](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/manage-claude/api-and-data-retention.md?plain=1#L138-L144)] [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#enable-30-day-retention-for-a-workspace)]
* The feature eligibility table's endpoint column was reformatted with `<br />` line breaks. [[lines 160-196](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/manage-claude/api-and-data-retention.md?plain=1#L160-L196)] [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#feature-eligibility)]

#### [manage-claude/cmek-aws-kms](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/manage-claude/cmek-aws-kms.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms)]

* Console navigation for encryption keys was updated, along with the other CMEK guides (`cmek-azure-key-vault`, `cmek-google-cloud-kms`) and `user-management`, to match the new Data retention page.

#### [managed-agents/agent-setup](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/managed-agents/agent-setup.md) [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]

* A new example in all SDKs and the CLI updates an agent's description unconditionally. [[line 465](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/managed-agents/agent-setup.md?plain=1#L465)] [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup#update-an-agent)]
* A new `ant apply code-reviewer.md` example shows clearing fields. Fields removed from the file are sent as `null`. Deleting a setting inside `multiagent` keeps its stored value, so the file sets `workflows: null`. [[line 572](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/managed-agents/agent-setup.md?plain=1#L572)] [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup#update-semantics)]

#### [managed-agents/event-deltas](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/managed-agents/event-deltas.md) [[Source](https://platform.claude.com/docs/en/managed-agents/event-deltas)]

* Full PHP examples replace the "see the SDK" placeholders. They use `eventDeltas` with `EventAccumulator` for session streams and child-thread streams. [[line 495](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/managed-agents/event-deltas.md?plain=1#L495)] [[line 904](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/managed-agents/event-deltas.md?plain=1#L904)] [[Source](https://platform.claude.com/docs/en/managed-agents/event-deltas#sdk-accumulator-helpers)]

#### [managed-agents/events-and-streaming](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/managed-agents/events-and-streaming.md) [[Source](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)]

* The PHP example for listing events filtered by type (`agent.tool_use`, `agent.tool_result`) replaces a placeholder comment. [[line 1774](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/managed-agents/events-and-streaming.md?plain=1#L1774)] [[Source](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#list-past-events)]
* PHP samples now use `use` imports, and JS samples use braces on `if` statements. These are style changes only.

#### [managed-agents/self-hosted-sandboxes](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/managed-agents/self-hosted-sandboxes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

* The quickstart can now be run with the `ant` CLI or an SDK. It explains the per-language name of the environment-ID variable. [[lines 46-46](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L46)] [[line 218](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L218)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#prerequisites)]
* The `workers_polling` check now has cURL, CLI and SDK examples in all languages. [[lines 220-297](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L220-L297)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#run-your-first-session)]
* The session-creation step gained multi-language examples, and extra content was added later in the page. [[line 299](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L299)] [[line 350](https://github.com/gpambrozio/ClaudeDocs/blob/9ff2088a6786598a14eaf59f5ec7b42f43262c0b/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L350)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#run-your-first-session)]

#### [API reference pages (`api/api/*`, all languages)](https://github.com/gpambrozio/ClaudeDocs/commit/9ff2088a6786598a14eaf59f5ec7b42f43262c0b)

* About 400 generated SDK reference pages were regenerated, including beta agents, sessions, models and messages for CLI, C#, Go, Java, PHP, Python, Ruby and TypeScript. They contain mostly formatting and type-listing updates, with no significant new content.
* Smaller tweaks were made to other guides (prompt caching, context editing, vision coordinates, the PHP SDK page and the advisor tool model table). These were wording or formatting only.
