# [Claude docs changes for February 8th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/56db574) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/56db574)]

## Executive Summary
- Fast mode launched in research preview for Claude Opus 4.6, providing up to 2.5x faster output token generation at premium pricing
- New fast mode documentation added for both API and Claude Code usage
- Claude Code versions 2.1.36 and 2.1.37 released with fast mode support and bug fixes
- API documentation updated with fast mode pricing, rate limits, and usage tracking across 200+ files

## New Claude Code versions

### [2.1.36](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/versions/2.1.36.md)

#### New features

* Fast mode is now available for Opus 4.6

### [2.1.37](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/versions/2.1.37.md)

#### Major bug fixes

* Fixed an issue where /fast was not immediately available after enabling /extra-usage

-----

## Claude Code changes

### New Documents

#### [Speed up responses with fast mode](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

New documentation for fast mode in Claude Code CLI and VS Code Extension. Fast mode delivers faster Opus 4.6 responses at higher cost per token using the same model with a different API configuration. Toggle with `/fast` command. Available to subscription plan users (Pro/Max/Team/Enterprise) via extra usage only. Features include:
- Up to 2.5x higher output tokens per second
- Premium pricing starting at $30/150 MTok (with 50% discount until Feb 16, 2026)
- Automatic fallback to standard speed when rate limits are hit
- Persistent across sessions
- Compatible with 1M token extended context window

The document covers toggling fast mode, understanding cost tradeoffs, deciding when to use it (rapid iteration, live debugging vs. long autonomous tasks), requirements (extra usage enabled, admin enablement for Teams/Enterprise), and rate limit handling with automatic fallback behavior.

-----

## API changes

### New Documents

#### [Fast mode (research preview)](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/build-with-claude/fast-mode.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

Comprehensive documentation for fast mode API parameter. Fast mode provides significantly faster output token generation for Claude Opus 4.6 by setting `speed: "fast"` in API requests, delivering up to 2.5x higher output tokens per second at premium pricing. Key details include:
- Requires `anthropic-beta: fast-mode-2026-02-01` header
- Same model weights and behavior, just faster inference configuration
- Pricing: 6x standard Opus rates for prompts ≤200K tokens ($30/$150 MTok), 12x for >200K tokens ($60/$225 MTok)
- Pricing stacks with prompt caching and data residency multipliers
- Dedicated rate limits separate from standard Opus, with specific headers for tracking (`anthropic-fast-input-tokens-*`, `anthropic-fast-output-tokens-*`)
- Response `usage` object includes `speed` field indicating "fast" or "standard"
- Automatic retry behavior with SDK, fallback strategies for rate limit handling
- Not available with Batch API or Priority Tier
- Switching between fast and standard speed invalidates prompt cache

### Changed documents

#### [Choosing a model](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/about-claude/models/choosing-a-model.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)]

* Added mention of fast mode for Claude Opus 4.6 in the Speed factor section, noting it can provide up to 2.5x higher output speed at premium pricing. [[line 10](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/about-claude/models/choosing-a-model.md?plain=1#L10)] [[Source](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)]

#### [Adaptive thinking](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* Updated contact email address encoding for accessing full thinking output on Claude 4 models. [[line 105](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/build-with-claude/adaptive-thinking.md?plain=1#L105)] [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

#### [Extended thinking](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Updated contact email address encoding for requesting access to full thinking output for Claude 4 models. [[line 105](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L105)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

#### [Files](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Updated contact email address encoding for requesting higher rate limits. [[line 284](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/build-with-claude/files.md?plain=1#L284)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

#### [Pricing](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* Added comprehensive fast mode pricing section explaining 6x/12x multipliers over standard Opus rates. [[lines 69-84](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/about-claude/pricing.md?plain=1#L69-L84)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]
* Clarified that fast mode pricing stacks with prompt caching and data residency multipliers. [[lines 78-80](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/about-claude/pricing.md?plain=1#L78-L80)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]
* Noted that fast mode is not available with Batch API. [[line 83](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/about-claude/pricing.md?plain=1#L83)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

#### [Prompt caching](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Added new row to cache invalidation table showing that switching between fast and standard speed invalidates system and message caches. [[line 222](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L222)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

#### [Usage and Cost API](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/build-with-claude/usage-cost-api.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/usage-cost-api)]

* Added speed dimension to the list of available filtering and grouping options. [[line 66](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/build-with-claude/usage-cost-api.md?plain=1#L66)] [[Source](https://platform.claude.com/docs/en/build-with-claude/usage-cost-api)]
* Added new section on tracking fast mode usage with examples of grouping by speed dimension and filtering to specific speed values. [[lines 148-177](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/build-with-claude/usage-cost-api.md?plain=1#L148-L177)] [[Source](https://platform.claude.com/docs/en/build-with-claude/usage-cost-api)]

#### [Rate limits](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/api/rate-limits.md) [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

* Added new section explaining fast mode rate limits are separate from standard Opus rate limits. [[lines 164-168](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/api/rate-limits.md?plain=1#L164-L168)] [[Source](https://platform.claude.com/docs/en/api/rate-limits)]
* Noted that fast mode responses include `anthropic-fast-*` headers for tracking rate limit status. [[line 168](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/api/rate-limits.md?plain=1#L168)] [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

#### [Release notes overview](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Added February 7, 2026 release note announcing fast mode research preview launch for Opus 4.6. [[lines 9-11](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/release-notes/overview.md?plain=1#L9-L11)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

#### [Create message (Beta API)](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/api/beta/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]

* Added "fast-mode-2026-02-01" to the list of available beta headers. [[line 69](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/api/beta/messages/create.md?plain=1#L69)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]
* Added new `speed` parameter to request body accepting "standard" or "fast" values. [[lines 3444-3452](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/api/beta/messages/create.md?plain=1#L3444-L3452)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]
* Added `speed` field to the usage response object showing which inference speed mode was used. [[lines 6470-6478](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/api/beta/messages/create.md?plain=1#L6470-L6478)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]
* Updated response examples to include the `speed` field in usage object. [[lines 6576, 6658](https://github.com/gpambrozio/ClaudeDocs/blob/56db574/docs-md/api/api/beta/messages/create.md?plain=1#L6576)]

#### Additional API endpoint updates

Fast mode support (`speed` parameter and beta header) was added to API documentation across all language SDKs and endpoints, including:
- Python, TypeScript, Go, Java, and Ruby SDK documentation for beta messages endpoints
- Count tokens endpoint
- Models list and retrieve endpoints
- Skills API endpoints
- Message batches endpoints
- Files API endpoints
- Admin API endpoints (cost reports, usage reports, invites, users)
- Completions endpoint (legacy)

These updates add the "fast-mode-2026-02-01" beta header option and document the `speed` parameter where applicable across approximately 180 API reference files.
