# Tools reference

Claude Code has access to a set of tools that help it understand and modify your codebase. The tool names below are the exact strings you use in [permission rules](permissions.md), [subagent tool lists](sub-agents.md), and [hook matchers](hooks.md).

| Tool | Description | Permission Required |
| --- | --- | --- |
| `Agent` | Spawns a [subagent](sub-agents.md) with its own context window to handle a task | No |
| `AskUserQuestion` | Asks multiple-choice questions to gather requirements or clarify ambiguity | No |
| `Bash` | Executes shell commands in your environment. See [Bash tool behavior](#bash-tool-behavior) | Yes |
| `CronCreate` | Schedules a recurring or one-shot prompt within the current session (gone when Claude exits). See [scheduled tasks](scheduled-tasks.md) | No |
| `CronDelete` | Cancels a scheduled task by ID | No |
| `CronList` | Lists all scheduled tasks in the session | No |
| `Edit` | Makes targeted edits to specific files | Yes |
| `EnterPlanMode` | Switches to plan mode to design an approach before coding | No |
| `EnterWorktree` | Creates an isolated [git worktree](common-workflows.md) and switches into it | No |
| `ExitPlanMode` | Presents a plan for approval and exits plan mode | Yes |
| `ExitWorktree` | Exits a worktree session and returns to the original directory | No |
| `Glob` | Finds files based on pattern matching | No |
| `Grep` | Searches for patterns in file contents | No |
| `ListMcpResourcesTool` | Lists resources exposed by connected [MCP servers](mcp.md) | No |
| `LSP` | Code intelligence via language servers. Reports type errors and warnings automatically after file edits. Also supports navigation operations: jump to definitions, find references, get type info, list symbols, find implementations, trace call hierarchies. Requires a [code intelligence plugin](discover-plugins.md) and its language server binary | No |
| `NotebookEdit` | Modifies Jupyter notebook cells | Yes |
| `Read` | Reads the contents of files | No |
| `ReadMcpResourceTool` | Reads a specific MCP resource by URI | No |
| `Skill` | Executes a [skill](skills.md) within the main conversation | Yes |
| `TaskCreate` | Creates a new task in the task list | No |
| `TaskGet` | Retrieves full details for a specific task | No |
| `TaskList` | Lists all tasks with their current status | No |
| `TaskOutput` | Retrieves output from a background task | No |
| `TaskStop` | Kills a running background task by ID | No |
| `TaskUpdate` | Updates task status, dependencies, details, or deletes tasks | No |
| `TodoWrite` | Manages the session task checklist. Available in non-interactive mode and the [Agent SDK](headless.md); interactive sessions use TaskCreate, TaskGet, TaskList, and TaskUpdate instead | No |
| `ToolSearch` | Searches for and loads deferred tools when [tool search](mcp.md) is enabled | No |
| `WebFetch` | Fetches content from a specified URL | Yes |
| `WebSearch` | Performs web searches | Yes |
| `Write` | Creates or overwrites files | Yes |

Permission rules can be configured using `/permissions` or in [permission settings](settings.md). Also see [Tool-specific permission rules](permissions.md).

## [​](#bash-tool-behavior) Bash tool behavior

The Bash tool runs each command in a separate process with the following persistence behavior:

- Working directory persists across commands. Set `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR=1` to reset to the project directory after each command.
- Environment variables do not persist. An `export` in one command will not be available in the next.

Activate your virtualenv or conda environment before launching Claude Code. To make environment variables persist across Bash commands, set [`CLAUDE_ENV_FILE`](env-vars.md) to a shell script before launching Claude Code, or use a [SessionStart hook](hooks.md) to populate it dynamically.

## [​](#see-also) See also

- [Permissions](permissions.md): permission system, rule syntax, and tool-specific patterns
- [Subagents](sub-agents.md): configure tool access for subagents
- [Hooks](hooks-guide.md): run custom commands before or after tool execution

---

*Copyright © Anthropic. All rights reserved.*
