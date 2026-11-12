# [Claude docs changes for November 12th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/cbf675e203b43c877047b34ae4bbc1c6bb183c2b) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/cbf675e203b43c877047b34ae4bbc1c6bb183c2b)]

## Executive Summary
- Self-hosted Claude Managed Agents launched: you can now run the whole Managed Agents service (API, agent loop, storage, sandboxes) on your own infrastructure, with a new 10-page documentation section covering quickstart, Kubernetes, configuration, upgrades and more.
- The preserved thinking guide was split into focused pages (prefix checks, changing tools or instructions, fixing "bound to a different conversation" errors), and Fable 5.2 / Mythos 5.2 now return a 400 error when the prefix check fails.
- New `disableRemotePreviewScripts` managed setting for the desktop app lets admins stop scripts in HTML previews for SSH and WSL sessions without disabling external browsing.
- The `/claude-api` skill gained a `latency-optimize` workflow, and the mods test kit documents a much larger set of `expect` assertions.

## New Claude Code versions

No new Claude Code versions were added today.

-----

## Claude Code changes

### Changed documents

#### [chrome](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/chrome.md) [[Source](https://code.claude.com/docs/en/chrome)]

* Plan mode permission prompt description no longer lists running a shortcut. [[line 127](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/chrome.md?plain=1#L127)] [[Source](https://code.claude.com/docs/en/chrome#browser-tools-in-plan-mode)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/claude-api` gained a `latency-optimize` subcommand. [[line 64](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/commands.md?plain=1#L64)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* New `disableRemotePreviewScripts` managed setting turns off only scripts in HTML previews for SSH and WSL sessions, without blocking external browsing (requires Desktop v5.1231.0+). Earlier versions ignore it; a note explains the `disableBrowserExternalNavigation` fallback. [[lines 147-153](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/desktop.md?plain=1#L147-L153)] [[Source](https://code.claude.com/docs/en/desktop#turn-off-scripts-in-ssh-and-wsl-previews-for-your-organization)]
* New section on checking a computer for scripts that still run, using the notice text above the preview. [[lines 167-170](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/desktop.md?plain=1#L167-L170)] [[Source](https://code.claude.com/docs/en/desktop#check-a-computer-for-scripts-that-still-run)]
* Managed settings table and MDM precedence text now list `disableRemotePreviewScripts` with per-key minimum Desktop versions. [[lines 2044-2057](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/desktop.md?plain=1#L2044-L2057)] [[Source](https://code.claude.com/docs/en/desktop#managed-settings)]
* Guidance on stopping users from signing in with their own API key or Console account: also deploy `forceLoginOrgUUID` in the Desktop policy, with cautions for Console organizations and the Enterprise Admin Console. [[lines 2122-2129](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/desktop.md?plain=1#L2122-L2129)] [[Source](https://code.claude.com/docs/en/desktop#restrict-sign-in-to-your-organization)]

#### [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/desktop-changelog.md) [[Source](https://code.claude.com/docs/en/desktop-changelog)]

* Mirrors the same `disableRemotePreviewScripts`, script-check, and `forceLoginOrgUUID` changes as the desktop page. [[line 147](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/desktop-changelog.md?plain=1#L147)] [[Source](https://code.claude.com/docs/en/desktop-changelog#turn-off-scripts-in-ssh-and-wsl-previews-for-your-organization)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* New note: if a reload interrupts Claude in plan mode, plan mode turns off and Claude doesn't continue on its own; select **Plan** to keep planning. [[line 398](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/ide-integrations.md?plain=1#L398)] [[Source](https://code.claude.com/docs/en/ide-integrations#interrupted-steps-after-a-reload)]
* New `claude-vscode.toggleDictation` shortcut (`Cmd/Ctrl+D`) for voice dictation. [[line 652](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/ide-integrations.md?plain=1#L652)] [[Source](https://code.claude.com/docs/en/ide-integrations#vs-code-commands-and-shortcuts)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* "Fix a mistyped model name" section moved earlier in the page, and the intro now points to the "did you mean" warning. [[lines 167-206](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/model-config.md?plain=1#L167-L206)] [[Source](https://code.claude.com/docs/en/model-config#setting-your-model)]

#### [plugins/mods/overview](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/plugins/mods/overview.md) [[Source](https://code.claude.com/docs/en/plugins/mods/overview)]

* The built-in mods table is now partial; for others, open the plugin's details in `/plugin` to read what it does or disable it. [[lines 217-232](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/plugins/mods/overview.md?plain=1#L217-L232)] [[Source](https://code.claude.com/docs/en/plugins/mods/overview#mods-built-into-claude-code)]

#### [plugins/mods/test](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/plugins/mods/test.md) [[Source](https://code.claude.com/docs/en/plugins/mods/test)]

* New "Check a result with `expect`" section listing many more assertions (`toStrictEqual`, `toStartWith`, numeric comparisons, `toHaveLength`, `toHaveProperty`, `toBeNull`, `toBeInstanceOf`, etc.) plus `.resolves` / `.rejects`. [[lines 193-204](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/plugins/mods/test.md?plain=1#L193-L204)] [[Source](https://code.claude.com/docs/en/plugins/mods/test#check-a-result-with-expect)]

#### [self-hosted-environments-reference](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/self-hosted-environments-reference.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-reference)]

* New `CLAUDE_RUNNER_DISABLE_RENEWAL_WARNING` runner variable suppresses the session access renewal refusal message (Claude Code v2.1.319+). [[line 124](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/self-hosted-environments-reference.md?plain=1#L124)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-reference#environment-variable-only-settings)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* New managed-only `disableRemotePreviewScripts` setting, with type, default, `parentSettingsBehavior` guidance and an example. [[lines 5005-5028](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/settings-reference.md?plain=1#L5005-L5028)] [[Source](https://code.claude.com/docs/en/settings-reference#disableremotepreviewscripts)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* The `/claude-api` skill gained a `latency-optimize` workflow that finds where time goes in existing Claude API code and proposes changes (v2.1.319+). [[line 90](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/skills.md?plain=1#L90)] [[Source](https://code.claude.com/docs/en/skills#work-on-claude-api-projects)]

#### [slash-commands](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/slash-commands.md) [[Source](https://code.claude.com/docs/en/slash-commands)]

* Same `latency-optimize` addition as in skills. [[line 90](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/slash-commands.md?plain=1#L90)] [[Source](https://code.claude.com/docs/en/slash-commands#work-on-claude-api-projects)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Same plan-mode reload note and `toggleDictation` shortcut as in ide-integrations. [[lines 398-652](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/claude-code/vs-code.md?plain=1#L398-L652)] [[Source](https://code.claude.com/docs/en/vs-code#interrupted-steps-after-a-reload)]

-----

## API changes

### New Documents

#### [build-with-claude/preserved-thinking/change-tools-or-instructions](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/build-with-claude/preserved-thinking/change-tools-or-instructions.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions)]

Split out of the preserved thinking guide. Shows how to change tools or system instructions without failing the prefix check, and how to append assistant turns exactly as returned.

#### [build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation)]

Troubleshooting page for the "The block is bound to a different conversation" 400 error, including the `drop_block` stopgap and its output-token cost.

#### [build-with-claude/preserved-thinking/prefix-checks](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/build-with-claude/preserved-thinking/prefix-checks.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks)]

Explains what the prefix check covers (system prompt, tools, earlier messages), what counts as an edit, and what to check in your integration.

#### [managed-agents/self-hosted](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/managed-agents/self-hosted.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted)]

Landing page for self-hosted Claude Managed Agents. Compares cloud sandboxes, self-hosted sandboxes, and a fully self-hosted service, and explains when to choose each. Access is by contacting your Anthropic account team.

#### [managed-agents/self-hosted-data-and-access](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/managed-agents/self-hosted-data-and-access.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-data-and-access)]

Describes where data lives and who can access it with self-hosted Managed Agents.

#### Self-hosted Managed Agents section (`managed-agents/self-hosted/`)

* [agent-identity](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/managed-agents/self-hosted/agent-identity.md): how agents authenticate and what identity they present.
* [call-the-api](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/managed-agents/self-hosted/call-the-api.md): calling your own server with the SDK and `ant` CLI.
* [configuration-reference](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/managed-agents/self-hosted/configuration-reference.md): all server configuration options.
* [configure](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/managed-agents/self-hosted/configure.md): how to configure your server.
* [console](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/managed-agents/self-hosted/console.md): using the console with your server.
* [differences](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/managed-agents/self-hosted/differences.md): where the self-hosted server differs from the hosted service.
* [inference-provider](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/managed-agents/self-hosted/inference-provider.md): choosing where model requests go (Anthropic by default, or another provider).
* [kubernetes](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/managed-agents/self-hosted/kubernetes.md): deploying on Kubernetes.
* [quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/managed-agents/self-hosted/quickstart.md): first-run walkthrough.
* [upgrade](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/managed-agents/self-hosted/upgrade.md): upgrading a running server.

### Changed documents

#### [about-claude/pricing](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* Self-hosted Managed Agents pricing is available through your Anthropic account team. [[line 441](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/about-claude/pricing.md?plain=1#L441)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing#claude-managed-agents-pricing)]

#### [api/errors](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/api/errors.md) [[Source](https://platform.claude.com/docs/en/api/errors)]

* Thinking block errors are reworded: a 400 occurs when thinking blocks don't match what the API returned, and the prefix check failure now links to the new prefix-checks page. [[lines 439-447](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/api/errors.md?plain=1#L439-L447)] [[Source](https://platform.claude.com/docs/en/api/errors#thinking-blocks-cannot-be-modified)]
* Two recovery options for a conversation whose history already holds an edit: use `drop_block` on every later request, or strip the named block and all later thinking blocks. [[lines 543-549](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/api/errors.md?plain=1#L543-L549)] [[Source](https://platform.claude.com/docs/en/api/errors#thinking-block-bound-to-a-different-conversation)]
* Removed the paragraph about 429 acceleration limits. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/api/errors.md?plain=1#L38)] [[Source](https://platform.claude.com/docs/en/api/errors#http-errors)]

#### [build-with-claude/effort](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/build-with-claude/effort.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

* Expanded per-model effort guidance for Fable 5.2, Opus 5.5 and Sonnet 5.5: where to start, run your own effort sweep, and set a large `max_tokens`. [[lines 267-310](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/build-with-claude/effort.md?plain=1#L267-L310)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort#effort-levels)]
* Changing top-level effort between requests can invalidate all or part of the prompt cache (previously stated as fully invalidating). [[line 432](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/build-with-claude/effort.md?plain=1#L432)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort#change-effort-mid-conversation)]

#### [build-with-claude/mid-conversation-system-messages](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/build-with-claude/mid-conversation-system-messages.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages)]

* Microsoft Foundry is now listed as stable, and the beta header guidance for mid-conversation tool changes was restructured around `inline-tools-2026-09-15`. [[lines 33-49](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/build-with-claude/mid-conversation-system-messages.md?plain=1#L33-L49)] [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#keep-at-least-one-non-deferred-tool-in-tools-so-a-tool-defined)]

#### [build-with-claude/overview](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/build-with-claude/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

* Added self-hosted Claude Managed Agents to the capabilities table. [[line 121](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/build-with-claude/overview.md?plain=1#L121)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview#managed-agents-features)]

#### [build-with-claude/preserved-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/build-with-claude/preserved-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking)]

* Substantially shortened; the prefix-check, tool/instruction-change and error-fix content moved into three new sub-pages.

#### [build-with-claude/structured-outputs](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* Large revision with significant additions (about 400 lines changed).

#### [managed-agents/overview](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/managed-agents/overview.md) [[Source](https://platform.claude.com/docs/en/managed-agents/overview)]

* Updated to reference self-hosted Managed Agents.

#### [managed-agents/permission-policies](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/managed-agents/permission-policies.md) [[Source](https://platform.claude.com/docs/en/managed-agents/permission-policies)]

* Substantial rework of the permission policies documentation.

#### [managed-agents/self-hosted-sandboxes](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/managed-agents/self-hosted-sandboxes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

* Now cross-references the full self-hosted Managed Agents option.

#### [managed-agents/tools-web-restrictions](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/managed-agents/tools-web-restrictions.md) [[Source](https://platform.claude.com/docs/en/managed-agents/tools-web-restrictions)]

* Updated web restriction documentation.

#### [models/fable-5-2/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/models/fable-5-2/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/fable-5-2/migration-guide)]

* Prefix check section revised to match the new preserved thinking pages.

#### [models/fable-5-2/whats-new-fable-5-2](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/models/fable-5-2/whats-new-fable-5-2.md) [[Source](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2)]

* Breaking change reframed as "Failed prefix checks return a 400 error", with links to the new sub-pages and the `drop_block` stopgap moved under it. [[lines 13-57](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/models/fable-5-2/whats-new-fable-5-2.md?plain=1#L13-L57)] [[Source](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2#whats-new-fable-5-2)]
* Microsoft Foundry added to platforms that use the `inline-tools-2026-09-15` header. [[line 91](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/models/fable-5-2/whats-new-fable-5-2.md?plain=1#L91)] [[Source](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2#feature-support)]

#### [models/opus-5-5/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/models/opus-5-5/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide)]

* Migration guidance updated for prefix checks and thinking blocks.

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* November 12, 2026 entry announcing the launch of self-hosted Claude Managed Agents. [[lines 15-18](https://github.com/gpambrozio/ClaudeDocs/blob/cbf675e203b43c877047b34ae4bbc1c6bb183c2b/docs-md/api/release-notes/overview.md?plain=1#L15-L18)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#november-12-2026)]
