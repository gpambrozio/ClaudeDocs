# [Claude docs changes for November 24th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625)]

## Executive Summary
- **Skills from MCP servers**: MCP servers can now supply skills (Claude Code v2.1.331+), with a new admin setting, `disableDirectMcpSkills`, to turn them on or off for an organization.
- **Code Mode opens up to cloud providers**: Code Mode (experimental) is now documented as usable on Amazon Bedrock, Google Cloud and other providers, with new hook failure behavior (`onFailure`) and mod requirements.
- **MCP tasks reach the cloud and subagents**: MCP tasks now work in cloud sessions, in claude.ai chats and from subagents. VS Code and the desktop app have their own behavior.
- **Fast-mode fallback and cloud-platform access docs**: the API docs now cover how fast mode requests fall back, how workspaces and IAM interact on Claude Platform on AWS and Google Cloud, and worker authentication for self-hosted sandboxes.
- **Smaller Claude Code changes**: recurring scheduled tasks now expire after 30 days (up from 7). New `/motion` and `/whiteboard` skills. The retry watchdog now stops on spend limits.

## New Claude Code versions

No new Claude Code versions were added today.

-----

## Claude Code changes

### New Documents

No new documents.

### Changed documents

#### [approvals](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/approvals.md) [[Source](https://code.claude.com/docs/en/approvals)]

* Approving reviews now come from `claude[bot]` where the Claude GitHub App reports the check. On pull requests that `claude[bot]` opened, they come from `claude-approvals[bot]` once the Claude Approvals GitHub App is added.

#### [approvals-troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/approvals-troubleshooting.md) [[Source](https://code.claude.com/docs/en/approvals-troubleshooting)]

* New section on GitHub IP allow lists. A GitHub organization that restricts access by IP address can leave a pull request with no check or comment, until it allows Anthropic's outbound addresses.

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* The Mantle `assume_role` upstream option now requires gateway v2.1.318 or later. The Mantle IAM actions go to the `assume_role` role when one is set.

#### [claude-apps-gateway-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/claude-apps-gateway-deploy.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy)]

* New troubleshooting row for `400` errors that begin with a field path and mention the `availableModels` allowlist or `deniedModels` denylist.

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* After a VM is reclaimed, tracking of running MCP tasks on a connector is now restored. Other background work is not.

#### [code-mode](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/code-mode.md) [[Source](https://code.claude.com/docs/en/code-mode)]

* Code Mode now works with a Claude subscription, a Console account, or a cloud provider such as Amazon Bedrock or Google Cloud. Gateways are still unsupported, with new error-message guidance. [[lines 38-58](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/code-mode.md?plain=1#L38-L58)] [[Source](https://code.claude.com/docs/en/code-mode#code-mode-limitations)]
* Using Code Mode with a mod that hooks tool calls requires v2.1.327 or later. [[line 53](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/code-mode.md?plain=1#L53)] [[Source](https://code.claude.com/docs/en/code-mode#requirements)]
* The page now documents which hook failures refuse a tool call and which let it run. It includes a table of `onFailure` (`block` / `continue`) results and a new "Tool call ran after a hook failed" section. [[lines 334-354](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/code-mode.md?plain=1#L334-L354)] [[Source](https://code.claude.com/docs/en/code-mode#permission-prompt-with-a-countdown)]
* Hooks that hide tool output can also clear `imagePagesFailed`, and on v2.1.331+ omit `uncutOutputNote`. [[lines 261-262](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/code-mode.md?plain=1#L261-L262)] [[Source](https://code.claude.com/docs/en/code-mode#redact-code-output)]
* Reworked the steps for getting background code to run in auto or `bypassPermissions` mode. Turning Code Mode off now covers `--settings` files. Cloud-provider users should deploy the off switch through MDM or managed settings. [[lines 127-141](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/code-mode.md?plain=1#L127-L141)] [[Source](https://code.claude.com/docs/en/code-mode#turn-off-code-mode)]
* More troubleshooting rows, including one for failing to read organization settings or policy.

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* Added the bundled skills `/motion` (makes a Claude Motion animation artifact) and `/whiteboard` (makes a Claude Whiteboards artifact).

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `CLAUDE_CODE_RETRY_WATCHDOG` now keeps retrying capacity errors past `CLAUDE_CODE_MAX_RETRIES`, but spend limits and exhausted usage credits can end the retries.
* MCP task variables are now scoped to interactive terminal sessions. MCP tasks and skills from MCP servers are listed among the features that need feature-flag fetching.

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New section "When the retry watchdog stops retrying". It stops on spend-limit 429s (v2.1.239+), exhausted usage credits, and responses with `x-should-retry: false` (v2.1.311+).
* `CLAUDE_CODE_MAX_RETRIES` is capped at 15. With the watchdog on v2.1.199+, the cap doesn't apply and the default for other transient errors is 300.
* New error-table rows for worktree and PR/MR errors, reserved marketplace names, missing plugin and commands paths, `GH_HOST`/`GH_REPO` hosts other than github.com, and broken settings in `-p` runs.

#### [feature-availability](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/feature-availability.md) [[Source](https://code.claude.com/docs/en/feature-availability)]

* Code Mode is now marked available (experimental, requirements apply) on the third-party provider columns. A new row shows availability of skills from MCP servers (admin-enabled on some plans).

#### [headless](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* Stream output: a `result` message may not be the last line, because a task notification can follow it and start another turn. Find results by `type`.
* Skills from MCP servers aren't supported in `-p` runs.

#### [managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/managed-settings.md) [[Source](https://code.claude.com/docs/en/managed-settings)]

* Added the `disableDirectMcpSkills` key. A `true` in any admin source turns these skills off, and a `false` is ignored in the HKCU registry.

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* New coverage of MCP tasks in the cloud, in VS Code and the desktop app, and from subagents. MCP tasks are no longer labeled public beta. [[lines 484-570](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/mcp.md?plain=1#L484-L570)] [[Source](https://code.claude.com/docs/en/mcp#automatic-backgrounding-of-long-tool-calls)]
* Outside an interactive terminal, MCP task questions are handled differently. `claude -p` and Agent SDK sessions cancel the task, while the cloud has its own flow. [[line 523](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/mcp.md?plain=1#L523)] [[Source](https://code.claude.com/docs/en/mcp#answer-a-question-from-an-mcp-task)]
* New sections on using skills from MCP servers, turning them on for an organization, and blocking a server's skills or asking first.

#### [plugins/mods/admin](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/plugins/mods/admin.md) [[Source](https://code.claude.com/docs/en/plugins/mods/admin)]

* The guidance on which mod `hooks:` lines to watch is now a table covering `tool.call`, `prompt.submit`, `tool.check`, `session.append`, `skill.prompt`, and `ui.render{component=AskUserQuestion}`.

#### [plugins/mods/reference](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/plugins/mods/reference.md) [[Source](https://code.claude.com/docs/en/plugins/mods/reference)]

* `session.append` can't rewrite rows that hold a skill from an MCP server.

#### [scheduled-tasks](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

* Recurring tasks now expire after 30 days instead of 7 (v2.1.330+). Tasks created with `CronCreate` on older versions keep the 7-day limit. The section was renamed "Recurring task expiry".

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New "Broken settings in a `-p` run" section. It shows the stderr output that lists settings that didn't load or were skipped, and says to run `claude doctor`.

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* Added the `disableDirectMcpSkills` setting. It defaults to off for Team and Enterprise members signed in with `/login`. It does not affect claude.ai connectors, and it carries a prompt-injection warning.

#### [share-sessions](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/share-sessions.md) [[Source](https://code.claude.com/docs/en/share-sessions)]

* Simplified the path to the sharing privacy settings: Settings > Privacy > Manage next to Shared Code sessions.

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* New "Skills from MCP servers" section. It lists the features that don't apply to them: most frontmatter fields, `!` commands, `@` references, and some variable substitution.
* Clarified argument handling. An unfilled indexed placeholder such as `$1` stays literal, and a named placeholder expands to an empty string.
* A few built-in commands, such as `/init` and `/security-review`, are available through the Skill tool.

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* A background subagent's command can move to the background after 3 minutes. The Skill tool can also prompt for MCP-server skills.

#### [worktrees](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/claude-code/worktrees.md) [[Source](https://code.claude.com/docs/en/worktrees)]

* New sections on resuming a kept worktree (`claude --worktree <name> --resume <session-id>`), resuming without `--worktree`, and transcript location.
* Cleanup only skips worktrees created outside `.claude/worktrees/`.
* PR/MR URL handling now ignores the host and repository in the URL. Ambiguous numbers produce a `Cannot use PR/MR #<number>` message.

-----

## API changes

### New Documents

No new documents.

### Changed documents

#### [build-with-claude/fallback-credit](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/build-with-claude/fallback-credit.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/fallback-credit)]

* Redeeming a fallback credit no longer requires an unchanged body. `speed` may be deleted (not added) to run at standard speed. [[line 570](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/build-with-claude/fallback-credit.md?plain=1#L570)] [[Source](https://platform.claude.com/docs/en/build-with-claude/fallback-credit#reference)]
* A rejected continuation is now fixed by removing the appended assistant message. A third header kind is exempt from the match.

#### [build-with-claude/files](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Added how cloud-platform IAM controls workspace access on Claude Platform on AWS and Google Cloud, with a caution about multitenant use. [[line 63](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/build-with-claude/files.md?plain=1#L63)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files#how-the-files-api-works)]
* New audit table mapping Files API operations to Compliance Activity Feed types (`platform_file_uploaded` and others). Listing and metadata retrieval aren't recorded. CloudTrail and Cloud Audit Logs cover the cloud platforms. [[line 1018](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/build-with-claude/files.md?plain=1#L1018)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files#audit-logging)]

#### [build-with-claude/refusals-and-fallback](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/build-with-claude/refusals-and-fallback.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)]

* New "Fallback for fast mode requests" section. It covers per-attempt speed, overriding `speed` on a `fallbacks` entry with `null` or `"fast"`, and SDK-specific syntax. [[line 1153](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/build-with-claude/refusals-and-fallback.md?plain=1#L1153)] [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#fallback-for-fast-mode-requests)]
* Documented fallback validation rules per beta header (`server-side-fallback-2026-07-01` and `2026-06-01`). A Sonnet 5.5 `between_tools` thinking request falls back with thinking disabled. [[line 649](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/build-with-claude/refusals-and-fallback.md?plain=1#L649)] [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#naming-your-own-fallback-models)]
* If a fallback model is rate limited, the API returns the preceding refusal and tries no later entries.

#### [build-with-claude/skills-guide](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/build-with-claude/skills-guide.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/skills-guide)]

* Added feature metadata at the top of the page: stable status, ZDR not eligible, and the list of supported models. [[lines 7-38](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/build-with-claude/skills-guide.md?plain=1#L7-L38)] [[Source](https://platform.claude.com/docs/en/build-with-claude/skills-guide#step-1-use-a-skill-to-create-a-file)]

#### [manage-claude/admin-api](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/manage-claude/admin-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api)]

* New "Cloud platforms" section. It lists the Admin API endpoints available on Claude Platform on AWS, including the new compliance settings endpoints, and on Claude Models on Google Cloud. [[line 1741](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/manage-claude/admin-api.md?plain=1#L1741)] [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api#cloud-platforms)]

#### [manage-claude/compliance-api-access](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/manage-claude/compliance-api-access.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-api-access)]

* Setup is now split by organization type. Enterprise uses Compliance Access Keys, standalone Console uses Admin API keys, and AWS and Google Cloud organizations enable the API without creating keys. Added steps for enabling it on each cloud platform. [[lines 30-54](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/manage-claude/compliance-api-access.md?plain=1#L30-L54)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-api-access#set-up-the-compliance-api)]

#### [manage-claude/workspaces](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/manage-claude/workspaces.md) [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces)]

* New "Access on cloud platforms" section. IAM controls access, and on Google Cloud a role applies to every workspace in the project, so use separate projects for isolation. [[line 69](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/manage-claude/workspaces.md?plain=1#L69)] [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces#access-on-cloud-platforms)]
* API key types don't apply on these platforms. Prompt cache isolation details moved to the prompt-caching page.

#### [managed-agents/choosing-an-environment](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/managed-agents/choosing-an-environment.md) [[Source](https://platform.claude.com/docs/en/managed-agents/choosing-an-environment)]

* Merged the per-platform sections into "Differences on cloud platforms". Memory stores need a cloud environment, MCP tunnels are Claude API only, and on Google Cloud you write your own worker. [[lines 93-116](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/managed-agents/choosing-an-environment.md?plain=1#L93-L116)] [[Source](https://platform.claude.com/docs/en/managed-agents/choosing-an-environment#differences-on-cloud-platforms)]

#### [managed-agents/secure-deployment](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/managed-agents/secure-deployment.md) [[Source](https://platform.claude.com/docs/en/managed-agents/secure-deployment)]

* New "Access through Google Cloud IAM" section. Separate workloads by project. Revoking Google Cloud access doesn't stop running sessions or scheduled deployments. [[line 880](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/managed-agents/secure-deployment.md?plain=1#L880)] [[Source](https://platform.claude.com/docs/en/managed-agents/secure-deployment#access-through-google-cloud-iam)]

#### [managed-agents/self-hosted-sandboxes](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/managed-agents/self-hosted-sandboxes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

* New "Worker authentication on cloud platforms" section. On AWS, attach the `AnthropicSelfHostedEnvironmentAccess` managed policy. On Google Cloud, write your own worker and grant `roles/claude.user`. It also lists the changes to the quickstart steps. [[line 570](https://github.com/gpambrozio/ClaudeDocs/blob/43e644ee96d9bbf3af6cd0ff98263ccff6ec3625/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L570)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#worker-authentication-on-cloud-platforms)]

#### API reference (`api/api/...`)

* Large regeneration of the auto-generated reference pages, including the Compliance Activities and Beta Messages references and the per-language SDK pages. Most of the diff is reordering. Model entries were reordered and deprecation notes updated (for example, `claude-opus-4-5` now ends on January 22, 2027). Agents, deployments, plugins and federation pages also got small updates.
* Minor edits to other `manage-claude` pages (CMEK, compliance, rate-limits API, WIF) mostly add cloud-platform cross-references.
