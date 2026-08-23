# [Claude docs changes for August 23rd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72)]

## Executive Summary
- Cloud/self-hosted environment administration is now restricted to the **Owner** role across the board — the Admin role can no longer open the Cloud environments admin page, enable self-hosted environments, or manage Trusted Devices
- New `/auto-mode-setup` command has Claude Code scan your project and recent sessions to draft `autoMode.environment` entries for you, instead of hand-writing them
- New **plugins synced from claude.ai**: Cowork and cloud sessions now download the plugins enabled on your claude.ai account and load them automatically as `<name>@synced`
- New MCP OAuth protection: Claude Code now rejects sign-ins whose redirect issuer doesn't match the server's advertised OAuth metadata (RFC 9207 mix-up-attack defense), with a clear new error message
- The archive's crawler fix recovered full content for 38 previously blank "Loading"-placeholder API reference pages (Messages API, Compliance API), but 4 Compliance pages that had full content before this sync now regressed to blank placeholders

## Claude Code changes

### Changed documents

#### [admin-setup](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

* Claude Code on the web's admin surface for organization-shared environments is now scoped to **Owners** only, not Owners and admins. [[line 83](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/admin-setup.md?plain=1#L83)] [[Source](https://code.claude.com/docs/en/admin-setup)]

#### [auto-mode-config](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/auto-mode-config.md) [[Source](https://code.claude.com/docs/en/auto-mode-config)]

* New `/auto-mode-setup` command drafts `autoMode.environment` (and sometimes rule) entries by scanning your project's `CLAUDE.md`/README/config/git remotes, your existing `autoMode`/`permissions.allow` settings, and recent session command history, then writes the accepted draft to `~/.claude/settings.json`. Requires a Pro, Max, or Team plan and v2.1.228+ (v2.1.233+ on native Windows); not available on Claude Code on the web. Can be turned off via a `skillOverrides` entry. [[line 143](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/auto-mode-config.md?plain=1#L143)] [[Source](https://code.claude.com/docs/en/auto-mode-config#generate-environment-entries)]

#### [chrome](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/chrome.md) [[Source](https://code.claude.com/docs/en/chrome)]

* Documented how Claude Code handles the Chrome tab group it opens for a session: `/clear` closes the group (including open pages) unless surviving work is still running, while switching sessions or exiting only closes it if it holds nothing but empty new tabs. [[line 5](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/chrome.md?plain=1#L5)] [[Source](https://code.claude.com/docs/en/chrome)]

#### [claude-apps-gateway](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/claude-apps-gateway.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway)]

* Claude Desktop's Cowork and Code tabs (and its Chat tab, once enabled) now all route their model requests through a configured Claude apps gateway, not just CLI-style sign-ins. Turn on the Chat tab with `chatTabEnabled` in Desktop's managed configuration or the policy's `desktop` block (gateway v2.1.227+). [[lines 248, 337](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/claude-apps-gateway.md?plain=1#L248-L337)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway#deliver-policy-to-claude-desktop-sessions)]

#### [cloud-environments](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/cloud-environments.md) [[Source](https://code.claude.com/docs/en/cloud-environments)]

* Creating and managing organization-shared cloud environments is now restricted to the **Owner** role; the Admin role can no longer open the **Cloud environments** admin page. [[line 76](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/cloud-environments.md?plain=1#L76)] [[Source](https://code.claude.com/docs/en/cloud-environments#organization-shared-environments)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* New `/auto-mode-setup` command entry. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/commands.md?plain=1#L38)] [[Source](https://code.claude.com/docs/en/commands)]
* `/claude-api` gained an `upgrade` subcommand that moves a project's Anthropic SDK dependency across a major version — currently the Python `anthropic` package from 0.x to 1.x. Requires v2.1.236+. [[line 48](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/commands.md?plain=1#L48)] [[Source](https://code.claude.com/docs/en/commands)]

#### [debug-your-config](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/debug-your-config.md) [[Source](https://code.claude.com/docs/en/debug-your-config)]

* Clarified exactly which managed-settings sources still apply in a clean debug config: MDM profiles, registry policy, and `managed-settings.json` from outside the config directory, plus server-managed settings fetched once credentials exist. [[line 68](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/debug-your-config.md?plain=1#L68)] [[Source](https://code.claude.com/docs/en/debug-your-config)]

#### [desktop-scheduled-tasks](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/desktop-scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks)]

* Local scheduled tasks require Claude Desktop 1.1.5368 or later; added troubleshooting for a missing **Routines** sidebar entry. [[line 28](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/desktop-scheduled-tasks.md?plain=1#L28)] [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Plugins enabled only in your user settings can now reach cloud sessions by enabling them for your claude.ai account (loaded as synced plugins), instead of only via the repo's `.claude/settings.json`. [[line 365](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/desktop.md?plain=1#L365)] [[Source](https://code.claude.com/docs/en/desktop)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `/auto-mode-setup` was added to the list of features gated behind feature-flag fetching. [[line 462](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/env-vars.md?plain=1#L462)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New error: **Issuer mismatch in authorization response (RFC 9207)** — during MCP OAuth sign-in, Claude Code now fails the flow if the redirect's `iss` doesn't match the issuer the server advertised in its OAuth metadata, a protection against authorization-server mix-up attacks. Bypass while a server is being fixed with `MCP_SDK_GENERATION=v1`. [[lines 65, 886](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/errors.md?plain=1#L886)] [[Source](https://code.claude.com/docs/en/errors#issuer-mismatch-in-authorization-response)]
* New error: **The current directory no longer exists** — a clear message when `claude` starts from a deleted or moved directory, replacing a raw `ENOENT`/`uv_cwd` crash from before v2.1.239. A permissions-related failure to read the directory now names the error code instead. [[lines 120, 1576](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/errors.md?plain=1#L1576)] [[Source](https://code.claude.com/docs/en/errors#the-current-directory-no-longer-exists)]

#### [how-claude-code-works](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/how-claude-code-works.md) [[Source](https://code.claude.com/docs/en/how-claude-code-works)]

* Removed the inline "Be specific upfront," "Give Claude something to verify against," and "Explore before implementing" tip sections in favor of a pointer to the new [Best practices](https://code.claude.com/docs/en/best-practices) page. [[line 139](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/how-claude-code-works.md?plain=1#L139)] [[Source](https://code.claude.com/docs/en/how-claude-code-works)]

#### [managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/managed-settings.md) [[Source](https://code.claude.com/docs/en/managed-settings)]

* Noted that a self-hosted-environment session still reads a small set of admin keys from the runner image's managed-settings file even when server-managed settings otherwise take precedence. [[line 76](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/managed-settings.md?plain=1#L76)] [[Source](https://code.claude.com/docs/en/managed-settings)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Same "keys read from every admin source" clarification applied to model-allowlist precedence in self-hosted environments. [[line 206](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/model-config.md?plain=1#L206)] [[Source](https://code.claude.com/docs/en/model-config)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* New **plugins synced from claude.ai**: Cowork and cloud sessions now download the plugins enabled on your claude.ai account into `~/.claude/plugins/synced/` and load each as `<name>@synced`, with no marketplace or install record. Manage with `claude plugin enable/disable <name>@synced`; turn one off for every synced session from claude.ai. Before v2.1.239 these loaded under the `@inline` identity instead. [[line 354](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/plugins-reference.md?plain=1#L354)] [[Source](https://code.claude.com/docs/en/plugins-reference#synced-plugins)]
* `--setting-sources` can now only remove `user` from the `pluginConfigs` precedence list; managed settings and `--settings` always stay in effect. [[line 544](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/plugins-reference.md?plain=1#L544)] [[Source](https://code.claude.com/docs/en/plugins-reference)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Trusted Devices is now enabled for an organization by an **Owner** only, not an Owner or admin. [[lines 185, 198](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/remote-control.md?plain=1#L198)] [[Source](https://code.claude.com/docs/en/remote-control#trusted-devices)]

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* Added a pointer to the "disabled by organization policy" section when **Routines** is missing from the Desktop sidebar. [[line 29](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/routines.md?plain=1#L29)] [[Source](https://code.claude.com/docs/en/routines)]

#### [self-hosted-environments](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/self-hosted-environments.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments)]

* Enabling self-hosted environments for an organization now requires the **Owner** role specifically, not Owner or admin. [[line 27](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/self-hosted-environments.md?plain=1#L27)] [[Source](https://code.claude.com/docs/en/self-hosted-environments)]

#### [self-hosted-environments-configuration](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/self-hosted-environments-configuration.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration)]

* Enabling self-hosted environments requires the **Owner** role specifically. Also clarified that even when server-managed settings take precedence, sessions still read the runner image's `env` block and other cross-source keys (sandbox locks, sandbox binary paths, `forceRemoteSettingsRefresh`) from the local managed-settings file. [[lines 3, 354](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L354)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration)]

#### [self-hosted-environments-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/self-hosted-environments-deploy.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy)]

* Hiding Anthropic-hosted environments organization-wide is now an **Owner**-only action. [[line 21](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L21)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy)]

#### [self-hosted-environments-identity](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/self-hosted-environments-identity.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-identity)]

* Enabling self-hosted environments now requires the **Owner** role specifically. [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/self-hosted-environments-identity.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-identity)]

#### [self-hosted-environments-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/self-hosted-environments-quickstart.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-quickstart)]

* Turning on self-hosted environments and running the guided runner setup now require the **Owner** role specifically, not Owner or admin. [[line 41](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/self-hosted-environments-quickstart.md?plain=1#L41)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-quickstart)]

#### [self-hosted-environments-reference](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/self-hosted-environments-reference.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-reference)]

* Enabling self-hosted environments, and retrying a circuit-broken spawn queue, are now **Owner**-only actions. [[lines 3, 147](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/self-hosted-environments-reference.md?plain=1#L147)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-reference)]

#### [self-hosted-environments-testing](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/self-hosted-environments-testing.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-testing)]

* Minting an admin token for CI, and enabling self-hosted environments, now require the **Owner** role specifically. [[lines 194, 215](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/self-hosted-environments-testing.md?plain=1#L215)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-testing)]

#### [sessions](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/sessions.md) [[Source](https://code.claude.com/docs/en/sessions)]

* Minor "See also" section intro added; no content change. [[line 204](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/sessions.md?plain=1#L204)] [[Source](https://code.claude.com/docs/en/sessions)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Same "keys read from every admin source" clarification applied to which managed settings reach a cloud session. [[line 291](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/settings.md?plain=1#L291)] [[Source](https://code.claude.com/docs/en/settings)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* The all-settings table gained an interactive topic/scope filter and sort control, plus a running count (210 settings) and a "Back to index" link. [[lines 3, 19](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/settings-reference.md?plain=1#L19)] [[Source](https://code.claude.com/docs/en/settings-reference)]

#### [slack](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/slack.md) [[Source](https://code.claude.com/docs/en/slack)]

* Recreating a Claude Tag channel's cloud environment as an organization-shared one is now an **Owner**-only fix, not Owner or admin. [[lines 178, 183](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/slack.md?plain=1#L183)] [[Source](https://code.claude.com/docs/en/slack#sessions-from-a-claude-tag-channel-fail-to-start)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Replaced the inline "Use git worktrees for parallel tasks" walkthrough (including the `--worktree` example) with a link to the dedicated [Worktrees](https://code.claude.com/docs/en/worktrees) page. [[line 388](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/vs-code.md?plain=1#L388)] [[Source](https://code.claude.com/docs/en/vs-code#work-with-git)]

#### [whats-new](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/whats-new.md) [[Source](https://code.claude.com/docs/en/whats-new)]

* Added the **Week 34** digest (v2.1.234–v2.1.239, August 17–21): a `/design` research preview bringing Claude Design's artboard workflow into the CLI and Desktop, a built-in **Concise output style**, **device cards** on mobile for any machine running `claude remote-control`, and `ANTHROPIC_DEFAULT_MODEL` to set the default model for new sessions. [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/whats-new.md?plain=1#L13)] [[Source](https://code.claude.com/docs/en/whats-new#week-34)]
* Added the **Week 33** digest (v2.1.225–v2.1.233, August 10–14): auto-continue after a Desktop usage limit resets, **fork mode** on by default for subagent side tasks, GitLab merge-request URL support in `--worktree` and `claude agents`, and `@`-mentioning another Claude session by name. [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/claude-code/whats-new.md?plain=1#L23)] [[Source](https://code.claude.com/docs/en/whats-new#week-33)]

-----

## API changes

### A note on this section

38 of the 42 changed pages below aren't real content changes from Anthropic — they're an archive crawler fix. These pages had been captured mid-render, before their JavaScript content finished loading, so the archive held only "Loading" placeholder text (sometimes for months). This sync finally captured their full rendered content, so each is summarized below as if new.

The remaining 4 pages went the other way: **`compliance/groups/members`**, **`compliance/organizations/settings/retrieve`**, **`compliance/organizations/users`**, and **`compliance/organizations/users/list`** had full content captured previously, but this sync's crawl regressed them back to blank "Loading" placeholders. Their descriptions below are inferred from their titles and prior content, not from what the archive currently holds.

### Messages API

#### [api/messages/create](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/messages/create)]

Core Messages API endpoint: sends a list of input messages (text and/or image content) and returns Claude's generated next message. Full parameter and response reference is now captured, including streaming, tool use, vision, and system prompts.

#### [api/messages/count_tokens](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/messages/count_tokens.md) [[Source](https://platform.claude.com/docs/en/api/messages/count_tokens)]

Counts the tokens a given set of messages, tools, images, and documents would consume, without creating a message.

#### [api/messages/batches](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/messages/batches.md) [[Source](https://platform.claude.com/docs/en/api/messages/batches)]

Index for the Message Batches API: create, retrieve, list, cancel, and delete batches, and fetch batch results for asynchronous bulk processing.

#### [api/beta/messages/create](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/beta/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]

Same as `api/messages/create`, with `anthropic-beta` header support for opt-in features such as extended thinking and the MCP client.

#### [api/beta/messages/count_tokens](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/beta/messages/count_tokens.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/count_tokens)]

Same as `api/messages/count_tokens`, with beta header support.

#### [api/beta/messages/batches](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/beta/messages/batches.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/batches)]

Beta-namespaced version of the Message Batches API index.

### Compliance API — Activities

#### [api/compliance/activities/list](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/activities/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/activities/list)]

Lists and filters compliance audit-log activities — account, key, and admin events — for the caller's tenant.

### Compliance API — Apps: artifacts

#### [api/compliance/apps/artifacts/download](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/artifacts/download.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/artifacts/download)]

Downloads the full text content of an artifact version for compliance review.

#### [api/compliance/apps/artifacts/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/artifacts/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/artifacts/retrieve)]

Returns artifact version metadata (type, hash, size, owning chat) without the content body.

### Compliance API — Apps: chats

#### [api/compliance/apps/chats/files](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/chats/files.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/files)]

Index for chat-file endpoints: retrieve metadata, delete, and download content.

#### [api/compliance/apps/chats/files/delete](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/chats/files/delete.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/files/delete)]

Permanently deletes a file attached to a chat.

#### [api/compliance/apps/chats/files/download](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/chats/files/download.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/files/download)]

Downloads the binary content of a file referenced in chat messages.

#### [api/compliance/apps/chats/generated_files](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/chats/generated_files.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files)]

Index for endpoints covering files Claude generated via tool use: metadata and download.

#### [api/compliance/apps/chats/generated_files/download](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/chats/generated_files/download.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/download)]

Downloads the binary content of a file the assistant created via tool use.

#### [api/compliance/apps/chats/generated_files/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/chats/generated_files/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/retrieve)]

Returns metadata for a Claude-generated file without its content.

#### [api/compliance/apps/chats/list](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/chats/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/list)]

Lists chat metadata across the tenant, with filtering, for compliance review.

#### [api/compliance/apps/chats/messages/list](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/chats/messages/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list)]

Retrieves message history and file metadata for a specific chat.

### Compliance API — Apps: projects

#### [api/compliance/apps/projects](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/projects.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/projects)]

Index for project endpoints: list, retrieve, and delete, for compliance purposes.

#### [api/compliance/apps/projects/attachments](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/projects/attachments.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments)]

Index for listing files and documents attached to a project.

#### [api/compliance/apps/projects/attachments/list](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/projects/attachments/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list)]

Lists files and project documents attached to a given project.

#### [api/compliance/apps/projects/collaborators/list](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/projects/collaborators/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list)]

Lists users, groups, and org-wide role grants on a project.

#### [api/compliance/apps/projects/delete](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/projects/delete.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/projects/delete)]

Hard-deletes a project and all associated data (documents, roles, knowledge base, sync sources); requires no attached chats.

#### [api/compliance/apps/projects/documents](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/projects/documents.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents)]

Index for project document endpoints: retrieve content, metadata, and delete.

#### [api/compliance/apps/projects/documents/delete](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/projects/documents/delete.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/delete)]

Hard-deletes a specific project document.

#### [api/compliance/apps/projects/documents/metadata](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/projects/documents/metadata.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/metadata)]

Returns document metadata (hash, size, filename) without its text content.

#### [api/compliance/apps/projects/documents/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/projects/documents/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/retrieve)]

Returns the full text content and metadata of a project document.

#### [api/compliance/apps/projects/list](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/projects/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/projects/list)]

Lists project metadata across the tenant, filterable, sorted by creation time.

#### [api/compliance/apps/projects/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/projects/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve)]

Returns detailed info (counts, timestamps) for a specific project.

### Compliance API — Apps: sessions

#### [api/compliance/apps/sessions](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/sessions.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/sessions)]

Index for local and remote session endpoints covering Claude Code and Cowork sessions.

#### [api/compliance/apps/sessions/local](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/sessions/local.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/sessions/local)]

Index for listing and retrieving local sessions — Claude Code/Cowork sessions run on a user's own machine.

#### [api/compliance/apps/sessions/local/messages](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/sessions/local/messages.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/sessions/local/messages)]

Model reference for the local-session transcript/message schema.

#### [api/compliance/apps/sessions/local/messages/list](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/sessions/local/messages/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/sessions/local/messages/list)]

Reads one local session's transcript oldest-first, respecting retention boundaries.

#### [api/compliance/apps/sessions/local/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/sessions/local/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/sessions/local/retrieve)]

Retrieves metadata for a single local session.

#### [api/compliance/apps/sessions/remote/list](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/sessions/remote/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/sessions/remote/list)]

Lists remote (cloud-hosted Cowork) sessions across accessible orgs, filterable and paginated.

#### [api/compliance/apps/sessions/remote/messages](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/sessions/remote/messages.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/sessions/remote/messages)]

Model reference for the remote-session transcript/message schema.

#### [api/compliance/apps/sessions/remote/messages/list](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/apps/sessions/remote/messages/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/sessions/remote/messages/list)]

Retrieves a remote session's transcript of prompts, responses, and tool calls.

### Compliance API — Groups and organizations

#### [api/compliance/groups/members](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/groups/members.md) [[Source](https://platform.claude.com/docs/en/api/compliance/groups/members)]

**Regressed to a blank "Loading" placeholder this sync** (had full content before). Previously documented listing the members of an RBAC group.

#### [api/compliance/organizations/roles](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/organizations/roles.md) [[Source](https://platform.claude.com/docs/en/api/compliance/organizations/roles)]

Index for compliance role endpoints: list and retrieve the roles defined for an organization.

#### [api/compliance/organizations/roles/list](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/organizations/roles/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/organizations/roles/list)]

Lists the compliance roles defined for an organization.

#### [api/compliance/organizations/settings](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/organizations/settings.md) [[Source](https://platform.claude.com/docs/en/api/compliance/organizations/settings)]

Index for the effective organization settings endpoint.

#### [api/compliance/organizations/settings/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/organizations/settings/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve)]

**Regressed to a blank "Loading" placeholder this sync** (had full content before). Previously documented the resolved settings in force for an organization.

#### [api/compliance/organizations/users](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/organizations/users.md) [[Source](https://platform.claude.com/docs/en/api/compliance/organizations/users)]

**Regressed to a blank "Loading" placeholder this sync** (had full content before). Previously an index of organization-user endpoints.

#### [api/compliance/organizations/users/list](https://github.com/gpambrozio/ClaudeDocs/blob/9de4ee1ba8e6029d1ed3e23e5e3f51185ff1ce72/docs-md/api/api/compliance/organizations/users/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/organizations/users/list)]

**Regressed to a blank "Loading" placeholder this sync** (had full content before). Previously listed the users in an organization.
