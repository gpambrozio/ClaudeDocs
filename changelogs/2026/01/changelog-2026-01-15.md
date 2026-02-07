# [Claude docs changes for January 15th, 2025](https://github.com/gpambrozio/ClaudeDocs/tree/80fef6e2713048afca3b3c9445e7c9cb90eadfea) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/80fef6e2713048afca3b3c9445e7c9cb90eadfea)]

## Executive Summary
- Agent SDK structured outputs documentation completely rewritten with new methods and streaming support
- New 'Let Claude interview you' workflow added using AskUserQuestion for interactive code generation
- Multiple MCP server naming updates and new modifier keys section for the computer use tool

## Detailed Changes

## Changed documents

### [agent-sdk/modifying-system-prompts](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agent-sdk/modifying-system-prompts.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/modifying-system-prompts)]

* Clarified that the Agent SDK uses a **minimal system prompt** by default (not empty), containing only essential tool instructions but omitting Claude Code's coding guidelines, response style, and project context. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agent-sdk/modifying-system-prompts.md?plain=1#L11)] [[Source](https://platform.claude.com/docs/en/agent-sdk/modifying-system-prompts#understanding-system-prompts)]

### [agent-sdk/structured-outputs](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agent-sdk/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/structured-outputs)]

* Major rewrite of the structured outputs documentation with improved explanations and practical examples. [[lines 1-232](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agent-sdk/structured-outputs.md?plain=1#L1-L232)] [[Source](https://platform.claude.com/docs/en/agent-sdk/structured-outputs)]
* Title changed from "Structured outputs in the SDK" to "Get structured output from agents". [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agent-sdk/structured-outputs.md?plain=1#L1)]
* New "Why structured outputs?" section with recipe app example explaining practical use cases. [[lines 9-17](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agent-sdk/structured-outputs.md?plain=1#L9-L17)] [[Source](https://platform.claude.com/docs/en/agent-sdk/structured-outputs#why-structured-outputs)]
* Renamed "Defining schemas with Zod" to "Type-safe schemas with Zod and Pydantic" with improved examples using a FeaturePlan schema. [[lines 58-117](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agent-sdk/structured-outputs.md?plain=1#L58-L117)] [[Source](https://platform.claude.com/docs/en/agent-sdk/structured-outputs#type-safe-schemas-with-zod-and-pydantic)]
* Simplified "Output format configuration" section with clearer parameter descriptions. [[lines 119-126](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agent-sdk/structured-outputs.md?plain=1#L119-L126)] [[Source](https://platform.claude.com/docs/en/agent-sdk/structured-outputs#output-format-configuration)]
* Updated TODO tracking agent example with better explanatory context. [[lines 128-183](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agent-sdk/structured-outputs.md?plain=1#L128-L183)] [[Source](https://platform.claude.com/docs/en/agent-sdk/structured-outputs#example-todo-tracking-agent)]
* Expanded error handling section with result subtypes table and tips for avoiding errors. [[lines 185-226](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agent-sdk/structured-outputs.md?plain=1#L185-L226)] [[Source](https://platform.claude.com/docs/en/agent-sdk/structured-outputs#error-handling)]

### [agent-sdk/subagents](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agent-sdk/subagents.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/subagents)]

* New "Resuming subagents" section explaining how to resume subagents with full conversation history, including session ID capture and agent ID extraction. [[lines 226-289](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agent-sdk/subagents.md?plain=1#L226-L289)] [[Source](https://platform.claude.com/docs/en/agent-sdk/subagents#resuming-subagents)]
* Documents transcript persistence behavior: transcripts persist independently of main conversation, survive compaction, and are cleaned up based on `cleanupPeriodDays` setting. [[lines 285-289](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agent-sdk/subagents.md?plain=1#L285-L289)] [[Source](https://platform.claude.com/docs/en/agent-sdk/subagents#resuming-subagents)]

### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agent-sdk/typescript.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]

* Updated `systemPrompt` parameter description to clarify default is "minimal prompt" instead of "empty prompt". [[line 125](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agent-sdk/typescript.md?plain=1#L125)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]

### [agents-and-tools/remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Updated Linear MCP server URL from `/sse` to `/mcp`. [[line 117](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L117)]
* Updated Hugging Face description to "Access the Hugging Face Hub" (previously "HF Hub") and URL now includes `gradio=none` parameter. [[lines 137-140](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L137-L140)]
* Updated Cloudflare server URL from `docs.mcp.cloudflare.com` to `bindings.mcp.cloudflare.com` and renamed to "Cloudflare Developer Platform". [[lines 229-234](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L229-L234)]
* Renamed "Hubspot" to "HubSpot" and updated documentation link. [[line 316](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L316)]
* Renamed "Monday" to "monday.com". [[line 412](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L412)]
* Renamed "Moody's Analytics" to "Moody's". [[line 420](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L420)]
* Renamed "PitchBook" to "PitchBook Premium". [[line 468](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L468)]

### [agents-and-tools/tool-use/computer-use-tool](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

* Clarified `hold_key` action description: now specifies it holds down a key "for a specified duration (in seconds)" instead of "while performing other actions". [[line 301](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md?plain=1#L301)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#available-actions)]
* Added new "Modifier keys with click and scroll actions" section. [[line 312](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md?plain=1#L312)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#modifier-keys-with-click-and-scroll-actions)]

### [claude-code/claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* Added `public.ecr.aws` to Container Registries allowlist. [[line 340](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L340)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#container-registries)]
* Added AWS domains (`*.amazonaws.com` and `*.api.aws`) to Cloud Platforms allowlist. [[lines 361-362](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L361-L362)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#cloud-platforms)]

### [claude-code/common-workflows](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Updated Plan Mode description to mention that Claude uses `AskUserQuestion` to gather requirements and clarify goals before proposing a plan. [[line 326](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/claude-code/common-workflows.md?plain=1#L326)] [[Source](https://code.claude.com/docs/en/common-workflows#use-plan-mode-for-safe-code-analysis)]
* New "Let Claude interview you" section with examples for gathering requirements through interactive questioning. [[lines 407-446](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/claude-code/common-workflows.md?plain=1#L407-L446)] [[Source](https://code.claude.com/docs/en/common-workflows#let-claude-interview-you)]

### [claude-code/mcp](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Updated Hugging Face description to "Access the Hugging Face Hub" (previously "HF Hub"). [[line 129](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/claude-code/mcp.md?plain=1#L129)]
* Updated Asana documentation link and command format. [[lines 137-141](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/claude-code/mcp.md?plain=1#L137-L141)]
* Updated Atlassian from "Atlassian Rovo" to "Atlassian" with new documentation link and transport changed from `http` to `sse`. [[lines 143-147](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/claude-code/mcp.md?plain=1#L143-L147)]
* Renamed "Cloudflare" to "Cloudflare Developer Platform". [[line 207](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/claude-code/mcp.md?plain=1#L207)]
* Renamed "Monday" to "monday.com". [[line 305](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/claude-code/mcp.md?plain=1#L305)]

### [claude-code/settings](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Updated `AskUserQuestion` tool description to "Asks multiple-choice questions to gather requirements or clarify ambiguity". [[line 819](https://github.com/gpambrozio/ClaudeDocs/blob/80fef6e2713048afca3b3c9445e7c9cb90eadfea/docs-md/claude-code/settings.md?plain=1#L819)] [[Source](https://code.claude.com/docs/en/settings)]
