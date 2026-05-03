# [Claude docs changes for May 3rd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab)]

## Executive Summary
- Three new dedicated documentation pages added: Sessions (session lifecycle, resume, branching), Worktrees (parallel Claude sessions with git worktrees), and Deep Links (`claude-cli://` URL scheme)
- Plan mode enhanced with a new `Ctrl+G` shortcut to edit plans in your editor before Claude proceeds, plus the ability to set plan mode as the default in settings
- Extended thinking controls fully documented in model-config: keyboard toggle (`Option+T`/`Alt+T`), `alwaysThinkingEnabled` setting, and `MAX_THINKING_TOKENS=0` to disable
- Headless mode docs now cover piping stdin to Claude and adding Claude as a build script step, with cost tracking via `--output-format json`
- Hooks guide now documents all notification hook matcher values (`permission_prompt`, `idle_prompt`, `auth_success`, etc.)

-----

## Claude Code changes

### New Documents

#### [Deep Links](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/deep-links.md) [[Source](https://code.claude.com/docs/en/deep-links)]

Documents the `claude-cli://` custom URL scheme registered by Claude Code (v2.1.91+). Covers the `claude-cli://open` URL format with `q` (prompt), `cwd`, and `repo` parameters; security model (never auto-executes — shows a review banner first); embedding links in runbooks and shell scripts across macOS, Linux, and Windows; OS-specific registration locations; supported terminal emulators; and the `disableDeepLinkRegistration` setting.

#### [Sessions](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/sessions.md) [[Source](https://code.claude.com/docs/en/sessions)]

Comprehensive reference for CLI session management. Covers resuming sessions via `--continue`, `--resume`, `--from-pr`, and `/resume`; session picker keyboard navigation; naming sessions at startup (`-n`), mid-session (`/rename`), or automatically on plan accept; branching sessions with `/branch` or `--fork-session`; context management (`/clear`, `/compact`, `/context`); exporting sessions; and storage/cleanup details including `CLAUDE_CODE_SKIP_PROMPT_HISTORY` and `--no-session-persistence` flags.

#### [Worktrees](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/worktrees.md) [[Source](https://code.claude.com/docs/en/worktrees)]

Dedicated reference for running parallel Claude sessions using git worktrees. Covers the `--worktree <name>` / `-w` flag; base branch selection; `.worktreeinclude` for copying gitignored files (e.g. `.env`) into new worktrees; isolating subagents with `isolation: worktree`; cleanup behavior (auto-removed if no changes, prompted otherwise); and non-git VCS support via `WorktreeCreate`/`WorktreeRemove` hooks.

### Changed documents

#### [Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Removed an enterprise sales promotional call-to-action block ("Deploying Claude Code across your organization?"). [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/amazon-bedrock.md?plain=1#L9)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#prerequisites)]

#### [Best Practices](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* "Resume conversations" section condensed to a brief summary with a link to the new dedicated [Sessions](sessions.md) page. [[line 397](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/best-practices.md?plain=1#L397)] [[Source](https://code.claude.com/docs/en/best-practices#rewind-with-checkpoints)]
* "Run parallel sessions" section updated to list four options with worktrees as a first-class entry, linking to the new [Worktrees](worktrees.md) page. [[line 419](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/best-practices.md?plain=1#L419)] [[Source](https://code.claude.com/docs/en/best-practices#run-non-interactive-mode)]

#### [CLI Reference](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* The `--worktree` / `-w` flag description now links to the dedicated [Worktrees](worktrees.md) page. [[line 105](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/cli-reference.md?plain=1#L105)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [Common Workflows](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Page significantly restructured: all former top-level sections ("Fix bugs," "Refactor code," "Write tests," etc.) are now grouped under a new "Prompt recipes" `##` section. A table of contents was added at the top. [[lines 9-19](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/common-workflows.md?plain=1#L9)] [[Source](https://code.claude.com/docs/en/common-workflows)]
* The detailed "Use specialized subagents" and "Use Plan Mode for safe code analysis" sections were removed.
* The detailed "Resume previous conversations" section was removed and replaced with a short summary linking to the new [Sessions](sessions.md) page. [[line 253](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/common-workflows.md?plain=1#L253)] [[Source](https://code.claude.com/docs/en/common-workflows#create-pull-requests)]
* The detailed "Run parallel Claude Code sessions with Git worktrees" section was removed and replaced with a brief summary linking to [Worktrees](worktrees.md). [[line 398](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/common-workflows.md?plain=1#L398)] [[Source](https://code.claude.com/docs/en/common-workflows#reference-files-and-directories)]
* The "Get notified when Claude needs your attention" section (desktop notification hooks) was removed.
* The "Use Claude as a Unix-style utility" section was removed and replaced with a short "Pipe Claude into scripts" summary linking to [headless.md](headless.md). [[line 498](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/common-workflows.md?plain=1#L498)] [[Source](https://code.claude.com/docs/en/common-workflows#plan-before-editing)]

#### [Google Vertex AI](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/google-vertex-ai.md) [[Source](https://code.claude.com/docs/en/google-vertex-ai)]

* Removed an enterprise sales promotional call-to-action block. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/google-vertex-ai.md?plain=1#L9)] [[Source](https://code.claude.com/docs/en/google-vertex-ai#prerequisites)]

#### [GitHub Actions](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/github-actions.md) [[Source](https://code.claude.com/docs/en/github-actions)]

* All occurrences of "AWS Bedrock" renamed to "Amazon Bedrock" throughout the file, including section headings and the section anchor ID. [[lines 255, 270, 322, 405](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/github-actions.md?plain=1#L255)]

#### [GitLab CI/CD](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/gitlab-ci-cd.md) [[Source](https://code.claude.com/docs/en/gitlab-ci-cd)]

* All occurrences of "AWS Bedrock" renamed to "Amazon Bedrock" throughout the file, including section headings and the section anchor ID. [[lines 19, 29, 91, 99](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/gitlab-ci-cd.md?plain=1#L19)]

#### [Headless](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* New "Pipe data through Claude" section added: explains piping stdin to Claude in non-interactive mode and notes that `--output-format json` includes per-invocation cost data (`total_cost_usd`). [[line 63](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/headless.md?plain=1#L63)] [[Source](https://code.claude.com/docs/en/headless#pipe-data-through-claude)]
* New "Add Claude to a build script" section added: shows how to wrap a non-interactive Claude call in a `package.json` script, piping `git diff main` into Claude as a linter/reviewer. [[line 79](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/headless.md?plain=1#L79)] [[Source](https://code.claude.com/docs/en/headless#add-claude-to-a-build-script)]

#### [Hooks Guide](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* New reference table added for notification hook matchers, documenting all 6 matcher values: `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog`, `elicitation_complete`, and `elicitation_response`, with descriptions of when each fires. [[lines 166-178](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/hooks-guide.md?plain=1#L166)] [[Source](https://code.claude.com/docs/en/hooks-guide#get-notified-when-claude-needs-input)]

#### [How Claude Code Works](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/how-claude-code-works.md) [[Source](https://code.claude.com/docs/en/how-claude-code-works)]

* "Resume or fork sessions" section condensed: the detailed `--fork-session` code example and warning about opening the same session in multiple terminals were removed; content now briefly describes the behavior and links to [Sessions](sessions.md). [[lines 91-107](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/how-claude-code-works.md?plain=1#L91)] [[Source](https://code.claude.com/docs/en/how-claude-code-works#work-across-branches)]

#### [Microsoft Foundry](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/microsoft-foundry.md) [[Source](https://code.claude.com/docs/en/microsoft-foundry)]

* Removed an enterprise sales promotional call-to-action block. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/microsoft-foundry.md?plain=1#L9)] [[Source](https://code.claude.com/docs/en/microsoft-foundry#prerequisites)]

#### [Model Config](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* `ultrathink` promoted to its own "Use ultrathink for one-off deep reasoning" subsection, with a new note clarifying that "think", "think hard", and "think more" are NOT recognized keywords and are passed as ordinary prompt text. [[line 176](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/model-config.md?plain=1#L176)] [[Source](https://code.claude.com/docs/en/model-config#choose-an-effort-level)]
* New "Extended thinking" subsection added with a controls reference table: `Option+T` / `Alt+T` to toggle, `/config` to set `alwaysThinkingEnabled`, `MAX_THINKING_TOKENS=0` to disable, `Ctrl+O` for verbose mode, and `showThinkingSummaries` setting. Also notes that users are charged for all thinking tokens even when collapsed or redacted. [[lines 198-209](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/model-config.md?plain=1#L198)] [[Source](https://code.claude.com/docs/en/model-config#adaptive-reasoning-and-fixed-thinking-budgets)]

#### [Overview](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/overview.md) [[Source](https://code.claude.com/docs/en/overview)]

* "Create custom commands" renamed to "Create skills" in the feature list. [[line 139](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/overview.md?plain=1#L139)] [[Source](https://code.claude.com/docs/en/overview#what-you-can-do)]

#### [Permission Modes](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* New content added to "Review and approve a plan": `Ctrl+G` keyboard shortcut opens the plan in the default text editor for direct editing before Claude proceeds; `showClearContextOnPlanAccept` setting now required to show the "clear context" option; accepting a plan automatically names the session. [[lines 109-130](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/permission-modes.md?plain=1#L109)] [[Source](https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode)]
* New "Set plan mode as the default" subsection added, showing how to set `"defaultMode": "plan"` in `.claude/settings.json`. [[lines 120-130](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/permission-modes.md?plain=1#L120)] [[Source](https://code.claude.com/docs/en/permission-modes#review-and-approve-a-plan)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* `disableDeepLinkRegistration` description simplified and now links to the new [Deep Links](deep-links.md) page for details on the `claude-cli://open?q=...` format. [[line 178](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/settings.md?plain=1#L178)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [Skills](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* The "Getting started" example changed from an "explain code with diagrams" skill to a `summarize-changes` skill that diffs git changes, with updated code samples and instructions throughout. [[line 10](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/skills.md?plain=1#L10)] [[Source](https://code.claude.com/docs/en/skills)]
* New warning added under `allowed-tools`: for project-scoped skills, `allowed-tools` only takes effect after accepting the workspace trust dialog; users are advised to review project skills before trusting a repo. [[line 286](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/skills.md?plain=1#L286)] [[Source](https://code.claude.com/docs/en/skills#pre-approve-tools-for-a-skill)]
* The `codebase-visualizer` example now uses `${CLAUDE_SKILL_DIR}` substitution variable and `python3` in the `allowed-tools` entry. [[line 482](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/skills.md?plain=1#L482)] [[Source](https://code.claude.com/docs/en/skills#generate-visual-output)]
* Security fix in the bundled `visualize.py` script: added `from html import escape` and applied HTML-escaping to `data["name"]` and `node.name` to prevent XSS in generated HTML output. [[line 528](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/skills.md?plain=1#L528)] [[Source](https://code.claude.com/docs/en/skills#generate-visual-output)]

#### [Enterprise Deployment Overview](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/third-party-integrations.md) [[Source](https://code.claude.com/docs/en/third-party-integrations)]

* Removed an enterprise sales promotional call-to-action block. [[line 10](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/third-party-integrations.md?plain=1#L10)] [[Source](https://code.claude.com/docs/en/third-party-integrations)]

#### [VS Code](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* "Launch a VS Code tab from other tools" section expanded with explicit, tabbed code blocks for macOS (`open`), Linux (`xdg-open`), and Windows (`cmd.exe`/`Start-Process`), including a note that `cmd.exe`'s `start` requires an empty title argument before the URL. [[line 228](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/vs-code.md?plain=1#L228)] [[Source](https://code.claude.com/docs/en/vs-code#launch-a-vs-code-tab-from-other-tools)]
* New reference added to [Deep Links](deep-links.md) for the CLI's `claude-cli://` handler as an alternative to the VS Code `vscode://` handler. [[line 255](https://github.com/gpambrozio/ClaudeDocs/blob/fe4fc3d8d8d58010c243265b0f5b7d7b799e06ab/docs-md/claude-code/vs-code.md?plain=1#L255)] [[Source](https://code.claude.com/docs/en/vs-code#launch-a-vs-code-tab-from-other-tools)]

-----

## API changes

### Changed documents

No significant API documentation changes today.
