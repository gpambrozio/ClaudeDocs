# [Claude docs changes for June 14th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/137433043655164fcaed97f31dcc0cf2a96c3fdd) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/137433043655164fcaed97f31dcc0cf2a96c3fdd)]

## Executive Summary
- New `enforceAvailableModels` setting (v2.1.175+) allows administrators to constrain the Default model option to the `availableModels` allowlist, closing the bypass where users could always pick "Default" regardless of model restrictions
- Changed merge behavior: when `availableModels` is set in managed or policy settings, it now **replaces** (not merges with) lower-precedence entries, enabling strict enterprise allowlists
- Blocked `--model` flag now shows a warning naming both the requested and substituted models, instead of silently ignoring the flag

## New Claude Code versions

None today.

-----

## Claude Code changes

### Changed documents

#### [admin-setup](https://github.com/gpambrozio/ClaudeDocs/blob/137433043655164fcaed97f31dcc0cf2a96c3fdd/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

* Clarified that after configuring managed settings, developers should check the **Status** tab's `Setting sources` line in `/status` to verify enterprise managed settings are active. [[line 97](https://github.com/gpambrozio/ClaudeDocs/blob/137433043655164fcaed97f31dcc0cf2a96c3fdd/docs-md/claude-code/admin-setup.md?plain=1#L97)] [[Source](https://code.claude.com/docs/en/admin-setup#verify-and-onboard)]

#### [claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/137433043655164fcaed97f31dcc0cf2a96c3fdd/docs-md/claude-code/claude-platform-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

* Removed the marketing banner ("Deploying Claude Code across your organization?") with links to pricing and sales contact from the top of the page.

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/137433043655164fcaed97f31dcc0cf2a96c3fdd/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* A blocked `--model` flag or `ANTHROPIC_MODEL` value now shows a warning at startup naming both the requested and substituted models, instead of being silently ignored. [[line 100](https://github.com/gpambrozio/ClaudeDocs/blob/137433043655164fcaed97f31dcc0cf2a96c3fdd/docs-md/claude-code/model-config.md?plain=1#L100)] [[Source](https://code.claude.com/docs/en/model-config#restrict-model-selection)]
* New `enforceAvailableModels` setting: when `true` alongside a non-empty `availableModels` list in managed or policy settings, the Default model option is also constrained to the allowlist rather than resolving to the tier default. Requires v2.1.175+. [[lines 110-112](https://github.com/gpambrozio/ClaudeDocs/blob/137433043655164fcaed97f31dcc0cf2a96c3fdd/docs-md/claude-code/model-config.md?plain=1#L110-L112)] [[Source](https://code.claude.com/docs/en/model-config#default-model-behavior)]
* Updated guidance for fully controlling the model experience now includes `enforceAvailableModels` as a required component alongside `availableModels`, `model`, and the `ANTHROPIC_DEFAULT_*` env vars. [[lines 115-145](https://github.com/gpambrozio/ClaudeDocs/blob/137433043655164fcaed97f31dcc0cf2a96c3fdd/docs-md/claude-code/model-config.md?plain=1#L115-L145)] [[Source](https://code.claude.com/docs/en/model-config#control-the-model-users-run-on)]
* Changed merge behavior: when `availableModels` is set in managed or policy settings, the managed/policy value now **replaces** the merged result from user/project/local settings entirely. Prior to v2.1.175, the managed list was merged with lower-precedence entries. [[lines 148-150](https://github.com/gpambrozio/ClaudeDocs/blob/137433043655164fcaed97f31dcc0cf2a96c3fdd/docs-md/claude-code/model-config.md?plain=1#L148-L150)] [[Source](https://code.claude.com/docs/en/model-config#special-model-behavior)]
* Added behavior note for `opusplan`: when `availableModels` excludes Opus, `opusplan` stays on Sonnet in plan mode instead of switching; similarly if Sonnet is excluded, the implicit Haiku-to-Sonnet plan-mode upgrade is skipped. [[line 174](https://github.com/gpambrozio/ClaudeDocs/blob/137433043655164fcaed97f31dcc0cf2a96c3fdd/docs-md/claude-code/model-config.md?plain=1#L174)] [[Source](https://code.claude.com/docs/en/model-config#opusplan-model-setting)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/137433043655164fcaed97f31dcc0cf2a96c3fdd/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `availableModels` and `enforceAvailableModels` to the security-enforcement fields table: invalid `availableModels` entries fall back to an empty allowlist (only Default available), and invalid `enforceAvailableModels` is treated as `true`. Both apply in v2.1.175+. [[lines 155-156](https://github.com/gpambrozio/ClaudeDocs/blob/137433043655164fcaed97f31dcc0cf2a96c3fdd/docs-md/claude-code/settings.md?plain=1#L155-L156)] [[Source](https://code.claude.com/docs/en/settings#invalid-entries-in-managed-settings)]
* Updated `availableModels` setting description to remove the previous note that it "does not affect the Default option" (now controlled via `enforceAvailableModels`). [[line 194](https://github.com/gpambrozio/ClaudeDocs/blob/137433043655164fcaed97f31dcc0cf2a96c3fdd/docs-md/claude-code/settings.md?plain=1#L194)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* New `enforceAvailableModels` setting entry added to the settings reference table. Requires v2.1.175+. [[line 219](https://github.com/gpambrozio/ClaudeDocs/blob/137433043655164fcaed97f31dcc0cf2a96c3fdd/docs-md/claude-code/settings.md?plain=1#L219)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Clarified array merge behavior: `availableModels` is now documented as a second exception (alongside `fallbackModel`) where a managed/policy value replaces lower-precedence entries instead of merging. [[line 547](https://github.com/gpambrozio/ClaudeDocs/blob/137433043655164fcaed97f31dcc0cf2a96c3fdd/docs-md/claude-code/settings.md?plain=1#L547)] [[Source](https://code.claude.com/docs/en/settings#settings-precedence)]
* Improved `/status` documentation: restructured into a bulleted list explaining what each layer's presence or absence means, with clearer separation between the Status tab and Config tab purposes. [[lines 554-561](https://github.com/gpambrozio/ClaudeDocs/blob/137433043655164fcaed97f31dcc0cf2a96c3fdd/docs-md/claude-code/settings.md?plain=1#L554-L561)] [[Source](https://code.claude.com/docs/en/settings#verify-active-settings)]

-----

## API changes

### Changed documents

No significant changes today. (Only obfuscated email URL updates in `adaptive-thinking`, `extended-thinking`, and `files`.)
