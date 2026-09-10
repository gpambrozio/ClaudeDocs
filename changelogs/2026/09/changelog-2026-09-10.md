# [Claude docs changes for September 10th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7)]

## Executive Summary
- The Admin API (organization members, RBAC groups/roles, MCP tunnels, spend limits, cost/usage reports, and Enterprise analytics) is now also exposed as a typed beta SDK surface — `client.beta.organization` in Python, TypeScript, C#, Go, Java, PHP, and Ruby, and `ant beta:organization` in the CLI — documented under a new `api/beta/organization/` reference tree alongside the existing REST-only Admin API docs, and every guide that used to link to `api/admin/*` now points at the new location.
- Claude Managed Agents permission policies gain a third option, `auto`: the server evaluates each agent or MCP tool call and runs it, denies it, or pauses it for your approval, reporting the outcome on `agent.tool_use`/`agent.mcp_tool_use` events via new `evaluated_permission` and `evaluation` fields.
- New `ant beta:sessions connect` CLI command attaches your terminal (or, with `--web`, the Claude Console's session viewer) to a live Managed Agents session, so you can follow its transcript, send messages, interrupt it, and allow or deny tool calls waiting for approval.
- Claude Code artifact publishing now validates the source file decodes as UTF-8 (or UTF-16 with a BOM) and refuses ones that don't, or that contain a stray `U+FFFD`, naming the exact line and column to fix; image-resize failures also now name specific causes such as a CMYK JPEG or animated WebP instead of a generic decode error.
- Effort caps (`maxEffortLevel` and organization-wide caps) now also constrain skill/subagent frontmatter effort and gate whether ultracode is available at all; `allowedChannelPlugins` gains a `"plugin@marketplace"` string shorthand, and managed `allowedHttpHookUrls`/`httpHookAllowedEnvVars` now fail open to lower-scoped settings instead of blocking everything when invalid.

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Clarified that `effortLevel: "ultracode"` *requests* `xhigh` effort with ultracode on, rather than guaranteeing it runs at `xhigh` — it can still be capped. [[line 586](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L586)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#applyflagsettings)]

#### [artifacts](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/artifacts.md) [[Source](https://code.claude.com/docs/en/artifacts)]

* The published source file must now decode as UTF-8, or as little-endian UTF-16 by its byte-order mark; a file that doesn't decode, or that contains the replacement character `U+FFFD`, is refused with the line and column to fix instead of being published. [[line 280](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/artifacts.md?plain=1#L280)] [[Source](https://code.claude.com/docs/en/artifacts#requirements)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `--effort ultracode` now *requests* `xhigh` effort with ultracode on, rather than guaranteeing it starts there — an effort cap or unsupported model can still lower it. [[line 81](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/cli-reference.md?plain=1#L81)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Added a new "The source file is not valid UTF-8 text" section (v2.1.267+): publishing an artifact from a file that doesn't decode as UTF-8/UTF-16, or that already contains `U+FFFD`, is refused before upload, naming the first bad position; before this version the server refused the publish instead. [[lines 212-213](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/errors.md?plain=1#L212-L213), [3092-3112](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/errors.md?plain=1#L3092-L3112)] [[Source](https://code.claude.com/docs/en/errors#the-source-file-is-not-valid-utf-8-text)]
* Added a new "Working directory no longer exists" background-session error (v2.1.257+), shown when dispatching or restarting a session whose working directory was deleted or moved; it previously appeared to start and then failed silently in agent view. [[line 232](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/errors.md?plain=1#L232), [3423-3435](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/errors.md?plain=1#L3423-L3435)] [[Source](https://code.claude.com/docs/en/errors#working-directory-no-longer-exists-when-starting-a-background-session)]
* Image-resize failure messages now name a specific cause when known — a CMYK JPEG, an animated WebP, or a possibly damaged file — and say what format to re-save as, instead of a generic "processing is unavailable" message. [[lines 1690-1701](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/errors.md?plain=1#L1690-L1701)] [[Source](https://code.claude.com/docs/en/errors#image-errors)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* The model-name button in the prompt box footer now shows the selected effort level (v2.1.257+). [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/ide-integrations.md?plain=1#L95)] [[Source](https://code.claude.com/docs/en/ide-integrations#use-the-prompt-box)]
* You can now paste an image from your clipboard directly into the prompt box, in addition to drag-and-drop. [[line 124](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/ide-integrations.md?plain=1#L124)] [[Source](https://code.claude.com/docs/en/ide-integrations#reference-files-and-folders)]
* Clicking a session in history that's already open in another tab of the current window now switches to that tab instead of opening a duplicate. [[line 130](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/ide-integrations.md?plain=1#L130)] [[Source](https://code.claude.com/docs/en/ide-integrations#resume-past-conversations)]

#### [managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/managed-settings.md) [[Source](https://code.claude.com/docs/en/managed-settings)]

* `allowedHttpHookUrls` and `httpHookAllowedEnvVars` now merge across settings files when the managed value is invalid: entries from user, project, or local settings still apply while the managed list falls back to empty, rather than blocking everything (v2.1.267+; earlier versions drop the whole key). [[line 329](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/managed-settings.md?plain=1#L329)] [[Source](https://code.claude.com/docs/en/managed-settings#fields-that-fail-open-to-a-safe-default)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Spelled out exactly when ultracode is unavailable — workflows turned off, the model doesn't support `xhigh` effort, or an effort cap below `xhigh` applies — and that `--effort ultracode` now starts the session at the highest allowed effort with ultracode off in those cases, rather than only covering the workflows-off case. [[lines 558-566](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/model-config.md?plain=1#L558-L566)] [[Source](https://code.claude.com/docs/en/model-config#when-ultracode-is-available)]
* Noted that a `maxEffortLevel` or organization effort cap still limits the level a skill's or subagent's frontmatter `effort` can run at. [[line 599](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/model-config.md?plain=1#L599)] [[Source](https://code.claude.com/docs/en/model-config#adjust-effort-level)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Clarified that the `user.email` telemetry attribute is sent only to the OTel endpoint you configure, never to Anthropic, matching the existing guarantee for other OTel fields. [[line 1331](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/monitoring-usage.md?plain=1#L1331)] [[Source](https://code.claude.com/docs/en/monitoring-usage#data-privacy-considerations)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Documented that when a `claude remote-control` server's registration credential expires, it re-registers with the Anthropic API automatically and keeps serving its sessions. [[line 218](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/remote-control.md?plain=1#L218)] [[Source](https://code.claude.com/docs/en/remote-control#security)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* `maxEffortLevel` now documents that a cap below `xhigh` also makes ultracode unavailable on the models it applies to. [[line 958](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/settings-reference.md?plain=1#L958)] [[Source](https://code.claude.com/docs/en/settings-reference#maxeffortlevel)]
* `allowedChannelPlugins` entries can now be written as a `"plugin@marketplace"` string (e.g. `"telegram@claude-plugins-official"`) instead of an object; the string form requires v2.1.267+, and earlier versions reject the whole value if one is used. [[line 4033](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/settings-reference.md?plain=1#L4033)] [[Source](https://code.claude.com/docs/en/settings-reference#allowedchannelplugins)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Received the same model-effort-badge, clipboard-image-paste, and open-tab-switching updates as [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/ide-integrations.md), since this page mirrors that content. [[lines 95, 124, 130](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/vs-code.md?plain=1#L95)]

#### [workflows](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* The `/effort` menu now links to the fuller "when ultracode is available" explanation (workflows off, unsupported model, or an effort cap) instead of only mentioning `xhigh`-effort model support. [[line 148](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/claude-code/workflows.md?plain=1#L148)] [[Source](https://code.claude.com/docs/en/workflows#let-claude-decide-with-ultracode)]

-----

## API changes

### New Documents

#### [api/beta/organization/analytics](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/api/beta/organization/analytics.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/analytics)]

The Claude Enterprise Analytics API — activity summaries plus per-area usage for artifacts, chat projects, connectors, cost, plugins, skills, usage, and users — is now documented as a typed beta SDK endpoint group (`client.beta.organization.analytics.*` in Python/TypeScript/C#/Go/Java/PHP/Ruby, `ant beta:organization`), functionally identical to the existing [Admin API analytics reference](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/api/admin/analytics.md) and requiring no beta header beyond the standard `anthropic-version`.

#### [api/beta/organization/cost_report](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/api/beta/organization/cost_report.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/cost_report)]

Beta-typed mirror of the Admin API's service-level cost report endpoint, grouping USD cost by workspace or description at daily granularity.

#### [api/beta/organization/mcp_tunnels](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/api/beta/organization/mcp_tunnels.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/mcp_tunnels)]

Beta-typed mirror of the Admin API's organization-scoped MCP Tunnels endpoints (list, retrieve, archive, reveal/rotate token, and certificate management). The doc marks this org-scoped surface **deprecated**: new integrations should use the dedicated `/v1/tunnels` API (`anthropic-beta: mcp-tunnels-2026-06-22`) instead.

#### [api/beta/organization/rbac_groups](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/api/beta/organization/rbac_groups.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/rbac_groups)]

Beta-typed mirror of the Admin API's RBAC Groups endpoints (list, get, create, update, delete, and member management) for Claude Enterprise organizations; requires the `anthropic-beta: ce-user-management-2026-07-13` header.

#### [api/beta/organization/rbac_roles](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/api/beta/organization/rbac_roles.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/rbac_roles)]

Beta-typed mirror of the Admin API's read-only custom-roles catalog (list roles, get role, list role permissions) for Claude Enterprise organizations.

#### [api/beta/organization/spend_limits](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/api/beta/organization/spend_limits.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/spend_limits)]

Beta-typed mirror of the Admin API's per-user spend limit endpoints (set, get, delete, list effective limits) plus spend-limit increase requests (list, get, approve, deny).

#### [api/beta/organization/usage_report](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/api/beta/organization/usage_report.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/usage_report)]

Beta-typed mirror of the Admin API's Messages and Claude Code usage report endpoints.

#### [cli-sdks-libraries/cli/sessions-connect](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/cli-sdks-libraries/cli/sessions-connect.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/sessions-connect)]

New page for `ant beta:sessions connect`, which attaches your terminal to a live Managed Agents session: it loads and follows the transcript, and lets you send messages, interrupt the agent, and allow or deny tool calls waiting for approval. `--web` instead serves the Claude Console's session viewer locally and opens it in your browser, following every thread of a multiagent session.

### Changed documents

#### [manage-claude/admin-api](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/manage-claude/admin-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api)]

* Documents that the Python, TypeScript, C#, Go, Java, PHP, and Ruby SDKs now expose the Admin API under `client.beta.organization`, and the `ant` CLI under `ant beta:organization`. [[line 29](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/manage-claude/admin-api.md?plain=1#L29)] [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api#authentication)]

#### [manage-claude/user-management](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/manage-claude/user-management.md) [[Source](https://platform.claude.com/docs/en/manage-claude/user-management)]

* The "Remove user" endpoint reference now points at the beta org API's `users/remove.md`, distinct from the old admin `users/delete.md` naming. [[line 159](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/manage-claude/user-management.md?plain=1#L159)] [[Source](https://platform.claude.com/docs/en/manage-claude/user-management#remove-a-member)]

#### [managed-agents/events-and-streaming](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/managed-agents/events-and-streaming.md) [[Source](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)]

* Tool confirmation now also pauses under the new `auto` policy when the server reaches no determination, not just under `always_ask`; `agent.tool_use`/`agent.mcp_tool_use` events carry a new `evaluated_permission` field and, usually, an `evaluation` object recording which policy produced the outcome, shown in a worked example. [[lines 2143-2150](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/managed-agents/events-and-streaming.md?plain=1#L2143-L2150)] [[Source](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#tool-confirmation)]
* Noted that `ant beta:sessions connect` can open the same Console session viewer from the CLI or follow a session in your terminal. [[line 2774](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/managed-agents/events-and-streaming.md?plain=1#L2774)] [[Source](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#console-observability)]

#### [managed-agents/migration](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/managed-agents/migration.md) [[Source](https://platform.claude.com/docs/en/managed-agents/migration)]

* Updated the SDK-migration comparison tables to mention `auto` as a third `permission_policy` option, and to note that under `auto` a call the server evaluates as safe runs without ever reaching your client (unlike `always_ask`, which always does). [[line 620](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/managed-agents/migration.md?plain=1#L620), [1297](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/managed-agents/migration.md?plain=1#L1297)]

#### [managed-agents/permission-policies](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/managed-agents/permission-policies.md) [[Source](https://platform.claude.com/docs/en/managed-agents/permission-policies)]

* Added a new `auto` permission policy: the server evaluates each agent or MCP tool call and either runs it (safe), denies it (high-risk, with no client override), or pauses it for approval (no determination reached). Set it via `permission_policy: {"type": "auto"}` on a toolset's `default_config` or a per-tool `configs` entry; no toolset uses it by default. Documented with a full multi-language example that sets `auto` as the default for an agent toolset and an MCP toolset while overriding `bash` to `always_ask`. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/managed-agents/permission-policies.md?plain=1#L19), [654-663](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/managed-agents/permission-policies.md?plain=1#L654-L663)] [[Source](https://platform.claude.com/docs/en/managed-agents/permission-policies#let-the-server-evaluate-each-call-with-auto)]

#### [managed-agents/reference](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/managed-agents/reference.md) [[Source](https://platform.claude.com/docs/en/managed-agents/reference)]

* `agent.tool_use` and `agent.mcp_tool_use` event descriptions now note they carry `evaluated_permission` and, usually, `evaluation`. [[lines 34, 36](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/managed-agents/reference.md?plain=1#L34)]

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Added a September 10, 2026 entry for the `auto` permission policy and `ant beta:sessions connect`. [[lines 15-18](https://github.com/gpambrozio/ClaudeDocs/blob/70c7d53a1f7f662f69d1b5aad9f68d5e6b8ae8f7/docs-md/api/release-notes/overview.md?plain=1#L15-L18)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#september-10-2026)]

### A note on the rest of this diff

Beyond the entries above, this sync touched roughly 1,500 files, almost all of it the same one-line change repeated: every guide and per-language SDK reference page (Python, TypeScript, C#, Go, Java, PHP, Ruby, and the CLI, across `api/admin`, `api/beta`, and each per-language tree) that used to link to an `api/admin/*` reference page now links to the equivalent `api/beta/organization/*` page instead. Per the "ignore small URL changes" rule, those are omitted here individually; the underlying reason for all of them is the new beta SDK surface described in the New Documents section above.
