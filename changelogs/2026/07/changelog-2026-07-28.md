# [Claude docs changes for July 28th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959)]

## Executive Summary
- Claude Desktop can now connect to a Cloud gateway deployment: point its managed `bootstrapUrl` at `/user/bootstrap` and opt a policy in with a `desktop` key to serve it model access, tool restrictions, and feature gates (requires gateway server v2.1.203+).
- Sandboxing gains a `strictAllowlist` setting that denies sandboxed commands access to any host outside the domain allowlist instead of prompting for approval (v2.1.219+).
- Hooks documentation now spells out that settings-file, managed-policy, and plugin hooks all run inside subagents, with `agent_id`/`agent_type` identifying the subagent, and that hook entries merge across settings levels rather than overriding each other.
- The Agent SDK Python `ResultMessage` gains a `terminal_reason` field describing why the query loop ended, and `model_usage` entries can now include `canonicalModel` and `provider`.
- Remote Control's "only available via api.anthropic.com" error now names the specific variable (e.g. `CLAUDE_CODE_USE_BEDROCK` or a custom `ANTHROPIC_BASE_URL`) that routed the session away from the Anthropic API (v2.1.219+).

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* `ResultMessage` gained a `terminal_reason` field explaining why the query loop terminated (`"completed"`, `"max_turns"`, `"aborted_streaming"`, etc.); `None` on older CLI versions. [[lines 1597-1607](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/agent-sdk/python.md?plain=1#L1597-L1607)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#resultmessage)]
* `model_usage` values are now typed as a `ModelUsage` TypedDict (importable from `claude_agent_sdk.types`), which can include a new `canonicalModel` key (the pricing-lookup model ID) and a `provider` key (e.g. `firstParty`, `bedrock`, `vertex`, `foundry`, `mantle`, `gateway`). [[line 1630](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/agent-sdk/python.md?plain=1#L1630)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#resultmessage)]

#### [claude-apps-gateway](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/claude-apps-gateway.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway)]

* New "Connect Claude Desktop" section: Claude Desktop can sign in to the same gateway via its own `bootstrapUrl` managed-configuration key, using a separate sign-in flow from the CLI and its own per-user session. Requires gateway server v2.1.203+. [[lines 325-328](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/claude-apps-gateway.md?plain=1#L325-L328)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway#connect-claude-desktop)]
* Feature-availability table now lists "Claude Desktop" support as "Available with opt-in", served at `/user/bootstrap` once a policy opts in with a `desktop` key. [[line 361](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/claude-apps-gateway.md?plain=1#L361)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway#availability-and-limitations)]

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* New "Claude Desktop overlay" section documenting the `/user/bootstrap` endpoint: it derives the model list, disabled tools, and egress allowlist from a policy's `cli` block, plus a new `desktop` block (`modelDiscoveryEnabled`, `coworkTabEnabled`, `isLocalDevMcpEnabled`, `disableAutoUpdates`, `banner`, etc.) for Desktop-only feature gates. Requires gateway server v2.1.203+ and an explicit `desktop` opt-in on the matching policy. [[lines 475-497](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L475-L497)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#claude-desktop-overlay)]
* Notes that embedding hosts able to supply policy via the SDK `managedSettings` option now explicitly include Claude Desktop as an example. [[line 761](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L761)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#client-side-managed-settings)]

#### [claude-apps-gateway-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/claude-apps-gateway-deploy.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy)]

* New audit events `desktop_bootstrap.serve` and `desktop_bootstrap.denied` are emitted for Claude Desktop bootstrap requests; denial reasons include `not_configured`, `policy_not_opted_in`, and `no_policy_matched`. [[lines 96-100](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/claude-apps-gateway-deploy.md?plain=1#L96-L100)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy#logs)]
* New troubleshooting row for when Claude Desktop can't fetch its bootstrap configuration (404 from `/user/bootstrap`). [[line 210](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/claude-apps-gateway-deploy.md?plain=1#L210)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy#troubleshooting)]

#### [fullscreen](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* Clipboard copying now also works for long selections inside GNU screen; before v2.1.219, selections longer than roughly 570 characters printed base64 text into the window instead of copying. [[line 150](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/fullscreen.md?plain=1#L150)] [[Source](https://code.claude.com/docs/en/fullscreen#keep-native-text-selection)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Clarifies that hooks from settings files, managed policy settings, and plugins all run inside subagents; tool-event hooks fire the same as in the main conversation and carry `agent_id`/`agent_type` in their input. [[line 176](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/hooks.md?plain=1#L176)] [[Source](https://code.claude.com/docs/en/hooks#hook-locations)]
* Documents that hook entries merge across settings levels instead of replacing each other, and that `disableAllHooks` can't disable managed hooks from outside managed settings. [[line 178](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/hooks.md?plain=1#L178)] [[Source](https://code.claude.com/docs/en/hooks#hook-locations)]
* Documents that the `allowedHttpHookUrls` and `httpHookAllowedEnvVars` HTTP hook allowlists apply to hooks from every source, including managed policy settings. [[line 179](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/hooks.md?plain=1#L179)] [[Source](https://code.claude.com/docs/en/hooks#hook-locations)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* The "Remote Control is only available via api.anthropic.com" error message now names the specific variable that routed the session away, such as `CLAUDE_CODE_USE_BEDROCK` or a custom `ANTHROPIC_BASE_URL`; before v2.1.219 the message gave no such detail. [[lines 268-269](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/remote-control.md?plain=1#L268-L269)] [[Source](https://code.claude.com/docs/en/remote-control#”remote-control-is-only-available-when-using-claude-via-api-anthropic-com”)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* New `strictAllowlist` setting: when set to `true` in user, managed, or CLI `--settings` settings, sandboxed commands are denied access to hosts outside the allowlist instead of being prompted for approval. Doesn't affect in-process tools like `WebFetch`, and has no effect if set in repo-level `.claude/settings.json`. Requires v2.1.219+. [[line 279](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/sandboxing.md?plain=1#L279)] [[Source](https://code.claude.com/docs/en/sandboxing#network-isolation)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Documents the new `network.strictAllowlist` setting (default `false`), covered in more detail in [sandboxing](#claude-code-changes). [[line 398](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/settings.md?plain=1#L398)] [[Source](https://code.claude.com/docs/en/settings#sandbox-settings)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Clarifies that session-wide hooks in `settings.json` also fire inside subagents: tool-event hooks fire for the subagent's own tool calls, and `SubagentStart`/`SubagentStop` fire when a subagent starts or finishes. [[lines 531-533](https://github.com/gpambrozio/ClaudeDocs/blob/46bd9838fb2482c3b8ea5816a8ed88b22d6d1959/docs-md/claude-code/sub-agents.md?plain=1#L531-L533)] [[Source](https://code.claude.com/docs/en/sub-agents#define-hooks-for-subagents)]

-----

## API changes

No significant documentation changes today — the only diffs in `docs-md/api` were Cloudflare email-obfuscation hash rotations in `files.md` and `thinking.md`, with no visible content changes.
