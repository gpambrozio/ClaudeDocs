# [Claude docs changes for September 21st, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/1badbed8eeaa0a36b023643e50f574dfe2b04f44) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/1badbed8eeaa0a36b023643e50f574dfe2b04f44)]

## Executive Summary
- `/design`'s output is now documented as a first-class Design artifact, not a "research preview" editor; edits made in a desktop browser now save automatically, and the command now requires Claude Code v2.1.265 or later.
- The `CLAUDE_CODE_BASH_EDIT_DIFF` env var and `bashEditDiffEnabled` setting docs were clarified: the recorded diff covers any files that changed while a Bash command ran, not only files that command itself changed.
- A previously claimed VS Code fix ("some claude.ai/code sessions opening in VS Code as an empty conversation with no messages") was retracted from the 2.1.275 release notes.

-----

## Claude Code changes

### Changed documents

#### [artifacts](https://github.com/gpambrozio/ClaudeDocs/blob/1badbed8eeaa0a36b023643e50f574dfe2b04f44/docs-md/claude-code/artifacts.md) [[Source](https://code.claude.com/docs/en/artifacts)]

* The design canvas published by `/design` is now described as "a Design artifact" rather than "an artifact that runs a research preview of Claude Design's editor." [[line 260](https://github.com/gpambrozio/ClaudeDocs/blob/1badbed8eeaa0a36b023643e50f574dfe2b04f44/docs-md/claude-code/artifacts.md?plain=1#L260)] [[Source](https://code.claude.com/docs/en/artifacts#draft-a-design-canvas)]
* Editing is now described as happening in a desktop browser, with edits saving automatically; the previous behavior — saving gated behind account-level availability, otherwise view/export only — is no longer mentioned. [[line 266](https://github.com/gpambrozio/ClaudeDocs/blob/1badbed8eeaa0a36b023643e50f574dfe2b04f44/docs-md/claude-code/artifacts.md?plain=1#L266)] [[Source](https://code.claude.com/docs/en/artifacts#draft-a-design-canvas)]
* `/design`'s minimum version requirement was raised from Claude Code v2.1.234 to v2.1.265. [[line 268](https://github.com/gpambrozio/ClaudeDocs/blob/1badbed8eeaa0a36b023643e50f574dfe2b04f44/docs-md/claude-code/artifacts.md?plain=1#L268)] [[Source](https://code.claude.com/docs/en/artifacts#draft-a-design-canvas)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/1badbed8eeaa0a36b023643e50f574dfe2b04f44/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* The `/design` command's description was updated to match the artifacts.md changes: it now publishes a Design artifact, is edited in a desktop browser with auto-save, and requires Claude Code v2.1.265 or later. [[line 72](https://github.com/gpambrozio/ClaudeDocs/blob/1badbed8eeaa0a36b023643e50f574dfe2b04f44/docs-md/claude-code/commands.md?plain=1#L72)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/1badbed8eeaa0a36b023643e50f574dfe2b04f44/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `CLAUDE_CODE_BASH_EDIT_DIFF`'s description was clarified to cover "files that changed while a Bash command ran," rather than "files a Bash command changed." [[line 208](https://github.com/gpambrozio/ClaudeDocs/blob/1badbed8eeaa0a36b023643e50f574dfe2b04f44/docs-md/claude-code/env-vars.md?plain=1#L208)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/1badbed8eeaa0a36b023643e50f574dfe2b04f44/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* `bashEditDiffEnabled`'s summary in the settings table was reworded to match the `CLAUDE_CODE_BASH_EDIT_DIFF` clarification above. [[line 574](https://github.com/gpambrozio/ClaudeDocs/blob/1badbed8eeaa0a36b023643e50f574dfe2b04f44/docs-md/claude-code/settings-reference.md?plain=1#L574)] [[Source](https://code.claude.com/docs/en/settings-reference#settings-index)]
* Added a caveat that a listed file isn't always one the Bash command itself changed — a change made by another program or another Bash call during the same window can also appear in the diff. [[line 2904](https://github.com/gpambrozio/ClaudeDocs/blob/1badbed8eeaa0a36b023643e50f574dfe2b04f44/docs-md/claude-code/settings-reference.md?plain=1#L2904)] [[Source](https://code.claude.com/docs/en/settings-reference#basheditdiffenabled)]

-----

## API changes

No changes today.
