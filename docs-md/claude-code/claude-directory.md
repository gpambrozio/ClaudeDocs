# Explore the .claude directory

Claude Code reads instructions, settings, skills, subagents, and memory from your project directory and from `~/.claude` in your home directory. Commit project files to git to share them with your team; files in `~/.claude` are personal configuration that applies across all your projects.
Most users only edit `CLAUDE.md` and `settings.json`. The rest of the directory is optional: add skills, rules, or subagents as you need them.
This page is an interactive explorer: click files in the tree to see what each one does, when it loads, and an example. For a quick reference, see the [file reference table](#file-reference) below.

The interactive explorer works best on a larger screen. See the [file reference table](#file-reference) below, or show the explorer anyway.

ProjectGlobal (~/)⊞⛶

CLAUDE.md

{}.mcp.json

.worktreeinclude

▾.claude/

{}settings.json

{}settings.local.json

▾rules/

testing.md

api-design.md

▾skills/

▾security-review/

SKILL.md

checklist.md

▾commands/

fix-issue.md

▸output-styles/

▾agents/

code-reviewer.md

▾agent-memory/

▾<agent-name>/

MEMORY.md

CLAUDE.md selected

your-project / CLAUDE.md

CLAUDE.md

Project instructions Claude reads every session

committed

When it loads

Loaded into context at the start of every session

Project-specific instructions that shape how Claude works in this repository. Put your conventions, common commands, and architectural context here so Claude operates with the same assumptions your team does.

Tips

●Target under 200 lines. Longer files still load in full but may reduce adherence

●CLAUDE.md loads into every session. If something only matters for specific tasks, move it to a [skill](skills.md) or a path-scoped [rule](memory.md) so it loads only when needed

●List the commands you run most, like build, test, and format, so Claude knows them without you spelling them out each time

●Run `/memory` to open and edit CLAUDE.md from within a session

●Also works at `.claude/CLAUDE.md` if you prefer to keep the project root clean

This example is for a TypeScript and React project. It lists the build and test commands, the framework conventions Claude should follow, and project-specific rules like export style and file layout.

CLAUDE.mdCopy

```
# Project conventions

## Commands
- Build: `npm run build`
- Test: `npm test`
- Lint: `npm run lint`

## Stack
- TypeScript with strict mode
- React 19, functional components only

## Rules
- Named exports, never default exports
- Tests live next to source: `foo.ts` -> `foo.test.ts`
- All API routes return `{ data, error }` shape
```

[Full docs →](memory.md)

## [​](#what’s-not-shown) What’s not shown

The explorer covers files you author and edit. A few authored files live elsewhere:

| File | Location | Purpose |
| --- | --- | --- |
| `managed-settings.json` | System-level, varies by OS | Enterprise-enforced settings that you can’t override. See [server-managed settings](server-managed-settings.md). |
| `CLAUDE.local.md` | Project root | Your private preferences for this project, loaded alongside CLAUDE.md. Create it manually and add it to `.gitignore`. |
| Installed plugins | `~/.claude/plugins/` | Cloned marketplaces, installed plugin versions, and per-plugin data, managed by `claude plugin` commands. Orphaned versions are deleted 7 days after a plugin update or uninstall. See [plugin caching](plugins-reference.md). |

`~/.claude` also holds data Claude Code writes as you work: transcripts, prompt history, file snapshots, caches, and logs. See [application data](#application-data) below.

## [​](#file-reference) File reference

This table lists every file the explorer covers. Project-scope files live in your repo under `.claude/` (or at the root for `CLAUDE.md`, `.mcp.json`, and `.worktreeinclude`). Global-scope files live in `~/.claude/` and apply across all projects.

Several things can override what you put in these files:

- [Managed settings](server-managed-settings.md) deployed by your organization take precedence over everything
- CLI flags like `--permission-mode` or `--settings` override `settings.json` for that session
- Some environment variables take precedence over their equivalent setting, but this varies: check the [environment variables reference](env-vars.md) for each one

See [settings precedence](settings.md) for the full order.

Click a filename to open that node in the explorer above.

| File | Scope | Commit | What it does | Reference |
| --- | --- | --- | --- | --- |
| [`CLAUDE.md`](#ce-claude-md) | Project and global | ✓ | Instructions loaded every session | [Memory](memory.md) |
| [`rules/*.md`](#ce-rules) | Project and global | ✓ | Topic-scoped instructions, optionally path-gated | [Rules](memory.md) |
| [`settings.json`](#ce-settings-json) | Project and global | ✓ | Permissions, hooks, env vars, model defaults | [Settings](settings.md) |
| [`settings.local.json`](#ce-settings-local-json) | Project only |  | Your personal overrides, auto-gitignored | [Settings scopes](settings.md) |
| [`.mcp.json`](#ce-mcp-json) | Project only | ✓ | Team-shared MCP servers | [MCP scopes](mcp.md) |
| [`.worktreeinclude`](#ce-worktreeinclude) | Project only | ✓ | Gitignored files to copy into new worktrees | [Worktrees](common-workflows.md) |
| [`skills/<name>/SKILL.md`](#ce-skills) | Project and global | ✓ | Reusable prompts invoked with `/name` or auto-invoked | [Skills](skills.md) |
| [`commands/*.md`](#ce-commands) | Project and global | ✓ | Single-file prompts; same mechanism as skills | [Skills](skills.md) |
| [`output-styles/*.md`](#ce-output-styles) | Project and global | ✓ | Custom system-prompt sections | [Output styles](output-styles.md) |
| [`agents/*.md`](#ce-agents) | Project and global | ✓ | Subagent definitions with their own prompt and tools | [Subagents](sub-agents.md) |
| [`agent-memory/<name>/`](#ce-agent-memory) | Project and global | ✓ | Persistent memory for subagents | [Persistent memory](sub-agents.md) |
| [`~/.claude.json`](#ce-claude-json) | Global only |  | App state, OAuth, UI toggles, personal MCP servers | [Global config](settings.md) |
| [`projects/<project>/memory/`](#ce-global-projects) | Global only |  | Auto memory: Claude’s notes to itself across sessions | [Auto memory](memory.md) |
| [`keybindings.json`](#ce-keybindings) | Global only |  | Custom keyboard shortcuts | [Keybindings](keybindings.md) |

## [​](#check-what-loaded) Check what loaded

The explorer shows what files can exist. To see what actually loaded in your current session, use these commands:

| Command | Shows |
| --- | --- |
| `/context` | Token usage by category: system prompt, memory files, skills, MCP tools, and messages |
| `/memory` | Which CLAUDE.md and rules files loaded, plus auto-memory entries |
| `/agents` | Configured subagents and their settings |
| `/hooks` | Active hook configurations |
| `/mcp` | Connected MCP servers and their status |
| `/skills` | Available skills from project, user, and plugin sources |
| `/permissions` | Current allow and deny rules |
| `/doctor` | Installation and configuration diagnostics |

Run `/context` first for the overview, then the specific command for the area you want to investigate.

## [​](#application-data) Application data

Beyond the config you author, `~/.claude` holds data Claude Code writes during sessions. These files are plaintext. Anything that passes through a tool (file contents, command output, pasted text) lands in a transcript on disk.

### [​](#swept-automatically) Swept automatically

Files older than [`cleanupPeriodDays`](settings.md) (default 30) are deleted on the next startup.

| Path under `~/.claude/` | Contents |
| --- | --- |
| `projects/<project>/<session>.jsonl` | Full conversation transcript: every message, tool call, and tool result |
| `projects/<project>/<session>/tool-results/` | Large tool outputs spilled to separate files |
| `file-history/<session>/` | Pre-edit snapshots of files Claude changed, used for [checkpoint restore](checkpointing.md) |
| `plans/` | Plan files written during [plan mode](permission-modes.md) |
| `debug/` | Per-session debug logs |
| `paste-cache/`, `image-cache/` | Contents of large pastes and attached images |
| `session-env/` | Per-session environment metadata |

### [​](#not-swept) Not swept

These persist until you delete them.

| Path under `~/.claude/` | Contents |
| --- | --- |
| `history.jsonl` | Every prompt you’ve typed, with timestamp and project path. Used for up-arrow recall. |
| `statsig/` | Feature-flag cache and a stable anonymous device ID |
| `stats-cache.json` | Aggregated token and cost counts shown by `/cost` |
| `backups/` | Timestamped copies of `~/.claude.json` taken before config migrations |
| `downloads/` | Native binary downloads staged by the auto-updater |
| `todos/` | Legacy per-session task lists. No longer written by current versions; safe to delete. |

`shell-snapshots/` and `sockets/` are runtime files removed when the session exits cleanly.

### [​](#plaintext-storage) Plaintext storage

Transcripts and history are not encrypted at rest; OS file permissions are the only protection. If a tool reads a `.env` file or a command prints a credential, that value is written to `projects/<project>/<session>.jsonl`. To reduce exposure:

- Lower `cleanupPeriodDays` to shorten how long transcripts are kept
- For headless runs, pass `--no-session-persistence` with `-p`, or set `persistSession: false` in the SDK, to skip writing transcripts entirely. There is no interactive-mode equivalent.
- Use [permission rules](permissions.md) to deny reads of credential files

### [​](#clear-local-data) Clear local data

You can delete these at any time. You lose the listed capability for past sessions; new sessions are unaffected.

| Delete | You lose |
| --- | --- |
| `~/.claude/projects/` | Resume, continue, and rewind for past sessions |
| `~/.claude/history.jsonl` | Up-arrow prompt recall |
| `~/.claude/file-history/` | Checkpoint restore for past sessions |
| `~/.claude/debug/`, `paste-cache/`, `image-cache/`, `todos/` | Nothing user-facing |

Don’t delete `~/.claude.json`, `settings.json`, or `plugins/`: those hold your auth, preferences, and installed plugins.

## [​](#related-resources) Related resources

- [Manage Claude’s memory](memory.md): write and organize CLAUDE.md, rules, and auto memory
- [Configure settings](settings.md): set permissions, hooks, environment variables, and model defaults
- [Create skills](skills.md): build reusable prompts and workflows
- [Configure subagents](sub-agents.md): define specialized agents with their own context

---

*Copyright © Anthropic. All rights reserved.*
