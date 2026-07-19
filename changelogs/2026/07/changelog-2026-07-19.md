# [Claude docs changes for July 19th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c)]

## Executive Summary
- Claude Code 2.1.215: Claude no longer runs the `/verify` and `/code-review` skills automatically on its own — invoke them explicitly with `/verify` or `/code-review` when you want them.
- The Claude Apps Gateway deployment guide now warns that the gateway's stderr, audit log, and debug files can contain developer identities and hook/MCP output, and to redact them before posting to a public issue.
- GitHub MCP setup docs (CLI and VS Code) clarify that `claude mcp add` accepts a placeholder personal access token without validating it — check `/mcp` for a `connected` vs. `failed` status to confirm the server actually works.
- `troubleshoot-install` now explains what a `403` (proxy/network filter or regional block) or `5xx` (temporary service issue) response means when checking connectivity to `downloads.claude.ai`, instead of only covering total connection failures.
- The VS Code extension's documented minimum VS Code version is corrected from 1.98.0 down to 1.94.0 in both the installation requirements and the "extension won't install" troubleshooting section.

-----

## New Claude Code versions

### [2.1.215](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/versions/2.1.215.md)

#### Existing feature improvements

* Claude no longer runs the `/verify` and `/code-review` skills on its own; invoke them with `/verify` or `/code-review` when you want them

-----

## Claude Code changes

### Changed documents

#### [artifacts](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/artifacts.md) [[Source](https://code.claude.com/docs/en/artifacts)]

* The "Settings > Claude Code > Capabilities", "Settings > Roles", and "Settings > Data & privacy controls" references for managing artifacts are now clickable links to the corresponding claude.ai admin pages instead of plain text. [[line 207](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/artifacts.md?plain=1#L207)] [[line 219](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/artifacts.md?plain=1#L219)] [[Source](https://code.claude.com/docs/en/artifacts)]

#### [Claude Apps Gateway deployment](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/claude-apps-gateway-deploy.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy)]

* New warning that the gateway's stderr includes the audit event stream, the audit log records developer identities, and the debug file records hook/MCP server output from the developer's machine — review and redact these before posting to a public issue. [[line 204](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/claude-apps-gateway-deploy.md?plain=1#L204)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy)]

#### [Claude Code on the web](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* The "Settings > Claude Code > Sharing settings" reference for requiring repository access or hiding your name from shared sessions is now a clickable link. [[line 706](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L706)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

#### [index](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/index.md), [overview](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/overview.md) [[Source](https://code.claude.com/docs/en/)]

* The `cd your-project` quick-start snippet now clarifies that `your-project` should be replaced with the path to a project directory on your machine. [[line 57](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/index.md?plain=1#L57)] [[Source](https://code.claude.com/docs/en/)]
* The `/desktop` bullet is reworded from "hand off a terminal session to the Desktop app" to "continue your current terminal session in the Desktop app," and now notes it's available on macOS and x64 Windows. [[line 157](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/index.md?plain=1#L157)] [[Source](https://code.claude.com/docs/en/)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* New note on the GitHub MCP setup example: `claude mcp add` saves the configuration without validating credentials, so a placeholder `YOUR_GITHUB_PAT` value is accepted but the server later fails to connect; run `/mcp` and check for `connected` vs. `failed` to verify. [[line 441](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/mcp.md?plain=1#L441)] [[Source](https://code.claude.com/docs/en/mcp)]

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* The "Settings > Connectors" reference for managing connectors outside the routine form is now a direct link to claude.ai/customize/connectors. [[line 298](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/routines.md?plain=1#L298)] [[Source](https://code.claude.com/docs/en/routines)]
* Turning on usage credits now links to claude.ai/settings/usage, and notes that on Team/Enterprise plans an admin turns them on for the organization at claude.ai/admin-settings/usage — previously this pointed only to a generic "Settings > Billing." [[line 341](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/routines.md?plain=1#L341)] [[Source](https://code.claude.com/docs/en/routines)]

#### [troubleshoot-install](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/troubleshoot-install.md) [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

* The three connectivity-check steps now explain that a `403` response usually means a proxy/network filter or that Claude Code isn't available in the region, and a `5xx` response usually means a temporary service issue to retry later, rather than only covering total connection failures. [[lines 53-58](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/troubleshoot-install.md?plain=1#L53-L58)] [[lines 329-332](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/troubleshoot-install.md?plain=1#L329-L332)] [[lines 408-410](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/troubleshoot-install.md?plain=1#L408-L410)] [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

#### [Troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* Clarifies that the memory breakdown referenced when inspecting a heap snapshot in Chrome DevTools is the file ending in `-diagnostics.json`. [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/troubleshooting.md?plain=1#L33)] [[Source](https://code.claude.com/docs/en/troubleshooting)]

#### [VS Code](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* The minimum required VS Code version is corrected from 1.98.0 to 1.94.0, in both the installation prerequisites and the "extension won't install" troubleshooting step. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/vs-code.md?plain=1#L11)] [[line 437](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/vs-code.md?plain=1#L437)] [[Source](https://code.claude.com/docs/en/vs-code)]
* Same GitHub MCP placeholder-PAT note added as in `mcp.md`, telling readers to type `/mcp` in the chat panel and check for `connected` vs. `failed`. [[line 346](https://github.com/gpambrozio/ClaudeDocs/blob/8f798ca4d45d55fb9e97e0e53db6453d3b215a6c/docs-md/claude-code/vs-code.md?plain=1#L346)] [[Source](https://code.claude.com/docs/en/vs-code)]

-----

## API changes

No substantive changes today — `adaptive-thinking`, `extended-thinking`, and `files` only had their obfuscated "contact us" email-protection links regenerated, with no content change.
