# [Claude docs changes for Oct, 29th 2026](https://github.com/gpambrozio/ClaudeDocs/tree/b7e0a33c0b262d0c9d74025fb6e160321f9559e4) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/b7e0a33c0b262d0c9d74025fb6e160321f9559e4)]

## Executive Summary
- Nearly every API feature page now ends with a standardized "Availability" section (API support for Messages API vs. Managed Agents, platforms, required beta headers, and ZDR/HIPAA data handling), backed by new `featureMetadata` front matter. The ZDR/HIPAA table in API and data retention was reorganized to match.
- The first-party Claude API request size limit for Messages and Token Counting is documented as 128 MB (previously 32 MB), and "direct Claude API" wording became "first-party Claude API".
- Claude Code gained `CLAUDE_CODE_EFFORT_LEVEL=auto` (send no effort level), `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS`, and MCP improvements: `${VAR:-default}` expansion, OAuth behind authenticating proxies, and handling of tools with invalid input schemas.
- Plugin docs now describe two Anthropic marketplaces (official and community), deprecate `claude-code-plugins`, and add README "Advice" output to `claude plugin validate`.
- Enterprise docs clarify which managed source supplies login keys (`forceLoginOrgUUID`, `forceLoginMethod`). Self-hosted environments gained an orchestrator `--shutdown-drain-sec` flag.

## New Claude Code versions

No new version files in this commit.

-----

## Claude Code changes

### New Documents

No new documents.

### Changed documents

#### [agent-sdk/agent-loop](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/agent-sdk/agent-loop.md) [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop)]

* Reworded the definition of a "turn" and the examples of how many turns simple and complex tasks take. [[lines 20-27](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/agent-sdk/agent-loop.md?plain=1#L20-L27)] [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop#the-loop-at-a-glance)]

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* Returning `PermissionResultAllow` with more than 4,096 `updated_permissions` items makes Claude Code treat the result as invalid and deny the tool call. [[line 1245](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/agent-sdk/python.md?plain=1#L1245)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#permissionresultallow)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Same 4,096-item limit on `updatedPermissions` for `allow` results. [[line 1404](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1404)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#permissionresult)]
* `CronCreateOutput` and `CronListOutput` gained an optional `nextFireAt` (epoch ms, jitter applied). [[lines 4705-4743](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L4705-L4743)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#croncreate)]
* `setMcpServers()` resolves after new servers connect or fail. Errors starting with `Blocked by enterprise` mean policy refused the server. [[lines 5462-5479](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L5462-L5479)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#mcpsetserversresult)]

#### [authentication](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/authentication.md) [[Source](https://code.claude.com/docs/en/authentication)]

* If the browser shows a login code instead of redirecting back, paste it at the `Paste code here if prompted` prompt. [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/authentication.md?plain=1#L16)] [[Source](https://code.claude.com/docs/en/authentication#log-in-to-claude-code)]
* Deploy `forceLoginMethod` and `forceLoginOrgUUID` through device management, because server-managed settings arrive only after authentication. [[line 182](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/authentication.md?plain=1#L182)] [[Source](https://code.claude.com/docs/en/authentication#restrict-login-to-your-organization)]

#### [claude-apps-gateway](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/claude-apps-gateway.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway)]

* Clarified how `forceLoginOrgUUID` from a parent is honored and how `managedSourcesBehavior: "merge"` applies. [[lines 445-453](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/claude-apps-gateway.md?plain=1#L445-L453)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway#settings-the-locks-dont-cover)]

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* New `timeouts.upstream_ttfb_ms` setting (default 120000 ms) for how long the gateway waits for upstream response headers. Non-Anthropic providers wait up to an hour unless set (gateway v2.1.295+). [[lines 630-633](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L630-L633)] [[line 1406](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L1406)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#multiple-upstreams)]
* Examples now use a custom restricted model id. `sshTransport` needs Claude Code v2.1.293+ on the gateway server. [[lines 420-879](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L420-L879)] [[line 1152](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L1152)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#bedrock-in-another-aws-account)]

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* `claude --cloud` and `--teleport` require claude.ai sign-in. Added the "Cloud sessions aren't available with this Console sign-in" message and its fix (`claude auth login`). [[lines 227-440](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L227-L440)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#teleport-is-unavailable)]

#### [claude-directory](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* Windows path note for `~/.claude`, and `CLAUDE_CONFIG_DIR` relocates every path on the page. Notes when `~/.claude.json` is created. [[lines 7-75](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/claude-directory.md?plain=1#L7-L75)] [[Source](https://code.claude.com/docs/en/claude-directory#explore-the-claude-directory)]

#### [corporate-launcher](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/corporate-launcher.md) [[Source](https://code.claude.com/docs/en/corporate-launcher)]

* Sessions opened from `claude-cli://` deep links bypass the launcher. Use `disableDeepLinkRegistration` to prevent them. [[line 35](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/corporate-launcher.md?plain=1#L35)] [[Source](https://code.claude.com/docs/en/corporate-launcher#processes-that-start-outside-the-launcher)]

#### [deep-links](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/deep-links.md) [[Source](https://code.claude.com/docs/en/deep-links)]

* Links only work on a machine after sending a prompt in an interactive session, which registers the handler. [[lines 7-103](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/deep-links.md?plain=1#L7-L103)] [[Source](https://code.claude.com/docs/en/deep-links#launch-sessions-from-links)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Added guidance for the "earlier layout" (no environment selector under the prompt box), including the Claude Desktop v4.29.0+ requirement for third-party provider sessions on your organization's infrastructure. [[lines 42-2127](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/desktop.md?plain=1#L42-L2127)] [[Source](https://code.claude.com/docs/en/desktop#start-a-session)]

#### [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/desktop-changelog.md) [[Source](https://code.claude.com/docs/en/desktop-changelog)]

* Same earlier-layout notes as the desktop page. [[lines 42-2127](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/desktop-changelog.md?plain=1#L42-L2127)] [[Source](https://code.claude.com/docs/en/desktop-changelog#start-a-session)]

#### [desktop-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/desktop-quickstart.md) [[Source](https://code.claude.com/docs/en/desktop-quickstart)]

* Pointer for users who see no environment under the prompt box. [[line 56](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/desktop-quickstart.md?plain=1#L56)] [[Source](https://code.claude.com/docs/en/desktop-quickstart#start-your-first-session)]

#### [devcontainer](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/devcontainer.md) [[Source](https://code.claude.com/docs/en/devcontainer)]

* Fallback for sign-in failing in containers: use the login URL shown above the paste prompt. [[line 78](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/devcontainer.md?plain=1#L78)] [[Source](https://code.claude.com/docs/en/devcontainer#add-claude-code-to-your-dev-container)]

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Marketplace add for GitHub repos supports `#ref` to pin a branch or tag. Linked to the new Anthropic marketplaces page. [[line 192](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/discover-plugins.md?plain=1#L192)] [[line 382](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/discover-plugins.md?plain=1#L382)] [[Source](https://code.claude.com/docs/en/discover-plugins#add-a-marketplace)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS`: removes `run_in_background`, the Ctrl+B shortcut and background runs of forked skills. [[line 232](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/env-vars.md?plain=1#L232)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_EFFORT_LEVEL` description updated (precedence over `--effort` and `/effort`). [[line 275](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/env-vars.md?plain=1#L275)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* Feature-flag fetching also controls excluding MCP tools whose input schema the API would reject. [[line 583](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/env-vars.md?plain=1#L583)] [[Source](https://code.claude.com/docs/en/env-vars#features-that-need-feature-flag-fetching)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New "Waiting for API response" banner section (20 s without data). [[line 487](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/errors.md?plain=1#L487)] [[Source](https://code.claude.com/docs/en/errors#waiting-for-api-response)]
* New "Command contains an invisible character" error (U+FEFF/U+180E) and expanded "No shell command was run" guidance. [[lines 3598-3614](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/errors.md?plain=1#L3598-L3614)] [[line 4572](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/errors.md?plain=1#L4572)] [[Source](https://code.claude.com/docs/en/errors#no-shell-command-in-a-skill-or-command-was-run)]
* New "The Claude Code program for this computer could not be found" VS Code extension error. [[line 5448](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/errors.md?plain=1#L5448)] [[Source](https://code.claude.com/docs/en/errors#the-claude-code-program-for-this-computer-could-not-be-found)]
* Tool input schema error: from v2.1.300 Claude Code retries without the rejected tool's parameters. [[line 2497](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/errors.md?plain=1#L2497)] [[Source](https://code.claude.com/docs/en/errors#tool-input-schema-is-invalid)]
* Console sign-in cloud session error added to the lookup table. [[line 218](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/errors.md?plain=1#L218)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Now covers Claude Opus 5.5 (available) plus Opus 5 and Opus 4.8 (research preview). Opus 5 and 4.8 on Console need provisioned access, and Opus 5.5 depends on usage tier. [[lines 7-148](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/fast-mode.md?plain=1#L7-L148)] [[Source](https://code.claude.com/docs/en/fast-mode#speed-up-responses-with-fast-mode)]
* Console admins enable fast mode in Claude Code preferences. Rate limits are separate from standard Opus. [[lines 145-202](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/fast-mode.md?plain=1#L145-L202)] [[Source](https://code.claude.com/docs/en/fast-mode#enable-fast-mode-for-your-organization)]

#### [feature-availability](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/feature-availability.md) [[Source](https://code.claude.com/docs/en/feature-availability)]

* Fast mode with Opus 5 and 4.8 requires provisioning. [[line 89](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/feature-availability.md?plain=1#L89)] [[Source](https://code.claude.com/docs/en/feature-availability#cli-capabilities-that-vary-by-provider)]

#### [github-actions](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/github-actions.md) [[Source](https://code.claude.com/docs/en/github-actions)]

* Example now uses the `claude-plugins-official` marketplace. [[line 240](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/github-actions.md?plain=1#L240)] [[Source](https://code.claude.com/docs/en/github-actions#run-a-skill)]

#### [github-enterprise-server](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/github-enterprise-server.md) [[Source](https://code.claude.com/docs/en/github-enterprise-server)]

* New troubleshooting for "Connection test passed, but a second test failed/could not run" (allow Anthropic's outbound IPs). [[line 220](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/github-enterprise-server.md?plain=1#L220)] [[Source](https://code.claude.com/docs/en/github-enterprise-server#connection-test-passes-but-a-second-test-fails)]

#### [iam](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/iam.md) [[Source](https://code.claude.com/docs/en/iam)]

* Same login-code and `forceLogin*` deployment notes as the authentication page. [[lines 16-182](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/iam.md?plain=1#L16-L182)] [[Source](https://code.claude.com/docs/en/iam#log-in-to-claude-code)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* Same VS Code changes as the vs-code page (command menu, Thinking switch, worktree banner, Focus view shortcut, `session` URI parameter, new error). [[lines 132-925](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/ide-integrations.md?plain=1#L132-L925)] [[Source](https://code.claude.com/docs/en/ide-integrations#use-the-prompt-box)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Background commands can be disabled with `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1` (also removes Ctrl+B). [[line 331](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/interactive-mode.md?plain=1#L331)] [[Source](https://code.claude.com/docs/en/interactive-mode#how-backgrounding-works)]

#### [managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/managed-settings.md) [[Source](https://code.claude.com/docs/en/managed-settings)]

* New section "Which managed source supplies login keys": `forceLoginOrgUUID`, `forceLoginMethod` and gateway login keys come from the MDM policy or managed file ahead of remote settings. [[line 181](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/managed-settings.md?plain=1#L181)] [[Source](https://code.claude.com/docs/en/managed-settings#which-managed-source-supplies-login-keys)]
* Merge table gained "highest-ranked source only" and "login keys" rows. [[lines 207-209](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/managed-settings.md?plain=1#L207-L209)] [[Source](https://code.claude.com/docs/en/managed-settings#compose-every-managed-source)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Removing a remote server also deletes stored OAuth tokens and client registration (tokens are not revoked at the issuer). [[line 241](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/mcp.md?plain=1#L241)] [[Source](https://code.claude.com/docs/en/mcp#managing-your-servers)]
* New `✘ Blocked by enterprise managed policy` server status. [[line 254](https://github.com/gpambrozo/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/mcp.md?plain=1#L254)] [[Source](https://code.claude.com/docs/en/mcp#server-status)]
* `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` turns off automatic backgrounding. [[line 471](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/mcp.md?plain=1#L471)] [[Source](https://code.claude.com/docs/en/mcp#automatic-backgrounding-of-long-tool-calls)]
* Environment variable expansion rewritten: `${VAR}` and `${VAR:-default}` in `command`, `args`, `env`, `url`, `headers`; new section on empty-string variables. [[lines 828-855](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/mcp.md?plain=1#L828-L855)] [[Source](https://code.claude.com/docs/en/mcp#environment-variable-expansion-in-mcpjson)]
* New section on OAuth for servers behind an authenticating proxy (v2.1.299+). [[line 1142](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/mcp.md?plain=1#L1142)] [[Source](https://code.claude.com/docs/en/mcp#use-oauth-with-a-server-behind-an-authenticating-proxy)]
* Tool input schema handling: tools breaking API rules are excluded, a new "Tools whose input schema the API refuses" section (v2.1.300+ retries without parameters), and behavior when feature flags are unavailable. [[lines 1555-1575](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/mcp.md?plain=1#L1555-L1575)] [[Source](https://code.claude.com/docs/en/mcp#tools-with-invalid-input-schemas)]
* New "Change the description length limits" via `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH`. [[line 1731](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/mcp.md?plain=1#L1731)] [[Source](https://code.claude.com/docs/en/mcp#change-the-description-length-limits)]

#### [mcp-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/mcp-quickstart.md) [[Source](https://code.claude.com/docs/en/mcp-quickstart)]

* Added the "Blocked by enterprise managed policy" status. [[line 64](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/mcp-quickstart.md?plain=1#L64)] [[Source](https://code.claude.com/docs/en/mcp-quickstart#add-and-verify-a-server)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* `CLAUDE_CODE_EFFORT_LEVEL=auto` (or `unset`) makes Claude Code send no effort level so the API default applies. New "Send no effort level" section describing `/effort status` output. [[lines 688-726](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/model-config.md?plain=1#L688-L726)] [[Source](https://code.claude.com/docs/en/model-config#set-the-effort-level)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* API request events now include `cache_creation_5m_tokens` and `cache_creation_1h_tokens`. [[line 860](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/monitoring-usage.md?plain=1#L860)] [[Source](https://code.claude.com/docs/en/monitoring-usage#api-request-event)]

#### [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Advice to give a marketplace a distinctive top-level name before pushing it. [[line 219](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugin-marketplaces.md?plain=1#L219)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#host-your-marketplace)]

#### [plugins](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* Claude Code adds the official marketplace on first interactive start unless managed policy prevents it. The official tier covers `claude-plugins-official` and related names. [[lines 65-87](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins.md?plain=1#L65-L87)] [[Source](https://code.claude.com/docs/en/plugins#get-plugins-from-a-marketplace)]

#### [plugins/anthropic-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins/anthropic-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugins/anthropic-marketplaces)]

* Reduced from three to two marketplaces: official (`claude-plugins-official`) and community (`claude-community`), compared in a table. [[lines 5-27](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins/anthropic-marketplaces.md?plain=1#L5-L27)] [[Source](https://code.claude.com/docs/en/plugins/anthropic-marketplaces#anthropics-marketplaces)]
* The `claude-code-plugins` marketplace is deprecated. `ralph-wiggum` is now `ralph-loop`, and `claude-opus-4-5-migration` is retired. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins/anthropic-marketplaces.md?plain=1#L36)] [[Source](https://code.claude.com/docs/en/plugins/anthropic-marketplaces#deprecated-claude-code-plugins-marketplace)]
* The community marketplace must be added with `/plugin marketplace add anthropics/claude-plugins-community`. [[line 68](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins/anthropic-marketplaces.md?plain=1#L68)] [[Source](https://code.claude.com/docs/en/plugins/anthropic-marketplaces#add-the-community-marketplace)]

#### [plugins/cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins/cli-reference.md) [[Source](https://code.claude.com/docs/en/plugins/cli-reference)]

* `claude plugin validate` now emits README "Advice" when a plugin README lacks an install line. It is exposed as `advice` in `--json` output, doesn't change the exit code, and has a new `contents` description. [[lines 637-680](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins/cli-reference.md?plain=1#L637-L680)] [[Source](https://code.claude.com/docs/en/plugins/cli-reference#output-and-exit-codes)]

#### [plugins/create](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins/create.md) [[Source](https://code.claude.com/docs/en/plugins/create)]

* Links to worked examples in the `claude-plugins-official` repository. [[line 375](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins/create.md?plain=1#L375)] [[Source](https://code.claude.com/docs/en/plugins/create#next-steps)]

#### [plugins/create-marketplace](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins/create-marketplace.md) [[Source](https://code.claude.com/docs/en/plugins/create-marketplace)]

* Same distinctive-name advice as plugin-marketplaces. [[line 219](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins/create-marketplace.md?plain=1#L219)] [[Source](https://code.claude.com/docs/en/plugins/create-marketplace#host-your-marketplace)]

#### [plugins/install](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins/install.md) [[Source](https://code.claude.com/docs/en/plugins/install)]

* `#ref` pinning for GitHub marketplaces, plus a link to Anthropic's marketplaces. [[lines 192-382](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins/install.md?plain=1#L192-L382)] [[Source](https://code.claude.com/docs/en/plugins/install#add-a-marketplace)]

#### [plugins/mods/api](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins/mods/api.md) [[Source](https://code.claude.com/docs/en/plugins/mods/api)]

* A foreground Bash/PowerShell command from `$.tool.call` that was already running when the user stopped the turn is stopped at its timeout. [[line 337](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins/mods/api.md?plain=1#L337)] [[Source](https://code.claude.com/docs/en/plugins/mods/api#work-your-mod-started-before-the-interruption)]

#### [plugins/overview](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins/overview.md) [[Source](https://code.claude.com/docs/en/plugins/overview)]

* Same official-marketplace auto-add and tier notes as the plugins page. [[lines 65-87](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins/overview.md?plain=1#L65-L87)] [[Source](https://code.claude.com/docs/en/plugins/overview#get-plugins-from-a-marketplace)]

#### [plugins/publish](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins/publish.md) [[Source](https://code.claude.com/docs/en/plugins/publish)]

* Pick a marketplace name other authors are unlikely to choose, since users can't have two marketplaces with the same name. [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins/publish.md?plain=1#L95)] [[Source](https://code.claude.com/docs/en/plugins/publish#add-the-marketplace-file-to-your-repository)]

#### [plugins/security](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins/security.md) [[Source](https://code.claude.com/docs/en/plugins/security)]

* Link to the Anthropic marketplaces page. [[line 75](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/plugins/security.md?plain=1#L75)] [[Source](https://code.claude.com/docs/en/plugins/security#official-marketplace-names)]

#### [self-hosted-environments-configuration](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/self-hosted-environments-configuration.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration)]

* New "Stop or restart the orchestrator" section: `--shutdown-drain-sec` lets running `spawn-runner` hooks finish on `SIGTERM` (v2.1.299+), with sizing guidance for stop timeouts and systemd `KillMode`. [[lines 456-488](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L456-L488)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#stop-or-restart-the-orchestrator)]
* Runner examples now pass `--base-dir '<writable-dir>'`. [[lines 17-20](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L17-L20)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#wrapper-scripts)]

#### [self-hosted-environments-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/self-hosted-environments-deploy.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy)]

* Runner shutdown timing: runners log how long they need after `SIGTERM`, with `terminationGracePeriodSeconds` and `stop_grace_period` guidance. [[line 582](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L582)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#shutdown-timing)]
* New troubleshooting for runner not appearing, log redirection, `was paused or too slow` and `Nobody can read this process's stdout anymore`. [[lines 841-909](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L841-L909)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#troubleshooting)]

#### [self-hosted-environments-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/self-hosted-environments-quickstart.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-quickstart)]

* Minor example update for the `--base-dir` flag.

#### [self-hosted-environments-reference](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/self-hosted-environments-reference.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-reference)]

* Added the `--shutdown-drain-sec <n>` orchestrator flag (default 0). [[line 94](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/self-hosted-environments-reference.md?plain=1#L94)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-reference#orchestrator-cli-flags)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* First-party sign-in keys (`forceLoginOrgUUID`, `forceLoginMethod` "claudeai"/"console") are exceptions to the no-merge rule. [[line 153](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/server-managed-settings.md?plain=1#L153)] [[Source](https://code.claude.com/docs/en/server-managed-settings#per-key-exceptions-across-managed-sources)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* Idle compaction conditions refined (session types, about an hour idle with the computer awake) and how to turn it off. [[lines 2423-2474](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/settings-reference.md?plain=1#L2423-L2474)] [[Source](https://code.claude.com/docs/en/settings-reference#idlecompaction)]
* Managed merge behavior: keys read from the highest-priority source only, and login-key lookup. [[lines 5584-5595](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/settings-reference.md?plain=1#L5584-L5595)] [[Source](https://code.claude.com/docs/en/settings-reference#managedsourcesbehavior)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* New troubleshooting: `<` and `>` in skill `description`/`when_to_use` display as `&lt;`/`&gt;`; use square brackets or `argument-hint`. [[line 1228](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/skills.md?plain=1#L1228)] [[Source](https://code.claude.com/docs/en/skills#angle-brackets-in-a-skill-description-show-as-lt-and-gt)]
* "No shell command was run" explanation for dynamic context commands. [[line 779](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/skills.md?plain=1#L779)] [[Source](https://code.claude.com/docs/en/skills#when-no-shell-command-was-run)]

#### [slash-commands](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/slash-commands.md) [[Source](https://code.claude.com/docs/en/slash-commands)]

* Same skills changes (angle-bracket display issue, "No shell command was run"). [[lines 779-1228](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/slash-commands.md?plain=1#L779-L1228)] [[Source](https://code.claude.com/docs/en/slash-commands#when-no-shell-command-was-run)]

#### [troubleshoot-install](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/troubleshoot-install.md) [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

* Rewrote the browser-login fallback as three steps (copy URL, sign in, paste code). Added a WSL2 `BROWSER` example. [[lines 1168-1196](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/troubleshoot-install.md?plain=1#L1168-L1196)] [[Source](https://code.claude.com/docs/en/troubleshoot-install#oauth-login-fails-in-wsl2-ssh-or-containers)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* New command menu (`/`) and a Thinking switch. Thinking blocks showing only a label need `showThinkingSummaries`. [[lines 132-190](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/vs-code.md?plain=1#L132-L190)] [[Source](https://code.claude.com/docs/en/vs-code#use-the-prompt-box)]
* New section on reopening a conversation that moved into a worktree. [[line 583](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/vs-code.md?plain=1#L583)] [[Source](https://code.claude.com/docs/en/vs-code#reopen-a-conversation-that-moved-into-a-worktree)]
* New "Toggle Focus view" shortcut. The URI handler's `session` parameter supports worktree sessions in v2.1.300+. [[line 642](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/vs-code.md?plain=1#L642)] [[line 688](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/vs-code.md?plain=1#L688)] [[Source](https://code.claude.com/docs/en/vs-code#vs-code-commands-and-shortcuts)]
* Linked the new "program for this computer could not be found" error. [[line 925](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/vs-code.md?plain=1#L925)] [[Source](https://code.claude.com/docs/en/vs-code#fix-common-issues)]

#### [worktrees](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/worktrees.md) [[Source](https://code.claude.com/docs/en/worktrees)]

* `--worktree` reuses an existing worktree of the same name. New troubleshooting for `Can only use --worktree in a git repository` and `belongs to a different repository` / `is a leftover worktree`. [[line 213](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/worktrees.md?plain=1#L213)] [[lines 352-366](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/claude-code/worktrees.md?plain=1#L352-L366)] [[Source](https://code.claude.com/docs/en/worktrees#reuse-a-worktree-name)]

-----

## API changes

### New Documents

No new documents.

### Changed documents

Most feature pages below also gained the new `featureMetadata` front matter and an `Availability` section (API support for the Messages API and Managed Agents, platform status, required beta headers, and ZDR/HIPAA data handling). Only pages with other substantive edits are described in detail.

#### [about-claude/models/optimizing-for-cost-and-intelligence](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/about-claude/models/optimizing-for-cost-and-intelligence.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)]

* New measurement of Claude Haiku 5.5 subagents under Opus 5.5 on an internal coding benchmark in Managed Agents: about 30% lower cost per attempt with 3-4 points fewer passes, an alternative to lowering effort rather than better. [[lines 598-1074](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/about-claude/models/optimizing-for-cost-and-intelligence.md?plain=1#L598-L1074)] [[Source](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#orchestrator-strategy-delegate-bulk-work)]
* Advice to judge pairings on your own workload; removed the Haiku 5.5 worker note. [[lines 533-590](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/about-claude/models/optimizing-for-cost-and-intelligence.md?plain=1#L533-L590)] [[Source](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#combine-models)]

#### [about-claude/pricing](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* Tokenizer note now names `claude-mythos-preview`. [[line 510](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/about-claude/pricing.md?plain=1#L510)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing#how-is-token-usage-calculated)]

#### [agents-and-tools/tool-use/advisor-tool](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/agents-and-tools/tool-use/advisor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

* The single executor/advisor compatibility table became per-executor-model lists of supported advisor models. Added Availability (beta on Claude API, AWS, Google Cloud Anthropic managed), beta header, and ZDR info. [[lines 1814-2053](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L1814-L2053)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#model-compatibility)]

#### [api/errors](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/api/errors.md) [[Source](https://platform.claude.com/docs/en/api/errors)]

* Messages and Token Counting request size limit raised from 32 MB to 128 MB on the first-party API. [[lines 45-54](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/api/errors.md?plain=1#L45-L54)] [[Source](https://platform.claude.com/docs/en/api/errors#request-size-limits)]

#### [api/overview](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/api/overview.md) [[Source](https://platform.claude.com/docs/en/api/overview)]

* Request limit now 128 MB for the first-party API. Claude Platform on AWS, Google Cloud (Anthropic managed) and Microsoft Foundry have their own Messages/Token Counting limits (32 MB). [[lines 106-118](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/api/overview.md?plain=1#L106-L118)] [[Source](https://platform.claude.com/docs/en/api/overview#request-size-limits)]

#### [api/opentelemetry/spans](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/api/opentelemetry/spans.md) [[Source](https://platform.claude.com/docs/en/api/opentelemetry/spans)]

* Availability metadata added (beta across all platforms). API spans for any cloud-platform request lack `server.address`, `server.port` and `url.full`. [[lines 12-87](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/api/opentelemetry/spans.md?plain=1#L12-L87)] [[Source](https://platform.claude.com/docs/en/api/opentelemetry/spans#spans)]

#### [api/service-tiers](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/api/service-tiers.md) [[Source](https://platform.claude.com/docs/en/api/service-tiers)]

* Marked service tiers as legacy and added an Availability section. [[lines 7-252](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/api/service-tiers.md?plain=1#L7-L252)] [[Source](https://platform.claude.com/docs/en/api/service-tiers#service-tiers)]

#### [build-with-claude/batch-processing](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/build-with-claude/batch-processing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]

* The Data retention section (29 days, not ZDR eligible) moved into the new Availability / Data handling section. [[lines 1821-1865](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/build-with-claude/batch-processing.md?plain=1#L1821-L1865)] [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing#batch-storage-and-privacy)]

#### [build-with-claude/compaction](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/build-with-claude/compaction.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

* Comparison table and links now point to each compaction page's "API support" section instead of "Compatibility". The same Availability restructuring applies to the on-demand, background, keep-recent-turns, thinking-blocks and threshold pages. [[lines 17-45](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/build-with-claude/compaction.md?plain=1#L17-L45)] [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction#choose-how-to-compact)]

#### [build-with-claude/effort](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/build-with-claude/effort.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

* Per-model recommendations consolidated under one "Recommended effort levels" heading, ordered newest first, with links to each model's overview and prompting guide. Opus 4.7's table became a list. [[lines 253-362](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/build-with-claude/effort.md?plain=1#L253-L362)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort#recommended-effort-levels)]
* Effort is documented as always on for both the Messages API (`output_config.effort`) and Managed Agents (`effort` on the model object). [[lines 37-40](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/build-with-claude/effort.md?plain=1#L37-L40)] [[line 698](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/build-with-claude/effort.md?plain=1#L698)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort#effort-only-system-message-the-new-level-takes-effect-from-the-next-user-turn)]

#### [build-with-claude/fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/build-with-claude/fast-mode.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

* Reorganized: "Supported platforms" and "Model availability" merged into Availability with Messages API and Managed Agents support, and Pricing moved to the end. Documents Opus 5.5 on Claude API, Google Cloud (Anthropic managed) and Microsoft Foundry (hosted on Azure). Opus 5 and 4.8 remain research preview and require the `fast-mode-2026-02-01` beta header. [[lines 7-24](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/build-with-claude/fast-mode.md?plain=1#L7-L24)] [[lines 659-727](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/build-with-claude/fast-mode.md?plain=1#L659-L727)] [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode#fast-mode)]

#### [build-with-claude/fallback-credit](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/build-with-claude/fallback-credit.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/fallback-credit)]

* Added availability: beta on Claude API, AWS, Bedrock, Google Cloud and Foundry. On Bedrock and Google Cloud the token is bound to the caller identity and `allowed_fallback_models` isn't exposed. [[lines 7-629](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/build-with-claude/fallback-credit.md?plain=1#L7-L629)] [[Source](https://platform.claude.com/docs/en/build-with-claude/fallback-credit#fallback-credit)]

#### [build-with-claude/overview](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/build-with-claude/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

* Features overview reorganized (large rewrite of the feature tables, now split into platform and model-level groups to match the data retention page).

#### [manage-claude/api-and-data-retention](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/manage-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

* The single ZDR/HIPAA feature table was split into groups following the Features overview, starting with "Platform features". In Managed Agents no feature is ZDR or HIPAA eligible. The advisor tool is now ZDR eligible. [[lines 154-220](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/manage-claude/api-and-data-retention.md?plain=1#L154-L220)] [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#feature-eligibility)]

#### [manage-claude/inference-hooks-configuration](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/manage-claude/inference-hooks-configuration.md) [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-configuration)]

* New "Inspect only selected roles" option. Turn on **Limit by role** and set **Inspect** to **Only selected roles** to pilot Inference hooks on part of the organization. Exclusions moved under **Who is inspected**, and changes are logged in the Activity Feed. [[lines 108-125](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/manage-claude/inference-hooks-configuration.md?plain=1#L108-L125)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-configuration#exclusions)]

#### [managed-agents/budgets](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/managed-agents/budgets.md) [[Source](https://platform.claude.com/docs/en/managed-agents/budgets)]

* Availability section added (session budgets in beta). The same metadata and Availability additions apply across the Managed Agents pages (agent-setup, dreams, environments, memory, multiagent-orchestration, scheduled-deployments, self-hosted-sandboxes, tools, vaults, webhooks, workflow-runs and others). [[line 447](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/managed-agents/budgets.md?plain=1#L447)] [[Source](https://platform.claude.com/docs/en/managed-agents/budgets#availability)]

#### [test-and-evaluate/strengthen-guardrails/handle-streaming-refusals](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)]

* Streaming refusals are always on in both the Messages API (`stop_reason: "refusal"` with `stop_details` on `message_delta`) and Managed Agents (session goes idle with `stop_reason.type` `"refusal"`). New Availability section lists models and platforms. [[lines 7-45](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md?plain=1#L7-L45)] [[line 357](https://github.com/gpambrozio/ClaudeDocs/blob/b7e0a33c0b262d0c9d74025fb6e160321f9559e4/docs-md/api/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md?plain=1#L357)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals#handle-streaming-refusals)]

#### Availability-section-only updates

The following pages gained the standardized `featureMetadata` and Availability section without other substantive changes: agents-and-tools/agent-skills/overview, mcp-connector, mcp-tunnels/overview, and the tool-use pages (bash, browser-use, code-execution, computer-use, define-tools, fine-grained-tool-streaming, memory, parallel-tool-use, programmatic-tool-calling, strict-tool-use, text-editor, tool-runner, tool-search, web-fetch, web-search). Also in this group are build-with-claude/cache-diagnostics, citations, context-editing, extended-thinking, files, mid-conversation-system-messages, multilingual-support, pdf-support, preserved-thinking, prompt-caching, refusals-and-fallback, search-results, streaming, structured-outputs, task-budgets, thinking, token-counting, vision and working-with-messages. The rest of the group is cli-sdks-libraries (apple-foundation-models, openai-sdk, middleware), manage-claude (data-residency, opentelemetry, opentelemetry/api, opentelemetry/sdk) and the remaining managed-agents pages.
