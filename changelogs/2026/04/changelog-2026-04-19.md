# [Claude docs changes for April 19th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/dbbd6e4) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/dbbd6e4)]

## Executive Summary
- New `deniedDomains` sandbox network config allows blocking specific domains even when a wildcard `allowedDomains` rule would otherwise permit them
- Significant keyboard shortcut additions: Shift+arrow selection extension in fullscreen mode, Ctrl+A/E for line navigation, Ctrl+W for word deletion, and Ctrl+P/N for history navigation
- Exec wrappers (`watch`, `setsid`, `ionice`, `flock`) always prompt and cannot be auto-approved by prefix rules — a security clarification for permission configurations
- The `/loop` command can now be stopped mid-wait by pressing `Esc`

-----

## Claude Code changes

### Changed documents

#### [Agent SDK - TypeScript](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* New `deniedDomains` field added to `SandboxNetworkConfig` type — takes precedence over `allowedDomains` to block specific domains. [[line 2807](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L2807)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sandboxnetworkconfig)]

#### [Commands](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/compact` description updated to clarify it summarizes the conversation to free context, with a link to how compaction handles rules, skills, and memory files. [[line 21](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/commands.md?plain=1#L21)] [[Source](https://code.claude.com/docs/en/commands)]
* `/less-permission-prompts` renamed to `/fewer-permission-prompts`. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/commands.md?plain=1#L36)] [[Source](https://code.claude.com/docs/en/commands)]

#### [Fullscreen](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* New keyboard selection extension: hold `Shift` and press arrow keys to extend a text selection; `Shift+↑`/`Shift+↓` scroll the viewport when the selection reaches the edge; `Shift+Home`/`Shift+End` extend to line start/end. [[line 45](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/fullscreen.md?plain=1#L45)] [[Source](https://code.claude.com/docs/en/fullscreen#use-the-mouse)]

#### [Interactive Mode](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* `Up/Down` arrows now also support `Ctrl+P`/`Ctrl+N` for history navigation; in multiline input the cursor moves within the prompt first before cycling history. [[line 26](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/interactive-mode.md?plain=1#L26)] [[Source](https://code.claude.com/docs/en/interactive-mode#general-controls)]
* New `Ctrl+A` / `Ctrl+E` shortcuts to move cursor to start/end of current line in multiline input. [[lines 37-38](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/interactive-mode.md?plain=1#L37-L38)] [[Source](https://code.claude.com/docs/en/interactive-mode#text-editing)]
* New `Ctrl+W` shortcut to delete the previous word (also `Ctrl+Backspace` on Windows); deleted text is pasteable with `Ctrl+Y`. [[line 41](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/interactive-mode.md?plain=1#L41)] [[Source](https://code.claude.com/docs/en/interactive-mode#text-editing)]
* `Ctrl+U` clarified: deletes from cursor to line start (not the entire buffer), and `Cmd+Backspace` on macOS maps to it in common terminal emulators. [[line 40](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/interactive-mode.md?plain=1#L40)] [[Source](https://code.claude.com/docs/en/interactive-mode#text-editing)]

#### [Keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* Six new keybinding actions documented for extending text selections: `selection:extendLeft`, `selection:extendRight`, `selection:extendUp`, `selection:extendDown`, `selection:extendLineStart`, `selection:extendLineEnd`. [[lines 324-329](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/keybindings.md?plain=1#L324-L329)] [[Source](https://code.claude.com/docs/en/keybindings#scroll-actions)]

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Clarification that exec wrappers such as `watch`, `setsid`, `ionice`, and `flock` always prompt and cannot be auto-approved by a prefix rule like `Bash(watch *)`; the same applies to `find -exec` or `find -delete`. [[line 118](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/permissions.md?plain=1#L118)] [[Source](https://code.claude.com/docs/en/permissions#process-wrappers)]
* Network restrictions section updated to mention `deniedDomains` alongside `allowedDomains`. [[line 249](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/permissions.md?plain=1#L249)] [[Source](https://code.claude.com/docs/en/permissions#how-permissions-interact-with-sandboxing)]

#### [Quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/quickstart.md) [[Source](https://code.claude.com/docs/en/quickstart)]

* Desktop install section now shows a `curl -fsSL https://claude.ai/install.sh | bash` command for macOS/Linux instead of linking to the desktop app download. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/quickstart.md?plain=1#L9)] [[Source](https://code.claude.com/docs/en/quickstart)]

#### [Remote Control](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Remote sessions now support `@` autocomplete for file paths from the local project. [[line 8](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/remote-control.md?plain=1#L8)] [[Source](https://code.claude.com/docs/en/remote-control)]
* `/extra-usage` added to the list of commands that work from mobile and web (not just local CLI). [[line 167](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/remote-control.md?plain=1#L167)] [[Source](https://code.claude.com/docs/en/remote-control#limitations)]

#### [Sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Added guidance on using `deniedDomains` to block specific domains that a broader `allowedDomains` wildcard would otherwise permit. [[line 218](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/sandboxing.md?plain=1#L218)] [[Source](https://code.claude.com/docs/en/sandboxing#how-sandboxing-relates-to-permissions)]

#### [Scheduled Tasks](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

* New "Stop a loop" section: pressing `Esc` while a `/loop` is waiting clears the pending wakeup and stops the loop. Manually scheduled tasks are unaffected by `Esc`. [[lines 104-107](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/scheduled-tasks.md?plain=1#L104-L107)] [[Source](https://code.claude.com/docs/en/scheduled-tasks#stop-a-loop)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New `network.deniedDomains` setting documented: array of domains to block for outbound traffic, supporting wildcards, taking precedence over `allowedDomains`, and merged from all settings sources regardless of `allowManagedDomainsOnly`. [[line 281](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/settings.md?plain=1#L281)] [[Source](https://code.claude.com/docs/en/settings#sandbox-settings)]

#### [Ultrareview](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/ultrareview.md) [[Source](https://code.claude.com/docs/en/ultrareview)]

* Confirmation dialog now shows file and line count when reviewing a branch. [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/dbbd6e4/docs-md/claude-code/ultrareview.md?plain=1#L33)] [[Source](https://code.claude.com/docs/en/ultrareview#run-ultrareview-from-the-cli)]

-----

## API changes

### Changed documents

No significant changes today.
