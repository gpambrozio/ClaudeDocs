# [Claude docs changes for May 31st, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/4490b21729531c1adb9c4862b344a4f8838493fb) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/4490b21729531c1adb9c4862b344a4f8838493fb)]

## Executive Summary
- Claude Opus 4.8 is now the default model for Max, Team Premium, Enterprise pay-as-you-go, and Anthropic API accounts, with high effort by default and `/effort xhigh` for the hardest tasks
- Dynamic workflows (research preview) let Claude write an orchestration script and run it across dozens to hundreds of subagents for large tasks like codebase audits or migrations
- The new security-guidance plugin reviews code changes for vulnerabilities in the same session, running checks on each edit and a deeper review on commit or push
- Auto mode is now available on the Pro plan, supporting Sonnet 4.6 alongside Opus and replacing permission prompts with background safety checks
- Fast mode now defaults to Opus 4.8 at $10/$50 per MTok, delivering ~2.5x the speed at 2x the standard rate

-----

## Claude Code changes

### New Documents

#### [whats-new/2026-w21](https://github.com/gpambrozio/ClaudeDocs/blob/4490b21729531c1adb9c4862b344a4f8838493fb/docs-md/claude-code/whats-new/2026-w21.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w21)]

Week 21 digest (May 18–22, 2026) covering releases v2.1.143–v2.1.149. Key highlights: auto mode is now on the Pro plan with Sonnet 4.6 support; `/usage` now shows per-category breakdown attributing usage to skills, subagents, plugins, and MCP servers; new `/code-review` command reports correctness bugs with optional inline GitHub PR comments; background sessions appear in `/resume` and stay alive when pinned with `Ctrl+T`; `claude agents —json` lists live sessions as JSON; PowerShell tool enabled by default on Windows for Bedrock/Vertex/Foundry users; `/plugin` marketplace shows projected context cost; new `worktree.bgIsolation: "none"` setting for repos where worktrees are impractical; and the `allowAllClaudeAiMcps` enterprise managed setting loads claude.ai cloud MCP connectors.

#### [whats-new/2026-w22](https://github.com/gpambrozio/ClaudeDocs/blob/4490b21729531c1adb9c4862b344a4f8838493fb/docs-md/claude-code/whats-new/2026-w22.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w22)]

Week 22 digest (May 25–29, 2026) covering releases v2.1.150–v2.1.157. Key highlights: Claude Opus 4.8 is the new default model; dynamic workflows orchestrate many subagents from a script Claude writes, managed with `/workflows`; the security-guidance plugin provides real-time vulnerability review; fast mode now defaults to Opus 4.8; `!` prefix in `claude agents` runs shell commands as background jobs; plugins in `.claude/skills` directories are auto-loaded and `claude plugin init` scaffolds new plugins; new `/reload-skills` command; skills can set `disallowed-tools` in frontmatter; new `MessageDisplay` hook event for transforming displayed assistant text; vim mode `/` in NORMAL mode opens reverse history search; and streaming tool execution is always enabled including on Bedrock/Vertex/Foundry.

### Changed documents

#### [claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/4490b21729531c1adb9c4862b344a4f8838493fb/docs-md/claude-code/claude-platform-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

* Added an enterprise deployment call-to-action block near the top of the page with links to pricing plans and a contact sales form. [[lines 9-11](https://github.com/gpambrozio/ClaudeDocs/blob/4490b21729531c1adb9c4862b344a4f8838493fb/docs-md/claude-code/claude-platform-on-aws.md?plain=1#L9-L11)] [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

#### [whats-new](https://github.com/gpambrozio/ClaudeDocs/blob/4490b21729531c1adb9c4862b344a4f8838493fb/docs-md/claude-code/whats-new.md) [[Source](https://code.claude.com/docs/en/whats-new)]

* Added Week 22 entry (v2.1.150–v2.1.157, May 25–29) summarizing Claude Opus 4.8, dynamic workflows, the security-guidance plugin, and fast mode on Opus 4.8. [[lines 11-19](https://github.com/gpambrozio/ClaudeDocs/blob/4490b21729531c1adb9c4862b344a4f8838493fb/docs-md/claude-code/whats-new.md?plain=1#L11-L19)] [[Source](https://code.claude.com/docs/en/whats-new#week-22)]
* Added Week 21 entry (v2.1.143–v2.1.149, May 18–22) summarizing auto mode on Pro, `/usage` cost breakdown, `/code-review`, and background session improvements. [[lines 21-29](https://github.com/gpambrozio/ClaudeDocs/blob/4490b21729531c1adb9c4862b344a4f8838493fb/docs-md/claude-code/whats-new.md?plain=1#L21-L29)] [[Source](https://code.claude.com/docs/en/whats-new#week-21)]
