# [Claude docs changes for October 26th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/92f66b7541eee35a14e068fbf991ec89d6e4ac0b) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/92f66b7541eee35a14e068fbf991ec89d6e4ac0b)]

## Executive Summary
- Plugin marketplaces now fetch only the git submodules that hold plugin files (v2.1.295+), avoiding clone timeouts. New docs explain the rules and how to structure your repo.
- The mods admin guide lists which hooks from a user's mod are skipped by the built-in guard in managed environments. `/plugin` shows a note about them (v2.1.299+).
- Desktop docs add a guide to verifying a remote machine's SSH host key, plus a troubleshooting section for host key verification failures.
- Fast mode and standard speed keep separate prompt caches. The prompt caching docs were rewritten to match.
- `UserPromptSubmit` hooks that block or stop a message now have documented effects on SDK results. Async `SessionStart` hooks no longer re-add identical output on every resume.

## New Claude Code versions

No new versions today.

-----

## Claude Code changes

### New Documents

None.

### Changed documents

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* When a `UserPromptSubmit` hook blocks a message that starts its own turn, or stops it with `continue: false`, you still get a success result with `num_turns: 0` and the block or stop message as `result`. [[line 1829](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1829)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#user_message_uuid)]
* A message sent mid-turn that a `UserPromptSubmit` hook blocks at pickup is dropped and produces no result. Set a timeout when waiting on such messages. [[lines 1837-1839](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1837-L1839)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#user_message_uuids)]

#### [claude-apps-gateway-spend-limits](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/claude-apps-gateway-spend-limits.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-spend-limits)]

* Claude Code now requests dollar spend amounts even when `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` is set. Before v2.1.295 it skipped the request, so `/usage` and the status line were percentage-only. [[line 97](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/claude-apps-gateway-spend-limits.md?plain=1#L97)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-spend-limits#usage-warnings-in-claude-code)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* New section "Check a remote machine's host key". It explains how to find which machine a fingerprint belongs to, get its real fingerprint (for example with `ssh-keygen -lf`), and compare before trusting. [[lines 993-1014](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/desktop.md?plain=1#L993-L1014)] [[Source](https://code.claude.com/docs/en/desktop#check-a-remote-machines-host-key)]
* New troubleshooting section "SSH host key verification failed", covering the error messages Desktop shows when it refuses a host key. [[line 2156](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/desktop.md?plain=1#L2156)] [[Source](https://code.claude.com/docs/en/desktop#ssh-host-key-verification-failed)]

#### [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/desktop-changelog.md) [[Source](https://code.claude.com/docs/en/desktop-changelog)]

* Same additions as `desktop`: the host key check guide and the SSH host key verification troubleshooting section. [[line 993](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/desktop-changelog.md?plain=1#L993)] [[Source](https://code.claude.com/docs/en/desktop-changelog#check-a-remote-machines-host-key)]

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* The cost note now says fast and standard speed keep separate caches, so each later switch reads part or all of the conversation uncached again. It no longer says the cost applies only once. [[line 79](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/fast-mode.md?plain=1#L79)] [[Source](https://code.claude.com/docs/en/fast-mode#understand-the-cost-tradeoff)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* An async `SessionStart` hook runs every time the event fires, but its output is skipped when it matches what Claude last received. It is redelivered when it changes or after compaction or `/clear`. Before v2.1.295 it was re-added on every resume. [[lines 4085](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/hooks.md?plain=1#L4085), [4153](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/hooks.md?plain=1#L4153)]

#### [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* New section "Keep unused submodules out of the clone" (v2.1.295+). Plugin placement decides which submodules are fetched, and root plugins should write out submodule paths explicitly, such as `${CLAUDE_PLUGIN_ROOT}/vendor/tool/run.sh`. [[lines 147-159](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/plugin-marketplaces.md?plain=1#L147-L159)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#keep-unused-submodules-out-of-the-clone)]

#### [plugins/create-marketplace](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/plugins/create-marketplace.md) [[Source](https://code.claude.com/docs/en/plugins/create-marketplace)]

* Adds the same "Keep unused submodules out of the clone" guidance.

#### [plugins/marketplace-reference](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/plugins/marketplace-reference.md) [[Source](https://code.claude.com/docs/en/plugins/marketplace-reference)]

* New section "Git submodules in the marketplace repository". It gives the exact rules for when submodules are fetched for subdirectory plugins and root plugins, the cases where all are fetched, and the `--sparse`/`sparsePaths` behavior. [[lines 171-200](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/plugins/marketplace-reference.md?plain=1#L171-L200)] [[Source](https://code.claude.com/docs/en/plugins/marketplace-reference#git-submodules-in-the-marketplace-repository)]

#### [plugins/mods/admin](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/plugins/mods/admin.md) [[Source](https://code.claude.com/docs/en/plugins/mods/admin)]

* New section "Know which hooks of a user's mod don't run". It has a table of events the built-in guard skips (`classic.<Event>`, `prompt.*`, `skill.prompt`, `attribution.text`, `session.compact`, `settings.read`, some `session.append` doors). `/plugin` shows a note about them (v2.1.299+). [[lines 94-130](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/plugins/mods/admin.md?plain=1#L94-L130)] [[Source](https://code.claude.com/docs/en/plugins/mods/admin#know-which-hooks-of-a-users-mod-dont-run)]
* Two ways to let those hooks run: install the mod as the organization's own, or remove `sec-default@builtin` from `prependPlugins`. [[lines 116-120](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/plugins/mods/admin.md?plain=1#L116-L120)] [[Source](https://code.claude.com/docs/en/plugins/mods/admin#know-which-hooks-of-a-users-mod-dont-run)]
* The note on `session.append` rewriting now excludes rows the guard passes over. [[line 178](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/plugins/mods/admin.md?plain=1#L178)] [[Source](https://code.claude.com/docs/en/plugins/mods/admin#review-what-a-mod-can-do)]

#### [plugins/mods/events](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/plugins/mods/events.md) [[Source](https://code.claude.com/docs/en/plugins/mods/events)]

* Notes that `classic.<Event>` hooks from a user's mod don't run where the built-in guard loads. [[line 376](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/plugins/mods/events.md?plain=1#L376)] [[Source](https://code.claude.com/docs/en/plugins/mods/events#handle-the-settings-hook-events)]

#### [plugins/troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/plugins/troubleshooting.md) [[Source](https://code.claude.com/docs/en/plugins/troubleshooting)]

* The git clone timeout entry now advises updating to v2.1.295+ if the repo has large submodules. [[line 317](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/plugins/troubleshooting.md?plain=1#L317)] [[Source](https://code.claude.com/docs/en/plugins/troubleshooting#git-clone-timed-out-after-120s)]
* New entry "A root plugin's files from a git submodule are missing after install", with the fix of writing out submodule paths in full. [[lines 1091-1098](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/plugins/troubleshooting.md?plain=1#L1091-L1098)] [[Source](https://code.claude.com/docs/en/plugins/troubleshooting#a-root-plugins-files-from-a-git-submodule-are-missing-after-install)]

#### [prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/prompt-caching.md) [[Source](https://code.claude.com/docs/en/prompt-caching)]

* The fast mode section was rewritten. Fast and standard speed keep separate caches, every toggle (including automatic fallbacks) can read uncached, and enabling fast mode on an unsupported model switches to Opus. [[lines 99-104](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/prompt-caching.md?plain=1#L99-L104)] [[Source](https://code.claude.com/docs/en/prompt-caching#turning-on-fast-mode)]
* Cache sharing is now described as depending on model, speed, and prefix. [[lines 311-318](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/prompt-caching.md?plain=1#L311-L318)] [[Source](https://code.claude.com/docs/en/prompt-caching#cache-scope)]

#### [self-hosted-environments-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/self-hosted-environments-deploy.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy)]

* The sample Dockerfile now installs `python3`, because control-plane hooks for Claude Tag sessions (including the Slack reply hook) run it. [[lines 347-352](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L347-L352)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#build-the-runner-image)]
* New troubleshooting item for Claude Tag not posting its Slack reply. It lists the checks: runner v2.1.229+, `python3` available, and hooks not disabled. [[line 824](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L824)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#troubleshooting)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* Cached `prependPlugins`, `appendPlugins`, or `enabledPlugins` values can't remove, move, or disable the built-in guard until the server confirms the payload. Plugins enabled only by a cached list count as the user's until then. [[lines 169-173](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/server-managed-settings.md?plain=1#L169-L173)] [[Source](https://code.claude.com/docs/en/server-managed-settings#fetch-and-caching-behavior)]

#### [statusline](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* Spend limit dollar fields are no longer absent when `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` is set (v2.1.295+). They are still optional. [[line 379](https://github.com/gpambrozio/ClaudeDocs/blob/92f66b7541eee35a14e068fbf991ec89d6e4ac0b/docs-md/claude-code/statusline.md?plain=1#L379)] [[Source](https://code.claude.com/docs/en/statusline#spend-limit-fields)]

-----

## API changes

No API documentation changes today.
