# [Claude docs changes for January 29th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/0dc5151f61e30efeb12b9b83d14d61507a7f31da) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/0dc5151f61e30efeb12b9b83d14d61507a7f31da)]

## New Claude Code versions

### [2.1.23](https://github.com/gpambrozio/ClaudeDocs/blob/0dc5151f61e30efeb12b9b83d14d61507a7f31da/versions/2.1.23.md)

#### New features

* Added customizable spinner verbs setting (`spinnerVerbs`)

#### Existing feature improvements

* Improved terminal rendering performance with optimized screen data layout
* Changed Bash commands to show timeout duration alongside elapsed time
* Changed merged pull requests to show a purple status indicator in the prompt footer

#### Major bug fixes

* Fixed mTLS and proxy connectivity for users behind corporate proxies or using client certificates
* Fixed per-user temp directory isolation to prevent permission conflicts on shared systems
* Fixed a race condition that could cause 400 errors when prompt caching scope was enabled
* Fixed pending async hooks not being cancelled when headless streaming sessions ended
* Fixed tab completion not updating the input field when accepting a suggestion
* Fixed ripgrep search timeouts silently returning empty results instead of reporting errors
* [IDE] Fixed model options displaying incorrect region strings for Bedrock users in headless mode

-----

## Claude Code changes

### New Documents

#### [Customize keyboard shortcuts](https://github.com/gpambrozio/ClaudeDocs/blob/0dc5151f61e30efeb12b9b83d14d61507a7f31da/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

New comprehensive documentation on customizing keyboard shortcuts in Claude Code. The document covers:

* Configuration file structure using `~/.claude/keybindings.json` with automatic change detection
* Available contexts (Global, Chat, Autocomplete, Settings, Confirmation, and many more)
* Complete reference of available actions organized by namespace (app, history, chat, autocomplete, confirmation, permission, transcript, task, theme, help, tabs, attachments, footer, message selector, diff, model picker, select, plugin, settings)
* Keystroke syntax including modifiers, uppercase letter handling, and chord sequences
* How to unbind default shortcuts by setting actions to `null`
* Reserved shortcuts (Ctrl+C, Ctrl+D) that cannot be rebound
* Terminal multiplexer conflict warnings (tmux, screen)
* Vim mode interaction behavior
* Validation system with `/doctor` command support

-----

## API changes

No significant changes to API documentation.
