# [Claude docs changes for September 19th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3)]

## Executive Summary
- **`AGENTS.md` is now read directly.** In a project with no `CLAUDE.md`, Claude Code reads `AGENTS.md` instead — no import, no setting — and a new **Project instructions** setting in `/config` chooses between `claude-md-or-agents-md` (the default), `claude-md-and-agents-md`, `claude-md`, and `managed-only`
- **Auto mode's classifier requests stop being charged** on the Claude API and Enterprise plans and on Bedrock, Vertex, Foundry and gateways, by moving the safety checks server-side (2.1.278). A dedicated new page explains the notice you get when a session falls back to billed local classifier requests — usually a gateway that strips headers or edits responses
- New `CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1` for Claude apps gateways whose only egress is a forward proxy, with a blunt warning that turning it on hands the SSRF guard to your proxy
- The Admin spend-limits API gained `organization` and `workspace` scopes for Claude Console organizations, in early-access preview
- A long tail of crash fixes in 2.1.277, most of them malformed values in `~/.claude.json` or a saved transcript taking down launch, `/mcp`, `/plugin` or a resume

## New Claude Code versions

### [2.1.277](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/versions/2.1.277.md)

#### New features

* Added AGENTS.md support: in a project with no CLAUDE.md, Claude Code reads AGENTS.md instead, changeable under **Project instructions** in `/config` (not yet on Bedrock, Vertex or Foundry)
* Added `CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1` for Claude apps gateways whose only egress is a forward proxy
* Added an optional `headers:` map on Claude apps gateway upstreams, for static headers to a proxy you run in front of a provider
* Added a line saying a background task's update is waiting when it finishes while a panel such as `/tasks` is open

#### Existing feature improvements

* Improved Grep and Glob to return an error when a search can't start because the system is out of processes, memory or file handles, instead of reporting no matches
* Improved the Write tool to report a clear error when the target path is an existing directory, instead of silently ending the turn as a declined permission
* Improved WebFetch and WebSearch in Cowork cloud sessions to tell Claude why a request was refused, such as a used-up fetch budget or an admin policy

#### Major bug fixes

* Fixed `claude -p` and Agent SDK sessions hanging with no result after an internal error; they now report the error and exit 1
* Fixed conversations failing every request with "text content blocks must be non-empty" when an earlier assistant turn held an empty text block beside other content
* Fixed being unexpectedly logged out when an older Claude Code build, such as an IDE extension's bundled CLI, runs on the same machine as the current one
* Fixed a cluster of crashes from malformed `~/.claude.json` values — `customApiKeyResponses`, `claudeAiMcpEverConnected`, and `theme` each used to break startup, `/mcp` or `/plugin manage`
* Fixed a crash when resuming a session whose saved history holds an assistant message stored as a plain string
* Fixed a crash when the prompt held text containing terminal color codes, such as a prompt recalled from history
* Fixed the Edit tool treating an escaped backslash followed by `uXXXX` text as a `\uXXXX` escape, which could rewrite an escaped backslash sequence during an edit of a non-ASCII character
* Fixed the Edit tool reporting "Invalid regular expression: regular expression too large" instead of "String not found in file" on a large non-ASCII edit
* Fixed a turn ending early with "Path contains null bytes" when a file path contained `\u0000` written as an escape sequence
* Fixed one malformed `strictKnownMarketplaces` or `blockedMarketplaces` entry silently disabling the whole enterprise marketplace policy
* Fixed `claude plugin install` failing and breaking the installed copy when reinstalling a version another session was using
* Fixed sessions continued after `/clear` missing part of their first message when a SessionStart hook printed output, causing a full prompt-cache miss
* Fixed `$TMPDIR` expanding empty in Bash commands that run outside the sandbox while sandboxing is enabled
* Fixed the Claude apps gateway's telemetry relay ignoring a collector hostname listed in `NO_PROXY` when a proxy is set
* Fixed failed auto-updates leaving large staged downloads behind in `~/.cache/claude/staging`

### [2.1.278](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/versions/2.1.278.md)

#### Existing feature improvements

* Changed auto mode for Claude API and Enterprise users, and on Bedrock, Vertex, Foundry and gateways, to default to the **server-side classifier, which doesn't charge for classifier overhead**; `CLAUDE_CODE_AUTO_MODE_SERVER=0` opts out on the third-party paths, and Claude Code warns when a session falls back to billed local checks
* Added an `Auto mode server` row to `/status` showing whether this session's classifier runs on the server

-----

## Claude Code changes

### New Documents

#### [auto-mode-classifier-billing](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/claude-code/auto-mode-classifier-billing.md) [[Source](https://code.claude.com/docs/en/auto-mode-classifier-billing)]

A page devoted to one notice: `We're changing auto mode to no longer charge for classifier requests in Claude Code. However, this session isn't eligible.`

From v2.1.278, Claude Code asks the server to run auto mode's safety checks as part of the session's own model requests and doesn't charge for them. When the server's checks can't reach a session, it falls back to its own classifier requests, billed as before, and holds the next checked action to show this notice.

* **Who sees it**: server-side checks are on by default for Enterprise plans, Claude API accounts, Claude Platform on AWS, Bedrock, Agent Platform and Foundry — subject to each platform's rollout. **Pro, Max and Team plans never see the notice.** Check a session with `/status`, whose **Auto mode server** row reads `Enabled` or `Disabled`.
* **Why it happens**: most often an LLM gateway or proxy that strips or rewrites request headers, drops unrecognized request fields, or edits responses — rewriting IDs or dropping keys from streaming events. When the configuration or the responses identify one, the notice names it.
* **How to respond**: **Enter** continues with billed local classifier requests, and if a gateway was named, acknowledging it suppresses the notice on that machine for 24 hours. **Esc** or **Ctrl+C** cancels the held action and stops the turn, remembering nothing.
* **How to fix it**: ask your gateway to pass requests and replies through unchanged — forwarding unrecognized fields such as `safeguards` and returning streaming events without dropping keys such as `safeguard_results` or rewriting tool-use IDs. Or, if you know your gateway can't, set `CLAUDE_CODE_AUTO_MODE_SERVER=0` — **a temporary setting that may be removed in a later release**, and one that isn't read on a direct connection to the Anthropic API.

Two useful details: an individual action the server couldn't check doesn't trigger the notice — Claude Code handles that action itself and asks again next request — and in `-p` mode the text goes to stderr while `stream-json` output emits it as a `system` warning an Agent SDK application can read.

### Changed documents

#### [claude-md](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/claude-code/claude-md.md) [[Source](https://code.claude.com/docs/en/claude-md)] and [memory](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/claude-code/memory.md)

* New "AGENTS.md" section with a three-row decision table: an `AGENTS.md` and no `CLAUDE.md` above you → your `AGENTS.md`; both present → your `CLAUDE.md` files only; a `CLAUDE.md` that already imports `AGENTS.md` → your `CLAUDE.md` with the import expanded. Requires v2.1.277, and isn't available on Bedrock or with telemetry disabled, where you still import it from a `CLAUDE.md`. [[lines 307-319](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/claude-code/claude-md.md?plain=1#L307-L319)] [[Source](https://code.claude.com/docs/en/claude-md#agentsmd)]
* Exactly which files suppress `AGENTS.md`: a `CLAUDE.md`, `.claude/CLAUDE.md` or `CLAUDE.local.md` in your working directory or any directory above it. Your `~/.claude/CLAUDE.md`, your organization's managed `CLAUDE.md`, and `.claude/rules/` files **don't** count and keep loading alongside. [[lines 325-326](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/claude-code/claude-md.md?plain=1#L325-L326)] [[Source](https://code.claude.com/docs/en/claude-md#when-claude-code-reads-agentsmd)]
* A trap worth knowing: **because `CLAUDE.local.md` counts, adding one for your own uncommitted instructions in an `AGENTS.md` project stops Claude reading `AGENTS.md` at all.** Set **Project instructions** to `claude-md-and-agents-md` to keep both. [[line 335](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/claude-code/claude-md.md?plain=1#L335)] [[Source](https://code.claude.com/docs/en/claude-md#when-claude-code-reads-agentsmd)]
* What's read and what isn't: every `AGENTS.md` and `.claude/AGENTS.md` up the tree at session start (announced in the conversation as `no CLAUDE.md found; AGENTS.md loaded: …`), a subdirectory's `AGENTS.md` when Claude reads a file there and that directory has no `CLAUDE.md` of its own, with `@path` imports expanded and `claudeMdExcludes` applying. **Not** read: `AGENTS.local.md`, `AGENTS.override.md`, or anything under `.agents/`. [[lines 330-333](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/claude-code/claude-md.md?plain=1#L330-L333)] [[Source](https://code.claude.com/docs/en/claude-md#when-claude-code-reads-agentsmd)]
* New "Choose which instruction files load" table for the four **Project instructions** values. `claude-md-and-agents-md` loads each directory's `CLAUDE.md` first then its `AGENTS.md`, skipping one already loaded so an imported or symlinked `AGENTS.md` isn't read twice. `managed-only` leaves out project, local and user `CLAUDE.md`, `.claude/rules/` and every `AGENTS.md` at launch — though a subdirectory's `CLAUDE.md`, `.claude/rules/` and path-scoped rules still load when Claude reads a file there. [[lines 337-346](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/claude-code/claude-md.md?plain=1#L337-L346)] [[Source](https://code.claude.com/docs/en/claude-md#choose-which-instruction-files-load)]

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* New "Proxy-only egress" section for `CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1`, for a gateway pod that reaches other hosts only through a forward proxy and can't resolve public DNS itself, or whose proxy refuses `CONNECT` to an IP address. It's **an environment variable rather than a `gateway.yaml` key specifically so that nothing in the config file can relax the gateway's address check**. Requires v2.1.277. [[lines 95-106](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L95-L106)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#proxy-only-egress)]
* A table of every outbound request class showing what changes: Anthropic upstreams, WIF token exchange and telemetry exports move from locally-resolved `CONNECT`-to-IP over to handing the proxy the hostname, IdP requests follow unless `oidc.use_proxy: false`, and the cloud-provider upstreams are unchanged. [[lines 110-114](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L110-L114)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#proxy-only-egress)]
* Three conditions must all hold or the gateway logs a warning naming the variable that stopped it and keeps the default: a proxy variable set, `NO_PROXY` **and** `no_proxy` both empty (listing a telemetry collector there keeps the feature off), and `CLAUDE_GATEWAY_ALLOW_LOOPBACK` not on — because a loopback address handed to the proxy would be the proxy host's own. [[lines 116-122](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L116-L122)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#proxy-only-egress)]
* The closing warning is unambiguous about what you're trading away: turn this on only when the proxy's allowlist is at least as strict as the gateway's own check, refusing cloud metadata endpoints, link-local addresses and the proxy's own loopback **by resolved address, not only by name** — because the gateway no longer catches a hostname that resolves to one of them. "A proxy that connects anywhere it's asked removes the gateway's SSRF guard for these requests." [[line 126](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L126)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#proxy-only-egress)]
* New `use_proxy` option on the `oidc` block, sending the gateway's own IdP requests through `HTTPS_PROXY` while honoring `NO_PROXY`. Requires v2.1.227. [[line 83](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L83)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#oidc)]

#### [llm-gateway-protocol](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/claude-code/llm-gateway-protocol.md) [[Source](https://code.claude.com/docs/en/llm-gateway-protocol)]

* The feature pass-through guidance gained the auto-mode safeguards case: a gateway must forward the `safeguards` request field and return the `safeguard_results` field and unrewritten tool-use IDs, or sessions behind it lose the server-side classifier and pay for local classifier requests.

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Auto mode's classifier section now points at the new billing page for the fallback notice and the `Auto mode server` row in `/status`.

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New entries covering the Grep/Glob resource-exhaustion error and the Write-to-a-directory error that 2.1.277 introduced in place of silent failures.

-----

## API changes

### Changed documents

#### [api/beta/organization/spend_limits](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/api/api/beta/organization/spend_limits.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/spend_limits)]

* The spend-limits API gained `organization` and `workspace` scopes alongside the existing `user` scope, with a new workspace-scope object carrying the workspace's tagged ID. The split is by organization type: **Claude Enterprise organizations set `user` limits, Claude Console organizations set `organization` and `workspace` limits, and any other combination returns 400.** The Console scopes are an early-access preview you request through your Anthropic account team. [[lines 32-66](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/api/api/beta/organization/spend_limits.md?plain=1#L32-L66)] [[Source](https://platform.claude.com/docs/en/api/beta/organization/spend_limits#body-parameters)]
* Delete is scope-dependent too: on a Claude Enterprise organization it removes a per-user override rather than the limit itself. [[lines 369-371](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/api/api/beta/organization/spend_limits.md?plain=1#L369-L371)] [[Source](https://platform.claude.com/docs/en/api/beta/organization/spend_limits#delete-spend-limit)]
* A scoped Admin API key can now act on behalf of the organization as the actor on these endpoints. [[line 487](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/api/api/beta/organization/spend_limits.md?plain=1#L487)] [[Source](https://platform.claude.com/docs/en/api/beta/organization/spend_limits#returns)]

#### [api/beta/organization/spend_limits/increase_requests](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/api/api/beta/organization/spend_limits/increase_requests.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/spend_limits/increase_requests)]

* The increase-request endpoints, including `approve` and `retrieve`, carry the same new scope shapes throughout.

#### [api/beta](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)] and [api/beta/organization](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/api/api/beta/organization.md)

* Both regenerated to carry the new spend-limit scope objects across the top-level beta reference.

#### [managed-agents/multiagent-orchestration](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/api/managed-agents/multiagent-orchestration.md) [[Source](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration)]

* Expanded with further orchestration examples across the SDK languages.

#### [api/compliance/activities](https://github.com/gpambrozio/ClaudeDocs/blob/4f7cd9986f0ed70bc4cd135a2a9b2710627684f3/docs-md/api/api/compliance/activities.md) [[Source](https://platform.claude.com/docs/en/api/compliance/activities)]

* The activity catalog was regenerated again, the largest single change in this commit at roughly 9,600 lines, adding activity types and reshaping existing schemas.
