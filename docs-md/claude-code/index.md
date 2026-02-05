## [​](#get-started-in-30-seconds) Get started in 30 seconds

Prerequisites:

- Meet the [system requirements](setup.md)
- A [Claude subscription](https://claude.com/pricing) (Pro, Max, Teams, or Enterprise) or [Claude Console](https://console.anthropic.com/) account

**Install Claude Code:**
To install Claude Code, use one of the following methods:

- Native Install (Recommended)
- Homebrew
- WinGet

**macOS, Linux, WSL:**

Copy

Ask AI

```shiki
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell:**

Copy

Ask AI

```shiki
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD:**

Copy

Ask AI

```shiki
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

Native installations automatically update in the background to keep you on the latest version.

Copy

Ask AI

```shiki
brew install --cask claude-code
```

Homebrew installations do not auto-update. Run `brew upgrade claude-code` periodically to get the latest features and security fixes.

Copy

Ask AI

```shiki
winget install Anthropic.ClaudeCode
```

WinGet installations do not auto-update. Run `winget upgrade Anthropic.ClaudeCode` periodically to get the latest features and security fixes.

**Start using Claude Code:**

Copy

Ask AI

```shiki
cd your-project
claude
```

You’ll be prompted to log in on first use. That’s it! [Continue with Quickstart (5 minutes) →](quickstart.md)

See [advanced setup](setup.md) for installation options, manual updates, or uninstallation instructions. Visit [troubleshooting](troubleshooting.md) if you hit issues.

Claude Code also runs in [VS Code](vs-code.md), [JetBrains IDEs](jetbrains.md), as a [desktop app](desktop.md), [on the web](claude-code-on-the-web.md), and in [Slack](slack.md). See [all platforms](#use-claude-code-everywhere) below.

## [​](#what-claude-code-does-for-you) What Claude Code does for you

- **Build features from descriptions**: Tell Claude what you want to build in plain English. It will make a plan, write the code, and ensure it works.
- **Debug and fix issues**: Describe a bug or paste an error message. Claude Code will analyze your codebase, identify the problem, and implement a fix.
- **Navigate any codebase**: Ask anything about your team’s codebase, and get a thoughtful answer back. Claude Code maintains awareness of your entire project structure, can find up-to-date information from the web, and with [MCP](mcp.md) can pull from external data sources like Google Drive, Figma, and Slack.
- **Automate tedious tasks**: Fix fiddly lint issues, resolve merge conflicts, and write release notes. Do all this in a single command from your developer machines, or automatically in CI.

## [​](#why-developers-love-claude-code) Why developers love Claude Code

- **Meets you where you work**: Use Claude Code in your terminal, your IDE, or a standalone desktop app. It integrates with the tools you already use.
- **Takes action**: Claude Code can directly edit files, run commands, and create commits. Need more? [MCP](mcp.md) lets Claude read your design docs in Google Drive, update your tickets in Jira, or use *your* custom developer tooling.
- **Unix philosophy**: Claude Code is composable and scriptable. `tail -f app.log | claude -p "Slack me if you see any anomalies appear in this log stream"` *works*. Your CI can run `claude -p "If there are new text strings, translate them into French and raise a PR for @lang-fr-team to review"`.
- **Enterprise-ready**: Use the Claude API, or host on AWS or GCP. Enterprise-grade [security](security.md), [privacy](data-usage.md), and [compliance](https://trust.anthropic.com/) is built-in.

## [​](#use-claude-code-everywhere) Use Claude Code everywhere

Claude Code works across your development environment: in your terminal, in your IDE, in the cloud, and in Slack.

- **[Terminal (CLI)](quickstart.md)**: the core Claude Code experience. Run `claude` in any terminal to start coding.
- **[Claude Code on the web](claude-code-on-the-web.md)**: use Claude Code from your browser at [claude.ai/code](https://claude.ai/code) or the Claude iOS app, with no local setup required. Run tasks in parallel, work on repos you don’t have locally, and review changes in a built-in diff view.
- **[Desktop app](desktop.md)**: a standalone application with diff review, parallel sessions via git worktrees, and the ability to launch cloud sessions.
- **[VS Code](vs-code.md)**: a native extension with inline diffs, @-mentions, and plan review.
- **[JetBrains IDEs](jetbrains.md)**: a plugin for IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains IDEs with IDE diff viewing and context sharing.
- **[GitHub Actions](github-actions.md)**: automate code review, issue triage, and other workflows in CI/CD with `@claude` mentions.
- **[GitLab CI/CD](gitlab-ci-cd.md)**: event-driven automation for GitLab merge requests and issues.
- **[Slack](slack.md)**: mention Claude in Slack to route coding tasks to Claude Code on the web and get PRs back.
- **[Chrome](chrome.md)**: connect Claude Code to your browser for live debugging, design verification, and web app testing.

## [​](#next-steps) Next steps

[## Quickstart

See Claude Code in action with practical examples](quickstart.md)[## Common workflows

Step-by-step guides for common workflows](common-workflows.md)[## Troubleshooting

Solutions for common issues with Claude Code](troubleshooting.md)[## Desktop app

Run Claude Code as a standalone application](desktop.md)

## [​](#additional-resources) Additional resources

[## About Claude Code

Learn more about Claude Code on claude.com](https://claude.com/product/claude-code)[## Build with the Agent SDK

Create custom AI agents with the Claude Agent SDK](agent-sdk/overview.md)[## Host on AWS or GCP

Configure Claude Code with Amazon Bedrock or Google Vertex AI](third-party-integrations.md)[## Settings

Customize Claude Code for your workflow](settings.md)[## Commands

Learn about CLI commands and controls](cli-reference.md)[## Reference implementation

Clone our development container reference implementation](https://github.com/anthropics/claude-code/tree/main/.devcontainer)[## Security

Discover Claude Code’s safeguards and best practices for safe usage](security.md)[## Privacy and data usage

Understand how Claude Code handles your data](data-usage.md)

---

*Copyright © Anthropic. All rights reserved.*
