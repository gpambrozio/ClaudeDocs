# [Claude docs changes for November 17th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10)]

## Executive Summary
- Claude Code 2.1.326 tightens permissions and sandboxing, starts HIPAA-configured organizations in auto mode by default, and adds many UI and performance improvements.
- New Claude Platform OAuth docs (beta) describe how customers can pay for their own Claude usage inside your app, with a new `billing_policy` request parameter on the Messages API.
- The Plugins API docs now cover pinning plugin versions, content-scan behavior, and a `reach` classification of what a plugin can do.
- Hooks docs clarify how exit code 2 interacts with JSON output and `continue: false`, and how TeammateIdle and TaskCompleted hooks control teammates.
- Desktop docs add iPhone Duo testing in the iOS simulator pane, and the model docs explain which model a resumed session uses.

## New Claude Code versions

### [2.1.326](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/versions/2.1.326.md)

#### New features

* Code Mode can now be turned on while agent teams are enabled
* Startup warning when `--allowedTools`, `--disallowedTools` or `--tools` has an incomplete rule
* `/status` has a row explaining when your provider or an environment variable such as `DISABLE_TELEMETRY` turns features off
* Ctrl+O shows hidden startup notices
* `OTEL_RESOURCE_INCLUDE_HOST` adds `host.name` and `host.id` to OpenTelemetry resource attributes (off by default)
* Mods: `overflowX="scroll"` on `Box`, and `maxLines` and `wrap="clip"` on `Text`
* Note in `/plugin` and `claude plugin list` when a malformed `plugin.json` field is ignored

#### Existing feature improvements

* Stronger Bash and Code Mode permission checks and sandbox protections on macOS, Linux and WSL; sandboxed commands write to fewer sensitive home folders by default (allow with `sandbox.filesystem.allowWrite`)
* Terminal and VS Code sessions in organizations with the Claude Code + Cowork HIPAA configuration now start in auto mode by default (`disableAutoMode` turns it off)
* A hook's `"decision": "block"` now holds in more cases, and PreToolUse `updatedInput` is kept when several hooks answer
* Hook failures, blocks and timeouts are color-coded in the transcript, with the reason shown
* Folder trust prompt names the project settings files it will load
* `/update-config` uses about 13,000 tokens of context instead of 93,000
* Remote Control replies now stream to phone or browser as they are written
* Better responsiveness, lower idle CPU use, and faster first response after `/compact`
* Many `/plugin` screens now fit short windows and support Home, End, PgUp, PgDn, mouse wheel and clicks
* Improved sign-in screens, key hints, list navigation, and sliders for `/autocompact` and `/scroll-speed`
* `/doctor` shares findings as it works; broken settings JSON errors give line and column

#### Major bug fixes

* Fixed sessions losing recent turns or history after a crash or low memory on resume
* Fixed `claude purge` hiding its prompts when stdout is redirected
* Fixed the spend limit menu removing the monthly limit without asking
* Fixed `/rewind` restoring only some files and misreporting "No code changes"
* Fixed settings files with deeply nested values crashing Claude Code
* Fixed the background service ending other users' processes when a process number was reused
* Fixed the folder trust prompt and auto mode offer accepting keystrokes unintentionally
* Fixed `cp` being refused when only the source was covered by an `Edit` deny rule

-----

## Claude Code changes

### New Documents

#### [desktop-ios-simulator](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/desktop-ios-simulator.md) [[Source](https://code.claude.com/docs/en/desktop-ios-simulator)]

The file was already present; a new section is listed under Changed documents.

#### [plugin-evals](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/plugin-evals.md) [[Source](https://code.claude.com/docs/en/plugin-evals)]

Additions to the plugin evaluation guide (15 lines).

### Changed documents

#### [desktop-ios-simulator](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/desktop-ios-simulator.md) [[Source](https://code.claude.com/docs/en/desktop-ios-simulator)]

* New section on testing your app on an iPhone Duo simulator, folding it closed, half open, and open. It requires Claude Desktop v4.29.0+ and Xcode 27.1+. [[lines 134-157](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/desktop-ios-simulator.md?plain=1#L134-L157)] [[Source](https://code.claude.com/docs/en/desktop-ios-simulator#test-your-app-on-an-iphone-duo)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New entries for login time-limit and claude.ai login expiry messages, and for `could not fully check your permission rules`. [[lines 104-106](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/errors.md?plain=1#L104-L106)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]
* New section: "Claude Code is unable to fetch from a host", explaining the WebFetch domain safety check. [[lines 5434-5445](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/errors.md?plain=1#L5434-L5445)] [[Source](https://code.claude.com/docs/en/errors#claude-code-is-unable-to-fetch-from-a-host)]
* Share uploads are limited to 8 MiB, and long sessions are progressively trimmed. [[line 2374](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/errors.md?plain=1#L2374)] [[Source](https://code.claude.com/docs/en/errors#couldnt-share-the-transcript)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Clarified that exit code 2 still blocks with most JSON output, and how `continue: false` takes precedence on events such as `Stop`. [[lines 845-848](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/hooks.md?plain=1#L845-L848)] [[Source](https://code.claude.com/docs/en/hooks#exit-code-2)]
* TeammateIdle and TaskCompleted hooks: documented `decision: "block"` and `continue: false` with `stopReason`. [[lines 2810-2812](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/hooks.md?plain=1#L2810-L2812)] [[lines 2993-2995](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/hooks.md?plain=1#L2993-L2995)] [[Source](https://code.claude.com/docs/en/hooks#taskcompleted-decision-control)]
* StopFailure error types now include `account_on_hold` and `cloud_credential_error`. [[line 2943](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/hooks.md?plain=1#L2943)] [[Source](https://code.claude.com/docs/en/hooks#stopfailure-input)]
* HTTP hook allowlists now apply in any settings file, not only managed settings. [[lines 264-268](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/hooks.md?plain=1#L264-L268)] [[Source](https://code.claude.com/docs/en/hooks#limit-http-hooks)]
* `Setup` supports only `command` hooks, and `SessionStart` supports `command` and `mcp_tool`. [[line 4016](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/hooks.md?plain=1#L4016)] [[Source](https://code.claude.com/docs/en/hooks#prompt-based-hooks)]
* `continueOnBlock` behavior for prompt hooks on `TaskCompleted` and `TeammateIdle`. [[lines 4084-4085](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/hooks.md?plain=1#L4084-L4085)] [[Source](https://code.claude.com/docs/en/hooks#response-schema)]

#### [iam](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/iam.md) [[Source](https://code.claude.com/docs/en/iam)]

* New "After the login expires" section: what happens without or with another credential, and the `/status` Login row. [[lines 234-243](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/iam.md?plain=1#L234-L243)] [[Source](https://code.claude.com/docs/en/iam#after-the-login-expires)]
* Bulk invite users from the Console Members page. [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/iam.md?plain=1#L95)] [[Source](https://code.claude.com/docs/en/iam#claude-console-authentication)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* New section "Which model a resumed session uses". [[lines 194-209](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/model-config.md?plain=1#L194-L209)] [[Source](https://code.claude.com/docs/en/model-config#setting-your-model)]
* `/model` in non-interactive mode applies to the current session only. [[line 142](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/model-config.md?plain=1#L142)] [[Source](https://code.claude.com/docs/en/model-config#setting-your-model)]
* The organization default model can override user, project and local settings. [[lines 456-458](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/model-config.md?plain=1#L456-L458)] [[Source](https://code.claude.com/docs/en/model-config#organization-default-model)]
* The startup header shows which settings file set the model, and `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` takes precedence over managed model settings. [[line 194](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/model-config.md?plain=1#L194)] [[Source](https://code.claude.com/docs/en/model-config#setting-your-model)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* HIPAA-configured organizations start in auto mode by default from v2.1.326. [[lines 81-157](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/permission-modes.md?plain=1#L81-L157)] [[Source](https://code.claude.com/docs/en/permission-modes#which-mode-a-session-starts-in)]
* PowerShell commands flagged `could not fully check your permission rules` are never auto-approved. [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/permission-modes.md?plain=1#L42)] [[Source](https://code.claude.com/docs/en/permission-modes#actions-no-mode-auto-approves)]
* `claude auto-mode defaults` prints the built-in rule lists. [[line 523](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/permission-modes.md?plain=1#L523)] [[Source](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default)]
* Classifier review with Code Mode and `SendMessage`; more broad allow rules are dropped on entering auto mode (wrappers with wildcard, leading-wildcard shell rules). [[lines 589-610](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/claude-code/permission-modes.md?plain=1#L589-L610)] [[Source](https://code.claude.com/docs/en/permission-modes#how-auto-mode-evaluates-actions)]

#### Other changed Claude Code documents

Smaller updates were made to desktop, desktop-changelog, env-vars, fullscreen, mcp, managed-mcp, settings-reference, sub-agents, plugins/mods/admin, plugins/org, prompt-caching, vs-code, ide-integrations, terminal-config, permissions and related pages, mostly reflecting the 2.1.326 changes.

-----

## API changes

### New Documents

#### [oauth-apps/overview](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/api/manage-claude/oauth-apps/overview.md) [[Source](https://platform.claude.com/docs/en/manage-claude/oauth-apps/overview)]

Introduces Claude Platform OAuth (beta). Users link their Claude organization to your app so their own organization is billed for the usage in your product. You choose per request who pays, and customers can set a spend cap or unlink at any time.

#### [oauth-apps/oauth-reference](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/api/manage-claude/oauth-apps/oauth-reference.md) [[Source](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference)]

Reference for the OAuth flow, endpoints and parameters.

#### [oauth-apps/organization-billing-connections](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/api/manage-claude/oauth-apps/organization-billing-connections.md) [[Source](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections)]

Guide to Linked billing, including the API for organization billing connections. It doesn't work for organizations billed through a cloud marketplace.

#### [oauth-apps/app-review](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/api/manage-claude/oauth-apps/app-review.md) [[Source](https://platform.claude.com/docs/en/manage-claude/oauth-apps/app-review)]

Describes the review process an app goes through before customers can link.

#### [oauth-apps/branding-samples](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/api/manage-claude/oauth-apps/branding-samples.md) [[Source](https://platform.claude.com/docs/en/manage-claude/oauth-apps/branding-samples)]

Branding guidance and samples for the "Link your Claude organization" button.

### Changed documents

#### [api/beta/messages/create](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/api/api/beta/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]

* New beta header `user-profiles-billing-2026-10-01`. [[line 124](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/api/api/beta/messages/create.md?plain=1#L124)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/create#headers)]
* New `billing_policy` parameter (`bill_to`: `self` or `user_profile`) bills the customer behind the `anthropic-user-profile-id` header. The same change applies to batches create, count_tokens and the per-language SDK references. [[lines 3626-3639](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/api/api/beta/messages/create.md?plain=1#L3626-L3639)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/create#body-parameters)]

#### [manage-claude/plugins-api](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/api/manage-claude/plugins-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/plugins-api)]

* New "Pins" section: how a plugin becomes pinned, that it can't be unpinned, and how claude.ai saves interact with API pins. [[lines 272-294](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/api/manage-claude/plugins-api.md?plain=1#L272-L294)] [[Source](https://platform.claude.com/docs/en/manage-claude/plugins-api#pins)]
* Versions uploaded through the API never wait for content scan, so pin first to keep members on the current version. [[line 338](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/api/manage-claude/plugins-api.md?plain=1#L338)] [[Source](https://platform.claude.com/docs/en/manage-claude/plugins-api#content-scanning)]
* New `reach` classification (`remote`, `privileged`, `contained`) describing what a plugin version can do. [[lines 352-380](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/api/manage-claude/plugins-api.md?plain=1#L352-L380)] [[Source](https://platform.claude.com/docs/en/manage-claude/plugins-api#reach)]
* Read scopes can download files of plugins in members' personal marketplaces. [[line 220](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/api/manage-claude/plugins-api.md?plain=1#L220)] [[Source](https://platform.claude.com/docs/en/manage-claude/plugins-api#access-to-members-plugin-files)]

#### [manage-claude/user-profiles](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/api/manage-claude/user-profiles.md) [[Source](https://platform.claude.com/docs/en/manage-claude/user-profiles)]

* Expanded with billing-related user profile behavior (39 lines changed).

#### [manage-claude/cmek-claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/api/manage-claude/cmek-claude-platform-on-aws.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-claude-platform-on-aws)]

* Updated customer-managed encryption key guidance for Claude Platform on AWS.

#### [manage-claude/access-transparency](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/api/manage-claude/access-transparency.md) [[Source](https://platform.claude.com/docs/en/manage-claude/access-transparency)]

* Updated access transparency details.

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/3543ab6c4c2bbc4d64c4c1ea5bdf3af174d65f10/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* New release notes entries added.

#### Other changed API documents

Cloud platform pages (Bedrock, Foundry, Google Cloud, Claude Platform on AWS), the Java SDK page, CLI usage and the SDK overview received smaller edits. The per-language SDK reference pages (beta endpoints in cli, csharp, go, java, python, ruby and typescript) were regenerated with the new `billing_policy` parameter and minor additions.
