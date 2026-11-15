# [Claude docs changes for November 15th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/978b7f068403db7250ffa2dbaf4781106448bdcc) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/978b7f068403db7250ffa2dbaf4781106448bdcc)]

## Executive Summary
- New "Work with Jupyter notebooks" docs: NotebookEdit clears a replaced cell's saved output and execution count, so re-run the cell, and save the notebook before asking for an edit.
- Data residency docs now include Console steps for setting allowed and default inference geos, plus Admin API details.
- The workspaces docs now spell out Default Workspace behavior and Workspace Limited Developer Console limits.
- Claude Platform on AWS docs now list the new Agents overview page and say Admins can set workspace spend limits.
- The self-hosted Managed Agents docs add a note for organizations that already have access.

## New Claude Code versions

No new versions in this update.

-----

## Claude Code changes

### Changed documents

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* New "Work with Jupyter notebooks" section. Replacing a code cell clears its saved output and execution count. No kernel restart is needed, because NotebookEdit only writes the file. Re-run the edited cell and any cells that depend on it. [[lines 605-618](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/claude-code/ide-integrations.md?plain=1#L605-L618)] [[Source](https://code.claude.com/docs/en/ide-integrations#work-with-jupyter-notebooks)]
* Save a notebook before asking for an edit, because the `autosave` setting doesn't save before NotebookEdit. The `autosave` description now says it saves before the Read, Edit, and Write tools run. [[line 750](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/claude-code/ide-integrations.md?plain=1#L750)] [[Source](https://code.claude.com/docs/en/ide-integrations#extension-settings)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* When a mod from outside the official marketplace and built-in bundle calls `$.model`, `api_request` events carry `marketplace.name`. It is redacted to `"third-party"` unless `OTEL_LOG_TOOL_DETAILS=1` is set. The `api_error` event points to this note. [[line 871](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/claude-code/monitoring-usage.md?plain=1#L871)] [[line 895](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/claude-code/monitoring-usage.md?plain=1#L895)] [[Source](https://code.claude.com/docs/en/monitoring-usage#api-request-event)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* New section: replacing a cell with NotebookEdit clears its execution count and saved outputs. Re-run the cell and its dependents to get the output back. [[lines 449-452](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/claude-code/tools-reference.md?plain=1#L449-L452)] [[Source](https://code.claude.com/docs/en/tools-reference#replacing-a-cell-clears-its-saved-outputs-in-the-file)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* New "Work with Jupyter notebooks" section covering cleared outputs after cell edits, no kernel restart needed, and saving the notebook before an edit. [[lines 605-618](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/claude-code/vs-code.md?plain=1#L605-L618)] [[Source](https://code.claude.com/docs/en/vs-code#work-with-jupyter-notebooks)]
* The `autosave` setting now saves before the Read, Edit, and Write tools run. [[line 750](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/claude-code/vs-code.md?plain=1#L750)] [[Source](https://code.claude.com/docs/en/vs-code#extension-settings)]

-----

## API changes

### Changed documents

#### [claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/api/build-with-claude/claude-platform-on-aws.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)]

* Console pages table: a new **Agents overview** page (session counts, error rates, active time) does not go through the AWS gateway, except for its list of agents. The **Agents** page's **Observability** tab also bypasses the gateway. Pages that bypass the gateway reach Anthropic directly and skip IAM action checks. [[lines 809-832](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/api/build-with-claude/claude-platform-on-aws.md?plain=1#L809-L832)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#available-pages)]
* Spend limits: with the Admin role you can set organization and workspace limits in US dollars at list prices. The Console steps are updated (Organization limit and Workspace limits sections). Tier-cap failures are documented as HTTP 429. A new list says who gets an email notice depending on what stopped the requests. [[lines 860-880](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/api/build-with-claude/claude-platform-on-aws.md?plain=1#L860-L880)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#spend-limits)]

#### [data-residency](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/api/manage-claude/data-residency.md) [[Source](https://platform.claude.com/docs/en/manage-claude/data-residency)]

* Requests with a disallowed `inference_geo` return a 400 error. `default_inference_geo` must be one of the allowed geos. [[lines 260-261](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/api/manage-claude/data-residency.md?plain=1#L260-L261)] [[Source](https://platform.claude.com/docs/en/manage-claude/data-residency#workspace-level-restrictions)]
* New step-by-step Console instructions for setting the allowed and default inference geos, and Admin API guidance. Both fields go inside the `data_residency` object of a Create or Update Workspace request, and an update keeps any field you leave out. [[lines 263-272](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/api/manage-claude/data-residency.md?plain=1#L263-L272)] [[Source](https://platform.claude.com/docs/en/manage-claude/data-residency#workspace-level-restrictions)]

#### [self-hosted](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/api/managed-agents/self-hosted.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted)]

* New note: if your Claude Console organization already has access to self-hosted Managed Agents, sign in to the Console, switch to that organization, and reload the page. The same note was added to the self-hosted subpages (agent-identity, call-the-api, configuration-reference, configure, console, differences, inference-provider, kubernetes, quickstart, upgrade) and to self-hosted-data-and-access. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/api/managed-agents/self-hosted.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted#self-hosted)]

#### [workspaces](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/api/manage-claude/workspaces.md) [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces)]

* The Default Workspace behavior is now spelled out. Responses carry its ID in the `anthropic-workspace-id` header. List Workspaces includes it only with `include_default=true`. The Usage and Cost Analytics API reports it under that ID, while the legacy Usage and Cost API shows `null`. An API key bound to it carries the ID in its `scope` field. [[lines 21-26](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/api/manage-claude/workspaces.md?plain=1#L21-L26)] [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces#how-workspaces-work)]
* Workspace Limited Developer limits apply only to the Console interface, not the API. In the Console they cannot open or start Managed Agents sessions, open memory stores, or manage deployments. They also cannot download or delete files on the Files page. [[lines 47-58](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/api/manage-claude/workspaces.md?plain=1#L47-L58)] [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces#workspace-roles-and-permissions)]
* Admin API endpoints reject keys scoped to a single workspace. List examples now document auto-pagination, where `limit` sets the page size rather than the total. The PHP and Ruby samples now use auto-paging iterators. [[lines 241-347](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/api/manage-claude/workspaces.md?plain=1#L241-L347)] [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces#using-the-admin-api)]
* Resource scoping: organization-level requests such as Admin API calls are exempt from the one-workspace rule. MCP tunnel details were added: the cap of 10 active tunnels is organization-wide, managing tunnels needs the Manage tunnels permission, and developers can view tunnels but not change them. [[lines 816-834](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/api/manage-claude/workspaces.md?plain=1#L816-L834)] [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces#api-keys-and-resource-scoping)]

#### [webhooks](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/api/managed-agents/webhooks.md) [[Source](https://platform.claude.com/docs/en/managed-agents/webhooks)]

* Small clarifications to the Console workspace picker and to how non-`2xx` responses are handled. A `3xx` disables the endpoint immediately, and other failures are retried. [[line 336](https://github.com/gpambrozio/ClaudeDocs/blob/978b7f068403db7250ffa2dbaf4781106448bdcc/docs-md/api/managed-agents/webhooks.md?plain=1#L336)] [[Source](https://platform.claude.com/docs/en/managed-agents/webhooks#handle-an-event)]
