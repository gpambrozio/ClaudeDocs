# [Claude docs changes for February 7th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3)]

## Executive Summary
- New version 2.1.34: Fixed sandbox bypass bug and crash when agent teams setting changed between renders
- New `TeammateIdle` and `TaskCompleted` hook events added for multi-agent workflows across all hooks documentation
- Seven new individual SDK documentation pages published for C#, Go, Java, PHP, Python, Ruby, and TypeScript
- Checkpointing expanded with new 'Summarize from here' option for partial conversation summarization

## Detailed Changes

## New Claude Code versions

### [2.1.34](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/versions/2.1.34.md)

#### Major bug fixes

* Fixed a crash when agent teams setting changed between renders
* Fixed a bug where commands excluded from sandboxing could bypass the Bash ask permission rule when `autoAllowBashIfSandboxed` was enabled

-----

## Claude Code changes

### Changed documents

#### [Agent Teams](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* Added section on enforcing quality gates with hooks using `TeammateIdle` and `TaskCompleted` hooks. [[lines 198-202](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/agent-teams.md?plain=1#L198-L202)] [[Source](https://code.claude.com/docs/en/agent-teams#enforce-quality-gates-with-hooks)]

#### [Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Removed the output token configuration section that recommended specific `CLAUDE_CODE_MAX_OUTPUT_TOKENS` and `MAX_THINKING_TOKENS` values for Bedrock. [[removed lines 174-190](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/amazon-bedrock.md)]

#### [Best Practices](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Updated rewind command description to mention the new summarize feature. [[line 387](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/best-practices.md?plain=1#L387)] [[Source](https://code.claude.com/docs/en/best-practices#course-correct-early-and-often)]
* Added information about using `/rewind` with summarize to compact only part of the conversation. [[lines 403-404](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/best-practices.md?plain=1#L403-L404)] [[Source](https://code.claude.com/docs/en/best-practices#manage-context-aggressively)]
* Updated checkpointing section to mention the new rewind menu with summarize option. [[line 436](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/best-practices.md?plain=1#L436)] [[Source](https://code.claude.com/docs/en/best-practices#rewind-with-checkpoints)]

#### [Checkpointing](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/checkpointing.md) [[Source](https://code.claude.com/docs/en/checkpointing)]

* Expanded rewind menu documentation to include four actions: restore code and conversation, restore conversation, restore code, and the new "Summarize from here" option. [[lines 17-26](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/checkpointing.md?plain=1#L17-L26)] [[Source](https://code.claude.com/docs/en/checkpointing#rewind-and-summarize)]
* Added new "Restore vs. summarize" section explaining the difference between restore operations and the summarize feature. [[lines 29-39](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/checkpointing.md?plain=1#L29-L39)] [[Source](https://code.claude.com/docs/en/checkpointing#restore-vs-summarize)]
* Added "Freeing context space" as a new use case for checkpoints with the summarize feature. [[line 48](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/checkpointing.md?plain=1#L48)] [[Source](https://code.claude.com/docs/en/checkpointing#common-use-cases)]

#### [CLI Reference](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Added `disallowedTools` parameter to custom subagent configuration. [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/cli-reference.md?plain=1#L82)] [[Source](https://code.claude.com/docs/en/cli-reference#agents-flag-format)]
* Added support for `Task(agent_type)` syntax in the tools parameter. [[line 81](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/cli-reference.md?plain=1#L81)] [[Source](https://code.claude.com/docs/en/cli-reference#agents-flag-format)]
* Added `skills`, `mcpServers`, and `maxTurns` parameters to custom subagent configuration. [[lines 83-85](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/cli-reference.md?plain=1#L83-L85)] [[Source](https://code.claude.com/docs/en/cli-reference#agents-flag-format)]

#### [Hooks Guide](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Added `TeammateIdle` and `TaskCompleted` hook events to the lifecycle table. [[lines 312-313](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/hooks-guide.md?plain=1#L312-L313)] [[Source](https://code.claude.com/docs/en/hooks-guide#how-hooks-work)]
* Added `bypass_permissions_disabled` as a new session end reason. [[line 433](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/hooks-guide.md?plain=1#L433)] [[Source](https://code.claude.com/docs/en/hooks-guide#filter-hooks-with-matchers)]
* Updated matcher support documentation to include `TeammateIdle` and `TaskCompleted` as events that always fire. [[line 437](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/hooks-guide.md?plain=1#L437)] [[Source](https://code.claude.com/docs/en/hooks-guide#filter-hooks-with-matchers)]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Updated hook lifecycle diagram image URL. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/hooks.md?plain=1#L11)] [[Source](https://code.claude.com/docs/en/hooks#hook-lifecycle)]
* Added `TeammateIdle` and `TaskCompleted` to the hook events table. [[lines 27-28](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/hooks.md?plain=1#L27-L28)] [[Source](https://code.claude.com/docs/en/hooks#hook-lifecycle)]
* Added `TeammateIdle` and `TaskCompleted` to the matcher support documentation. [[line 176](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/hooks.md?plain=1#L176)] [[Source](https://code.claude.com/docs/en/hooks#matcher-patterns)]
* Added `TeammateIdle` and `TaskCompleted` to the exit code 2 blocking behaviors table. [[lines 469-470](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/hooks.md?plain=1#L469-L470)] [[Source](https://code.claude.com/docs/en/hooks#exit-code-2-behavior-per-event)]
* Added `TeammateIdle` and `TaskCompleted` to the decision control patterns table. [[line 516](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/hooks.md?plain=1#L516)] [[Source](https://code.claude.com/docs/en/hooks#decision-control)]
* Added complete documentation for the new `TeammateIdle` hook event with input schema and decision control examples. [[lines 1232-1277](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/hooks.md?plain=1#L1232-L1277)] [[Source](https://code.claude.com/docs/en/hooks#teammateidle)]
* Added complete documentation for the new `TaskCompleted` hook event with input schema and decision control examples. [[lines 1279-1335](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/hooks.md?plain=1#L1279-L1335)] [[Source](https://code.claude.com/docs/en/hooks#teammateidle-decision-control)]
* Updated prompt-based hooks to include `TaskCompleted` and clarified that `TeammateIdle` does not support prompt-based hooks. [[line 1406](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/hooks.md?plain=1#L1406)] [[Source](https://code.claude.com/docs/en/hooks#prompt-based-hooks)]

#### [How Claude Code Works](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/how-claude-code-works.md) [[Source](https://code.claude.com/docs/en/how-claude-code-works)]

* Updated session description to mention auto memory as a way to persist learnings across sessions. [[line 62](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/how-claude-code-works.md?plain=1#L62)] [[Source](https://code.claude.com/docs/en/how-claude-code-works#work-with-sessions)]

#### [Interactive Mode](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Updated `Esc` + `Esc` keybinding description to include summarize functionality. [[line 26](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/interactive-mode.md?plain=1#L26)] [[Source](https://code.claude.com/docs/en/interactive-mode#general-controls)]
* Updated `/rewind` command description to include summarize functionality. [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/interactive-mode.md?plain=1#L95)] [[Source](https://code.claude.com/docs/en/interactive-mode#built-in-commands)]

#### [Keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* Updated `MessageSelector` context description to mention summarize functionality. [[line 58](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/keybindings.md?plain=1#L58)] [[Source](https://code.claude.com/docs/en/keybindings#contexts)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added Consensus MCP server for exploring scientific research. [[lines 267-271](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/mcp.md?plain=1#L267-L271)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* Added Context7 MCP server for up-to-date docs for LLMs and AI code editors. [[lines 273-277](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/mcp.md?plain=1#L273-L277)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]

#### [Memory](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Updated introduction to differentiate between auto memory and CLAUDE.md files. [[lines 3-7](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/memory.md?plain=1#L3-L7)] [[Source](https://code.claude.com/docs/en/memory)]
* Added auto memory to the memory locations table. [[line 21](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/memory.md?plain=1#L21)] [[Source](https://code.claude.com/docs/en/memory#determine-memory-type)]
* Updated memory loading behavior description to include auto memory loading. [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/memory.md?plain=1#L23)] [[Source](https://code.claude.com/docs/en/memory#determine-memory-type)]
* Added comprehensive auto memory section covering what Claude remembers, storage location, how it works, and management. [[lines 27-79](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/memory.md?plain=1#L27-L79)] [[Source](https://code.claude.com/docs/en/memory#auto-memory)]

#### [Plugins Reference](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Added `TeammateIdle` and `TaskCompleted` to the available hook events list. [[lines 111-112](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/plugins-reference.md?plain=1#L111-L112)] [[Source](https://code.claude.com/docs/en/plugins-reference#hooks)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `CLAUDE_CODE_DISABLE_AUTO_MEMORY` environment variable for controlling auto memory feature. [[line 845](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/settings.md?plain=1#L845)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]
* Updated `SLASH_COMMAND_TOOL_CHAR_BUDGET` description to reflect dynamic scaling at 2% of context window with 16,000 character fallback. [[line 897](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/settings.md?plain=1#L897)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]

#### [Skills](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Added section on loading skills from additional directories using `--add-dir`. [[lines 117-120](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/skills.md?plain=1#L117-L120)] [[Source](https://code.claude.com/docs/en/skills#skills-from-additional-directories)]
* Updated skills character budget documentation to reflect dynamic scaling at 2% of context window. [[lines 726-727](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/skills.md?plain=1#L726-L727)] [[Source](https://code.claude.com/docs/en/skills#claude-doesn’t-see-all-my-skills)]

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Updated CLI agents documentation to list all supported frontmatter fields including new ones. [[line 185](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/sub-agents.md?plain=1#L185)] [[Source](https://code.claude.com/docs/en/sub-agents#choose-the-subagent-scope)]
* Added `delegate` permission mode to the permission modes table. [[line 298](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/sub-agents.md?plain=1#L298)] [[Source](https://code.claude.com/docs/en/sub-agents#permission-modes)]
* Added `maxTurns` and `mcpServers` to the frontmatter fields table. [[lines 223-226](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/sub-agents.md?plain=1#L223-L226)] [[Source](https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields)]
* Added section on restricting which subagents can be spawned using `Task(agent_type)` syntax. [[lines 260-286](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/sub-agents.md?plain=1#L260-L286)] [[Source](https://code.claude.com/docs/en/sub-agents#restrict-which-subagents-can-be-spawned)]
* Updated `SubagentStop` hook to support matchers for targeting specific agent types. [[line 507](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/claude-code/sub-agents.md?plain=1#L507)] [[Source](https://code.claude.com/docs/en/sub-agents#project-level-hooks-for-subagent-events)]

-----

## API changes

### New Documents

#### [C# SDK](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/api/sdks/csharp.md) [[Source](https://platform.claude.com/docs/en/api/sdks/csharp)]

Comprehensive documentation for the C# SDK including installation, basic usage, streaming, async operations, Microsoft.Extensions.AI.IChatClient integration, error handling, and platform support for Claude API, Amazon Bedrock, and Google Vertex AI.

#### [Go SDK](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/api/sdks/go.md) [[Source](https://platform.claude.com/docs/en/api/sdks/go)]

Comprehensive documentation for the Go SDK including installation, basic usage, streaming, context-based cancellation, functional options pattern, error handling, retry configuration, and platform support for Claude API, Amazon Bedrock, and Google Vertex AI.

#### [Java SDK](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/api/sdks/java.md) [[Source](https://platform.claude.com/docs/en/api/sdks/java)]

Comprehensive documentation for the Java SDK including installation (Gradle and Maven), basic usage, streaming, async operations with CompletableFuture, builder pattern, structured outputs, error handling, retry configuration, timeouts, and platform support for Claude API, Amazon Bedrock, and Google Vertex AI.

#### [PHP SDK](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/api/sdks/php.md) [[Source](https://platform.claude.com/docs/en/api/sdks/php)]

Comprehensive documentation for the PHP SDK including installation, basic usage, streaming, async operations with Amp, value objects, error handling, retry configuration, timeouts, and platform support for Claude API, Amazon Bedrock, and Google Vertex AI.

#### [Python SDK](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/api/sdks/python.md) [[Source](https://platform.claude.com/docs/en/api/sdks/python)]

Comprehensive documentation for the Python SDK including installation with extras for Bedrock/Vertex/aiohttp, basic usage, async operations, streaming, Pydantic integration, structured outputs with `client.messages.parse()`, error handling, retry configuration, timeouts, and platform support for Claude API, Amazon Bedrock, and Google Vertex AI.

#### [Ruby SDK](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/api/sdks/ruby.md) [[Source](https://platform.claude.com/docs/en/api/sdks/ruby)]

Comprehensive documentation for the Ruby SDK including installation, basic usage, streaming, Sorbet type support, structured outputs with BaseModel, error handling, retry configuration, timeouts, and platform support for Claude API, Amazon Bedrock, and Google Vertex AI.

#### [TypeScript SDK](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/api/sdks/typescript.md) [[Source](https://platform.claude.com/docs/en/api/sdks/typescript)]

Comprehensive documentation for the TypeScript SDK including installation, basic usage for Node.js/Deno/Bun/browsers, streaming, async operations, Zod integration, structured outputs, error handling, retry configuration, timeouts, and platform support for Claude API, Amazon Bedrock, and Google Vertex AI.

### Changed documents

#### [Client SDKs](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/api/client-sdks.md) [[Source](https://platform.claude.com/docs/en/api/client-sdks)]

* Complete restructure of the page into a landing page format with links to individual SDK pages. [[entire file](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/api/client-sdks.md)]
* Added quick installation section with tabs for each SDK. [[lines 23-62](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/api/client-sdks.md?plain=1#L23-L62)] [[Source](https://platform.claude.com/docs/en/api/client-sdks)]
* Added platform support table showing Claude API, Amazon Bedrock, Google Vertex AI, and Microsoft Foundry. [[lines 79-85](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/api/client-sdks.md?plain=1#L79-L85)] [[Source](https://platform.claude.com/docs/en/api/client-sdks)]
* Added beta features section with example code. [[lines 87-99](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/api/client-sdks.md?plain=1#L87-L99)] [[Source](https://platform.claude.com/docs/en/api/client-sdks)]
* Added requirements table for all SDKs. [[lines 101-110](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/api/client-sdks.md?plain=1#L101-L110)] [[Source](https://platform.claude.com/docs/en/api/client-sdks)]

#### [Adaptive Thinking](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* Updated contact email obfuscation link. [[line 172](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/build-with-claude/adaptive-thinking.md?plain=1#L172)] [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

#### [Claude on Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/build-with-claude/claude-on-amazon-bedrock.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock)]

* Added SDK tabs for Python, TypeScript, Java, Go, and Boto3 installation instructions. [[lines 27-42](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/build-with-claude/claude-on-amazon-bedrock.md?plain=1#L27-L42)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock)]

#### [Claude on Vertex AI](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/build-with-claude/claude-on-vertex-ai.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

* Added SDK tabs for Python, TypeScript, Java, and Go installation instructions. [[lines 20-32](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/build-with-claude/claude-on-vertex-ai.md?plain=1#L20-L32)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]
* Added links to Amazon Bedrock and Microsoft Foundry documentation. [[line 90](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/build-with-claude/claude-on-vertex-ai.md?plain=1#L90)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

#### [Extended Thinking](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Updated contact email obfuscation link. [[line 105](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L105)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

#### [Files](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Updated contact email obfuscation link for rate limit increases. [[line 284](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/build-with-claude/files.md?plain=1#L284)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

#### [Structured Outputs](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* Updated SDK helpers section to mention Java and Ruby support in addition to Python and TypeScript. [[line 110](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L110)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]
* Added section on using native schema definitions with examples for Python Pydantic, TypeScript Zod, Java classes, and Ruby BaseModel. [[lines 115-121](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L115-L121)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]
* Added SDK tabs for Python and Java examples in SDK-specific methods section. [[lines 175-183](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L175-L183)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

#### [Vision](https://github.com/gpambrozio/ClaudeDocs/blob/bddd4e7558aef7fdecbeaeb9b97f9436126ea5b3/docs-md/api/build-with-claude/vision.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]

* Minor wording changes throughout for improved clarity and consistency.
