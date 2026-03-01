# [Claude docs changes for March 1st, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/645e5b246e60bd407f31ae08aabc04cdd826ce37) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/645e5b246e60bd407f31ae08aabc04cdd826ce37)]

## Executive Summary
- The `Task` tool has been renamed to `Agent` across permissions, settings, CLI, and hook documentation (with backward compatibility for pre-2.1.63 references)
- Memory documentation completely restructured with a new title, improved comparison tables, guidance for large teams, and better organization of CLAUDE.md, rules, and auto memory
- New HTTP hook type added, allowing hooks to POST event data to external URLs (web servers, cloud functions, shared audit services)
- Three bundled skills now ship with Claude Code: `/simplify`, `/batch`, and `/debug`
- Remote Control is now available on Pro plans (previously Max only)

-----

## Claude Code changes

### Changed documents

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* The `--agents` flag documentation updated: `Task(agent_type)` syntax changed to `Agent(agent_type)` to reflect the tool rename. [[line 91](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/cli-reference.md?plain=1#L91)] [[Source](https://code.claude.com/docs/en/cli-reference#agents-flag-format)]

#### [features-overview](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/features-overview.md) [[Source](https://code.claude.com/docs/en/features-overview)]

* Added a new "CLAUDE.md vs Rules vs Skills" comparison to the feature comparison list, with a full table covering loading behavior, context cost, and best use cases for each. [[lines 74-80](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/features-overview.md?plain=1#L74-L80)] [[Source](https://code.claude.com/docs/en/features-overview#compare-similar-features)]
* Added guidance on bundled skills (simplify, batch, debug) that ship with Claude Code. [[line 163](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/features-overview.md?plain=1#L163)] [[Source](https://code.claude.com/docs/en/features-overview#understand-how-features-load)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Added documentation for the new `type: "http"` hook, which POSTs event data to an HTTP endpoint instead of running a shell command. Useful for shared audit services and external event processing. [[line 376](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/hooks-guide.md?plain=1#L376)] [[Source](https://code.claude.com/docs/en/hooks-guide#how-hooks-work)]
* New dedicated HTTP hooks section added covering POST behavior, authorization headers with environment variable interpolation, and when to prefer HTTP hooks over command hooks. [[lines 680-724](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/hooks-guide.md?plain=1#L680-L724)] [[Source](https://code.claude.com/docs/en/hooks-guide#http-hooks)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Hook type list updated to include `http` as a fourth hook type alongside command hooks. [[line ~1749](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/hooks.md?plain=1#L1749)]
* PreToolUse and SubagentStart hook documentation updated to reference "Agent tool" instead of "Task tool". [[lines ~855, ~944, ~1247](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/hooks.md?plain=1#L855)]

#### [how-claude-code-works](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/how-claude-code-works.md) [[Source](https://code.claude.com/docs/en/how-claude-code-works)]

* Added auto memory (MEMORY.md) to the list of things Claude can access at the start of each session, noting the first 200 lines are loaded automatically. [[line ~51](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/how-claude-code-works.md?plain=1#L51)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* Session history panel now supports rename and remove actions: hover over a session to reveal options to rename it with a descriptive title or remove it from the list. [[line 93](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/ide-integrations.md?plain=1#L93)] [[Source](https://code.claude.com/docs/en/ide-integrations#resume-past-conversations)]

#### [index](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/index.md) [[Source](https://code.claude.com/docs/en/index)]

* Added mention of auto memory to the customization section, describing how Claude builds notes automatically as it works. [[line ~162](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/index.md?plain=1#L162)]
* Added "Store instructions and memories" as a recommended next step linking to the memory guide. [[line ~221](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/index.md?plain=1#L221)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Major expansion of the built-in commands table with many newly documented commands including: `/agents`, `/chrome`, `/copy`, `/diff`, `/fast`, `/feedback`, `/fork`, `/hooks`, `/ide`, `/insights`, `/keybindings`, `/mobile`, `/output-style`, `/plugin`, `/pr-comments`, `/release-notes`, `/remote-control`, `/review`, `/sandbox`, `/skills`, `/statusline`, `/theme`, `/upgrade`, `/vim`, and more. [[lines 80-137](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/interactive-mode.md?plain=1#L80-L137)] [[Source](https://code.claude.com/docs/en/interactive-mode#built-in-commands)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added `ENABLE_CLAUDEAI_MCP_SERVERS` environment variable documentation: set to `false` to disable claude.ai MCP servers in Claude Code (enabled by default for logged-in users). [[line ~1144](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/mcp.md?plain=1#L1144)]

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Page completely restructured with new title "How Claude remembers your project" and a clearer intro roadmap. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/memory.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/memory)]
* New comparison table contrasting CLAUDE.md files vs auto memory across multiple dimensions. [[lines 19-27](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/memory.md?plain=1#L19-L27)] [[Source](https://code.claude.com/docs/en/memory#claude-md-vs-auto-memory)]
* New subsections added for: choosing CLAUDE.md file scope (project/user/repo), setting up a project CLAUDE.md with `/init`, and writing effective instructions (size limits, structure, specificity). [[lines 44-84](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/memory.md?plain=1#L44-L84)] [[Source](https://code.claude.com/docs/en/memory#choose-where-to-put-claude-md-files)]
* New "Manage CLAUDE.md for large teams" section covering organization-wide deployment via configuration management, excluding specific files, and team-level controls. [[line 237](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/memory.md?plain=1#L237)] [[Source](https://code.claude.com/docs/en/memory#manage-claude-md-for-large-teams)]
* Reorganized `.claude/rules/` section with dedicated subsections for path-specific rules, glob patterns, symlinks, and user-level rules. [[line 130](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/memory.md?plain=1#L130)] [[Source](https://code.claude.com/docs/en/memory#organize-rules-with-claude/rules/)]

#### [overview](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/overview.md) [[Source](https://code.claude.com/docs/en/overview)]

* Added mention of auto memory to the customization section and updated navigation links to point to the memory guide. [[line ~162](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/overview.md?plain=1#L162)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Subagent permission rules renamed from `Task(AgentName)` to `Agent(AgentName)` syntax throughout, including examples for Explore, Plan, and custom agents. [[lines 161-178](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/permissions.md?plain=1#L161-L178)] [[Source](https://code.claude.com/docs/en/permissions#agent-subagents)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Remote Control is now available as a research preview on both Max and Pro plans (previously described as Max only with Pro "coming soon"). [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/remote-control.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/remote-control)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `ENABLE_CLAUDEAI_MCP_SERVERS` to the environment variables table: set to `false` to disable claude.ai MCP servers. [[line 989](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/settings.md?plain=1#L989)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]
* Tools table updated: `Task` tool renamed to `Agent` (runs a sub-agent to handle complex, multi-step tasks). [[line 1028](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/settings.md?plain=1#L1028)] [[Source](https://code.claude.com/docs/en/settings#tools-available-to-claude)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* New "Bundled skills" section added documenting three default skills that ship with every Claude Code installation: `/simplify` (parallel code review and cleanup), `/batch` (large-scale parallel codebase changes via git worktrees), and `/debug` (session troubleshooting). [[lines 9-18](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/skills.md?plain=1#L9-L18)] [[Source](https://code.claude.com/docs/en/skills#bundled-skills)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Task tool officially renamed to Agent tool as of version 2.1.63, with a backward compatibility note that existing `Task(...)` references in settings and agent definitions still work as aliases. [[lines 277-279](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/sub-agents.md?plain=1#L277-L279)] [[Source](https://code.claude.com/docs/en/sub-agents#restrict-which-subagents-can-be-spawned)]
* All code examples updated to use `Agent(...)` syntax instead of `Task(...)`. [[lines 288-309](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/sub-agents.md?plain=1#L288-L309)] [[Source](https://code.claude.com/docs/en/sub-agents#restrict-which-subagents-can-be-spawned)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Session history panel now supports rename and remove actions: hover over a session to reveal options to rename it with a descriptive title or remove it from the list. [[line 93](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/claude-code/vs-code.md?plain=1#L93)] [[Source](https://code.claude.com/docs/en/vs-code#resume-past-conversations)]

-----

## API changes

### Changed documents

#### [typescript](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/api/agent-sdk/typescript.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]

* Added `supportedAgents()` method to the `Query` interface, returning available subagents. [[line 200](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/api/agent-sdk/typescript.md?plain=1#L200)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]
* Added `agents` field to the `SDKControlInitializeResponse` type. [[line 241](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/api/agent-sdk/typescript.md?plain=1#L241)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]
* New `AgentInfo` type documented, describing available subagents with `name`, `description`, and optional `model` fields. [[line 1995](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/api/agent-sdk/typescript.md?plain=1#L1995)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]

#### [remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* New MCP server added: Dremio Cloud — analyze and get insights from lakehouse data (user-specific URL). [[line ~962](https://github.com/gpambrozio/ClaudeDocs/blob/645e5b246e60bd407f31ae08aabc04cdd826ce37/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L962)]
* MCP server list reordered (various entries moved between positions).
