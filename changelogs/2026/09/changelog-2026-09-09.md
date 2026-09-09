# [Claude docs changes for September 9th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/01058d9b99076c474fab7c5ea09377a8cd47da37) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/01058d9b99076c474fab7c5ea09377a8cd47da37)]

## Executive Summary
- Claude Code 2.1.265 adds a 1 GB cap (with truncation notice) on tool results saved to disk, lets `--plugin-dir` point at a folder of plugins that's watched for changes, and fixes two prompt-cache regressions around resumed subagents.
- 2.1.266 is a same-day follow-up fixing a 2.1.265 regression that broke LLM-gateway and proxy setups using the undocumented `CLAUDE_CODE_USE_GATEWAY` variable, forcing them into failed Cloud-gateway sign-in.
- Auto mode (v2.1.261+) now also blocks posting a link to a public paste, diagram, or data-sharing service when the URL itself carries the shared content, unless you named that service as trusted.
- Switching output styles mid-session (v2.1.251+) now applies starting with your very next message instead of requiring `/clear` or a restart, at the cost of one full cache rebuild.
- The `settings` and `settings-reference` docs were retitled and reorganized ("Settings files and precedence" / "All settings"), and the skills-location docs were restructured into clearer "Choose where skills load" and "Resolve skills that share a name" sections.

-----

## New Claude Code versions

### [2.1.265](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/versions/2.1.265.md)

#### New features

* Added `user.email` and `user.groups` to the telemetry Claude Desktop and Cowork send through a Claude apps gateway, matching terminal sessions
* Added support for pointing `--plugin-dir` at a folder of plugins: each child folder with a manifest loads, and children added or removed while running are picked up
* Added a 1 GB cap on tool results saved to disk; the in-conversation preview says when a saved file was truncated
* [VSCode] Added automatic archiving of sessions inactive for a set period (new "Archive inactive sessions" setting, default 14 days)

#### Existing feature improvements

* Improved `--worktree` startup on large repositories: the new worktree is now checked out in parallel (git 2.32+)
* Improved `/workflows` agent detail: tool calls are marked running, failed or done, the subagent's task list is shown when it has one, and Enter unfolds the listed calls with their inputs and results
* Improved slash commands typed mid-prompt: matches now show in a list (Tab opens it outside fullscreen) instead of a single suggestion, and a plugin skill is now found by its bare name
* Improved remote MCP servers that need sign-in: Claude Code no longer registers an OAuth client with them until you actually authenticate
* Improved the time to resume long sessions that read many files
* Improved the error shown when an image over the size limits cannot be decoded: it now names the cause and how to fix it instead of only citing the limit
* Improved the Artifact tool's read of an artifact someone else wrote: the summary now treats the page as untrusted content and flags embedded instructions rather than relaying them
* Changed image processing to use the runtime's built-in image support; the CLI no longer extracts a native image module to the temp directory
* Changed Claude apps gateway sessions to export OpenTelemetry directly to a collector named in `OTEL_EXPORTER_OTLP_ENDPOINT`, instead of through the gateway's relay; sessions without a named collector still use the relay

#### Major bug fixes

* Fixed resuming a foreground-spawned subagent changing its tool list and system prompt prefix, which broke prompt-cache reuse for that agent
* Fixed agent teammates and resumed subagents moving SubagentStart hook context and preloaded skills out of the prompt prefix on later turns, which broke prompt-cache reuse
* Fixed resume after the previous process died while a tool was running: the last prompt is no longer rewritten, and the interrupted tool call is kept and marked interrupted
* Fixed `/model opusplan[1m]` being rejected with "Model not found"
* Fixed a plugin path containing a backslash bypassing the symlink containment check on macOS and Linux
* Fixed plugin directories whose names begin with two dots being wrongly refused as outside the plugin root
* Fixed VS Code and SDK sessions occasionally requiring re-login when a session was closed while refreshing its token
* Fixed Remote Control sessions sending the end-of-turn signal before the reply's last message, which could show a reply as finished in the Claude app before its last part arrived
* Fixed background (`--bg`) sessions occasionally being retired mid-turn when a message arrived just before the idle timeout
* Fixed Claude Code's own git status and diff probes running clean filters configured by a nested repository inside the working tree
* Fixed the advisor tool and its instructions being re-decided per request from the request's model; the decision is now made once and announced in the conversation when it changes
* Fixed artifact publish accepting connector tool names the connector doesn't expose; the publish is now refused when none of the declared tools exist, and warned when only some don't
* Fixed `/add-dir <subdirectory>` refusing to load a subdirectory's agents when managed settings lock only skills to plugins, and promising agents when only agents are locked
* Fixed two-key keyboard shortcuts cancelling silently when the second key arrived more than a second later, as happens inside tmux; they now wait 3 seconds and show a notice when they time out
* Fixed forked skills (`context: fork`) not streaming their kickoff prompt and, with `--forward-subagent-text`, their text turns as progress events in stream-json
* Fixed a plugin's default component folder that the OS cannot check, such as a symlink loop, being silently skipped; it is now reported in `/plugin` with the error code
* Fixed the Claude apps gateway's OTLP telemetry relay pausing all forwarding to a collector for 30 seconds after it rejected a few payloads as malformed or too large
* Fixed `/login` showing "no gateway URL is configured" when re-run in a session that signed in to a Claude apps gateway set by managed settings
* Fixed `/model` claiming a model was "saved as your default" when the settings file couldn't be written; it now says the save failed and why
* Fixed `/clear` from Remote Control waiting on SessionStart hooks and on open terminal dialogs before completing
* Fixed resuming a workflow run after its container restarted; a resume whose run journal is missing now fails with a clear error instead of rerunning every agent
* Fixed non-interactive sessions (`-p` with stream-json input, Agent SDK, cloud sessions) resetting the shell working directory at each new user message; a `cd` now persists across turns
* Fixed MCP servers configured as `http` that only speak the legacy HTTP+SSE transport never connecting; Claude Code now falls back to SSE as the MCP spec describes
* Fixed some claude.ai connectors in cloud sessions showing as needing authentication even though they are connected in claude.ai (servers that answer an unsupported request with HTTP 401)
* Fixed remote sessions keeping their sandbox container alive while a connector approval or sign-in link waits for you
* Fixed the `claude-api` skill's error-code reference: model access failures return 404 and unavailable beta headers return 400, not 403
* Windows: Fixed Read, Write and Edit refusing every file ("symlink resolution changed after permission was checked") when running inside an AppContainer or restricted-token sandbox
* [VSCode] Fixed the sidebar chat coming back blank after Reload Window or a restart when the conversation had been open for more than 10 minutes

### [2.1.266](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/versions/2.1.266.md)

#### Major bug fixes

* Fixed a 2.1.265 regression affecting LLM-gateway and proxy setups: the undocumented `CLAUDE_CODE_USE_GATEWAY` environment variable, previously ignored unless `ANTHROPIC_BASE_URL` and `ANTHROPIC_AUTH_TOKEN` were both set, began forcing Cloud-gateway sign-in on its own, so configurations that set it alongside an API key, `apiKeyHelper`, or custom auth headers failed every request with "Not signed in to the Cloud gateway". The variable on its own is ignored again

-----

## Claude Code changes

### Changed documents

#### [claude-directory](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* Clarified that output style files are read at startup, but the style selected via `outputStyle` is now added to the system prompt on every turn rather than only being "applied at session start". [[lines 321](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/claude-directory.md?plain=1#L321), [638](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/claude-directory.md?plain=1#L638)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `ANTHROPIC_*_MODEL_NAME` variables (custom, Fable, Haiku, Opus, Sonnet) now document that when unset, the `/model` picker shows the model's recognized display name instead of the raw pinned ID, rather than always falling back to the ID. [[line 140](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/env-vars.md?plain=1#L140)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [llm-gateway-protocol](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/llm-gateway-protocol.md) [[Source](https://code.claude.com/docs/en/llm-gateway-protocol)]

* Documented a change to `/model` picker naming for gateway-discovered entries: `display_name` is used only when it differs from `id`; otherwise the entry shows the model's recognized name, or the raw `id` if unrecognized (e.g. `my-gateway-claude-sonnet-4-6` now displays as `Sonnet 4.6`). [[line 199](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/llm-gateway-protocol.md?plain=1#L199)] [[Source](https://code.claude.com/docs/en/llm-gateway-protocol#picker-entries-and-caching)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Added a "Customize pinned model display and capabilities" explanation of when a pinned third-party model ID is "recognized" (shows its real name, e.g. `Sonnet 4.5`) versus "not recognized" (shows the raw ID or ARN), including that Microsoft Foundry deployment names are never recognized. [[lines 778-781](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/model-config.md?plain=1#L778-L781)] [[Source](https://code.claude.com/docs/en/model-config#customize-pinned-model-display-and-capabilities)]

#### [output-styles](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/output-styles.md) [[Source](https://code.claude.com/docs/en/output-styles)]

* Documented that switching output styles mid-session now applies starting with your next message and rebuilds the prompt cache once, instead of requiring `/clear` or a new session (changed in v2.1.251). A style file created or edited mid-session in the terminal still needs a restart to be picked up. [[lines 43](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/output-styles.md?plain=1#L43), [81](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/output-styles.md?plain=1#L81)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Documented a new auto mode default block (v2.1.261+): posting or writing a link to a public paste, diagram, or data-sharing service anywhere it will be opened or fetched is blocked when the URL itself carries the shared content, unless that service was explicitly trusted. [[line 380](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/permission-modes.md?plain=1#L380)] [[Source](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default)]

#### [prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/prompt-caching.md) [[Source](https://code.claude.com/docs/en/prompt-caching)]

* Moved "Changing output style" from the actions that keep the cache to the actions that invalidate it: a mid-session switch now re-reads the whole conversation with no cache hits on the next message, so switching right after `/clear`/`/compact` or before the first message keeps the cost small. [[lines 69](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/prompt-caching.md?plain=1#L69), [152-156](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/prompt-caching.md?plain=1#L152-L156)]

#### [sessions](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/sessions.md) [[Source](https://code.claude.com/docs/en/sessions)]

* Added a new "Delete session data" section documenting `claude project purge` to delete a project's transcripts and related state before the retention sweep, and noting that `claude rm <id>` on a background session leaves its transcript on disk, resumable with `claude --resume`. [[lines 233-235](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/sessions.md?plain=1#L233-L235)] [[Source](https://code.claude.com/docs/en/sessions#delete-session-data)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Retitled from "Claude Code settings" to "Settings files and precedence" and trimmed a large block of redundant anchor placeholders and duplicated intro text; the "which value Claude Code uses" content now links out to "All settings" for the full key index. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/settings.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/settings#settings-files-and-precedence)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* Retitled from "Claude Code settings reference" to "All settings", and its key-index heading changed from "All settings" to "Settings index". [[lines 1](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/settings-reference.md?plain=1#L1), [525](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/settings-reference.md?plain=1#L525)]
* The `outputStyle` key's description now matches the new mid-session-switch behavior: it applies from your next message and rebuilds the prompt cache once, instead of waiting for `/clear` or a new session. [[line 1109](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/settings-reference.md?plain=1#L1109)] [[Source](https://code.claude.com/docs/en/settings-reference#outputstyle)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Restructured "Where skills live" into "Choose where skills load" (now including Nested and Additional-directory rows in the location table, and noting personal skills don't load in Cowork/cloud sessions) and a new "Resolve skills that share a name" table covering every location pair at once. [[line 101](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/skills.md?plain=1#L101), [147](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/skills.md?plain=1#L147)]
* "Live change detection" was renamed to "Edit a skill during a session" and now notes it doesn't apply in bare mode; corrected that Desktop scheduled tasks do load `~/.claude/skills/` (previously documented as loading from "the same locations" without saying so explicitly). [[line 228](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/skills.md?plain=1#L228)] [[Source](https://code.claude.com/docs/en/skills#how-claude-code-handles-the-body-of-a-synced-skill)]

#### [slash-commands (agent-sdk)](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/slash-commands.md) [[Source](https://code.claude.com/docs/en/slash-commands)]

* Received the same "Choose where skills load" / "Resolve skills that share a name" restructuring as [skills](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/skills.md), since this page mirrors that content. [[line 101](https://github.com/gpambrozio/ClaudeDocs/blob/01058d9b99076c474fab7c5ea09377a8cd47da37/docs-md/claude-code/slash-commands.md?plain=1#L101)] [[Source](https://code.claude.com/docs/en/slash-commands#create-your-first-skill)]
