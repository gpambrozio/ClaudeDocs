# [Claude docs changes for November 16th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/baf6e5b48766d8f79d9a9a8f8d4eadca63b112c2) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/baf6e5b48766d8f79d9a9a8f8d4eadca63b112c2)]

## Executive Summary
- Anthropic's text watermark now applies to Claude Opus 4.6, Opus 4.5, Sonnet 4.5 and Haiku 4.5 on supported platforms, not just Sonnet 4.6.
- Claude Code now assumes a 1M token context window by default for unrecognized model IDs (since v2.1.323). Older versions assumed 200K and need `[1m]` appended to the ID.
- Docs no longer carry several "requires Claude Code v2.1.2xx or later" notes for plugin and worktree features.

## New Claude Code versions

No new Claude Code versions today.

-----

## Claude Code changes

### Changed documents

#### [llm-gateway-protocol](https://github.com/gpambrozio/ClaudeDocs/blob/baf6e5b48766d8f79d9a9a8f8d4eadca63b112c2/docs-md/claude-code/llm-gateway-protocol.md) [[Source](https://code.claude.com/docs/en/llm-gateway-protocol)]

* Clarified that the 1M token context window default applies since v2.1.323. [[line 109](https://github.com/gpambrozio/ClaudeDocs/blob/baf6e5b48766d8f79d9a9a8f8d4eadca63b112c2/docs-md/claude-code/llm-gateway-protocol.md?plain=1#L109)] [[Source](https://code.claude.com/docs/en/llm-gateway-protocol#settings-for-unrecognized-model-ids)]

#### [microsoft-foundry](https://github.com/gpambrozio/ClaudeDocs/blob/baf6e5b48766d8f79d9a9a8f8d4eadca63b112c2/docs-md/claude-code/microsoft-foundry.md) [[Source](https://code.claude.com/docs/en/microsoft-foundry)]

* Before v2.1.323 Claude Code assumed a 200K window for unmatched deployment names, so append `[1m]` to the name on those versions if the model accepts 1M. [[line 172](https://github.com/gpambrozio/ClaudeDocs/blob/baf6e5b48766d8f79d9a9a8f8d4eadca63b112c2/docs-md/claude-code/microsoft-foundry.md?plain=1#L172)] [[Source](https://code.claude.com/docs/en/microsoft-foundry#1m-token-context-window)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/baf6e5b48766d8f79d9a9a8f8d4eadca63b112c2/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Same pre-v2.1.323 note: 200K was the default for unmatched IDs, so append `[1m]` on older versions. [[line 1032](https://github.com/gpambrozio/ClaudeDocs/blob/baf6e5b48766d8f79d9a9a8f8d4eadca63b112c2/docs-md/claude-code/model-config.md?plain=1#L1032)] [[Source](https://code.claude.com/docs/en/model-config#pin-models-for-third-party-deployments)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/baf6e5b48766d8f79d9a9a8f8d4eadca63b112c2/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/status` now documented as working while Claude is responding; the historical version note was removed. [[line 144](https://github.com/gpambrozio/ClaudeDocs/blob/baf6e5b48766d8f79d9a9a8f8d4eadca63b112c2/docs-md/claude-code/commands.md?plain=1#L144)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [plugins/cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/baf6e5b48766d8f79d9a9a8f8d4eadca63b112c2/docs-md/claude-code/plugins/cli-reference.md) [[Source](https://code.claude.com/docs/en/plugins/cli-reference)]

* Removed version requirements (v2.1.229 / v2.1.233) from `--yes` flags and component-file validation. [[line 81](https://github.com/gpambrozio/ClaudeDocs/blob/baf6e5b48766d8f79d9a9a8f8d4eadca63b112c2/docs-md/claude-code/plugins/cli-reference.md?plain=1#L81)] [[Source](https://code.claude.com/docs/en/plugins/cli-reference#plugin-install)]

-----

## API changes

### Changed documents

#### [build-with-claude/text-watermark](https://github.com/gpambrozio/ClaudeDocs/blob/baf6e5b48766d8f79d9a9a8f8d4eadca63b112c2/docs-md/api/build-with-claude/text-watermark.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/text-watermark)]

* The watermark section now applies to Opus 4.6, Sonnet 4.6, Opus 4.5, Sonnet 4.5 (deprecated), Haiku 4.5 and Opus 3 (retired, access on request), instead of Sonnet 4.6 only. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/baf6e5b48766d8f79d9a9a8f8d4eadca63b112c2/docs-md/api/build-with-claude/text-watermark.md?plain=1#L15)] [[Source](https://platform.claude.com/docs/en/build-with-claude/text-watermark#sampling-settings)]

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/baf6e5b48766d8f79d9a9a8f8d4eadca63b112c2/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* New November 16, 2026 entry: text from Opus 4.6, Opus 4.5, Sonnet 4.5 and Haiku 4.5 carries the text watermark on supported platforms. It also covers how requests setting non-default `temperature`, `top_p` or `top_k` are affected. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/baf6e5b48766d8f79d9a9a8f8d4eadca63b112c2/docs-md/api/release-notes/overview.md?plain=1#L15)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#november-16-2026)]
