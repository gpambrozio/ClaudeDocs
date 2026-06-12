# [Claude docs changes for June 12th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/ca030e46) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/ca030e46)]

## Executive Summary
- New **Access Transparency** feature lets eligible enterprise customers receive audit events whenever Anthropic personnel manually view their data, delivered via the Compliance API
- New **WIF Admin API** guide enables programmatic management of Workload Identity Federation resources (service accounts, federation issuers, federation rules) via infrastructure as code
- New **`enforceAvailableModels`** managed setting (2.1.175) lets admins lock the Default model to the `availableModels` allowlist and prevent users from widening it
- **Memory tool** now supports Java (`BetaMemoryToolHandler`) and C# SDK helpers, expanding cross-language coverage
- New Compliance API endpoints for Code Artifacts management and organization settings retrieval

## New Claude Code versions

### [2.1.174](https://github.com/gpambrozio/ClaudeDocs/blob/ca030e46/versions/2.1.174.md)

#### New features

* Added `wheelScrollAccelerationEnabled` setting to disable mouse-wheel scroll acceleration in fullscreen mode
* [VSCode] Added usage attribution to the Account & usage dialog (`/usage`) showing cache misses, long context, subagents, and per-skill/agent/plugin/MCP breakdowns over the last 24h or 7d

#### Existing feature improvements

* Fixed `/model` picker so Opus now appears as its own row on Max/Team Premium/Enterprise plans, Sonnet on Pro/Team plans, and Opus on pay-as-you-go API accounts (was previously hidden behind Default)
* Fixed skill hot-reload to only re-announce changed skills instead of re-sending the entire skill listing

#### Major bug fixes

* Fixed Bedrock GovCloud regions (`us-gov-*`) deriving the wrong inference profile prefix (`global` instead of `us-gov`), causing 400 errors
* Fixed background sessions inheriting another session's `ANTHROPIC_*` provider env (gateway URL, custom headers, `/model` aliases) from the shell that started the background daemon
* Fixed a 1-2 second pause when exiting Claude Code shortly after a shell command was interrupted or killed on macOS and Linux
* Fixed the `/advisor` dialog pre-selecting a saved advisor model that is blocked by the `availableModels` allowlist
* Fixed Workflow tool `agent()` subagents missing per-agent attribution headers
* Fixed pre-warmed background workers failing with "Could not resolve authentication method" when claimed after sitting idle

### [2.1.175](https://github.com/gpambrozio/ClaudeDocs/blob/ca030e46/versions/2.1.175.md)

#### New features

* Added `enforceAvailableModels` managed setting — when enabled, the `availableModels` allowlist also constrains the Default model (a Default that would resolve to a disallowed model now falls back to the first allowed model), and user or project settings can no longer widen a managed `availableModels` list

-----

## Claude Code changes

No Claude Code documentation changes today.

-----

## API changes

### New Documents

#### [Access Transparency](https://github.com/gpambrozio/ClaudeDocs/blob/ca030e46/docs-md/api/manage-claude/access-transparency.md) [[Source](https://platform.claude.com/docs/en/manage-claude/access-transparency)]

New document describing the Access Transparency feature for eligible enterprise customers. When enabled, every manual view of retained data by an Anthropic employee generates an `anthropic_access` activity in the Compliance API Activity Feed. Covers what content is included (Claude API and Claude Code sessions), what is excluded (automated processing, Batch/Files API, consumer products), reason codes (`safety_review`, `incident_response`), CMEK content preservation events, and surface eligibility. Access Transparency is available on request and is not self-serve.

#### [Manage WIF with the Admin API](https://github.com/gpambrozio/ClaudeDocs/blob/ca030e46/docs-md/api/manage-claude/wif-admin-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/wif-admin-api)]

New guide for programmatically managing Workload Identity Federation resources via the Admin API. Covers creating and managing service accounts, federation issuers (with JWKS discovery, explicit URL, or inline key sets), and federation rules. Explains how to bootstrap a workload with `org:admin` scope to manage WIF via CI/CD, authentication using OAuth bearer tokens, workspace membership management, pagination, archiving behavior, and permissions constraints.

#### [Compliance API — Code Artifacts](https://github.com/gpambrozio/ClaudeDocs/blob/ca030e46/docs-md/api/api/compliance/code.md) [[Source](https://platform.claude.com/docs/en/api/compliance/code)]

New Compliance API reference section for Code Artifacts (hosted sites published via Claude Code). Covers listing artifacts, downloading artifact version content, and deleting artifacts. Includes the `ArtifactListResponse` model with fields for owner, published version, read mode (`org`, `owner`, `users`), and version history.

#### [Compliance API — Organization Settings](https://github.com/gpambrozio/ClaudeDocs/blob/ca030e46/docs-md/api/api/compliance/organizations/settings.md) [[Source](https://platform.claude.com/docs/en/api/compliance/organizations/settings)]

New Compliance API endpoint to retrieve effective organization settings (`GET /v1/compliance/organizations/{organization_id}/settings`). Returns resolved settings including boolean flags (SSO enforcement, code execution, IP allowlist, etc.), session duration, allowed invite domains, SSO provisioning mode, and data retention periods.

#### [Compliance API — Project Collaborators](https://github.com/gpambrozio/ClaudeDocs/blob/ca030e46/docs-md/api/api/compliance/apps/projects/collaborators.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators)]

New Compliance API endpoint to list project collaborators (`GET /v1/compliance/apps/projects/{project_id}/collaborators`). Supports four collaborator types: individual users, RBAC groups, entire organizations, and organization-role-based grants, each with associated role (`admin`, `editor`, `owner`, `viewer`) and `granted_at` timestamps.

### Changed documents

#### [Memory Tool](https://github.com/gpambrozio/ClaudeDocs/blob/ca030e46/docs-md/api/agents-and-tools/tool-use/memory-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)]

* Added Java SDK support: `BetaMemoryToolHandler` interface for implementing custom memory backends, with a link to the Java example. [[lines 125-130](https://github.com/gpambrozio/ClaudeDocs/blob/ca030e46/docs-md/api/agents-and-tools/tool-use/memory-tool.md?plain=1#L125-L130)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)]
* Added C# SDK support: `BetaAbstractMemoryTool` base class noted alongside Python, with a link to the C# example. [[lines 125-130](https://github.com/gpambrozio/ClaudeDocs/blob/ca030e46/docs-md/api/agents-and-tools/tool-use/memory-tool.md?plain=1#L125-L130)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)]
