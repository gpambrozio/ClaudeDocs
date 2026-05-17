# [Claude docs changes for May 17th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/e6e99ff5ba4384e5e4ec21a31665e8865be9e634) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/e6e99ff5ba4384e5e4ec21a31665e8865be9e634)]

## Executive Summary
- Microsoft Foundry setup guide now includes a step-by-step "Run Claude Code" section, clarifying that Foundry has no interactive setup wizard (unlike Bedrock/Vertex AI)
- Effort level settings clarified: `effortLevel` in settings files accepts `low`, `medium`, `high`, or `xhigh`; `max` is session-only and cannot be set in config
- Skills substitution behavior documented: command placeholders are expanded once and output is not re-scanned for nested placeholders

-----

## Claude Code changes

### Changed documents

#### [claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/e6e99ff5ba4384e5e4ec21a31665e8865be9e634/docs-md/claude-code/claude-platform-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

* Removed the enterprise sales/pricing promotional banner from the top of the page.

#### [microsoft-foundry](https://github.com/gpambrozio/ClaudeDocs/blob/e6e99ff5ba4384e5e4ec21a31665e8865be9e634/docs-md/claude-code/microsoft-foundry.md) [[Source](https://code.claude.com/docs/en/microsoft-foundry)]

* Added a new "5. Run Claude Code" section explaining how to start Claude Code after configuring environment variables, and noting that Foundry has no interactive setup wizard — environment variables are the only configuration path, unlike Bedrock and Vertex AI. [[lines 96-104](https://github.com/gpambrozio/ClaudeDocs/blob/e6e99ff5ba4384e5e4ec21a31665e8865be9e634/docs-md/claude-code/microsoft-foundry.md?plain=1#L96-L104)] [[Source](https://code.claude.com/docs/en/microsoft-foundry#5-run-claude-code)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/e6e99ff5ba4384e5e4ec21a31665e8865be9e634/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Clarified that the `effortLevel` settings file option accepts `low`, `medium`, `high`, or `xhigh`; the `max` level is session-only and is not accepted in settings files. [[line 192](https://github.com/gpambrozio/ClaudeDocs/blob/e6e99ff5ba4384e5e4ec21a31665e8865be9e634/docs-md/claude-code/model-config.md?plain=1#L192)] [[Source](https://code.claude.com/docs/en/model-config#set-the-effort-level)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/e6e99ff5ba4384e5e4ec21a31665e8865be9e634/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Added clarification that command substitution in skill prompts runs only once — command output is inserted as plain text and is not re-scanned for further placeholders, preventing nested placeholder expansion. [[line 383](https://github.com/gpambrozio/ClaudeDocs/blob/e6e99ff5ba4384e5e4ec21a31665e8865be9e634/docs-md/claude-code/skills.md?plain=1#L383)] [[Source](https://code.claude.com/docs/en/skills#inject-dynamic-context)]
