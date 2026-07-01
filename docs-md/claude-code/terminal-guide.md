# Terminal guide for new users

You can use Claude Code even if you’ve never used a terminal before. This guide walks you through opening a terminal, installing Claude Code, and your first interactions.

- [macOS and Linux](#macos-and-linux)
- [Windows](#windows)

Don’t want to use the terminal? The Claude Code desktop app lets you skip the terminal entirely. Download it for [macOS](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect?utm_source=claude_code&utm_medium=docs), [Windows](https://claude.com/download?utm_source=claude_code&utm_medium=docs), or [Linux](https://claude.com/download?utm_source=claude_code&utm_medium=docs), then see the [Desktop quickstart](desktop-quickstart.md) to get started.

## [​](#macos-and-linux) macOS and Linux

Follow these steps to install and start Claude Code from a macOS or Linux terminal. Claude Code requires macOS 13.0 or later. See the [system requirements](setup.md) for supported Linux distributions.

1

Open a terminal

**macOS**: Press `Cmd + Space` to open Spotlight Search, type `Terminal`, and press `Enter`.**Linux**: Open your terminal app. On most distributions, press `Ctrl + Alt + T` or search for “Terminal” in your application menu.A window will appear with a blinking cursor. This is your terminal, where you type commands.

2

Install Claude Code

Copy this line, paste it into your terminal (`Cmd + V` on macOS, `Ctrl + Shift + V` on Linux), and press `Enter`:

```shiki
curl -fsSL https://claude.ai/install.sh | bash
```

This downloads and runs the Claude Code installer from claude.ai. You’ll see text scrolling as it works. When it’s done, you’ll see “Claude Code successfully installed!” If you see an error instead, check the [troubleshooting section](#macos-and-linux-troubleshooting) below.

3

Start Claude Code

Type `claude` and press `Enter`:

```shiki
claude
```

You’ll be prompted to [log in](authentication.md) with your Claude account. Follow the on-screen instructions. A browser window will open for you to sign in.

4

Start using Claude Code

Once logged in, you can start asking Claude questions about your code or anything else. Claude Code runs entirely in text. You type messages and press `Enter` to send them. A few things to know:

- You can’t click on things in the terminal. Use the arrow keys to move around.
- Press `Esc` to interrupt Claude if it’s running.
- Type `exit` or press `Ctrl + D` to leave Claude Code.
- Type `/help` to see available commands.

---

## [​](#windows) Windows

Follow these steps to optionally install Git for Windows, set up PowerShell, and start Claude Code on Windows. Claude Code requires Windows 10 version 1809 or later. See the [system requirements](setup.md) for full details.

1

Install Git for Windows (optional)

Git for Windows provides Git Bash, which enables the Bash tool. Without it, Claude Code uses PowerShell instead. You won’t need to learn Git yourself.If you don’t already have it:

1. Go to [git-scm.com/downloads/win](https://git-scm.com/downloads/win) and download the installer
2. Run the installer. Click Next on each screen to accept the defaults. The installer has many screens, but you don’t need to change anything.
3. If it asks you to choose an editor, keep the default and click Next.
4. When you see “Adjusting your PATH environment,” keep the recommended option selected.

Already have Git? You can skip this step. If you’re not sure, install it anyway. Reinstalling won’t cause problems.

2

Open PowerShell

PowerShell is Windows’ built-in terminal for typing commands. It comes pre-installed on every Windows computer.Press `Win + X` and select **Windows PowerShell** (or **Terminal**) from the menu. A window with a blinking cursor will appear. This is where you’ll type commands.

Windows has two command-line programs: PowerShell and CMD. They look similar but use different commands. Make sure you’re in PowerShell for the next step.How to tell which one you’re in:

- **PowerShell**: shows `PS C:\Users\YourName>` at the start of each line
- **CMD**: shows `C:\Users\YourName>` without the `PS`

3

Install Claude Code

Copy this line, paste it into PowerShell with `Ctrl + V` or right-click, and press `Enter`:

```shiki
irm https://claude.ai/install.ps1 | iex
```

This downloads and runs the Claude Code installer. `irm` fetches the file and `iex` runs it. You’ll see text scrolling as it works. When it’s done, you’ll see “Claude Code successfully installed!” If you see an error instead, check the [troubleshooting section](#windows-troubleshooting) below.

If you’re in CMD instead of PowerShell, use this command:

```shiki
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

4

Start Claude Code

Run `claude`. If PowerShell says `'claude' is not recognized`, the install directory isn’t on your PATH yet. Follow the [‘claude is not recognized’](#windows-troubleshooting) fix below, then open a new PowerShell window and try again.

```shiki
claude
```

You’ll be prompted to [log in](authentication.md) with your Claude account. Follow the on-screen instructions. A browser window will open for you to sign in.

5

Start using Claude Code

Once logged in, you can start asking Claude questions about your code or anything else. Claude Code runs entirely in text. You type messages and press `Enter` to send them. A few things to know:

- You can’t click on things in the terminal. Use the arrow keys to move around.
- Press `Esc` to interrupt Claude if it’s running.
- Type `exit` or press `Ctrl + D` to leave Claude Code.
- Type `/help` to see available commands.

---

## [​](#what’s-next) What’s next?

Once you see the Claude Code welcome screen, you’re ready to go. You don’t need to know how to code. Describe what you want in plain English, and Claude writes the code for you.

### [​](#build-something) Build something

Claude can create projects from a description:

```shiki
make me a simple webpage that says hello world
```

Claude creates the files for you. Double-click the HTML file to open it in your browser.

### [​](#work-with-files-on-your-computer) Work with files on your computer

Claude can read and organize files you already have:

```shiki
look at the screenshots on my Desktop and rename them based on what's in each image
```

### [​](#ask-questions) Ask questions

Claude can explain things, help you learn, or plan out a project:

```shiki
I want to build a personal budget tracker. What would I need?
```

If you don’t have a project yet, that’s fine. Claude can help you start a new one.

### [​](#other-ways-to-use-claude-code) Other ways to use Claude Code

You don’t have to use the terminal. Claude Code is also available in:

- [VS Code](vs-code.md) and [JetBrains IDEs](jetbrains.md) as editor extensions
- The [desktop app](desktop-quickstart.md), with no terminal required
- The [web](claude-code-on-the-web.md) at claude.ai/code for cloud sessions
- [GitHub Actions](github-actions.md) and [GitLab CI/CD](gitlab-ci-cd.md) for automation

### [​](#learn-more) Learn more

- [Quickstart](quickstart.md): a guided walkthrough of your first project with Claude Code
- [How Claude Code works](how-claude-code-works.md): understand how Claude reads your files, runs commands, and makes edits
- [Best practices](best-practices.md): get better results with effective prompting and project setup
- [Common workflows](common-workflows.md): step-by-step guides for debugging, testing, refactoring, and more
- [Terminal configuration](terminal-config.md): customize your terminal for the best Claude Code experience

---

## [​](#troubleshooting) Troubleshooting

### [​](#macos-and-linux-troubleshooting) macOS and Linux troubleshooting

If you run into problems installing on macOS or Linux, check these common issues:

'command not found: claude'

If you see `command not found: claude` after installing, the folder where the installer put `claude` isn’t in your PATH. The installer prints the exact fix under `Setup notes` at the end of the install, so run that command, or use the one for your shell below.For Zsh, the macOS default shell:

```shiki
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

For Bash, the Linux default shell:

```shiki
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Then open a new terminal and try `claude` again. If it still isn’t found, check that the file `~/.local/bin/claude` exists. If it doesn’t, the install didn’t finish. For more details, see [fix your PATH](troubleshoot-install.md).

Error with HTML code or 'syntax error near unexpected token'

If you see `bash: line 1: syntax error near unexpected token '<'` or HTML code like `<!DOCTYPE html>` in your terminal, the install URL returned a web page instead of the installer script.If the page says “App unavailable in region,” Claude Code is not available in your country. See [supported countries](https://www.anthropic.com/supported-countries).Otherwise, try running the command again. If it keeps happening, install with [Homebrew](https://brew.sh) instead:

```shiki
brew install --cask claude-code
```

'dyld' error or 'built for Mac OS X 13.0'

If you see `dyld: cannot load`, `dyld: Symbol not found`, or `built for Mac OS X 13.0`, your macOS version is likely older than Claude Code supports.Open the Apple menu and select About This Mac to check your version. If it’s older than 13.0, update macOS through Software Update. See the [macOS troubleshooting guide](troubleshoot-install.md) for more details.

For other errors, see the full [installation troubleshooting guide](troubleshoot-install.md).

### [​](#windows-troubleshooting) Windows troubleshooting

If you run into problems installing on Windows, check these common issues:

'irm is not recognized'

You’re in CMD, not PowerShell. Close this window and open PowerShell instead (`Win + X` then select Windows PowerShell).Alternatively, use the CMD install command:

```shiki
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

SSL/TLS error or 'Could not create SSL/TLS secure channel'

This usually happens on older Windows 10 systems. Run this line first, then retry the install:

```shiki
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
irm https://claude.ai/install.ps1 | iex
```

'Claude Code on Windows requires either Git for Windows (for bash) or PowerShell'

Neither PowerShell nor Git Bash was found. Claude Code needs at least one shell.

1. Ensure `powershell.exe` is on your `PATH`. Its default location is `C:\Windows\System32\WindowsPowerShell\v1.0\`. Alternatively, install [PowerShell 7](https://aka.ms/powershell), which provides `pwsh`.
2. If you’d rather use Git Bash, install [Git for Windows](https://git-scm.com/downloads/win) per the [first step in the Windows section](#windows).
3. If Git is installed but Claude Code can’t find it, tell it where to look:

   ```shiki
   $env:CLAUDE_CODE_GIT_BASH_PATH="C:\Program Files\Git\bin\bash.exe"
   ```

   Then run `claude` again. If your Git is installed somewhere else, find the path by running:

   ```shiki
   Get-Command git | Select-Object Source
   ```

   Look for the `Git\bin` folder in that path and use it instead.

To make this permanent so you don’t have to set it every time, see [configure Git Bash path](troubleshoot-install.md).

'claude is not recognized'

This error means the install directory isn’t in your PATH. Run these commands in PowerShell to add it:

```shiki
$currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User')
[Environment]::SetEnvironmentVariable('PATH', "$currentPath;$env:USERPROFILE\.local\bin", 'User')
```

Close PowerShell, open a new window, and try `claude` again. See [verify your PATH](troubleshoot-install.md) for more details.

For other errors, see the full [installation troubleshooting guide](troubleshoot-install.md).

---

*Copyright © Anthropic. All rights reserved.*
