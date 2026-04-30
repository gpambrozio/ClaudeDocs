# [Claude docs changes for April 30th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/de3cce4) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/de3cce4)]

## Executive Summary
- New **cache pre-warming** feature documented: use `max_tokens: 0` to load system prompts into the cache before user traffic arrives, eliminating cold-start latency
- New `allowMachLookup` field in the Python Agent SDK allows sandboxed macOS processes to access XPC/Mach services by name
- Skills clarification: the **directory name** (not a `name` frontmatter field) determines a skill's slash command
- New Windows troubleshooting section for file-lock errors during install, plus PATH guidance for fish and Nushell users

-----

## Claude Code changes

### Changed documents

#### [Agent SDK - Python](https://github.com/gpambrozio/ClaudeDocs/blob/de3cce4/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* Added new `allowMachLookup` field to `SandboxNetworkConfig`: macOS-only setting that allows sandboxed processes to access named XPC/Mach services, with support for a trailing wildcard. [[lines 3064-3077](https://github.com/gpambrozio/ClaudeDocs/blob/de3cce4/docs-md/claude-code/agent-sdk/python.md?plain=1#L3064-L3077)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#sandboxnetworkconfig)]

#### [Skills](https://github.com/gpambrozio/ClaudeDocs/blob/de3cce4/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Clarified that the **directory name** (not the `name` field in YAML frontmatter) becomes the slash command for a skill. The `name:` field has been removed from the example `SKILL.md`. [[line 41](https://github.com/gpambrozio/ClaudeDocs/blob/de3cce4/docs-md/claude-code/skills.md?plain=1#L41)] [[Source](https://code.claude.com/docs/en/skills#create-your-first-skill)]

#### [Troubleshoot installation](https://github.com/gpambrozio/ClaudeDocs/blob/de3cce4/docs-md/claude-code/troubleshoot-install.md) [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

* Added new troubleshooting entry and resolution section for the Windows error `The process cannot access the file ... because it is being used by another process`, which occurs when antivirus or a prior installer run locks files in the downloads folder. [[lines 27, 424-432](https://github.com/gpambrozio/ClaudeDocs/blob/de3cce4/docs-md/claude-code/troubleshoot-install.md?plain=1#L424-L432)]
* Added guidance for fish and Nushell users to add `~/.local/bin` to their PATH using their shell's own configuration syntax. [[line 106](https://github.com/gpambrozio/ClaudeDocs/blob/de3cce4/docs-md/claude-code/troubleshoot-install.md?plain=1#L106)] [[Source](https://code.claude.com/docs/en/troubleshoot-install#verify-your-path)]

#### [Ultrareview](https://github.com/gpambrozio/ClaudeDocs/blob/de3cce4/docs-md/claude-code/ultrareview.md) [[Source](https://code.claude.com/docs/en/ultrareview)]

* Added a note pointing users to the Code Review integration for GitHub PRs, which posts inline PR comments without requiring a CLI step. [[line 78](https://github.com/gpambrozio/ClaudeDocs/blob/de3cce4/docs-md/claude-code/ultrareview.md?plain=1#L78)] [[Source](https://code.claude.com/docs/en/ultrareview#run-ultrareview-non-interactively)]

-----

## API changes

### Changed documents

#### [Batch processing](https://github.com/gpambrozio/ClaudeDocs/blob/de3cce4/docs-md/api/build-with-claude/batch-processing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]

* Added constraint that each batched request must have `max_tokens` of at least `1`; `max_tokens: 0` (cache pre-warming) is not supported inside batches because a cache entry written during batch processing would likely expire before the follow-up request runs. [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/de3cce4/docs-md/api/build-with-claude/batch-processing.md?plain=1#L47)] [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]

#### [Extended thinking](https://github.com/gpambrozio/ClaudeDocs/blob/de3cce4/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Added note that extended thinking cannot be combined with `max_tokens: 0` (cache pre-warming) because `budget_tokens` must be less than `max_tokens`. [[line 87](https://github.com/gpambrozio/ClaudeDocs/blob/de3cce4/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L87)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

#### [Prompt caching](https://github.com/gpambrozio/ClaudeDocs/blob/de3cce4/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Added a major new **"Pre-warming the cache"** section documenting how to use `max_tokens: 0` to load system prompts or tool definitions into the cache before user traffic arrives, eliminating cold-start TTFT penalties. Includes code examples, typical usage patterns, and a discussion of limitations (incompatible with streaming, extended thinking, structured outputs, and forced tool choice). [[lines 501-641](https://github.com/gpambrozio/ClaudeDocs/blob/de3cce4/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L501-L641)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]
* Added guidance on replacing the old `max_tokens: 1` warm-up workaround with the new `max_tokens: 0` approach, which produces no output tokens and bills nothing for output. [[line 633](https://github.com/gpambrozio/ClaudeDocs/blob/de3cce4/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L633)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]
