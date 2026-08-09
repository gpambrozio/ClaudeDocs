# [Claude docs changes for August 9th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/cd9e54d72286f1970a5dd376d321cffcab1da786) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/cd9e54d72286f1970a5dd376d321cffcab1da786)]

## Executive Summary
- New `promptSuggestionEnabled` settings.json option lets you disable prompt suggestions without an environment variable, and can be paired with `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION` in managed settings to enforce it organization-wide.
- The Claude Platform on AWS doc dropped its enterprise sales/pricing promo banner.

-----

## Claude Code changes

### Changed documents

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/cd9e54d72286f1970a5dd376d321cffcab1da786/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION` now documented as taking precedence over the new `promptSuggestionEnabled` setting. [[line 236](https://github.com/gpambrozio/ClaudeDocs/blob/cd9e54d72286f1970a5dd376d321cffcab1da786/docs-md/claude-code/env-vars.md?plain=1#L236)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/cd9e54d72286f1970a5dd376d321cffcab1da786/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Documents three ways to disable prompt suggestions: the `/config` toggle, the new `promptSuggestionEnabled` setting, or the `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION` env var (which takes precedence). [[lines 312-322](https://github.com/gpambrozio/ClaudeDocs/blob/cd9e54d72286f1970a5dd376d321cffcab1da786/docs-md/claude-code/interactive-mode.md?plain=1#L312-L322)] [[Source](https://code.claude.com/docs/en/interactive-mode#prompt-suggestions)]
* Adds guidance for disabling prompt suggestions org-wide via managed settings, setting both `promptSuggestionEnabled` and the managed `env` key so users can't override it. [[line 322](https://github.com/gpambrozio/ClaudeDocs/blob/cd9e54d72286f1970a5dd376d321cffcab1da786/docs-md/claude-code/interactive-mode.md?plain=1#L322)] [[Source](https://code.claude.com/docs/en/interactive-mode#prompt-suggestions)]

#### [claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/cd9e54d72286f1970a5dd376d321cffcab1da786/docs-md/claude-code/claude-platform-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

* Removed the enterprise sales/pricing promo banner at the top of the page. [[lines 1-5](https://github.com/gpambrozio/ClaudeDocs/blob/cd9e54d72286f1970a5dd376d321cffcab1da786/docs-md/claude-code/claude-platform-on-aws.md?plain=1#L1-L5)] [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/cd9e54d72286f1970a5dd376d321cffcab1da786/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added new `promptSuggestionEnabled` setting (default `true`) to toggle prompt suggestions; the `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION` env var takes precedence when both are set. [[line 285](https://github.com/gpambrozio/ClaudeDocs/blob/cd9e54d72286f1970a5dd376d321cffcab1da786/docs-md/claude-code/settings.md?plain=1#L285)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

-----

## API changes

No significant changes today.
