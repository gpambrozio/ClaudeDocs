# [Claude docs changes for August 16th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/7d7cbad2fdce2b538f44db7c82666a46a7d5e660) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/7d7cbad2fdce2b538f44db7c82666a46a7d5e660)]

## Executive Summary
- Claude Code adds a new `[claude-code:unrecognized_model]` stderr/debug-log diagnostic that fires whenever a request uses a model ID the installed version doesn't recognize, on every provider, with guidance on fixing it via `modelOverrides`.
- The task-tracking tools (todos, `TaskCreate`/`TaskGet`/`TaskList`/`TaskUpdate`) are now opt-in: a session only gets them if one is explicitly named in `allowedTools`/`tools`, which also affects when Claude creates todos and when agent teams get a shared task list.
- Docs now consistently refer to the "Agent tool" (previously "Task tool") for spawning subagents, matching a recent rename.
- The Compliance API's "List organization users" reference page is now fully documented (it previously rendered only placeholder "Loading" text), covering the `GET /v1/compliance/organizations/{org_uuid}/users` endpoint, its parameters, and response shape.

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/custom-tools](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/agent-sdk/custom-tools.md) [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools)]

* Naming a task-tracking tool in `allowedTools` now also opts the session into those tools. [[line 313](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/agent-sdk/custom-tools.md?plain=1#L313)] [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools#configure-allowed-tools)]

#### [agent-sdk/hooks](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* The `TaskCompleted` hook's trigger is clarified as "a task is marked completed" rather than "background task completes," and now links to its own docs. [[line 171](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L171)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#available-hooks)]

#### [agent-sdk/observability](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/agent-sdk/observability.md) [[Source](https://code.claude.com/docs/en/agent-sdk/observability)]

* Tracing docs now say subagents are spawned through the "Agent tool" rather than the "Task tool." [[line 140](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/agent-sdk/observability.md?plain=1#L140)] [[Source](https://code.claude.com/docs/en/agent-sdk/observability#read-agent-traces)]

#### [agent-sdk/permissions](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/agent-sdk/permissions.md) [[Source](https://code.claude.com/docs/en/agent-sdk/permissions)]

* Naming a task-tracking tool in `allowed_tools` now also opts the session into those tools. [[line 61](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L61)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#allow-and-deny-rules)]

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* The `allowed_tools` reference now notes that naming a task-tracking tool there also opts the session into those tools. [[line 766](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/agent-sdk/python.md?plain=1#L766)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#claudeagentoptions)]

#### [agent-sdk/todo-tracking](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/agent-sdk/todo-tracking.md) [[Source](https://code.claude.com/docs/en/agent-sdk/todo-tracking)]

* Clarifies that Claude only creates todos in a session that has the task-tracking tools. [[line 34](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/agent-sdk/todo-tracking.md?plain=1#L34)] [[Source](https://code.claude.com/docs/en/agent-sdk/todo-tracking#when-todos-are-used)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* The `allowedTools` reference now notes that naming a task-tracking tool there also opts the session into those tools. [[line 394](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L394)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#options)]

#### [agent-teams](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* The shared task list and "all agents can see task status" language is now scoped to agents that have the task-tracking tools. [[lines 33, 67, 226, 250](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/agent-teams.md?plain=1#L250)]

#### [agents](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/agents.md) [[Source](https://code.claude.com/docs/en/agents)]

* Teammates sharing a task list is now conditioned on the team having the task-tracking tools. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/agents.md?plain=1#L36)] [[Source](https://code.claude.com/docs/en/agents#choose-an-approach)]

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* Subagents are now spawned with the "Agent tool" rather than the "Task tool." [[line 190](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L190)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#manage-context)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `--allowedTools`/`--allowed-tools` and `--tools` now note that naming a task-tracking tool opts the session into those tools. [[line 56](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/cli-reference.md?plain=1#L56), [line 122](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/cli-reference.md?plain=1#L122)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Added a new "Unrecognized model ID on a request" section documenting the `[claude-code:unrecognized_model]` diagnostic line: when it's written, its JSON payload (`model`, `query_source`), where it goes (stderr under `-p`, debug log otherwise), and how to silence it with `modelOverrides`. [[lines 2024-2058](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/errors.md?plain=1#L2024-L2058)] [[Source](https://code.claude.com/docs/en/errors#unrecognized-model-id-on-a-request)]
* Notes the diagnostic line is written on every provider, even when the "not a recognized model id" check itself only runs on the Anthropic API. [[line 1181](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/errors.md?plain=1#L1181)] [[Source](https://code.claude.com/docs/en/errors#model-is-not-a-recognized-model-id)]
* The `TaskCreate` background-subagent tool-drop example was removed, leaving `LSP` as the example of a tool background subagents drop. [[line 1678](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/errors.md?plain=1#L1678)] [[Source](https://code.claude.com/docs/en/errors#agent-would-be-spawned-with-zero-tools)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Notes that Claude Code can still write the new unrecognized-model diagnostic line even on providers where the model-ID check itself doesn't run. [[line 102](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/model-config.md?plain=1#L102)] [[Source](https://code.claude.com/docs/en/model-config#setting-your-model)]
* Documents that adding a `modelOverrides` entry for a gateway alias stops the `[claude-code:unrecognized_model]` diagnostic line for that ID. [[line 660](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/model-config.md?plain=1#L660)] [[Source](https://code.claude.com/docs/en/model-config#override-model-ids-per-version)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* A completed background subagent now stays listed in `/tasks` for the same window as the footer hint, rather than "until the session cleans up its task list." [[line 728](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/sub-agents.md?plain=1#L728)] [[Source](https://code.claude.com/docs/en/sub-agents#run-subagents-in-foreground-or-background)]
* Clarifies you can only resume a self-stopped subagent by typing into its transcript while its row is still in the subagent panel. [[line 878](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/claude-code/sub-agents.md?plain=1#L878)] [[Source](https://code.claude.com/docs/en/sub-agents#resume-subagents)]

-----

## API changes

### Changed documents

#### [api/compliance/organizations/users/list](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/api/api/compliance/organizations/users/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/organizations/users/list)]

* The page previously rendered only placeholder "Loading" text; it now fully documents `GET /v1/compliance/organizations/{org_uuid}/users`, including the `limit`/`page` query parameters, the `data` array fields (`id`, `created_at`, `email`, `full_name`, `organization_role`), pagination fields (`has_more`, `next_page`), and example request/response. [[lines 1-138](https://github.com/gpambrozio/ClaudeDocs/blob/7d7cbad2fdce2b538f44db7c82666a46a7d5e660/docs-md/api/api/compliance/organizations/users/list.md?plain=1#L1-L138)] [[Source](https://platform.claude.com/docs/en/api/compliance/organizations/users/list)]
