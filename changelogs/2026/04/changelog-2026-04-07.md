# [Claude docs changes for April 7th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/9a646ae83fa1b46993e66e12c5ae6c2eafc6a767) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/9a646ae83fa1b46993e66e12c5ae6c2eafc6a767)]

## Executive Summary
- `max` effort level is now available on Claude Sonnet 4.6 (previously restricted to Opus 4.6 only)
- Prefilling is no longer described as "deprecated" — it now explicitly returns a 400 error on Opus 4.6 and Sonnet 4.6, and Claude Sonnet 4.5 is no longer listed as a restricted model
- The `llms-full.txt` resource link has been removed from the API resources overview

-----

## API changes

### Changed documents

#### [Adaptive Thinking](https://github.com/gpambrozio/ClaudeDocs/blob/9a646ae83fa1b46993e66e12c5ae6c2eafc6a767/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* The `max` effort level is now available on Claude Sonnet 4.6 in addition to Opus 4.6 (previously stated as Opus 4.6 only). [[line 63](https://github.com/gpambrozio/ClaudeDocs/blob/9a646ae83fa1b46993e66e12c5ae6c2eafc6a767/docs-md/api/build-with-claude/adaptive-thinking.md?plain=1#L63)] [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

#### [Effort](https://github.com/gpambrozio/ClaudeDocs/blob/9a646ae83fa1b46993e66e12c5ae6c2eafc6a767/docs-md/api/build-with-claude/effort.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

* The `max` effort level is now available on Claude Sonnet 4.6 in addition to Opus 4.6 (previously stated as Opus 4.6 only). [[line 34](https://github.com/gpambrozio/ClaudeDocs/blob/9a646ae83fa1b46993e66e12c5ae6c2eafc6a767/docs-md/api/build-with-claude/effort.md?plain=1#L34)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]
* Added a bullet point for `max` effort in the Sonnet 4.6 usage guidance section. [[line 48](https://github.com/gpambrozio/ClaudeDocs/blob/9a646ae83fa1b46993e66e12c5ae6c2eafc6a767/docs-md/api/build-with-claude/effort.md?plain=1#L48)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]
* Updated guidance on when to use `max` effort to reflect its availability on Sonnet 4.6. [[line 74](https://github.com/gpambrozio/ClaudeDocs/blob/9a646ae83fa1b46993e66e12c5ae6c2eafc6a767/docs-md/api/build-with-claude/effort.md?plain=1#L74)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

#### [Increase Consistency](https://github.com/gpambrozio/ClaudeDocs/blob/9a646ae83fa1b46993e66e12c5ae6c2eafc6a767/docs-md/api/test-and-evaluate/strengthen-guardrails/increase-consistency.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency)]

* Prefilling note updated: no longer described as "deprecated". Claude Sonnet 4.5 removed from the list of models that don't support prefilling. [[line 21](https://github.com/gpambrozio/ClaudeDocs/blob/9a646ae83fa1b46993e66e12c5ae6c2eafc6a767/docs-md/api/test-and-evaluate/strengthen-guardrails/increase-consistency.md?plain=1#L21)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency)]

#### [Overview](https://github.com/gpambrozio/ClaudeDocs/blob/9a646ae83fa1b46993e66e12c5ae6c2eafc6a767/docs-md/api/resources/overview.md) [[Source](https://platform.claude.com/docs/en/resources/overview)]

* The `llms-full.txt` link (complete LLM-optimized documentation) has been removed from the resources overview. [[line 51](https://github.com/gpambrozio/ClaudeDocs/blob/9a646ae83fa1b46993e66e12c5ae6c2eafc6a767/docs-md/api/resources/overview.md?plain=1#L51)] [[Source](https://platform.claude.com/docs/en/resources/overview)]

#### [Reduce Prompt Leak](https://github.com/gpambrozio/ClaudeDocs/blob/9a646ae83fa1b46993e66e12c5ae6c2eafc6a767/docs-md/api/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak)]

* Prefilling note updated: no longer described as "deprecated". Claude Sonnet 4.5 removed from the list of models that don't support prefilling. [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/9a646ae83fa1b46993e66e12c5ae6c2eafc6a767/docs-md/api/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak.md?plain=1#L20)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak)]

#### [Working with Messages](https://github.com/gpambrozio/ClaudeDocs/blob/9a646ae83fa1b46993e66e12c5ae6c2eafc6a767/docs-md/api/build-with-claude/working-with-messages.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)]

* Prefilling clarified: no longer described as "deprecated" — now explicitly stated to return a 400 error on Opus 4.6 and Sonnet 4.6. Claude Sonnet 4.5 removed from the list of affected models. A link to the migration guide was added. [[line 145](https://github.com/gpambrozio/ClaudeDocs/blob/9a646ae83fa1b46993e66e12c5ae6c2eafc6a767/docs-md/api/build-with-claude/working-with-messages.md?plain=1#L145)] [[Source](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)]
