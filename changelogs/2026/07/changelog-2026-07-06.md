# [Claude docs changes for July 6th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/873dea03150df9fc8723829401096e904e0cab5d) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/873dea03150df9fc8723829401096e904e0cab5d)]

## Executive Summary
- GitHub Enterprise Server plugin marketplaces got a major documentation overhaul: credential requirements now differ by surface (CLI, managed settings, claude.ai org/user settings, web), and a new troubleshooting section covers a common "Marketplace couldn't be added" error caused by a missing GitHub Enterprise connection.
- A new `extraKnownMarketplaces` pre-registration guide explains how to roll out GHES marketplaces organization-wide without requiring per-user GitHub Enterprise connections.
- The Claude Code on AWS guide's "talk to sales" enterprise promo banner reappeared after being removed just yesterday.
- No new Claude Code versions were released today.

-----

## Claude Code changes

### Changed documents

#### [claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/873dea03150df9fc8723829401096e904e0cab5d/docs-md/claude-code/claude-platform-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

* Re-added the enterprise sales promo banner ("Deploying Claude Code across your organization? Talk to sales about enterprise plans, SSO, and centralized billing.") at the top of the page, with links to pricing and contact sales. [[lines 3-5](https://github.com/gpambrozio/ClaudeDocs/blob/873dea03150df9fc8723829401096e904e0cab5d/docs-md/claude-code/claude-platform-on-aws.md?plain=1#L3-L5)] [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

#### [github-enterprise-server](https://github.com/gpambrozio/ClaudeDocs/blob/873dea03150df9fc8723829401096e904e0cab5d/docs-md/claude-code/github-enterprise-server.md) [[Source](https://code.claude.com/docs/en/github-enterprise-server)]

* Clarified that plugin marketplaces hosted on GHES are supported but that credential requirements now vary by surface, pointing to a new dedicated section. [[line 5](https://github.com/gpambrozio/ClaudeDocs/blob/873dea03150df9fc8723829401096e904e0cab5d/docs-md/claude-code/github-enterprise-server.md?plain=1#L5)] [[Source](https://code.claude.com/docs/en/github-enterprise-server)]
* The feature-support table's "Plugin marketplaces" row now links to the new credential-by-surface breakdown instead of just noting the full-URL requirement. [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/873dea03150df9fc8723829401096e904e0cab5d/docs-md/claude-code/github-enterprise-server.md?plain=1#L18)] [[Source](https://code.claude.com/docs/en/github-enterprise-server#what-works-with-github-enterprise-server)]
* Added a table breaking down how marketplace installation and credentials work across five surfaces (CLI/desktop, managed settings, claude.ai org settings, claude.ai user settings, and Claude Code on the web), including a note that Claude Code on the web is unreliable for GHES-hosted marketplaces. [[lines 104-114](https://github.com/gpambrozio/ClaudeDocs/blob/873dea03150df9fc8723829401096e904e0cab5d/docs-md/claude-code/github-enterprise-server.md?plain=1#L104-L114)] [[Source](https://code.claude.com/docs/en/github-enterprise-server#plugin-marketplaces-on-ghes)]
* Explained that GitHub Enterprise connections on claude.ai are per-user for marketplaces added via user settings, but org-added marketplaces (via the organization plugin settings) don't impose this requirement since they use the org's GitHub App for ongoing fetches. [[line 116](https://github.com/gpambrozio/ClaudeDocs/blob/873dea03150df9fc8723829401096e904e0cab5d/docs-md/claude-code/github-enterprise-server.md?plain=1#L116)] [[Source](https://code.claude.com/docs/en/github-enterprise-server#plugin-marketplaces-on-ghes)]
* Now recommends HTTPS URLs over SSH for adding a GHES marketplace (previously SSH was shown first), noting Claude Code runs git non-interactively and rejects SSH hosts not already in `known_hosts`. [[lines 122-133](https://github.com/gpambrozio/ClaudeDocs/blob/873dea03150df9fc8723829401096e904e0cab5d/docs-md/claude-code/github-enterprise-server.md?plain=1#L122-L133)] [[Source](https://code.claude.com/docs/en/github-enterprise-server#add-a-ghes-marketplace)]
* Added a new "Pre-register GHES marketplaces with managed settings" section covering the `extraKnownMarketplaces` setting, including a config example and a rollout checklist (use a full git URL, prefer HTTPS, confirm each machine can clone, confirm the setting reaches each machine). [[lines 135-154](https://github.com/gpambrozio/ClaudeDocs/blob/873dea03150df9fc8723829401096e904e0cab5d/docs-md/claude-code/github-enterprise-server.md?plain=1#L135-L154)] [[Source](https://code.claude.com/docs/en/github-enterprise-server#pre-register-ghes-marketplaces-with-managed-settings)]
* Added a new troubleshooting entry, "Marketplace add on claude.ai fails with a GitHub access error," explaining that a generic "Marketplace couldn't be added" error usually means the user's own GitHub Enterprise account isn't connected, and describing how to connect it (or have an Owner add the marketplace at the org level instead). [[lines 193-196](https://github.com/gpambrozio/ClaudeDocs/blob/873dea03150df9fc8723829401096e904e0cab5d/docs-md/claude-code/github-enterprise-server.md?plain=1#L193-L196)] [[Source](https://code.claude.com/docs/en/github-enterprise-server#marketplace-add-on-claude-ai-fails-with-a-github-access-error)]

-----

## API changes

No significant changes today. The `docs-md/api` diffs were re-encoded Cloudflare email-obfuscation links (no visible content change) and a transient crawl error on the C# `sessions/events` page ("Console temporarily unavailable"), which is a fetch artifact rather than a real documentation change.
