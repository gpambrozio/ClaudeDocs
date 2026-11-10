# [Claude docs changes for November 10th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/5b19720e769fac70deccfd5ef489d95f78ed49c3) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/5b19720e769fac70deccfd5ef489d95f78ed49c3)]

## Executive Summary
- Claude Code 2.1.322 adds fast mode on Vertex AI in the global, US and EU regions. It falls back to standard speed if Vertex refuses it.
- The API gains a Compliance API endpoint for an organization's security posture, plus an Admin API endpoint that signs a member out of Claude everywhere (beta `admin-user-sign-out-2026-10-08`).
- The API beta Messages docs add the `claude-fable-5-2` and `claude-mythos-5-2` models and updated guidance on sending back assistant turns that contain `fallback` blocks.
- The OpenTelemetry SDK guide now covers sending `user.id` baggage to identify end users, and the Go, Java and PHP examples register baggage propagators.
- Claude Code hooks, plugins and artifacts docs gain several new sections: tmux/screen terminal notifications, `--add-dir` plugin loading, one-step artifact updates and many new error entries.

## New Claude Code versions

### [2.1.322](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/versions/2.1.322.md)

#### New features

* Added fast mode on Vertex in the global, us and eu regions, falling back to standard speed if Vertex refuses it

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/structured-outputs](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/agent-sdk/structured-outputs.md) [[Source](https://code.claude.com/docs/en/agent-sdk/structured-outputs)]

* The TypeScript and Python examples now check `!message.is_error` before reading `structured_output`. [[line 80](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/agent-sdk/structured-outputs.md?plain=1#L80)] [[Source](https://code.claude.com/docs/en/agent-sdk/structured-outputs#quick-start)]

#### [artifacts](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/artifacts.md) [[Source](https://code.claude.com/docs/en/artifacts)]

* New section "Turn off one-step artifact updates", which explains setting `CLAUDE_CODE_ARTIFACT_PUBLISH_EDITS=0`. [[lines 88-103](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/artifacts.md?plain=1#L88-L103)] [[Source](https://code.claude.com/docs/en/artifacts#turn-off-one-step-artifact-updates)]
* If you shared an artifact publicly, Claude now also asks before each reply to a comment on it. [[line 63](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/artifacts.md?plain=1#L63)] [[Source](https://code.claude.com/docs/en/artifacts#when-claude-code-asks-before-publishing)]
* On Team and Enterprise plans, you can share an artifact by moving it to a shared folder. [[line 126](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/artifacts.md?plain=1#L126)] [[Source](https://code.claude.com/docs/en/artifacts#share-an-artifact)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New entry: transcript could not be saved because the disk is full (ENOSPC) or the disk quota is used up (EDQUOT). [[lines 3381-3395](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/errors.md?plain=1#L3381-L3395)] [[Source](https://code.claude.com/docs/en/errors#claude-code-could-not-save-because-the-disk-is-full)]
* New entry: `claude remote-control` did not start because a first-run question got no answer. [[lines 3467-3480](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/errors.md?plain=1#L3467-L3480)] [[Source](https://code.claude.com/docs/en/errors#remote-control-did-not-start-because-a-question-got-no-answer)]
* New entry: plugin MCP or LSP server file path not read, because it is absolute or has a `..` part. [[lines 4486-4501](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/errors.md?plain=1#L4486-L4501)] [[Source](https://code.claude.com/docs/en/errors#server-file-path-not-read)]
* New entry: `--permission-prompt-tool` returned an invalid result, with the expected response format and MCP SDK settings. [[lines 4724-4740](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/errors.md?plain=1#L4724-L4740)] [[Source](https://code.claude.com/docs/en/errors#permission-prompt-tool-returned-an-invalid-result)]
* New entry: refusing to apply artifact edits because a hook is configured for file edits in the session. [[lines 5198-5214](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/errors.md?plain=1#L5198-L5214)] [[Source](https://code.claude.com/docs/en/errors#refusing-to-apply-edits-a-hook-is-configured-for-file-edits-in-this-session)]
* Removed the note that API-key, OAuth-token and third-party sessions never see the saved-login messages. [[line 1439](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/errors.md?plain=1#L1439)] [[Source](https://code.claude.com/docs/en/errors#login-expired)]

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Removed the paragraph about resending fast mode status to Remote Control devices. [[line 65](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/fast-mode.md?plain=1#L65)] [[Source](https://code.claude.com/docs/en/fast-mode#switch-models-while-fast-mode-is-on)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* MCP tool hooks: documented the errors shown when the tool's answer is too large to read. `PreToolUse` refuses the tool call, and other events don't block. [[lines 571-581](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/hooks.md?plain=1#L571-L581)] [[Source](https://code.claude.com/docs/en/hooks#how-the-tools-result-is-read)]
* How to start long-running programs, such as dev servers, from a hook: run them in the background and redirect stdout and stderr. [[lines 902-906](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/hooks.md?plain=1#L902-L906)] [[Source](https://code.claude.com/docs/en/hooks#hooks-that-start-a-background-process)]
* `terminalSequence` works only from hooks that don't run in the background (no `async` or `asyncRewake`). [[line 1119](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/hooks.md?plain=1#L1119)] [[Source](https://code.claude.com/docs/en/hooks#emit-terminal-notifications)]
* New section on getting terminal notifications inside tmux (3.3+, `allow-passthrough`) or GNU screen. [[lines 1136-1142](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/hooks.md?plain=1#L1136-L1142)] [[Source](https://code.claude.com/docs/en/hooks#get-terminal-notifications-inside-tmux-or-gnu-screen)]
* In Cowork cloud sessions, `updatedToolOutput` is ignored for `AskUserQuestion` and `ExitPlanMode`. [[line 1208](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/hooks.md?plain=1#L1208)] [[Source](https://code.claude.com/docs/en/hooks#decision-control)]
* Documented how `updatedPermissions` rules map `Tool(specifier)` onto `toolName` and `ruleContent`, with examples. MCP allow rules must omit `ruleContent`. [[lines 2225-2232](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/hooks.md?plain=1#L2225-L2232)] [[Source](https://code.claude.com/docs/en/hooks#permission-update-entries)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* The `OTEL_METRICS_INCLUDE_*` variables now apply to events as well as metrics. [[lines 145-153](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/monitoring-usage.md?plain=1#L145-L153)] [[Source](https://code.claude.com/docs/en/monitoring-usage#metrics-cardinality-control)]
* `app.entrypoint` gains `claude-desktop` and `claude-desktop-3p` values. [[line 586](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/monitoring-usage.md?plain=1#L586)] [[Source](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)]
* Clarified the retention sweep event, where `result` is `complete` or `skipped`, and how a `settings.read` hook affects `period_days`. [[lines 1457-1473](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/monitoring-usage.md?plain=1#L1457-L1473)] [[Source](https://code.claude.com/docs/en/monitoring-usage#retention-sweep-event)]
* New guidance on comparing active users across surfaces by counting distinct `user.account_uuid` per entrypoint. [[lines 1556-1559](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/monitoring-usage.md?plain=1#L1556-L1559)] [[Source](https://code.claude.com/docs/en/monitoring-usage#usage-monitoring)]
* Clarified that events can include raw content if `OTEL_LOG_TOOL_DETAILS` or `OTEL_LOG_RAW_API_BODIES` is set. [[line 1790](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/monitoring-usage.md?plain=1#L1790)] [[Source](https://code.claude.com/docs/en/monitoring-usage#security-and-privacy)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* The first-run dialog can reappear if `--setting-sources` omits `user`. Include `user` to skip it. [[line 685](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/permission-modes.md?plain=1#L685)] [[Source](https://code.claude.com/docs/en/permission-modes#skip-all-checks-with-bypasspermissions-mode)]

#### [plugins/loading](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/plugins/loading.md) [[Source](https://code.claude.com/docs/en/plugins/loading)]

* New section on plugins enabled in an `--add-dir` directory but not loaded, because of `--setting-sources`. [[lines 172-185](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/plugins/loading.md?plain=1#L172-L185)] [[Source](https://code.claude.com/docs/en/plugins/loading#enabled-in-an-add-dir-directory-but-not-loaded)]
* Rewrote the project-enabled plugin install steps (`claude plugin install <name>@<marketplace> --scope project`, then `/reload-plugins`) and listed the cases that load without an install. [[lines 188-208](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/plugins/loading.md?plain=1#L188-L208)] [[Source](https://code.claude.com/docs/en/plugins/loading#enabled-in-project-settings-but-not-installed)]

#### [plugins/mods/admin](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/plugins/mods/admin.md) [[Source](https://code.claude.com/docs/en/plugins/mods/admin)]

* The built-in guard and `prependPlugins`/`appendPlugins` rules now also treat a `managed-mcp.json` file like managed settings. [[lines 56-59](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/plugins/mods/admin.md?plain=1#L56-L59)] [[Source](https://code.claude.com/docs/en/plugins/mods/admin#know-what-happens-by-default)]
* `allowModsToOverrideDenyRules` now lets mods approve calls past most of the outcomes that stay in place by default. [[line 259](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/plugins/mods/admin.md?plain=1#L259)] [[Source](https://code.claude.com/docs/en/plugins/mods/admin#set-options-on-the-built-in-guard)]
* Repositories can't set the plugin ordering lists. Users can set them only in limited cases. [[lines 349-350](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/plugins/mods/admin.md?plain=1#L349-L350)] [[Source](https://code.claude.com/docs/en/plugins/mods/admin#install-your-organizations-mods-and-set-the-order)]

#### [plugins/mods/reference](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/plugins/mods/reference.md) [[Source](https://code.claude.com/docs/en/plugins/mods/reference)]

* New `breakPromptCache: true` option for `prompt.section` and `tool.describe`, which sends a changed section or description to Claude in a running conversation. It needs v2.1.321 or later and restarts the prompt cache. [[lines 107-112](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/plugins/mods/reference.md?plain=1#L107-L112)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#send-a-changed-system-prompt-section-or-tool-description-with-breakpromptcache)]
* Render element ids changed to "the drawn row's id", and `InfoNotice` ids are prefixed with `notice:`. [[lines 251-258](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/plugins/mods/reference.md?plain=1#L251-L258)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#render-sites)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Troubleshooting entry for git's `Unable to create '…/index.lock'` error when Claude Code is started from a repository subdirectory. [[lines 902-905](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/sandboxing.md?plain=1#L902-L905)] [[Source](https://code.claude.com/docs/en/sandboxing#a-git-command-fails-with-unable-to-create-indexlock)]

#### [self-hosted-environments-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/self-hosted-environments-deploy.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy)]

* Incident response guidance: after a suspected compromise, first revoke the session's token, then replace the environment secret. [[lines 22-23](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L22-L23)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#harden-your-deployment)]
* Defined what counts as the global git config for the governed git proxy. [[line 205](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L205)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#use-the-anthropic-git-proxy)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Note that a subagent under `bypassPermissions` can still prompt for actions that no mode auto-approves. [[line 592](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/claude-code/sub-agents.md?plain=1#L592)] [[Source](https://code.claude.com/docs/en/sub-agents#permission-modes)]

-----

## API changes

### New Documents

#### [api/beta/organization/users/sign_out](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/api/api/beta/organization/users/sign_out.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/users/sign_out)]

New Admin API endpoint, `POST /v1/organizations/users/{user_id}/sign_out`. It signs a member out of Claude everywhere without removing them from the organization. It ends their sessions, trusted devices and OAuth tokens for the organization. A token can take up to an hour to stop working. The member keeps their role and can sign in again.

#### [api/compliance/organizations/security_posture](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/api/api/compliance/organizations/security_posture.md) [[Source](https://platform.claude.com/docs/en/api/compliance/organizations/security_posture)]

New Compliance API reference page for an organization's security posture. It covers the security controls and their attestations.

#### [api/compliance/organizations/security_posture/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/api/api/compliance/organizations/security_posture/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/compliance/organizations/security_posture/retrieve)]

New endpoint, `GET /v1/compliance/organizations/{organization_id}/security_posture`. It returns the organization's security controls, evaluated at request time, in a single unpaginated `controls` list. A missing control is not a pass. It requires the `anthropic-version` header and takes no query parameters. It returns 400 if the Compliance API is not enabled and 404 for unknown or unreadable organizations.

### Changed documents

#### [api/beta/messages](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/api/api/beta/messages.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages)]

* Added the `admin-user-sign-out-2026-10-08` beta flag.
* Added the `claude-fable-5-2` and `claude-mythos-5-2` models. Mythos is available through verification programs.
* Revised the `fallback` block guidance: keep the block when you send the assistant turn back, but leave out some earlier blocks and their `tool_result`s. It links to the refusals and fallback guide. The same change applies across the per-language SDK beta and messages references (Python, TypeScript, Go, Java, C#, Ruby, PHP, CLI).

#### [api/compliance/activities](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/api/api/compliance/activities.md) [[Source](https://platform.claude.com/docs/en/api/compliance/activities)]

* Very large rewrite of the Compliance API activities reference, which also affects `api/compliance` and `api/compliance/activities/list`. It likely adds or expands the activity types and schemas. I did not review it line by line.

#### [api/beta/organization](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/api/api/beta/organization.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization)]

* Large update that adds the sign-out user endpoint and its models. Related pages `organization/users`, `organization/claude_tag` and `claude_tag/slack_channels` also changed substantially.

#### [cli-sdks-libraries/sdks/java](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/api/cli-sdks-libraries/sdks/java.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/java)]

* The Java SDK version in the install snippets was bumped from 3.7.0 to 3.8.0. The same bump is in `manage-claude/opentelemetry/sdk`. [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/api/cli-sdks-libraries/sdks/java.md?plain=1#L18)] [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/java#installation)]

#### [manage-claude/opentelemetry/sdk](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/api/manage-claude/opentelemetry/sdk.md) [[Source](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk)]

* New "Identify your end users" section. It shows how to send a `user.id` baggage entry, via a `baggage` header or OpenTelemetry baggage in each SDK, to set `user.id` on API spans. [[lines 662-798](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/api/manage-claude/opentelemetry/sdk.md?plain=1#L662-L798)] [[Source](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk#identify-your-end-users)]
* The Go, Java and PHP examples now register both W3C trace context and baggage propagators. [[line 254](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/api/manage-claude/opentelemetry/sdk.md?plain=1#L254)] [[Source](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk#2-register-a-tracer-provider)]

#### [managed-agents/self-hosted-sandboxes](https://github.com/gpambrozio/ClaudeDocs/blob/5b19720e769fac70deccfd5ef489d95f78ed49c3/docs-md/api/managed-agents/self-hosted-sandboxes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

* Updated the overview. The sibling self-hosted sandbox pages (custom tools, memory, operations, reference, security) and `cloud-sandboxes-reference` each gained a short 5-line addition.
