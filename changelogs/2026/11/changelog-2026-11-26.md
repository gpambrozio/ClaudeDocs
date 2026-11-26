# [Claude docs changes for November 26th 2026](https://github.com/gpambrozio/ClaudeDocs/tree/5185072d76f8f14344b881a0f466b15c187285a6) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/5185072d76f8f14344b881a0f466b15c187285a6)]

## Executive Summary
- The `claude-security` CLI now needs a `--provider` flag (`anthropic`, `bedrock`, `vertex` or `foundry`) for sandboxed scans, with optional `--model-base-url`.
- New guidance explains how to find your provider value from `/status`, and when to scan in a session instead.
- Windows scans now use `--no-sandbox` in place of the provider flags.
- The Claude Security plugin minimum version rose to 0.13.1.

-----

## Claude Code changes

### Changed documents

#### [claude-security](https://github.com/gpambrozio/ClaudeDocs/blob/5185072d76f8f14344b881a0f466b15c187285a6/docs-md/claude-code/claude-security.md) [[Source](https://code.claude.com/docs/en/claude-security)]

* The minimum plugin version for working commands and options is now 0.13.1 (was 0.13.0). [[line 66](https://github.com/gpambrozio/ClaudeDocs/blob/5185072d76f8f14344b881a0f466b15c187285a6/docs-md/claude-code/claude-security.md?plain=1#L66)] [[Source](https://code.claude.com/docs/en/claude-security#update-the-plugin)]
* Sandboxed CLI scans now require `--provider` with `anthropic`, `bedrock`, `vertex` or `foundry`. Each value names the provider that receives your code. [[lines 289-295](https://github.com/gpambrozio/ClaudeDocs/blob/5185072d76f8f14344b881a0f466b15c187285a6/docs-md/claude-code/claude-security.md?plain=1#L289-L295)] [[Source](https://code.claude.com/docs/en/claude-security#scan-from-your-shell)]
* New instructions for finding your provider value from the `API provider` and base URL rows in `/status`. Providers such as Amazon Bedrock (Mantle) should scan in a session. A custom base URL is passed with `--model-base-url`. If both rows are absent, ask your administrator or use `anthropic`. [[lines 297-303](https://github.com/gpambrozio/ClaudeDocs/blob/5185072d76f8f14344b881a0f466b15c187285a6/docs-md/claude-code/claude-security.md?plain=1#L297-L303)] [[Source](https://code.claude.com/docs/en/claude-security#scan-from-your-shell)]
* Security warning: with a base URL, your credential can be sent to that host. Export `ANTHROPIC_AUTH_TOKEN` or `ANTHROPIC_API_KEY` as the host issued it. [[line 305](https://github.com/gpambrozio/ClaudeDocs/blob/5185072d76f8f14344b881a0f466b15c187285a6/docs-md/claude-code/claude-security.md?plain=1#L305)] [[Source](https://code.claude.com/docs/en/claude-security#scan-from-your-shell)]
* The example commands now include `--provider <provider>` (full codebase, `--changes`, `--tui`). A new Windows example uses `--no-sandbox` in place of the provider flags. [[lines 307-312](https://github.com/gpambrozio/ClaudeDocs/blob/5185072d76f8f14344b881a0f466b15c187285a6/docs-md/claude-code/claude-security.md?plain=1#L307-L312)] [[Source](https://code.claude.com/docs/en/claude-security#scan-from-your-shell)]

-----

## API changes

No API documentation changes today.
