# [Claude docs changes for July 24th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/fe96bbaf1c156bae39cb148255f05367cc403095) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/fe96bbaf1c156bae39cb148255f05367cc403095)]

## Executive Summary
- `/code-review` now runs as a background subagent by default, so it no longer fills your conversation window; a new doc section explains when it still runs in the foreground and how `ultra` now accepts a plain-language note describing what to review.
- Agent view's background/foreground switching (`←`) got a big UX pass: a confirmation step before switching away from an emptied prompt, a "conversation moved to the background" banner, and a fix for an "Ambiguous ←" double-press issue on Windows.
- Read-only Bash command detection got more precise: `docker` pointed at another daemon, `file` with path-opening flags, Windows UNC paths, and unparseable commands now correctly prompt instead of silently running.
- New error reference entries cover `API Error: 401 Invalid authentication credentials`, `Claude Code process exited with code N` (wrapper/IDE errors), and the `--print` input-required error.
- New Claude API refusal category `general_harms`, and a new Admin API FAQ on what happens to a user's API keys after they leave the organization.

-----

## Claude Code changes

### Changed documents

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* v2.1.218: pressing `←` within two seconds of emptying the prompt or moving through prompt history now asks you to confirm with a second press instead of switching immediately, and a `←` inside pasted/scripted input no longer triggers the switch. [[line 167](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/agent-view.md?plain=1#L167)] [[Source](https://code.claude.com/docs/en/agent-view#attach-to-a-session)]
* Backgrounding a foreground session with `←` now shows "Your conversation moved to the background" above the list, and `Esc` at the agent-view root returns to that conversation instead of exiting. [[line 26](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/agent-view.md?plain=1#L26)] [[Source](https://code.claude.com/docs/en/agent-view#quick-start)]
* On Windows, pressing `←` within about half a second of attaching now shows `Ambiguous ←, press again to detach` instead of misfiring on a redelivered keypress. [[line 162](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/agent-view.md?plain=1#L162)] [[Source](https://code.claude.com/docs/en/agent-view#attach-to-a-session)]
* Full version history table entries added for v2.1.218, v2.1.216, and v2.1.213 covering the background-session dialog history. [[lines 662-664](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/agent-view.md?plain=1#L662-L664)] [[Source](https://code.claude.com/docs/en/agent-view#version-history)]

#### [checkpointing](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/checkpointing.md) [[Source](https://code.claude.com/docs/en/checkpointing)]

* New "Subagent edits not restored" section: edits from a subagent (including background `/code-review --fix` and forked skills running in the background) land outside your session's checkpoints, so `/rewind` can't undo them — use git instead. Foreground forks still restore normally. [[line 75](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/checkpointing.md?plain=1#L75)] [[Source](https://code.claude.com/docs/en/checkpointing#subagent-edits-not-restored)]

#### [claude-security](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/claude-security.md) [[Source](https://code.claude.com/docs/en/claude-security)]

* Documented that Fable 5's cybersecurity safety classifiers may block certain scan activities and auto-downgrade to Opus, and that this is expected. [[line 133](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/claude-security.md?plain=1#L133)] [[Source](https://code.claude.com/docs/en/claude-security#troubleshooting)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `--max-budget-usd`: subagent spend now counts toward the cap; once reached, spawning a subagent fails with `Budget limit reached` and running background subagents are stopped (requires v2.1.217+). [[line 88](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/cli-reference.md?plain=1#L88)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [code-review](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/code-review.md) [[Source](https://code.claude.com/docs/en/code-review)]

* The "Review a diff locally" section was rewritten into a step-by-step walkthrough: `/code-review` now runs as a background subagent with its own context window by default (previously it ran inline), and findings arrive in your conversation when it completes. [[line 278](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/code-review.md?plain=1#L278)] [[Source](https://code.claude.com/docs/en/code-review#review-a-diff-locally)]
* New "Run in the foreground" section listing the three cases that still run the review inline: a second concurrent `/code-review`, non-interactive mode (`-p`/Agent SDK), or `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1`. Also notes `/code-review` can't be used as a scheduled-task prompt since it's marked `disable-model-invocation`. [[line 298](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/code-review.md?plain=1#L298)] [[Source](https://code.claude.com/docs/en/code-review#run-in-the-foreground)]
* Stacking `/code-review /fix-issue 123` now treats everything after `/code-review` as review-target text rather than expanding `/fix-issue` as a second stacked skill, since `/code-review` runs as a forked subagent as of v2.1.218. [[line 295](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/code-review.md?plain=1#L295)] [[Source](https://code.claude.com/docs/en/code-review#tune-effort-and-arguments)]
* New "Escalate to ultrareview" section: you can now start a cloud ultrareview from a script or CI with `claude -p '/code-review ultra'`, which launches and prints a tracking link (requires v2.1.218+); if the run would bill usage credits, it stops and directs you to `claude ultrareview` instead, since billing confirmation needs an interactive session. [[line 308](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/code-review.md?plain=1#L308)] [[Source](https://code.claude.com/docs/en/code-review#escalate-to-ultrareview)]

#### [desktop-ios-simulator](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/desktop-ios-simulator.md) [[Source](https://code.claude.com/docs/en/desktop-ios-simulator)]

* Named the managed policy key that disables the simulator pane and Claude's tools entirely: `requireCoworkFullVmSandbox`, which runs Claude's tools inside an isolated VM instead of on your Mac. [[line 92](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/desktop-ios-simulator.md?plain=1#L92)] [[Source](https://code.claude.com/docs/en/desktop-ios-simulator#turn-off-simulator-access)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New "API Error: 401 Invalid authentication credentials" section: covers the case where a credential's format is valid but the account/organization behind it was revoked, disabled, or deactivated, with guidance to check `/status` to know whether your API key or your login is active. [[line 533](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/errors.md?plain=1#L533)] [[Source](https://code.claude.com/docs/en/errors#api-error-401-invalid-authentication-credentials)]
* New "Input must be provided either through stdin or as a prompt argument when using --print" section, covering bare `claude` falling into non-interactive mode when stdout isn't a real terminal (e.g. PowerShell ISE, some IDE panes). [[line 1160](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/errors.md?plain=1#L1160)] [[Source](https://code.claude.com/docs/en/errors#input-must-be-provided-when-using-print)]
* New "Wrapper and IDE errors" section and `Claude Code process exited with code N` entry, covering errors printed by the launching program (IDE extension, Agent SDK app) rather than Claude Code itself. [[line 1399](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/errors.md?plain=1#L1399)] [[Source](https://code.claude.com/docs/en/errors#wrapper-and-ide-errors)]
* Clarified that "Auto mode cannot determine the safety of an action" can now also mean an Amazon Bedrock account can't invoke the named classifier model (a persistent, not transient, failure), in addition to the classifier being overloaded/rate-limited. [[lines 197-207](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/errors.md?plain=1#L197-L207)] [[Source](https://code.claude.com/docs/en/errors#auto-mode-cannot-determine-the-safety-of-an-action)]
* Usage-limits section now distinguishes plan-quota errors from `Server is temporarily limiting requests` (a server-side throttle) and `Usage credits required for 1M context` (an entitlement check, not a quota). [[line 265](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/errors.md?plain=1#L265)] [[Source](https://code.claude.com/docs/en/errors#usage-limits)]

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* A `Fast mode ON`/`OFF` confirmation and the `↯` icon now appear consistently whenever a model switch changes fast mode state, including switches via `/config model=<model>` or Remote Control (previously those two paths changed fast mode silently). [[line 35](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/fast-mode.md?plain=1#L35)] [[Source](https://code.claude.com/docs/en/fast-mode#toggle-fast-mode)]

#### [network-config](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/network-config.md) [[Source](https://code.claude.com/docs/en/network-config)]

* In Claude Desktop sessions where the app manages the provider connection (Code tab on a third-party provider, Cowork sessions), Claude Code now reads proxy/TLS environment variables only from managed settings and `~/.claude/settings.json`, ignoring a repository's own settings files, so a checked-out repo can't redirect the connection (requires v2.1.217+ for this scoping). [[line 94](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/network-config.md?plain=1#L94)] [[Source](https://code.claude.com/docs/en/network-config#mtls-authentication)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Clarified that the "auto mode cannot determine the safety" message means a classifier request failed — usually transient, but on Amazon Bedrock it can repeat until the account is granted access to the named model. [[line 166](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/permission-modes.md?plain=1#L166)] [[Source](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Read-only Bash commands now correctly prompt in more cases: `docker`/Podman pointed at another daemon (`-H`, `--context`, `--url`, `--connection`), `file` with `-m`/`-f` path-opening flags, commands containing a Windows UNC network path, and commands longer than 10,000 characters or otherwise unparseable. [[lines 176-179](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/permissions.md?plain=1#L176-L179)] [[Source](https://code.claude.com/docs/en/permissions#read-only-commands)]
* Clarified that a single-segment relative directory pattern like `src/**` matches differently by rule type: as an allow rule it matches only `<cwd>/src`, but as a deny/ask rule it matches a `src` directory at any depth. Added a worked example table. [[lines 274-277](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/permissions.md?plain=1#L274-L277)] [[Source](https://code.claude.com/docs/en/permissions#read-and-edit)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Boolean frontmatter fields (e.g. `disable-model-invocation`) in plugin skills/commands now accept `yes`/`no`/`on`/`off`/`1`/`0` in any case, in addition to `true`/`false` (v2.1.218+). [[line 34](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/plugins-reference.md?plain=1#L34)] [[Source](https://code.claude.com/docs/en/plugins-reference#skills)]

#### [sessions](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/sessions.md) [[Source](https://code.claude.com/docs/en/sessions)]

* Clarified that resuming a session started with a custom `--agent` now looks in two places for that agent — the session's original directory (if trusted), then the directory you resume from — so a project-scoped agent still loads from elsewhere. [[line 26](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/sessions.md?plain=1#L26)] [[Source](https://code.claude.com/docs/en/sessions#what-a-resumed-session-restores)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New managed-settings-only key `disableMobileSimulatorTools` to block Claude's access to the desktop app's iOS Simulator pane while leaving manual use intact. [[line 236](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/settings.md?plain=1#L236)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* New `background` frontmatter field (applies with `context: fork`): set to `false` to wait for the forked subagent's result in the invoking turn instead of running it in the background. Default is now `true` — forked skills run in the background by default as of v2.1.218 (previously they always blocked the turn). [[line 230](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/skills.md?plain=1#L230)] [[Source](https://code.claude.com/docs/en/skills#frontmatter-reference)]
* Documented exceptions that still force a forked skill to wait for its result (non-interactive mode, `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1`, a second concurrent invocation, or a scheduled task), and that a backgrounded fork uses the narrower background-subagent tool set. Background fork edits also land outside session checkpoints. [[line 482 onward](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/skills.md?plain=1#L482)]
* Boolean frontmatter fields now accept `yes`/`no`/`on`/`off`/`1`/`0` in any case, in addition to `true`/`false` (v2.1.218+). [[line 213](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/skills.md?plain=1#L213)] [[Source](https://code.claude.com/docs/en/skills#frontmatter-reference)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Clarified that conversation-forking subagents are exempt from the smaller tool set that otherwise applies to background subagents. [[line 674](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/sub-agents.md?plain=1#L674)] [[Source](https://code.claude.com/docs/en/sub-agents#run-subagents-in-foreground-or-background)]

#### [troubleshoot-install](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/troubleshoot-install.md) [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

* New section on `running scripts is disabled on this system` / `PSSecurityException` when npm's `.ps1` launchers are blocked by PowerShell's execution policy, with three fixes (allow local scripts, use the `.cmd` launcher, or use the PowerShell installer). [[line ~469](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/troubleshoot-install.md?plain=1#L469)]
* "Native binary not found after npm install" rewritten: explains the new explicit `Error: claude native binary not installed` message (macOS/Linux) when postinstall didn't run or the optional platform dependency wasn't downloaded, plus a `cli-wrapper.cjs` fallback launcher and Windows placeholder-executable behavior. [[line 711](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/troubleshoot-install.md?plain=1#L711)] [[Source](https://code.claude.com/docs/en/troubleshoot-install#native-binary-not-found-after-npm-install)]
* Broadened the PowerShell "install script returns HTML" symptom description to cover version/language-dependent parse errors (`ParserError`/`ParseException`, `Missing expression after unary operator`), not just the single message shown before. [[lines 277-289](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/troubleshoot-install.md?plain=1#L277-L289)] [[Source](https://code.claude.com/docs/en/troubleshoot-install#install-script-returns-html-instead-of-a-shell-script)]

#### [troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* Added a lookup-table row pointing `Claude Code process exited with code 1` in VS Code or an SDK app to the new error-reference entry. [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/troubleshooting.md?plain=1#L14)] [[Source](https://code.claude.com/docs/en/troubleshooting)]

#### [ultrareview](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/ultrareview.md) [[Source](https://code.claude.com/docs/en/ultrareview)]

* Reorganized into dedicated subsections ("Review against a different base," "Review a pull request," "Diff limits and fallbacks") and added a new "Pass a request in plain words" section: on v2.1.218+, `/code-review ultra check my auth changes` reviews your current branch and relates findings to your note; a single word is still read as a branch/PR reference. [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/ultrareview.md?plain=1#L47)] [[Source](https://code.claude.com/docs/en/ultrareview#pass-a-request-in-plain-words)]
* Non-interactive `/code-review ultra` (e.g. `claude -p '/code-review ultra'`) now launches the cloud review and prints a tracking link without waiting, instead of running a local review as before v2.1.218; it still stops before launching if the run would bill usage credits, since that needs interactive confirmation. [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/ultrareview.md?plain=1#L95)] [[Source](https://code.claude.com/docs/en/ultrareview#run-ultrareview-non-interactively)]

#### [workflows](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* `/deep-research` now only runs when explicitly invoked; before v2.1.218, Claude could start it on its own. [[line 72](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/claude-code/workflows.md?plain=1#L72)] [[Source](https://code.claude.com/docs/en/workflows#bundled-workflows)]

-----

## API changes

### Changed documents

#### [refusals-and-fallback](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/api/build-with-claude/refusals-and-fallback.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)]

* Added a new refusal category `"general_harms"` to the `stop_details` table: requests related to an area determined to be harmful, which may also trigger on benign work. [[line 78](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/api/build-with-claude/refusals-and-fallback.md?plain=1#L78)] [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)]

#### [user-management](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/api/manage-claude/user-management.md) [[Source](https://platform.claude.com/docs/en/manage-claude/user-management)]

* New FAQ: "What happens to an Admin API key when the person who created it leaves?" — keys are org-scoped and don't expire, so they keep working after the creator is removed or downgraded; admins must manually delete and replace them when offboarding a key creator. [[line 655](https://github.com/gpambrozio/ClaudeDocs/blob/fe96bbaf1c156bae39cb148255f05367cc403095/docs-md/api/manage-claude/user-management.md?plain=1#L655)] [[Source](https://platform.claude.com/docs/en/manage-claude/user-management)]
