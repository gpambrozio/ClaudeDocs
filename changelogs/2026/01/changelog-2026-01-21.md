# [Claude docs changes for January 21st, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/6c95db3) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/6c95db3)]

## Executive Summary
- New version 2.1.14: History-based autocomplete in bash mode, plugin pinning to git commit SHAs, and context window fix
- Major terminology change: 'slash commands' renamed to 'skills' with `SKILL.md` files throughout all documentation
- Comprehensive VS Code extension documentation rewrite and new AWS Guardrails section for Bedrock

## Detailed Changes

## New Claude Code versions

### [2.1.14](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/versions/2.1.14.md)

#### New features

* Added history-based autocomplete in bash mode (`!`) - type a partial command and press Tab to complete from your bash command history
* Added search to installed plugins list - type to filter by name or description
* Added support for pinning plugins to specific git commit SHAs, allowing marketplace entries to install exact versions
* [VSCode] Added `/usage` command to display current plan usage

#### Existing feature improvements

* Improved backspace to delete pasted text as a single token instead of one character at a time

#### Major bug fixes

* Fixed a regression where the context window blocking limit was calculated too aggressively, blocking users at ~65% context usage instead of the intended ~98%
* Fixed memory issues that could cause crashes when running parallel subagents
* Fixed memory leak in long-running sessions where stream resources were not cleaned up after shell commands completed
* Fixed `@` symbol incorrectly triggering file autocomplete suggestions in bash mode
* Fixed `@`-mention menu folder click behavior to navigate into directories instead of selecting them
* Fixed `/feedback` command generating invalid GitHub issue URLs when description is very long
* Fixed `/context` command to show the same token count and percentage as the status line in verbose mode
* Fixed an issue where `/config`, `/context`, `/model`, and `/todos` command overlays could close unexpectedly
* Fixed slash command autocomplete selecting wrong command when typing similar commands (e.g., `/context` vs `/compact`)
* Fixed inconsistent back navigation in plugin marketplace when only one marketplace is configured
* Fixed iTerm2 progress bar not clearing properly on exit, preventing lingering indicators and bell sounds

-----

## Claude Code changes

### New Documents

#### [plan-mode](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/plan-mode.md) [[Source](https://code.claude.com/docs/en/plan-mode)]

New file appears to be a 404 page indicating the plan-mode documentation has been removed or relocated.

### Changed documents

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Added AWS Guardrails section showing how to use Amazon Bedrock Guardrails for content filtering with custom headers configuration. [[lines 242-256](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/amazon-bedrock.md?plain=1#L242-L256)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#guardrails)]

#### [checkpointing](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/checkpointing.md) [[Source](https://code.claude.com/docs/en/checkpointing)]

* Terminology updated from "slash commands" to "skills" throughout the document.

#### [chrome](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/chrome.md) [[Source](https://code.claude.com/docs/en/chrome)]

* Terminology updated from "slash commands" to "skills" throughout the document.

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Added new CLI flags: `--init` (run Setup hooks and start interactive mode), `--init-only` (run Setup hooks and exit), and `--maintenance` (run Setup hooks with maintenance trigger and exit). [[lines 38-43](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/cli-reference.md?plain=1#L38-L43)] [[Source](https://code.claude.com/docs/en/cli-reference#available-flags)]

#### [common-workflows](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Replaced "Create custom slash commands" section with new "Create custom skills and commands" section that shows how to create skills Claude can use automatically vs manual invocation using `SKILL.md` files with frontmatter. [[lines 324-418](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/common-workflows.md?plain=1#L324-L418)] [[Source](https://code.claude.com/docs/en/common-workflows#create-custom-skills-and-commands)]

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* Enhanced cost overview with clarification that costs vary by codebase size, query complexity, and conversation length, plus added table of contents. [[lines 1-5](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/costs.md?plain=1#L1-L5)] [[Source](https://code.claude.com/docs/en/costs#overview)]
* Updated `/cost` command description to clarify it's for API users, not Claude Max/Pro subscribers who should use `/stats` instead. [[lines 10-23](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/costs.md?plain=1#L10-L23)] [[Source](https://code.claude.com/docs/en/costs#track-costs)]
* Updated LiteLLM reference to support Bedrock, Vertex, and Foundry (previously just Bedrock and Vertex). [[lines 26-31](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/costs.md?plain=1#L26-L31)] [[Source](https://code.claude.com/docs/en/costs#track-costs)]
* Major expansion of "Reduce token usage" section with new strategies including: manage context proactively, choose the right model, reduce MCP server overhead, offload processing to hooks and skills, move instructions from CLAUDE.md to skills, adjust extended thinking, delegate verbose operations to subagents, write specific prompts, and work efficiently on complex tasks. [[lines 54-221](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/costs.md?plain=1#L54-L221)] [[Source](https://code.claude.com/docs/en/costs#reduce-token-usage)]

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Terminology updated from "slash commands" to "skills" throughout the document.

#### [github-actions](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/github-actions.md) [[Source](https://code.claude.com/docs/en/github-actions)]

* Terminology updated from "slash commands" to "skills" throughout the document.

#### [headless](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* Terminology updated from "slash commands" to "skills" throughout the document.

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Terminology updated from "custom slash commands" to "custom skills" throughout the document.

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Added `Setup` to events that don't require matchers (alongside `UserPromptSubmit`, `Stop`, `SubagentStop`). [[lines 54-57](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/hooks.md?plain=1#L54-L57)] [[Source](https://code.claude.com/docs/en/hooks#anatomy-of-a-hook)]
* Changed hooks scope documentation from "Hooks in Skills, Agents, and Slash Commands" to "Hooks in skills and agents". [[lines 154-159](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/hooks.md?plain=1#L154-L159)] [[Source](https://code.claude.com/docs/en/hooks#scope)]
* Clarified that `once: true` option is only supported for skills, not agents. [[lines 197-199](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/hooks.md?plain=1#L197-L199)] [[Source](https://code.claude.com/docs/en/hooks#limit-hooks-to-a-single-invocation)]
* Added new Setup hook event that runs when invoked with `--init`, `--init-only`, or `--maintenance` flags for one-time operations like dependency installation, with matchers `init` and `maintenance` and access to `CLAUDE_ENV_FILE` environment variable. [[lines 438-451](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/hooks.md?plain=1#L438-L451)] [[Source](https://code.claude.com/docs/en/hooks#setup)]
* Updated SessionStart hook description to clarify it's for per-session operations, not one-time setup, recommending Setup hooks for dependencies/migrations. [[lines 454-457](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/hooks.md?plain=1#L454-L457)] [[Source](https://code.claude.com/docs/en/hooks#sessionstart)]
* Added Setup hook input format showing JSON structure with `trigger` field (`"init"` or `"maintenance"`). [[lines 771-789](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/hooks.md?plain=1#L771-L789)] [[Source](https://code.claude.com/docs/en/hooks#input-format)]
* Updated hook output behavior table showing Setup stderr is only shown to user. [[line 859](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/hooks.md?plain=1#L859)] [[Source](https://code.claude.com/docs/en/hooks#modify-hook-behavior)]
* Added Setup hook decision control showing `additionalContext` field for loading context, with multiple hooks' context values concatenated and access to `CLAUDE_ENV_FILE`. [[lines 1053-1073](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/hooks.md?plain=1#L1053-L1073)] [[Source](https://code.claude.com/docs/en/hooks#decision-control-structured-output)]
* Updated hook output documentation showing Setup hook stdout is added as context for Claude (like UserPromptSubmit/SessionStart). [[lines 1363-1366](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/hooks.md?plain=1#L1363-L1366)] [[Source](https://code.claude.com/docs/en/hooks#hook-output)]

#### [iam](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/iam.md) [[Source](https://code.claude.com/docs/en/iam)]

* Added clarification on `:*` vs `*` wildcards - `:*` enforces word boundary (e.g., `ls:*` matches `ls -la` but not `lsof`) while `*` has no word boundary constraint (e.g., `ls*` matches both). [[lines 115-117](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/iam.md?plain=1#L115-L117)] [[Source](https://code.claude.com/docs/en/iam#allow-patterns)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Updated shortcut table description for `/` from "Slash command" to "Command or skill". [[line 65](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/interactive-mode.md?plain=1#L65)] [[Source](https://code.claude.com/docs/en/interactive-mode#keyboard-shortcuts)]
* Added new "Built-in commands" section with comprehensive table of commonly used built-in commands including `/clear`, `/compact`, `/config`, `/context`, `/cost`, `/doctor`, `/exit`, `/export`, `/help`, `/init`, `/mcp`, `/memory`, `/model`, `/permissions`, `/plan`, `/rename`, `/resume`, `/rewind`, `/stats`, `/status`, `/statusline`, `/tasks`, `/teleport`, `/theme`, `/todos`, `/usage`. [[lines 68-105](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/interactive-mode.md?plain=1#L68-L105)] [[Source](https://code.claude.com/docs/en/interactive-mode#built-in-commands)]
* Added MCP prompts subsection explaining MCP-exposed prompts using `/mcp__<server>__<prompt>` format. [[lines 107-110](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/interactive-mode.md?plain=1#L107-L110)] [[Source](https://code.claude.com/docs/en/interactive-mode#mcp-prompts)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Changed "Use MCP prompts as slash commands" to "Use MCP prompts as commands". [[line 1212](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/mcp.md?plain=1#L1212)] [[Source](https://code.claude.com/docs/en/mcp#use-mcp-prompts-as-commands)]

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Terminology updated from "slash commands" to "skills" throughout the document.

#### [output-styles](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/output-styles.md) [[Source](https://code.claude.com/docs/en/output-styles)]

* Changed comparison section from "Output Styles vs. Custom Slash Commands" to "Output Styles vs. Skills" with updated explanation of the difference. [[lines 105-109](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/output-styles.md?plain=1#L105-L109)] [[Source](https://code.claude.com/docs/en/output-styles#output-styles-vs-skills)]

#### [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Terminology updated from "slash commands" to "skills" throughout the document.

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Restructured plugin components section with Skills section moved before Agents, showing skills now support both `skills/` and `commands/` directories with `SKILL.md` format within skill directories. [[lines 9-41](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/plugins-reference.md?plain=1#L9-L41)] [[Source](https://code.claude.com/docs/en/plugins-reference#plugin-components)]
* Added Setup hook event available for `--init`, `--init-only`, or `--maintenance` flags. [[line 117](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/plugins-reference.md?plain=1#L117)] [[Source](https://code.claude.com/docs/en/plugins-reference#hooks)]
* Updated component location table showing Commands directory is now legacy and recommends `skills/` for new skills. [[line 489](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/plugins-reference.md?plain=1#L489)] [[Source](https://code.claude.com/docs/en/plugins-reference#where-to-put-plugin-components)]

#### [plugins](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* Updated plugin component list from "slash commands, agents, Skills, hooks" to "skills, agents, hooks". [[lines 3-4](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/plugins.md?plain=1#L3-L4)] [[Source](https://code.claude.com/docs/en/plugins#overview)]
* Changed comparison table and guidance from "Slash command names" to "Skill names" with all references updated. [[lines 9-25](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/plugins.md?plain=1#L9-L25)] [[Source](https://code.claude.com/docs/en/plugins#overview)]
* Updated quickstart introduction from "custom slash command" to "custom skill". [[lines 19-30](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/plugins.md?plain=1#L19-L30)] [[Source](https://code.claude.com/docs/en/plugins#quickstart)]
* Changed manifest field descriptions from "slash command namespace" to "skill namespace". [[lines 94-97](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/plugins.md?plain=1#L94-L97)] [[Source](https://code.claude.com/docs/en/plugins#create-a-manifest-file)]
* Restructured skill creation section from "Add a slash command" to "Add a skill" using `skills/hello/SKILL.md` structure with `disable-model-invocation: true` frontmatter. [[lines 103-127](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/plugins.md?plain=1#L103-L127)] [[Source](https://code.claude.com/docs/en/plugins#add-a-skill)]
* Updated skill arguments section from "slash command arguments" to "skill arguments". [[lines 158-192](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/plugins.md?plain=1#L158-L192)] [[Source](https://code.claude.com/docs/en/plugins#add-skill-arguments)]
* Updated plugin structure table showing Commands description notes it contains skills and is legacy, and Skills row shows `<name>/SKILL.md` structure. [[lines 204-227](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/plugins.md?plain=1#L204-L227)] [[Source](https://code.claude.com/docs/en/plugins#plugin-structure)]
* Updated conversion introduction from "commands, Skills, or hooks" to "skills or hooks". [[line 345](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/plugins.md?plain=1#L345)] [[Source](https://code.claude.com/docs/en/plugins#convert-existing-projects-to-plugins)]

#### [quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/quickstart.md) [[Source](https://code.claude.com/docs/en/quickstart)]

* Terminology updated from "slash commands" to "skills" throughout the document.

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Terminology updated from "slash commands" to "skills" throughout the document.

#### [security](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/security.md) [[Source](https://code.claude.com/docs/en/security)]

* Terminology updated from "slash commands" to "skills" throughout the document.

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Enhanced Bash wildcard documentation with word boundary explanation for `:*` suffix and clarification that `*` has no word boundary constraint, plus updated examples with more specific behavior descriptions. [[lines 219-226](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/settings.md?plain=1#L219-L226)] [[Source](https://code.claude.com/docs/en/settings#permissions)]
* Updated Bash permission limitations warning from generic bypass warning to specific explanation about argument-constraining patterns being fragile with concrete example of `curl` command bypass scenarios. [[line 263](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/settings.md?plain=1#L263)] [[Source](https://code.claude.com/docs/en/settings#permissions)]
* Changed terminology from "Slash commands" to "Skills". [[line 464](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/settings.md?plain=1#L464)] [[Source](https://code.claude.com/docs/en/settings#session)]
* Updated plugin configuration description from "custom commands, agents, hooks" to "skills, agents, hooks". [[line 508](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/settings.md?plain=1#L508)] [[Source](https://code.claude.com/docs/en/settings#session)]
* Updated environment variable description showing `SLASH_COMMAND_TOOL_CHAR_BUDGET` is now documented as legacy name kept for backwards compatibility. [[line 906](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/settings.md?plain=1#L906)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]
* Updated Skill tool description from "skill or slash command" to just "skill". [[line 931](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/settings.md?plain=1#L931)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]

#### [setup](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Terminology updated from "slash commands" to "skills" throughout the document.

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Major restructure of introduction changing title from "Agent Skills" to "Extend Claude with skills" with simplified explanation focusing on `SKILL.md` files, noting custom slash commands have been merged into skills, and explaining backwards compatibility for existing `.claude/commands/` files. [[lines 1-5](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/skills.md?plain=1#L1-L5)] [[Source](https://code.claude.com/docs/en/skills#overview)]
* Comprehensive rewrite throughout the entire file merging slash commands functionality into skills concept, updating all examples to use `skills/` directory structure with `SKILL.md` files, adding `disable-model-invocation` frontmatter option to control invocation, updating terminology (removed "Agent Skills"), and reorganizing sections for clarity on skill creation, invocation, and management. [[lines 8-1100+](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/skills.md?plain=1#L8-L1100)] [[Source](https://code.claude.com/docs/en/skills)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Updated default model behavior from `sonnet` to `inherit` (uses same model as main conversation). [[lines 218-220](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/sub-agents.md?plain=1#L218-L220)] [[Source](https://code.claude.com/docs/en/sub-agents#model)]
* Updated model field documentation showing if omitted, now defaults to `inherit` instead of `sonnet`. [[lines 228-230](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/sub-agents.md?plain=1#L228-L230)] [[Source](https://code.claude.com/docs/en/sub-agents#model)]
* Added new "Preload skills into subagents" subsection showing how to use `skills` field to inject skill content at startup and explaining difference from running skill in subagent via `context: fork`. [[lines 270-294](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/sub-agents.md?plain=1#L270-L294)] [[Source](https://code.claude.com/docs/en/sub-agents#preload-skills-into-subagents)]

#### [troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* Added browser authentication tip that if browser doesn't open automatically during login, press `c` to copy OAuth URL. [[line 175](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/troubleshooting.md?plain=1#L175)] [[Source](https://code.claude.com/docs/en/troubleshooting#browser-login-not-working)]
* Changed terminology from "custom slash commands" to "custom skills". [[line 251](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/troubleshooting.md?plain=1#L251)] [[Source](https://code.claude.com/docs/en/troubleshooting#skill-invocation-issues)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Clarified that extension includes CLI (no separate install needed) and updated reload window guidance. [[lines 12-20](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/vs-code.md?plain=1#L12-L20)] [[Source](https://code.claude.com/docs/en/vs-code#prerequisites)]
* Enhanced "Get started" workflow with detail about auto-seeing selected text, clarified `Alt+K`/`Option+K` adds @-mention reference, and enhanced diff explanation. [[lines 46-57](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/vs-code.md?plain=1#L46-L57)] [[Source](https://code.claude.com/docs/en/vs-code#get-started)]
* Added extension tutorials section showing VS Code walkthrough command and interactive checklist via graduation cap icon. [[lines 59-71](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/vs-code.md?plain=1#L59-L71)] [[Source](https://code.claude.com/docs/en/vs-code#extension-tutorials)]
* Added new "Use the prompt box" section covering permission modes with default setting, command menu details, context indicator, extended thinking toggle, and multi-line input. [[lines 74-87](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/vs-code.md?plain=1#L74-L87)] [[Source](https://code.claude.com/docs/en/vs-code#use-the-prompt-box)]
* Added sections on file references and conversation history covering @-mentions with fuzzy matching, selection visibility controls, drag-and-drop file attachments, and conversation history search and resume. [[lines 89-126](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/vs-code.md?plain=1#L89-L126)] [[Source](https://code.claude.com/docs/en/vs-code#reference-files-and-code)]
* Expanded "Customize your workflow" section with detailed layout options with use cases and multi-conversation support with status indicators. [[lines 128-163](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/vs-code.md?plain=1#L128-L163)] [[Source](https://code.claude.com/docs/en/vs-code#customize-your-workflow)]
* Updated commands and shortcuts section adding focus context explanation, updated keyboard shortcuts table with more details, and clarified when commands are available. [[lines 165-186](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/vs-code.md?plain=1#L165-L186)] [[Source](https://code.claude.com/docs/en/vs-code#commands-and-keyboard-shortcuts)]
* Restructured and expanded settings section split into Extension settings and Claude Code settings with comprehensive settings table with defaults and descriptions organized by setting name. [[lines 188-217](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/vs-code.md?plain=1#L188-L217)] [[Source](https://code.claude.com/docs/en/vs-code#settings)]
* Major expansion of "VS Code extension vs. Claude Code CLI" section with updated feature comparison table and added subsections on running CLI in VS Code, switching between modes, terminal output inclusion, background process monitoring, and MCP configuration. [[lines 219-277](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/vs-code.md?plain=1#L219-L277)] [[Source](https://code.claude.com/docs/en/vs-code#vs-code-extension-vs-claude-code-cli)]
* Added new "Work with git" section showing how to create commits and pull requests and use git worktrees for parallel tasks. [[lines 279-320](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/vs-code.md?plain=1#L279-L320)] [[Source](https://code.claude.com/docs/en/vs-code#work-with-git)]
* Enhanced security section with privacy statement about code usage and clarified data handling. [[lines 322-337](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/vs-code.md?plain=1#L322-L337)] [[Source](https://code.claude.com/docs/en/vs-code#security-and-privacy)]
* Expanded troubleshooting section with updated installation issues, enhanced Spark icon visibility troubleshooting, and updated non-responsive Claude troubleshooting. [[lines 339-376](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/claude-code/vs-code.md?plain=1#L339-L376)] [[Source](https://code.claude.com/docs/en/vs-code#troubleshooting)]

-----

## API changes

### Changed documents

#### [agent-sdk/modifying-system-prompts](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/api/agent-sdk/modifying-system-prompts.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/modifying-system-prompts)]

* Updated Python syntax for setting system prompt preset from `system_prompt="claude_code"` to `system_prompt={"type": "preset", "preset": "claude_code"}`. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/api/agent-sdk/modifying-system-prompts.md?plain=1#L11)] [[Source](https://platform.claude.com/docs/en/agent-sdk/modifying-system-prompts#overview)]

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/api/agent-sdk/python.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]

* Added new configuration options to `ClaudeAgentOptions`: `tools` field for tools configuration with preset support, `max_budget_usd` for session budget limits, `fallback_model` for automatic fallback when primary model fails, `betas` for enabling beta features, `cli_path` for custom CLI executable path, and `max_thinking_tokens` for controlling thinking block limits. [[lines 452-512](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/api/agent-sdk/python.md?plain=1#L452-L512)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python#options)]
* Enhanced existing field documentation with `include_partial_messages` clarified to yield `StreamEvent` messages and `can_use_tool` updated to reference new permission types section. [[lines 484-493](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/api/agent-sdk/python.md?plain=1#L484-L493)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python#options)]
* Added comprehensive permission callback types including new `CanUseTool` type alias for permission callbacks, new `ToolPermissionContext` dataclass, new `PermissionResult`, `PermissionResultAllow`, and `PermissionResultDeny` types, new `PermissionUpdate` dataclass for programmatic permission updates, and new `SdkBeta` literal type for beta features. [[lines 696-818](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/api/agent-sdk/python.md?plain=1#L696-L818)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python#permission-callback-types)]
* Added `StreamEvent` message type for partial updates during streaming (requires `include_partial_messages=True`). [[lines 947-968](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/api/agent-sdk/python.md?plain=1#L947-L968)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python#streamevent)]
* Added comprehensive hook input/output types including new `HookInput` union type covering all hook event inputs, new hook-specific input types: `PreToolUseHookInput`, `PostToolUseHookInput`, `UserPromptSubmitHookInput`, `StopHookInput`, `SubagentStopHookInput`, `PreCompactHookInput`, and new `HookJSONOutput` types for hook return values. [[lines 1150-1327](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/api/agent-sdk/python.md?plain=1#L1150-L1327)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python#hook-types)]

#### [agents-and-tools/tool-use/tool-search-tool](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/api/agents-and-tools/tool-use/tool-search-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)]

* Extended Amazon Bedrock support - tool search now supports Claude Sonnet 4.5 (previously Opus 4.5 only). [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/api/agents-and-tools/tool-use/tool-search-tool.md?plain=1#L20)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#tool-search)]

#### [build-with-claude/context-editing](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/api/build-with-claude/context-editing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-editing)]

* Minor terminology and formatting updates throughout the document.

#### [build-with-claude/files](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Minor terminology and formatting updates throughout the document.

#### [resources/overview](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/api/resources/overview.md) [[Source](https://platform.claude.com/docs/en/resources/overview)]

* Minor terminology and formatting updates throughout the document.

#### [resources/prompt-library/review-classifier](https://github.com/gpambrozio/ClaudeDocs/blob/6c95db3/docs-md/api/resources/prompt-library/review-classifier.md) [[Source](https://platform.claude.com/docs/en/resources/prompt-library/review-classifier)]

* Minor terminology and formatting updates throughout the document.
