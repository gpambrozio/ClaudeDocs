# [Claude docs changes for February 6th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb)]

## Executive Summary
- New versions 2.1.32-2.1.33: Claude Opus 4.6 available, research preview agent teams for multi-agent collaboration, and auto memory feature
- Claude API: Major release with adaptive thinking, compaction API, data residency controls, and 128K output tokens for Opus 4.6
- Seven new language-specific SDK documentation pages and comprehensive migration guide for Claude 4.6

## Detailed Changes

## New Claude Code versions

### [2.1.32](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/versions/2.1.32.md)

#### New features

* Claude Opus 4.6 is now available
* Added research preview agent teams feature for multi-agent collaboration (token-intensive feature, requires setting CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1)
* Claude now automatically records and recalls memories as it works
* Added "Summarize from here" to the message selector, allowing partial conversation summarization

#### Existing feature improvements

* Skills defined in `.claude/skills/` within additional directories (`--add-dir`) are now loaded automatically
* Updated --resume to re-use --agent value specified in previous conversation by default
* Skill character budget now scales with context window (2% of context), so users with larger context windows can see more skill descriptions without truncation

#### Major bug fixes

* Fixed `@` file completion showing incorrect relative paths when running from a subdirectory
* Fixed Bash tool no longer throws "Bad substitution" errors when heredocs contain JavaScript template literals like `${index + 1}`
* Fixed Thai/Lao spacing vowels not rendering correctly in the input field
* VSCode: Fixed slash commands incorrectly being executed when pressing Enter with preceding text in the input field
* VSCode: Added spinner when loading past conversations list

### [2.1.33](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/versions/2.1.33.md)

#### New features

* Added `TeammateIdle` and `TaskCompleted` hook events for multi-agent workflows
* Added support for restricting which sub-agents can be spawned via `Task(agent_type)` syntax in agent "tools" frontmatter
* Added `memory` frontmatter field support for agents, enabling persistent memory with `user`, `project`, or `local` scope
* Added plugin name to skill descriptions and `/skills` menu for better discoverability
* VSCode: Added support for remote sessions, allowing OAuth users to browse and resume sessions from claude.ai
* VSCode: Added git branch and message count to the session picker, with support for searching by branch name

#### Existing feature improvements

* Improved error messages for API connection failures — now shows specific cause (e.g., ECONNREFUSED, SSL errors) instead of generic "Connection error"
* Errors from invalid managed settings are now surfaced

#### Major bug fixes

* Fixed agent teammate sessions in tmux to send and receive messages
* Fixed warnings about agent teams not being available on your current plan
* Fixed an issue where submitting a new message while the model was in extended thinking would interrupt the thinking phase
* Fixed an API error that could occur when aborting mid-stream, where whitespace text combined with a thinking block would bypass normalization and produce an invalid request
* Fixed API proxy compatibility issue where 404 errors on streaming endpoints no longer triggered non-streaming fallback
* Fixed an issue where proxy settings configured via `settings.json` environment variables were not applied to WebFetch and other HTTP requests on the Node.js build
* Fixed `/resume` session picker showing raw XML markup instead of clean titles for sessions started with slash commands
* VSCode: Fixed scroll-to-bottom under-scrolling on initial session load and session switch

-----

## Claude Code changes

### New Documents

#### [Agent Teams](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

Experimental feature that allows multiple Claude Code instances to work in parallel with a team lead coordinating work and teammates communicating directly with each other. The document covers use cases, enabling the feature (requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`), controlling teams, display modes, and best practices for leveraging parallel exploration on research, reviews, and complex debugging tasks.

### Changed documents

#### [Analytics](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/analytics.md) [[Source](https://code.claude.com/docs/en/analytics)]

* Added Opus 4.6 to the model IDs table. [[line 63](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/analytics.md?plain=1#L63)] [[Source](https://code.claude.com/docs/en/analytics#review-summary-metrics)]

#### [Best Practices](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Updated model recommendation from Claude Sonnet 4.5 to Claude Opus 4.6 for most tasks. [[line 40](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/best-practices.md?plain=1#L40)] [[Source](https://code.claude.com/docs/en/best-practices#explore-first-then-plan-then-code)]

#### [CLI Reference](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Updated default model from Sonnet 4.5 to Opus 4.6 in examples. [[lines 120-121](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/cli-reference.md?plain=1#L120-L121)] [[Source](https://code.claude.com/docs/en/cli-reference#system-prompt-flags)]

#### [Common Workflows](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Updated model references from Sonnet 4.5 to Opus 4.6 throughout examples. [[line 155](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/common-workflows.md?plain=1#L155)] [[Source](https://code.claude.com/docs/en/common-workflows#fix-bugs-efficiently)]

#### [Costs](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* Added Claude Opus 4.6 pricing information to the pricing table. [[line 17](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/costs.md?plain=1#L17)] [[Source](https://code.claude.com/docs/en/costs#using-the-/cost-command)]
* Updated cost calculations and examples to use Opus 4.6 pricing. [[lines 85-90](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/costs.md?plain=1#L85-L90)] [[Source](https://code.claude.com/docs/en/costs#manage-context-proactively)]

#### [Features Overview](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/features-overview.md) [[Source](https://code.claude.com/docs/en/features-overview)]

* Updated model recommendation to Opus 4.6. [[line 25](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/features-overview.md?plain=1#L25)] [[Source](https://code.claude.com/docs/en/features-overview#match-features-to-your-goal)]

#### [GitHub Actions](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/github-actions.md) [[Source](https://code.claude.com/docs/en/github-actions)]

* Updated workflow examples to use Opus 4.6 instead of Sonnet 4.5. [[line 98](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/github-actions.md?plain=1#L98)] [[Source](https://code.claude.com/docs/en/github-actions#before-and-after-example)]

#### [Google Vertex AI](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/google-vertex-ai.md) [[Source](https://code.claude.com/docs/en/google-vertex-ai)]

* Updated Vertex AI model mapping table to include Opus 4.6. [[line 62](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/google-vertex-ai.md?plain=1#L62)] [[Source](https://code.claude.com/docs/en/google-vertex-ai#4-configure-claude-code)]

#### [How Claude Code Works](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/how-claude-code-works.md) [[Source](https://code.claude.com/docs/en/how-claude-code-works)]

* Updated model references to Opus 4.6 in description of Claude Code capabilities. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/how-claude-code-works.md?plain=1#L9)] [[Source](https://code.claude.com/docs/en/how-claude-code-works#the-agentic-loop)]

#### [Interactive Mode](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Updated model examples from Sonnet 4.5 to Opus 4.6. [[line 58](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/interactive-mode.md?plain=1#L58)] [[Source](https://code.claude.com/docs/en/interactive-mode#multiline-input)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Updated model name references to Opus 4.6. [[line 282](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/mcp.md?plain=1#L282)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]

#### [Microsoft Foundry](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/microsoft-foundry.md) [[Source](https://code.claude.com/docs/en/microsoft-foundry)]

* Added Opus 4.6 to the Microsoft Foundry model mapping table. [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/microsoft-foundry.md?plain=1#L47)] [[Source](https://code.claude.com/docs/en/microsoft-foundry#2-configure-azure-credentials)]

#### [Model Config](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Updated model configuration examples to use Opus 4.6 as default. [[lines 24-25](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/model-config.md?plain=1#L24-L25)] [[Source](https://code.claude.com/docs/en/model-config#model-aliases)]
* Added Opus 4.6 to available models list. [[line 49](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/model-config.md?plain=1#L49)] [[Source](https://code.claude.com/docs/en/model-config#setting-your-model)]

#### [Plugins](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* Updated model references in plugin examples to Opus 4.6. [[line 148](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/plugins.md?plain=1#L148)] [[Source](https://code.claude.com/docs/en/plugins#create-your-first-plugin)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Updated default model setting from Sonnet 4.5 to Opus 4.6. [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/settings.md?plain=1#L42)] [[Source](https://code.claude.com/docs/en/settings#when-to-use-each-scope)]

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Added clarification about the difference between subagents and agent teams. [[lines 3-5](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/sub-agents.md?plain=1#L3-L5)] [[Source](https://code.claude.com/docs/en/sub-agents)]
* Improved description of persistent memory functionality. [[line 300](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/sub-agents.md?plain=1#L300)] [[Source](https://code.claude.com/docs/en/sub-agents#enable-persistent-memory)]
* Added note about using agent teams for tasks requiring sustained parallelism. [[line 568](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/claude-code/sub-agents.md?plain=1#L568)] [[Source](https://code.claude.com/docs/en/sub-agents#run-parallel-research)]

-----

## API changes

### New Documents

#### [Adaptive Thinking](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

Explains Claude Opus 4.6's new adaptive thinking mode, which allows the model to dynamically decide when and how much to think based on request complexity. Demonstrates how to use it with the effort parameter for controlling thinking depth and shows how it improves upon the older fixed budget_tokens approach.

#### [Claude Prompting Best Practices](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/prompt-engineering/claude-prompting-best-practices.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)]

Best practices guide covering prompt engineering techniques for the latest Claude models, emphasizing explicit instructions, context provision, and attention to examples. Includes guidance for specific scenarios like managing context in long-horizon tasks, tool usage patterns, adaptive thinking integration, and migration considerations from earlier models.

#### [Compaction](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/compaction.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

Beta feature that automatically summarizes conversation context when approaching token limits, enabling effectively infinite conversations for long-running tasks. Covers configuration options, parameter settings, streaming behavior, and includes complete examples for implementing this context management strategy.

#### [Data Residency](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/data-residency.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/data-residency)]

Feature that allows users to control where model inference runs on a per-request basis using the `inference_geo` parameter (global or US-only) and where data is stored at rest through workspace geo settings. US-only inference is priced at 1.1x the standard rate on Claude Opus 4.6 and newer models.

#### [Handling Stop Reasons (Messages API)](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/handling-stop-reasons.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)]

Comprehensive guide explaining the Messages API's `stop_reason` field across different response scenarios, covering stop reason values, best practices for handling truncation and refusals, and common patterns for tool use workflows. Includes extensive code examples and distinctions between stop reasons and actual API errors.

#### [Migration Guide](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/about-claude/models/migration-guide.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]

Step-by-step migration instructions for upgrading to Claude 4.6, Claude Sonnet 4.5, and Claude Haiku 4.5 models. Covers breaking changes (like prefill removal and tool parameter quoting differences), deprecated features to update, and provides detailed checklists for each model tier to ensure smooth transitions.

#### [Stop Reasons (Agent SDK)](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/agent-sdk/stop-reasons.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/stop-reasons)]

Explains how to interpret the `stop_reason` field in Agent SDK result messages to understand why the model stopped generating. Covers available stop reasons (end_turn, max_tokens, refusal, etc.), their meanings, and how to handle them appropriately in code.

#### [What's New in Claude 4.6](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/about-claude/models/whats-new-claude-4-6.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6)]

Announces Claude Opus 4.6's major new features including adaptive thinking mode, effort parameter GA, compaction API for managing long conversations, fine-grained tool streaming GA, 128K output tokens, and data residency controls. Also details deprecations like the old thinking budget tokens approach and the legacy prefill functionality.

### Changed documents

#### [Agent Skills Quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/agents-and-tools/agent-skills/quickstart.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart)]

* Updated model references in code examples from Sonnet 4.5 to Opus 4.6. [[lines 77-78](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/agents-and-tools/agent-skills/quickstart.md?plain=1#L77-L78)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart)]

#### [Agent SDK Migration Guide](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/agent-sdk/migration-guide.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/migration-guide)]

* Updated model examples to Opus 4.6 throughout the migration examples. [[lines 68-69](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/agent-sdk/migration-guide.md?plain=1#L68-L69)] [[Source](https://platform.claude.com/docs/en/agent-sdk/migration-guide)]

#### [Agent SDK Sessions](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/agent-sdk/sessions.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/sessions)]

* Updated code examples to use Opus 4.6. [[lines 95-96](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/agent-sdk/sessions.md?plain=1#L95-L96)] [[Source](https://platform.claude.com/docs/en/agent-sdk/sessions)]

#### [Agent SDK TypeScript](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/agent-sdk/typescript.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]

* Updated model references in all code examples to Opus 4.6. [[lines 38-39](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/agent-sdk/typescript.md?plain=1#L38-L39)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]

#### [Agent SDK TypeScript V2 Preview](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/agent-sdk/typescript-v2-preview.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript-v2-preview)]

* Updated all code examples to use Opus 4.6 instead of Sonnet 4.5. [[lines 31-32](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/agent-sdk/typescript-v2-preview.md?plain=1#L31-L32)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript-v2-preview)]

#### [Batch Processing](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/batch-processing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]

* Added Claude Opus 4.6 to supported models list. [[line 25](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/batch-processing.md?plain=1#L25)] [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]
* Updated model references in examples to Opus 4.6. [[line 51](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/batch-processing.md?plain=1#L51)] [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]

#### [Citations](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/citations.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/citations)]

* Updated model references in code examples to Opus 4.6. [[line 141](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/citations.md?plain=1#L141)] [[Source](https://platform.claude.com/docs/en/build-with-claude/citations)]

#### [Claude Code Analytics API](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/claude-code-analytics-api.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-code-analytics-api)]

* Added Opus 4.6 to the model IDs table. [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/claude-code-analytics-api.md?plain=1#L82)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-code-analytics-api)]

#### [Claude in Microsoft Foundry](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/claude-in-microsoft-foundry.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)]

* Added Claude Opus 4.6 to the supported models table. [[line 43](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/claude-in-microsoft-foundry.md?plain=1#L43)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)]

#### [Claude on Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/claude-on-amazon-bedrock.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock)]

* Added Claude Opus 4.6 to the Bedrock model IDs table. [[line 48](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/claude-on-amazon-bedrock.md?plain=1#L48)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock)]
* Updated model references in examples to Opus 4.6. [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/claude-on-amazon-bedrock.md?plain=1#L95)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock)]

#### [Claude on Vertex AI](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/claude-on-vertex-ai.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

* Added Claude Opus 4.6 to the Vertex AI model names table. [[line 62](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/claude-on-vertex-ai.md?plain=1#L62)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]
* Updated model references in examples to Opus 4.6. [[line 107](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/claude-on-vertex-ai.md?plain=1#L107)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

#### [Context Editing](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/context-editing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-editing)]

* Updated model references in examples to Opus 4.6. [[line 40](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/context-editing.md?plain=1#L40)] [[Source](https://platform.claude.com/docs/en/build-with-claude/context-editing)]

#### [Context Windows](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/context-windows.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]

* Added Claude Opus 4.6 to the list of models supporting 1M token context window. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/context-windows.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]
* Updated model references in examples to Opus 4.6. [[line 44](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/context-windows.md?plain=1#L44)] [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]

#### [Effort](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/effort.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

* Added Claude Opus 4.6 to supported models list with adaptive thinking integration. [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/effort.md?plain=1#L13)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]
* Updated note about Opus 4.6 using adaptive thinking with effort parameter. [[lines 15-17](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/effort.md?plain=1#L15-L17)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

#### [Extended Thinking](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Added notice that adaptive thinking is recommended for Opus 4.6 instead of manual thinking mode. [[lines 7-8](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L7-L8)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]
* Added Claude Opus 4.6 to supported models list with deprecation note for manual mode. [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L13)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]
* Added note that Opus 4.6 supports up to 128K output tokens. [[line 85](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L85)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]
* Added Opus 4.6 support for interleaved thinking with automatic enablement. [[lines 277-279](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L277-L279)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

#### [Files](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Updated model references in examples to Opus 4.6. [[line 44](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/files.md?plain=1#L44)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

#### [Get Started](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/get-started.md) [[Source](https://platform.claude.com/docs/en/get-started)]

* Updated quickstart code examples to use Opus 4.6. [[line 54](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/get-started.md?plain=1#L54)] [[Source](https://platform.claude.com/docs/en/get-started)]

#### [Intro](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/intro.md) [[Source](https://platform.claude.com/docs/en/intro)]

* Updated model recommendation to Opus 4.6. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/intro.md?plain=1#L15)] [[Source](https://platform.claude.com/docs/en/intro)]

#### [MCP Connector](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/agents-and-tools/mcp-connector.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)]

* Updated model references in examples to Opus 4.6. [[line 182](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/agents-and-tools/mcp-connector.md?plain=1#L182)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)]

#### [Model Deprecations](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/about-claude/model-deprecations.md) [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]

* Added information about Claude 4.6 deprecating prefill functionality and manual extended thinking mode. [[lines 25-35](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/about-claude/model-deprecations.md?plain=1#L25-L35)] [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]

#### [Models Overview](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/about-claude/models/overview.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]

* Updated model recommendation from Sonnet 4.5 to Opus 4.6 for most complex tasks. [[line 7](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/about-claude/models/overview.md?plain=1#L7)] [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]
* Added Claude Opus 4.6 as first column in the latest models comparison table. [[lines 15-30](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/about-claude/models/overview.md?plain=1#L15-L30)] [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]
* Added adaptive thinking feature row to model comparison table. [[line 24](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/about-claude/models/overview.md?plain=1#L24)] [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]
* Updated migration guide link to point to new Claude 4.6 migration guide. [[line 56](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/about-claude/models/overview.md?plain=1#L56)] [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]

#### [Pricing](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* Added Claude Opus 4.6 to the main pricing table. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/about-claude/pricing.md?plain=1#L15)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]
* Added new section for data residency pricing with 1.1x multiplier for US-only inference. [[lines 61-67](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/about-claude/pricing.md?plain=1#L61-L67)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]
* Added Opus 4.6 to batch processing pricing table. [[line 75](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/about-claude/pricing.md?plain=1#L75)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]
* Added Opus 4.6 to long context pricing table with higher rates. [[lines 95-98](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/about-claude/pricing.md?plain=1#L95-L98)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]
* Added Opus 4.6 to tool use system prompt token counts table. [[line 155](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/about-claude/pricing.md?plain=1#L155)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

#### [Prompt Caching](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Added Claude Opus 4.6 to supported models list. [[line 17](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L17)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]
* Updated model references in examples to Opus 4.6. [[line 56](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L56)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

#### [Prompt Engineering Overview](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/prompt-engineering/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)]

* Updated link to Claude 4 best practices to point to new Claude prompting best practices guide. [[line 70](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/prompt-engineering/overview.md?plain=1#L70)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)]

#### [Search Results](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/search-results.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/search-results)]

* Updated model references in examples to Opus 4.6. [[line 98](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/search-results.md?plain=1#L98)] [[Source](https://platform.claude.com/docs/en/build-with-claude/search-results)]

#### [Skills Guide](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/skills-guide.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/skills-guide)]

* Updated model references in examples to Opus 4.6. [[line 53](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/skills-guide.md?plain=1#L53)] [[Source](https://platform.claude.com/docs/en/build-with-claude/skills-guide)]

#### [Streaming](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/streaming.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/streaming)]

* Updated model references in examples to Opus 4.6. [[line 29](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/streaming.md?plain=1#L29)] [[Source](https://platform.claude.com/docs/en/build-with-claude/streaming)]

#### [Structured Outputs](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* Updated model references in examples to Opus 4.6. [[line 176](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L176)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

#### [Token Counting](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/token-counting.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/token-counting)]

* Updated model references in examples to Opus 4.6. [[line 40](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/token-counting.md?plain=1#L40)] [[Source](https://platform.claude.com/docs/en/build-with-claude/token-counting)]

#### [Vision](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/vision.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]

* Updated model references in examples to Opus 4.6. [[line 46](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/vision.md?plain=1#L46)] [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]

#### [Working with Messages](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/working-with-messages.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)]

* Updated model references in examples to Opus 4.6. [[line 27](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/working-with-messages.md?plain=1#L27)] [[Source](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)]
* Added Opus 4.6 to max output tokens information (128K). [[line 60](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/build-with-claude/working-with-messages.md?plain=1#L60)] [[Source](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)]

#### [All Messages API Reference Documents](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/api/)

* Added Claude Opus 4.6 (`claude-opus-4-6`) to model ID lists and updated code examples across all language SDK documentation (Python, TypeScript, Go, Java, Ruby). This includes updates to Messages API, Beta Messages API, Admin API, and all related endpoints.

#### [All Tool Use Documentation](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/agents-and-tools/tool-use/)

* Updated model references in code examples from Sonnet 4.5 to Opus 4.6 across all tool documentation pages (Bash tool, Code Execution, Computer Use, Fine-grained Streaming, Implement Tool Use, Memory Tool, Overview, Programmatic Tool Calling, Text Editor, Tool Search, Web Fetch, Web Search).

#### [All Prompt Library Examples](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/resources/prompt-library/)

* Updated model references from Sonnet 4.5 to Opus 4.6 across all 60+ prompt library examples.

#### [All Use Case Guides](https://github.com/gpambrozio/ClaudeDocs/blob/fa323a5b51a0fd1c33f433e13b2b594a0eb0bafb/docs-md/api/about-claude/use-case-guides/)

* Updated model references in code examples to Opus 4.6 for Content Moderation, Customer Support Chat, and Legal Summarization guides.
