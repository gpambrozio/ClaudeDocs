# [Claude docs changes for November 22nd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/b5b6d5fa92ad93e0e358541fdfaac729fd514d17) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/b5b6d5fa92ad93e0e358541fdfaac729fd514d17)]

## Executive Summary
- Organization webhooks gain two encryption key (CMEK) events, `external_key.failed` and `external_key.recovered`, with guidance on responding, timing, and missed events.
- Organization webhooks now stay available for organizations whose Default Workspace uses a customer-managed key, with documented failure behavior while the key is unusable.
- The Compliance API docs now explain which content endpoints cover chats, local sessions, and remote sessions, and note that standalone Console organizations can query only the Activity Feed.
- Claude Mythos 5 is added to the refusals and fallback docs, with a new tip on `<thinking>` tags triggering `reasoning_extraction` refusals.

## New Claude Code versions

No new Claude Code versions today.

-----

## Claude Code changes

No Claude Code documentation changes today.

-----

## API changes

### Changed documents

#### [cmek-coverage-claude-platform](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/manage-claude/cmek-coverage-claude-platform.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-platform)]

* Organization webhooks (endpoint names, descriptions, signing secrets) are now listed as data encrypted with your key. [[line 17](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/manage-claude/cmek-coverage-claude-platform.md?plain=1#L17)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-platform#encrypted-with-your-key)]
* Organization webhooks are no longer turned off for keyed Default Workspaces; they stay available, but endpoints depending on the key lose events while the key is unusable. [[line 32](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/manage-claude/cmek-coverage-claude-platform.md?plain=1#L32)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-platform#turned-off-or-changed)]

#### [cmek-key-lifecycle](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/manage-claude/cmek-key-lifecycle.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle)]

* Clarified that Anthropic can no longer decrypt data within about an hour of disabling the key. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/manage-claude/cmek-key-lifecycle.md?plain=1#L19)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle#what-each-action-does)]
* Organizations with webhooks can receive events when a key is disabled or restored. [[line 29](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/manage-claude/cmek-key-lifecycle.md?plain=1#L29)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle#what-disabling-does-and-what-comes-back)]

#### [compliance-api](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/manage-claude/compliance-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-api)]

* New table describing what chat/file/project, local session, and remote session content endpoints return. [[line 58](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/manage-claude/compliance-api.md?plain=1#L58)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-api#how-the-compliance-api-works)]
* Standalone Claude Console organizations use Admin API keys and can query the Activity Feed only.

#### [compliance-errors](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/manage-claude/compliance-errors.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-errors)]

* Standalone Console organizations cannot create a Compliance Access Key, so scope fixes don't apply to them. [[line 197](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/manage-claude/compliance-errors.md?plain=1#L197)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-errors#403-forbidden)]

#### [organization-webhooks](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/manage-claude/organization-webhooks.md) [[Source](https://platform.claude.com/docs/en/manage-claude/organization-webhooks)]

* Page reframed around general organization events; user profile events are still not delivered. [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/manage-claude/organization-webhooks.md?plain=1#L14)] [[Source](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#organization-webhooks)]
* New access rules: HIPAA-ready organizations can't use webhooks; CMEK-capable organizations have them. [[line 22](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/manage-claude/organization-webhooks.md?plain=1#L22)] [[Source](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#before-you-start)]
* New "Encryption key events" section: `external_key.failed` and `external_key.recovered`, payload format, how to respond by validating the key and checking each workspace, expected arrival times, and cases where events may not arrive. [[lines 87-164](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/manage-claude/organization-webhooks.md?plain=1#L87-L164)] [[Source](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#encryption-key-events)]
* New "Catch up on missed events" section covering regular reconciliation of profiles and keys. [[line 219](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/manage-claude/organization-webhooks.md?plain=1#L219)] [[Source](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#catch-up-on-missed-events)]
* Endpoints can be managed in the Claude Console (Organization tab of Webhooks) by admins. [[line 493](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/manage-claude/organization-webhooks.md?plain=1#L493)] [[Source](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#manage-endpoints)]
* New section on what happens when the Default Workspace uses an encryption key: which values are encrypted and which requests fail while the key is unusable. [[line 496](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/manage-claude/organization-webhooks.md?plain=1#L496)] [[Source](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#if-your-default-workspace-uses-an-encryption-key)]
* Removed the 400 error for keyed Default Workspaces. [[line 526](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/manage-claude/organization-webhooks.md?plain=1#L526)] [[Source](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#errors)]

#### [overview](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Release note announcing the `external_key.failed` and `external_key.recovered` organization webhook events (beta). [[line 22](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/release-notes/overview.md?plain=1#L22)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#november-16-2026)]

#### [refusals-and-fallback](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/build-with-claude/refusals-and-fallback.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)]

* Claude Mythos 5 (and Mythos 5.1/5.2) listed among models that can return `reasoning_extraction` refusals, and in the classifier refusals availability table. [[line 227](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/build-with-claude/refusals-and-fallback.md?plain=1#L227)] [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#keep-reasoning-in-thinking-blocks)]
* Earlier assistant turns or examples showing reasoning in tags such as `<thinking>` may also trigger this refusal. [[line 222](https://github.com/gpambrozio/ClaudeDocs/blob/b5b6d5fa92ad93e0e358541fdfaac729fd514d17/docs-md/api/build-with-claude/refusals-and-fallback.md?plain=1#L222)] [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#keep-reasoning-in-thinking-blocks)]
