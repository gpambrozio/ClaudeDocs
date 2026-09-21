# [Claude docs changes for September 5th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/0542a8b827cf62cf2747ceba4b16647c4ad23952) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/0542a8b827cf62cf2747ceba4b16647c4ad23952)]

## Executive Summary
- New `ant apply` page: manage Claude API resources — agents, environments, skills, memory stores, deployments — as files in your repository, reconciled through a committed `claude-lock.json`, with a plan-and-approve flow, `--prune`, and a documented CI recipe
- "Preserved thinking" was rewritten from a section of the thinking page into a standalone treatment, and it carries a forward-looking warning: **later models will enforce the prefix check for all accounts**, so make your integration append-only now
- `/diff` gains a full diff panel in fullscreen rendering: it opens beside the conversation, refreshes as Claude edits, lets you select lines to attach to your next prompt, and cycles what it compares against with `Ctrl+X B`
- Word-editing keys now follow readline conventions unconditionally — `Ctrl+W` deletes back to whitespace while `Alt+B`/`Alt+F`/`Alt+D` stop at word boundaries — and the `keybindingFlavor` setting that used to toggle this is deprecated with no effect
- New `/skill-doctor` command shows what each loaded skill costs in context and how often it's used, so you can prune the unused ones

## New Claude Code versions

### [2.1.261](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/versions/2.1.261.md)

#### New features

* Added `/skill-doctor` to show which loaded skills go unused and what they cost in context
* Added `bashOutputMaxChars` and `taskOutputMaxChars` settings to raise how much command and background-task output Claude receives inline, up to 128K characters
* Added an "Organization policy" line to `/status` and `claude doctor` explaining why your organization's policy couldn't be loaded
* Added `--append-subagent-system-prompt-file` for subagent prompts too large to pass on the command line

#### Existing feature improvements

* Improved the `/model` picker and VS Code model pill to show a model's name instead of its raw Bedrock, Vertex AI or gateway ID
* Improved the dangerous-`rm` safety prompt to also catch `rm -rf` on positional parameters and inside double-quoted `sh -c` scripts
* Improved handling when the API sends no response headers: the retry now waits up to `API_TIMEOUT_MS` instead of another 3 minutes
* Improved startup on Google Vertex AI when `GOOGLE_APPLICATION_CREDENTIALS` is set, avoiding repeated project discovery and extra `gcloud` processes
* Changed the prompt's word-editing keys to match Bash; `keybindingFlavor` no longer has any effect
* Changed auto mode to treat a link that packs content into a public diagram renderer's URL as an upload to that site
* Changed machines whose managed settings pin `forceLoginMethod: "gateway"` to ignore a leftover API key or claude.ai login
* Changed `/context` token counting to use a local estimate when the token-counting API is unavailable

#### Major bug fixes

* Fixed typed or pasted characters occasionally landing out of order or being dropped during fast input or key repeat
* Fixed resuming a session losing hook output and other context around parallel tool calls, which changed the resumed request
* Fixed SDK and cloud sessions ignoring a Stop or interrupt sent just after the first prompt, before the turn had started
* Fixed in-process agent-team teammates re-sending first-turn announcements on the second turn, which missed the prompt cache
* Fixed sustained high CPU usage when a background agent could not be resumed and its wake-up was retried in a tight loop
* Fixed feature flags gated to a newer version occasionally applying to an older Claude Code version on the same machine
* Fixed `SendMessage` to an offline Remote Control session on another machine reading as delivered
* Fixed several Remote Control issues: stale permission mode on attach, stuck spinners after stopping a turn remotely, failures behind TLS-inspecting proxies on native Windows, and `/teleport` uploads appearing appended to the original session
* Fixed cloud sessions discarding a plugin synced from claude.ai when managed settings force-enable it in `enabledPlugins`
* Fixed `claude -p --resume <file>` adopting a malformed session ID recorded in the transcript

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/permissions](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/agent-sdk/permissions.md) [[Source](https://code.claude.com/docs/en/agent-sdk/permissions)]

* The final step of the permission flow now covers `permissionPrompts: 'none'`: your `canUseTool` callback isn't called, a `PermissionRequest` hook still gets a chance, and Claude Code denies the call if it doesn't decide. [[line 43](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L43)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#how-permissions-are-evaluated)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* New `permissionPrompts` option (`'host' | 'none'`), the SDK counterpart of `--permission-prompts`. Requires Claude Code v2.1.259. [[line 435](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L435)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#options)]
* New `user_message_uuids` field, listing the `uuid`s of every message answered in a turn. It exists because Claude Code can **merge several messages sent close together into one turn**, in which case the singular `user_message_uuid` names only the last of them. The list holds at most 64 entries, and a message picked up mid-turn between tool calls appears only in the result's list. [[lines 1324-1328](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1324-L1328)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#user_message_uuids)]
* `user_message_uuid` now documented across three kinds of frame — the result, the turn's first reply, and every `thinking_tokens` frame — each with its own SDK version requirement. [[lines 1309-1322](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1309-L1322)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#user_message_uuid)]
* The interrupt receipt's `still_queued` explained in full: listed messages are processed after the interrupt unless you cancel them, and **a listed message you don't cancel enters the conversation whether or not it gets a response, so resending it delivers it twice**. [[lines 652-653](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L652-L653)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkcontrolinterruptresponse)]
* New latency fields `first_content_frame_ms` (counting thinking blocks as content) plus three `first_stream_post_*` timings recorded only in sessions streamed to claude.ai. [[lines 1277-1278](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1277-L1278)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkresultmessage)]
* The permission-denied event's three configurations spelled out, including that with an **MCP prompt tool Claude Code doesn't emit the event at all**, not even for its own rule denials. [[lines 1471-1474](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1471-L1474)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkpermissiondeniedmessage)]
* The live-tasks event's `tasks` array is the full live set — replace any cached set with each payload rather than pairing start and completion events, so the next membership change corrects anything you missed. [[lines 4815-4816](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L4815-L4816)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkbackgroundtaskschangedmessage)]
* `ambient` documented as marking tasks that aren't part of the session's work, including live-update watchers — exclude them from activity indicators. [[line 4758](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L4758)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdktaskstartedmessage)]

#### [auto-mode-config](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/auto-mode-config.md) [[Source](https://code.claude.com/docs/en/auto-mode-config)]

* New **Host containment** context slot. It defaults to assuming an ordinary developer machine with open internet, and **until the slot names the task's identity the classifier blocks requests for the host's own credentials**. Requires v2.1.257. [[lines 73-83](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/auto-mode-config.md?plain=1#L73-L83)] [[Source](https://code.claude.com/docs/en/auto-mode-config#define-trusted-infrastructure)]

#### [checkpointing](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/checkpointing.md) [[Source](https://code.claude.com/docs/en/checkpointing)]

* File snapshots are deleted by the retention sweep about 30 days after a session last saved one, so rewinding to an older checkpoint can fail with `No files were restored`. Raise `cleanupPeriodDays` to keep them longer. [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/checkpointing.md?plain=1#L16)] [[Source](https://code.claude.com/docs/en/checkpointing#automatic-tracking)]

#### [claude-directory](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* Auto memory is now exempt from the retention sweep: Claude Code removes `projects/<project>/memory/` only after it has been empty for the whole retention period. Before v2.1.228 the sweep treated folders inside it as session data and could delete old files. [[line 209](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/claude-directory.md?plain=1#L209)] [[Source](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically)]
* New table of paths the sweep never removes, including `history.jsonl` — every prompt you've typed, with timestamp and project path. [[lines 219-223](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/claude-directory.md?plain=1#L219-L223)] [[Source](https://code.claude.com/docs/en/claude-directory#kept-until-you-delete-them)]

#### [cloud-environments](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/cloud-environments.md) [[Source](https://code.claude.com/docs/en/cloud-environments)]

* `*.frame.claudeusercontent.com` is no longer needed in a cloud environment's allowlist for reading your own artifacts — Claude Code reads them through the session's connection to Anthropic. Two cases still need it: opening another organization's public artifacts, and configuring the local CLI or a self-hosted runner. [[lines 189-192](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/cloud-environments.md?plain=1#L189-L192)] [[Source](https://code.claude.com/docs/en/cloud-environments#allow-specific-domains)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* New `/skill-doctor` and `/diff` entries. `/skill-doctor` requires v2.1.252 and feature-flag fetching. [[lines 64-121](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/commands.md?plain=1#L64-L121)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]
* `/add-dir` run while Claude is responding now asks you to confirm right away, and once confirmed Claude's next tool call in the same turn can use it. Before v2.1.234 the command was queued until the turn finished. [[line 34](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/commands.md?plain=1#L34)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* The cache-miss threshold is now stated: a request counts as a miss when it re-processed more than 5% **and** at least 2,000 tokens of what it could have read from cache. When a likely cause can be identified, the line names it, such as `likely cause: tool definitions changed`. Requires v2.1.260. [[line 37](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/costs.md?plain=1#L37)] [[Source](https://code.claude.com/docs/en/costs#prompt-cache-statistics)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `BASH_MAX_OUTPUT_LENGTH` and `TASK_MAX_OUTPUT_LENGTH` are now **ignored** when the corresponding `bashOutputMaxChars` / `taskOutputMaxChars` setting is present. [[lines 164-447](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/env-vars.md?plain=1#L164-L447)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` gained the same inverted-boolean warning as `FALLBACK_FOR_ALL_PRIMARY_MODELS`: setting it to `0` or `false` **still disables** the traffic; you have to unset it. The entry also now lists the background runs of plugin `command` sources, which are local rather than network but can trigger dependency installs. [[line 233](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/env-vars.md?plain=1#L233)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS`, capping idle waiting for background subagents and workflows after the final `-p` turn at 10 minutes by default, restarting each time Claude takes a turn to handle a background result. [[line 309](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/env-vars.md?plain=1#L309)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* "No response from API" rewritten with the actual deadline arithmetic. The first attempt's header wait comes from `CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS` (clamped to 10 seconds–30 minutes) plus one second per 32KB of request body; the **retry** waits one second less than `API_TIMEOUT_MS`, just under 10 minutes, so it can outlast a proxy that holds the response until generation completes. A positive `API_TIMEOUT_MS` under 11 seconds turns the deadline off entirely. [[lines 335-354](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/errors.md?plain=1#L335-L354)] [[Source](https://code.claude.com/docs/en/errors#no-response-from-api)]
* New "Task output swap refused" section: a directory on the Bash output file's path is a symlink or was moved, so Claude Code refuses to run the command rather than write through it. Upgrade to v2.1.260, where earlier versions sometimes raised this with no link present. [[lines 2511-2522](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/errors.md?plain=1#L2511-L2522)] [[Source](https://code.claude.com/docs/en/errors#task-output-swap-refused)]
* New "Skill usage reports are not available on this connection": `/skill-doctor` doesn't send its report over Remote Control. [[lines 2198-2208](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/errors.md?plain=1#L2198-L2208)] [[Source](https://code.claude.com/docs/en/errors#skill-usage-reports-are-not-available-on-this-connection)]
* The plugin path-escape check now follows symlinks and names where the path resolves. Before v2.1.257 it looked only at the path's spelling. [[lines 2282-2293](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/errors.md?plain=1#L2282-L2293)] [[Source](https://code.claude.com/docs/en/errors#path-escapes-plugin-directory)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* New "Review changes with /diff" section documenting the **diff panel**. It needs fullscreen rendering, a git repository, a terminal at least 110 columns wide, and v2.1.260. It opens on its own once Claude starts editing files if your terminal is at least 144 columns wide, and once you've opened it manually it opens on edits in later sessions too — closing it makes that stick until you run `/diff` again. [[lines 466-490](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/interactive-mode.md?plain=1#L466-L490)] [[Source](https://code.claude.com/docs/en/interactive-mode#review-changes-with-/diff)]
* While the panel is open you can select lines with the mouse to attach them to your next prompt, expand the test and generated files it skips, and press `Ctrl+X B` to cycle between this session's changes, all uncommitted changes, and everything since the branch split — remembered per project. [[lines 483-488](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/interactive-mode.md?plain=1#L483-L488)] [[Source](https://code.claude.com/docs/en/interactive-mode#diff-panel)]
* New "Word boundaries in editing shortcuts" section. `Alt+B`, `Alt+F`, `Alt+D`, `Option+Delete` and `Ctrl+Backspace` treat a word as a run of letters and digits, so `src/utils/foo.ts` takes four `Alt+B` presses — while `Ctrl+W` ignores punctuation and removes the whole path in one. These conventions apply from v2.1.261 and **can't be remapped**, since the keybindings file has no actions for them. [[lines 47-53](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/interactive-mode.md?plain=1#L47-L53)] [[Source](https://code.claude.com/docs/en/interactive-mode#make-ctrl-w-delete-back-to-whitespace)]
* The diff **viewer** (the classic renderer's version) documented separately, with its turn views built from Claude's file edits rather than git — so a change Claude makes through a shell command appears only under Current. [[lines 492-502](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/interactive-mode.md?plain=1#L492-L502)] [[Source](https://code.claude.com/docs/en/interactive-mode#diff-viewer)]

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* The `/plugin` interface gained a **Stats** tab carrying the same skill cost-and-usage report as `/skill-doctor`. [[lines 142-148](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/discover-plugins.md?plain=1#L142-L148)] [[Source](https://code.claude.com/docs/en/discover-plugins#try-it-add-the-demo-marketplace)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* New `bashOutputMaxChars` and `taskOutputMaxChars` settings; `keybindingFlavor` marked deprecated with no effect. The settings count rose to 225. [[lines 19-223](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/settings-reference.md?plain=1#L19-L223)] [[Source](https://code.claude.com/docs/en/settings-reference#all-settings)]
* A useful scope note on deny rules: Read and Edit denies cover the built-in file tools, the file commands Claude Code recognizes in Bash such as `cat`, `head`, `tail` and `sed`, and Bash redirection targets — but **not arbitrary subprocesses**, so OS-level enforcement means enabling the sandbox. [[line 911](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/settings-reference.md?plain=1#L911)] [[Source](https://code.claude.com/docs/en/settings-reference#permissions-deny)]

#### [deep-links](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/deep-links.md) [[Source](https://code.claude.com/docs/en/deep-links)]

* The `cwd` parameter now rejects network and UNC paths, `..` segments, and invisible or bidirectional control characters. [[line 45](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/deep-links.md?plain=1#L45)] [[Source](https://code.claude.com/docs/en/deep-links#build-a-link)]

#### [agent-sdk/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/agent-sdk/migration-guide.md) [[Source](https://code.claude.com/docs/en/agent-sdk/migration-guide)]

* Added a pointer to an OpenAI Agents SDK migration recipe mapping each primitive onto the Claude Agent SDK through one worked example. [[line 4](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/claude-code/agent-sdk/migration-guide.md?plain=1#L4)] [[Source](https://code.claude.com/docs/en/agent-sdk/migration-guide#overview)]

-----

## API changes

### New Documents

#### [cli-sdks-libraries/cli/apply](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/api/cli-sdks-libraries/cli/apply.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/apply)]

`ant apply` creates and updates Claude API resources from files — agents, environments, skills, memory stores and deployments — so they live in your repository and change through the same review as your code. Requires CLI 1.30.0 or later. The page covers:

* **The lockfile.** The first run writes `claude-lock.json` in the directory you ran it from, recording each file's resource ID, the organization and workspace, and two hashes fingerprinting what was last sent and what the API returned — which is how a later run notices an edited file, or a resource changed outside these files. Commit it.
* **Kind inference**, in order: a top-level `type` field, then the containing directory (`agents/`, `environments/`, `memory_stores/`, `deployments/`), then a filename starting with the kind. Files matching none are skipped unless named explicitly; a named Markdown file that matches none is treated as an agent, while a named YAML or JSON file that matches none is an error.
* **Drift handling.** A resource edited, archived or deleted outside these files makes the plan end with `This plan cannot be applied:` and exit with `refusing to apply`; `--force` overwrites. Deleting a file leaves the resource in place with a warning unless you pass `--prune`, so **renaming a file declares a new resource and leaves the old one behind**.
* **A hard limit worth knowing**: `ant apply` can't adopt a resource created in the Console or with `ant beta:agents create` — applying a file describing an existing agent creates a second one. The Console's **Export as code** download does include its own lockfile.
* **CI guidance**: run `ant apply --yes .` naming the project directory (a bare `ant apply --yes` skips newly added files), `--dry-run .` on pull requests, commit the updated lockfile even when the apply step failed partway since a partial apply still records what it created, run one apply at a time because nothing locks the lockfile, and authenticate with Workload Identity Federation — `ant apply` refuses credentials resolving to a different organization or workspace.

### Changed documents

#### [build-with-claude/preserved-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/api/build-with-claude/preserved-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking)]

* Substantially rewritten (462 lines changed), absorbing 74 lines moved out of the thinking page and gaining a precise account of the two checks on a returned block's `signature`: a model check that applies to every account, and a prefix check enforced by default only for accounts created on or after August 31, 2026 00:00 UTC. **"Later models will enforce the prefix check for all accounts"** is now stated outright. [[lines 7-12](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/api/build-with-claude/preserved-thinking.md?plain=1#L7-L12)] [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#preserved-thinking)]
* The recommended handling on a model switch is counterintuitive and now explicit: **keep sending the full history including thinking blocks and let the API drop what the current model can't read.** The API never edits your `messages` array, so when the history returns to Fable 5.1 its blocks are readable again — the reasoning is lost for good only if your own client strips them. [[line 21](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/api/build-with-claude/preserved-thinking.md?plain=1#L21)] [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#switching-models-mid-conversation)]
* The checked prefix has exactly three parts, and `effort`, `max_tokens`, `output_config`, `tool_choice`, `metadata` and `cache_control` markers are explicitly outside it. Under server-side compaction the prefix starts at the most recent compaction block. [[lines 45-53](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/api/build-with-claude/preserved-thinking.md?plain=1#L45-L53)] [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#keeping-the-prefix-unchanged)]
* Production recovery advice for a 400 you're already hitting: retrying the same body fails the same way, so retry with the beta header and `prefix_mismatch_behavior: "drop_block"` and keep sending it for the rest of the session, or strip every thinking block yourself and retry once. **In the Message Batches API an item that leaves the field unset drops failing blocks rather than erroring**, so set `"error"` explicitly there if you want batch items to fail. [[line 86](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/api/build-with-claude/preserved-thinking.md?plain=1#L86)] [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#what-the-api-does-with-an-invalid-block)]
* A tampered or undecryptable signature is a distinct failure that always returns a 400 and that `prefix_mismatch_behavior` never applies to. [[line 88](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/api/build-with-claude/preserved-thinking.md?plain=1#L88)] [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#what-the-api-does-with-an-invalid-block)]
* A neat framing of the discipline required: "the edits that invalidate thinking are the edits that restart the cache." [[line 57](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/api/build-with-claude/preserved-thinking.md?plain=1#L57)] [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#keeping-the-prefix-unchanged)]

#### [build-with-claude/thinking](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/api/build-with-claude/thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking)]

* Shed 142 lines as the preserved-thinking material moved to its own page.

#### [api/admin/analytics/usage/list](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/api/api/admin/analytics/usage/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/usage/list)]

* New Claude Tag filters across the four analytics endpoints: by spend category, and by Slack user ID (not claude.ai user ID), each with a matching `group_by[]` value. Two gotchas are documented — usage with no category never matches, and `dm` usage is reported under the user's own product, so combining the category filter with `products[]=claude-tag` excludes it. [[lines 48-68](https://github.com/gpambrozio/ClaudeDocs/blob/0542a8b827cf62cf2747ceba4b16647c4ad23952/docs-md/api/api/admin/analytics/usage/list.md?plain=1#L48-L68)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#query-parameters)]
