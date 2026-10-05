# [Claude docs changes for October 5th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/ab4d12a3887d27b92cacb6a589a5f37abbbde203) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/ab4d12a3887d27b92cacb6a589a5f37abbbde203)]

## Executive Summary
- New guide for setting up Claude Code (local mode) in HIPAA-ready Enterprise organizations. The BAA can now cover the CLI and the Desktop Code tab without ZDR, and several features are turned off or off by default under the configuration.
- The Models API now returns a `line` field (`haiku`, `sonnet`, `opus`, `fable`, `mythos`) that groups models without parsing IDs. It is documented across all SDKs and the CLI.
- Claude Code errors docs cover a new `reasoning_extraction` safeguard refusal, and MCP output docs add a 50,000-character limit for text results.
- Compliance API adds a `claude_skill_downloaded` activity type. The Voyage AI embeddings guide now uses MongoDB Atlas keys and lists `rerank-3` and `voyage-code-4`.
- Admin UI references changed from "Admin settings" to "Organization settings", and GitHub setup moved to a new Git providers page.

## New Claude Code versions

No new Claude Code versions in this update.

-----

## Claude Code changes

### New Documents

#### [hipaa-setup](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/hipaa-setup.md) [[Source](https://code.claude.com/docs/en/hipaa-setup)]

Guide for IT and security administrators preparing computers to run Claude Code (local mode) under the HIPAA configuration on Claude Enterprise plans with a BAA. It covers:

* Which connections are eligible: direct Claude API with an Enterprise account. Bedrock, Google Cloud, Foundry, Claude Platform on AWS and Claude apps gateways are not.
* Minimum Claude Code and Desktop versions, required network access, and deploying managed settings before the configuration is applied.
* How to confirm the configuration on a computer, and what developers see in Claude Code, including Anthropic credentials in commands, hooks and MCP servers.
* Managing local session data for Claude Code, the Code tab and Cowork: deleting data right away and offboarding a developer.

### Changed documents

#### [admin-setup](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

* The GitHub admin page is now **Organization settings > Git providers**. A new **Add organization** button is available once an account is connected. [[lines 116-128](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/admin-setup.md?plain=1#L116-L128)] [[Source](https://code.claude.com/docs/en/admin-setup#decide-what-to-enforce)]
* Added a HIPAA configuration row linking to the new setup guide. [[line 158](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/admin-setup.md?plain=1#L158)] [[Source](https://code.claude.com/docs/en/admin-setup#review-data-handling)]

#### [agent-sdk/mcp](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/agent-sdk/mcp.md) [[Source](https://code.claude.com/docs/en/agent-sdk/mcp)]

* The output limit applies to successful results. Unless a tool declares `anthropic/maxResultSizeChars`, text results over 50,000 characters are saved to a file regardless of the token limit. [[lines 844-846](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/agent-sdk/mcp.md?plain=1#L844-L846)] [[Source](https://code.claude.com/docs/en/agent-sdk/mcp#tool-output-exceeds-maximum-allowed-tokens)]

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* Added a `fallback_credit` field to the agent tool's usage output. [[line 2478](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/agent-sdk/python.md?plain=1#L2478)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#agent)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Added `fallback_credit` to `AgentOutput` and `Usage`, typed `BetaFallbackCreditUsage | null`. It requires `@anthropic-ai/sdk` 0.115.0 or later. `NonNullableUsage` keeps it nullable. [[lines 4857-4900](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L4857-L4900)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#nonnullableusage)]

#### [chrome](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/chrome.md) [[Source](https://code.claude.com/docs/en/chrome)]

* In HIPAA-enabled Enterprise organizations, Claude in Chrome is off by default and an Owner can turn it on. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/chrome.md?plain=1#L38)] [[Source](https://code.claude.com/docs/en/chrome#prerequisites)]

#### [claude-directory](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* Desktop and Cowork transcripts are deleted after `cleanupPeriodDays` when managed settings set it or when the HIPAA configuration applies. [[lines 1340-1345](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/claude-directory.md?plain=1#L1340-L1345)] [[Source](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically)]
* Under the HIPAA configuration, each cleanup sweep removes old `history.jsonl` entries. [[line 1378](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/claude-directory.md?plain=1#L1378)] [[Source](https://code.claude.com/docs/en/claude-directory#kept-until-you-delete-them)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Transcript view modes are now switched from the session menu caret beside the title. [[line 199](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/desktop.md?plain=1#L199)] [[Source](https://code.claude.com/docs/en/desktop#switch-view-modes)]
* Admin toggles were renamed **Desktop** and **Cloud sessions**. Under HIPAA the Desktop toggle is off by default, and applying the configuration turns it off. [[lines 708-713](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/desktop.md?plain=1#L708-L713)] [[Source](https://code.claude.com/docs/en/desktop#admin-console-controls)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New section on refusals where safeguards flag a request for asking Claude to reproduce its reasoning (`Details: [reasoning_extraction]`, shown since v2.1.234). It explains how to remove such instructions, check with `--safe-mode`, and ask for explanations instead. [[lines 2703-2723](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/errors.md?plain=1#L2703-L2723)] [[Source](https://code.claude.com/docs/en/errors#safety-measures-flagged-a-cybersecurity-topic)]

#### [feature-availability](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/feature-availability.md) [[Source](https://code.claude.com/docs/en/feature-availability)]

* Noted that some features are turned off under the HIPAA configuration. [[line 284](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/feature-availability.md?plain=1#L284)] [[Source](https://code.claude.com/docs/en/feature-availability#availability-by-subscription-plan)]

#### [github-enterprise-server](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/github-enterprise-server.md) [[Source](https://code.claude.com/docs/en/github-enterprise-server)]

* Setup moved to **Organization settings > Git providers**, with **Add instance** and **Set up automatically** or **Add manually** choices. Claude Security was removed from the list of features to enable. [[lines 32-74](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/github-enterprise-server.md?plain=1#L32-L74)] [[Source](https://code.claude.com/docs/en/github-enterprise-server#admin-setup)]
* Marketplace troubleshooting lists where to connect a GHES account, or an Owner can add the marketplace to remove the per-user requirement. [[lines 201-206](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/github-enterprise-server.md?plain=1#L201-L206)] [[Source](https://code.claude.com/docs/en/github-enterprise-server#marketplace-add-on-claudeai-fails-with-a-github-access-error)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Stop hooks have an 8-consecutive-continuation cap. The next block is overridden and the turn ends, and the count resets when Claude calls a tool. [[line 2521](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/hooks.md?plain=1#L2521)] [[Source](https://code.claude.com/docs/en/hooks#stop-input)]

#### [legal-and-compliance](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/legal-and-compliance.md) [[Source](https://code.claude.com/docs/en/legal-and-compliance)]

* A BAA now extends to Claude Code through either the HIPAA configuration (CLI or Desktop Code tab on Enterprise) or ZDR. Cloud sessions, Remote Control, mobile, and third-party cloud or gateway use are not covered under HIPAA. [[lines 33-38](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/legal-and-compliance.md?plain=1#L33-L38)] [[Source](https://code.claude.com/docs/en/legal-and-compliance#healthcare-compliance-baa)]

#### [llm-gateway-protocol](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/llm-gateway-protocol.md) [[Source](https://code.claude.com/docs/en/llm-gateway-protocol)]

* Streaming requirements were rewritten as a list of how gateway behavior affects users: buffering stalls Claude Code, the full event sequence is expected, Bedrock guardrail events must be relayed as sent, pings keep the idle timeout from firing, and Bedrock event streams can't be converted to SSE. [[lines 60-66](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/llm-gateway-protocol.md?plain=1#L60-L66)] [[Source](https://code.claude.com/docs/en/llm-gateway-protocol#streaming)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Output limits are now documented as applying to successful results. Foreground text results over 50,000 characters are saved to a file unless the tool declares `anthropic/maxResultSizeChars`. Error results over about 11,000 characters keep only the first and last 5,000. [[lines 1243-1261](https://github.com/gpambrozo/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/mcp.md?plain=1#L1243-L1261)] [[Source](https://code.claude.com/docs/en/mcp#mcp-output-limits-and-warnings)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Added `rm -rf` targets ending in `/*` or `/*/` to the critical-path table, since Claude Code can't tell in advance which directories they reach. [[line 676](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/permission-modes.md?plain=1#L676)] [[Source](https://code.claude.com/docs/en/permission-modes#other-targets-that-count-as-critical-paths)]

#### [plugins/cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/plugins/cli-reference.md) [[Source](https://code.claude.com/docs/en/plugins/cli-reference)]

* Removed the minimum-version notes for `--config`, `--strict`, and `/plugin configure`. [[line 78](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/plugins/cli-reference.md?plain=1#L78)] [[Source](https://code.claude.com/docs/en/plugins/cli-reference#plugin-install)]

#### [web-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/web-quickstart.md) [[Source](https://code.claude.com/docs/en/web-quickstart)]

* "Quick web setup" was renamed "Quick setup". Cloud sessions and `/web-setup` are unavailable with the HIPAA configuration, as with ZDR. [[lines 73-87](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/web-quickstart.md?plain=1#L73-L87)] [[Source](https://code.claude.com/docs/en/web-quickstart#connect-github)]

#### [zero-data-retention](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/zero-data-retention.md) [[Source](https://code.claude.com/docs/en/zero-data-retention)]

* Notes that HIPAA-enabled Enterprise organizations can bring the CLI and Desktop Code tab under their BAA without ZDR. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/claude-code/zero-data-retention.md?plain=1#L9)] [[Source](https://code.claude.com/docs/en/zero-data-retention#zero-data-retention)]

-----

## API changes

### New Documents

None. The new Models API `line` pages for each SDK (`api/models`, `api/beta/models` and their `list` and `retrieve` pages) are new reference pages mirroring the existing Models API, for the CLI and the C#, Go, Java, PHP, Python, Ruby and TypeScript SDKs.

### Changed documents

#### [about-claude/models/optimizing-for-cost-and-intelligence](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/about-claude/models/optimizing-for-cost-and-intelligence.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)]

* Reworked the "agent runs finish sooner" guidance with figures for Claude Opus 5.5 on DRACO research tasks: 47% less time and 60% lower cost on the typical task, with a 4.1-point lower score. [[line 37](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/about-claude/models/optimizing-for-cost-and-intelligence.md?plain=1#L37)] [[Source](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#start-here)]

#### [api/compliance](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/api/compliance.md) [[Source](https://platform.claude.com/docs/en/api/compliance)]

* Added the `claude_skill_downloaded` activity type, with its full `ClaudeSkillDownloaded` object schema. There are now 514 activity types. The same change appears in the `compliance/activities` pages. [[line 676](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/api/compliance.md?plain=1#L676)] [[Source](https://platform.claude.com/docs/en/api/compliance#query-parameters)]
* Reworded the HIPAA self-serve and "taint" descriptions to refer to a compliance marker recording the HIPAA configuration. [[line 1246](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/api/compliance.md?plain=1#L1246)] [[Source](https://platform.claude.com/docs/en/api/compliance#query-parameters)]

#### [api/models](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/api/models.md) [[Source](https://platform.claude.com/docs/en/api/models)] (also beta, CLI and all SDK variants)

* Model objects now include `line` (`haiku`, `sonnet`, `opus`, `fable`, `mythos`, or `null`), with a `BetaModelLine` type. [[line 276](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/api/models/list.md?plain=1#L276)] [[Source](https://platform.claude.com/docs/en/api/models/list#returns)]

#### [api/beta/organization](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/api/beta/organization.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization)]

* The list workspaces endpoint takes a new `include_default` boolean, default `false`, to include the default workspace. [[line 8112](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/api/beta/organization.md?plain=1#L8112)] [[Source](https://platform.claude.com/docs/en/api/beta/organization#query-parameters)]

#### [api/beta/sessions](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/api/beta/sessions.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions)]

* The thread events list example now includes an `agent.message` event and a realistic `next_page` cursor. [[line 25492](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/api/beta/sessions.md?plain=1#L25492)] [[Source](https://platform.claude.com/docs/en/api/beta/sessions#response-200)]

#### [build-with-claude/embeddings](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/build-with-claude/embeddings.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/embeddings)]

* Updated Voyage AI model tables: added `voyage-code-4` and `rerank-3` / `rerank-3-lite`, and marked `voyage-3.x`, `voyage-code-3`, `voyage-context-3` and `rerank-2.5` as previous generation. [[lines 29-70](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/build-with-claude/embeddings.md?plain=1#L29-L70)] [[Source](https://platform.claude.com/docs/en/build-with-claude/embeddings#available-models)]
* Access now goes through a MongoDB Atlas model API key (`voyageai` 0.3.7 or later), and docs links point to the MongoDB documentation. [[lines 81-95](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/build-with-claude/embeddings.md?plain=1#L81-L95)] [[Source](https://platform.claude.com/docs/en/build-with-claude/embeddings#getting-started-with-voyage-ai)]
* `voyage-context-3`'s 120,000-token limit applies only with `enable_auto_chunking`. Otherwise the total across inputs is 32,000. [[line 66](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/build-with-claude/embeddings.md?plain=1#L66)] [[Source](https://platform.claude.com/docs/en/build-with-claude/embeddings#available-models)]

#### [home](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/home.md) [[Source](https://platform.claude.com/docs/en/home)]

* The API home page now includes multi-language Messages API quickstart examples (Python, TypeScript, Go, Java, Ruby and more) using `claude-opus-5-5`. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/home.md?plain=1#L15)] [[Source](https://platform.claude.com/docs/en/home#home)]

#### [manage-claude/cmek](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/manage-claude/cmek.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

* With CMEK, Claude Code can't publish artifacts. Claude smart reports and GitHub contribution metrics are disabled, and skill and plugin security scanning is unavailable. [[lines 93-97](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/manage-claude/cmek.md?plain=1#L93-L97)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek#disabled-or-modified)]

#### [manage-claude/inference-hooks](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/manage-claude/inference-hooks.md) [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks)]

* Listed features that make their own model calls and aren't governed requests or sent to your endpoint: Claude Security scans, Code Review, and smart reports. [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/manage-claude/inference-hooks.md?plain=1#L82)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks#availability)]

#### [manage-claude/plugins-api](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/manage-claude/plugins-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/plugins-api)]

* With content scanning on, a version saved in claude.ai can wait for its scan before being served. API uploads never wait. `updated_at`, `served_version_pinned` and the audit steps were updated to cover waiting and unserved versions. [[lines 259-302](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/manage-claude/plugins-api.md?plain=1#L259-L302)] [[Source](https://platform.claude.com/docs/en/manage-claude/plugins-api#versions-and-the-served-version)]

#### [manage-claude/usage-cost-api](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/manage-claude/usage-cost-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/usage-cost-api)]

* Added Tempo to the partner integrations, for usage and cost attribution to Jira work items. [[line 62](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/manage-claude/usage-cost-api.md?plain=1#L62)] [[Source](https://platform.claude.com/docs/en/manage-claude/usage-cost-api#partner-solutions)]

#### [models/overview](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/models/overview.md) [[Source](https://platform.claude.com/docs/en/models/overview)]

* Explains the new `line` field for grouping models, for example in a model picker. It is `null` for models without a line, and the set of values isn't fixed. [[line 68](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/models/overview.md?plain=1#L68)] [[Source](https://platform.claude.com/docs/en/models/overview#using-the-models-api)]

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Added an October 1, 2026 entry announcing the `line` field on `GET /v1/models` and `GET /v1/models/{model_id}`. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/ab4d12a3887d27b92cacb6a589a5f37abbbde203/docs-md/api/release-notes/overview.md?plain=1#L15)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#october-1-2026)]
