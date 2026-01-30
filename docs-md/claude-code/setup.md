## [​](#system-requirements) System requirements

- **Operating Systems**: macOS 13.0+, Ubuntu 20.04+/Debian 10+, or Windows 10 1809+ / Windows Server 2019+ (with WSL 1, WSL 2, or Git for Windows)
- **Hardware**: 4 GB+ RAM
- **Network**: Internet connection required (see [network configuration](network-config.md))
- **Shell**: Works best in Bash or Zsh
- **Location**: [Anthropic supported countries](https://www.anthropic.com/supported-countries)

### [​](#additional-dependencies) Additional dependencies

- **ripgrep**: Usually included with Claude Code. If search fails, see [search troubleshooting](troubleshooting.md).
- **[Node.js 18+](https://nodejs.org/en/download)**: Only required for [deprecated npm installation](#npm-installation-deprecated)

## [​](#installation) Installation

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

After the installation process completes, navigate to your project and start Claude Code:

Copy

Ask AI

```shiki
cd your-awesome-project
claude
```

If you encounter any issues during installation, consult the [troubleshooting guide](troubleshooting.md).

Run `claude doctor` after installation to check your installation type and version.

**Alpine Linux and other musl/uClibc-based distributions**: The native installer requires `libgcc`, `libstdc++`, and `ripgrep`. For Alpine: `apk add libgcc libstdc++ ripgrep`. Set `USE_BUILTIN_RIPGREP=0`.

### [​](#authentication) Authentication

#### [​](#for-individuals) For individuals

1. **Claude Pro or Max plan** (recommended): Subscribe to Claude’s [Pro or Max plan](https://claude.ai/pricing) for a unified subscription that includes both Claude Code and Claude on the web. Manage your account in one place and log in with your Claude.ai account.
2. **Claude Console**: Connect through the [Claude Console](https://console.anthropic.com) and complete the OAuth process. Requires active billing in the Anthropic Console. A “Claude Code” workspace is automatically created for usage tracking and cost management. You can’t create API keys for the Claude Code workspace; it’s dedicated exclusively for Claude Code usage.

#### [​](#for-teams-and-organizations) For teams and organizations

1. **Claude for Teams or Enterprise** (recommended): Subscribe to [Claude for Teams](https://claude.com/pricing#team-&-enterprise) or [Claude for Enterprise](https://anthropic.com/contact-sales) for centralized billing, team management, and access to both Claude Code and Claude on the web. Team members log in with their Claude.ai accounts.
2. **Claude Console with team billing**: Set up a shared [Claude Console](https://console.anthropic.com) organization with team billing. Invite team members and assign roles for usage tracking.
3. **Cloud providers**: Configure Claude Code to use [Amazon Bedrock, Google Vertex AI, or Microsoft Foundry](third-party-integrations.md) for deployments with your existing cloud infrastructure.

### [​](#install-a-specific-version) Install a specific version

The native installer accepts either a specific version number or a release channel (`latest` or `stable`). The channel you choose at install time becomes your default for auto-updates. See [Configure release channel](#configure-release-channel) for more information.
To install the latest version (default):

- macOS, Linux, WSL
- Windows PowerShell
- Windows CMD

Copy

Ask AI

```shiki
curl -fsSL https://claude.ai/install.sh | bash
```

Copy

Ask AI

```shiki
irm https://claude.ai/install.ps1 | iex
```

Copy

Ask AI

```shiki
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

To install the stable version:

- macOS, Linux, WSL
- Windows PowerShell
- Windows CMD

Copy

Ask AI

```shiki
curl -fsSL https://claude.ai/install.sh | bash -s stable
```

Copy

Ask AI

```shiki
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) stable
```

Copy

Ask AI

```shiki
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd stable && del install.cmd
```

To install a specific version number:

- macOS, Linux, WSL
- Windows PowerShell
- Windows CMD

Copy

Ask AI

```shiki
curl -fsSL https://claude.ai/install.sh | bash -s 1.0.58
```

Copy

Ask AI

```shiki
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) 1.0.58
```

Copy

Ask AI

```shiki
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd 1.0.58 && del install.cmd
```

### [​](#binary-integrity-and-code-signing) Binary integrity and code signing

- SHA256 checksums for all platforms are published in the release manifests, currently located at `https://storage.googleapis.com/claude-code-dist-86c565f3-f756-42ad-8dfa-d59b1c096819/claude-code-releases/{VERSION}/manifest.json` (example: replace `{VERSION}` with `2.0.30`)
- Signed binaries are distributed for the following platforms:
  - macOS: Signed by “Anthropic PBC” and notarized by Apple
  - Windows: Signed by “Anthropic, PBC”

## [​](#npm-installation-deprecated) NPM installation (deprecated)

NPM installation is deprecated. Use the [native installation](#installation) method when possible. To migrate an existing npm installation to native, run `claude install`.
**Global npm installation**

Copy

Ask AI

```shiki
npm install -g @anthropic-ai/claude-code
```

Do NOT use `sudo npm install -g` as this can lead to permission issues and security risks.
If you encounter permission errors, see [troubleshooting permission errors](troubleshooting.md) for recommended solutions.

## [​](#windows-setup) Windows setup

**Option 1: Claude Code within WSL**

- Both WSL 1 and WSL 2 are supported
- WSL 2 supports [sandboxing](sandboxing.md) for enhanced security. WSL 1 does not support sandboxing.

**Option 2: Claude Code on native Windows with Git Bash**

- Requires [Git for Windows](https://git-scm.com/downloads/win)
- For portable Git installations, specify the path to your `bash.exe`:

  Copy

  Ask AI

  ```shiki
  $env:CLAUDE_CODE_GIT_BASH_PATH="C:\Program Files\Git\bin\bash.exe"
  ```

## [​](#update-claude-code) Update Claude Code

### [​](#auto-updates) Auto updates

Claude Code automatically keeps itself up to date to ensure you have the latest features and security fixes.

- **Update checks**: Performed on startup and periodically while running
- **Update process**: Downloads and installs automatically in the background
- **Notifications**: You’ll see a notification when updates are installed
- **Applying updates**: Updates take effect the next time you start Claude Code

Homebrew and WinGet installations do not auto-update. Use `brew upgrade claude-code` or `winget upgrade Anthropic.ClaudeCode` to update manually.**Known issue:** Claude Code may notify you of updates before the new version is available in these package managers. If an upgrade fails, wait and try again later.

### [​](#configure-release-channel) Configure release channel

Configure which release channel Claude Code follows for both auto-updates and `claude update` with the `autoUpdatesChannel` setting:

- `"latest"` (default): Receive new features as soon as they’re released
- `"stable"`: Use a version that is typically about one week old, skipping releases with major regressions

Configure this via `/config` → **Auto-update channel**, or add it to your [settings.json file](settings.md):

Copy

Ask AI

```shiki
{
  "autoUpdatesChannel": "stable"
}
```

For enterprise deployments, you can enforce a consistent release channel across your organization using [managed settings](iam.md).

### [​](#disable-auto-updates) Disable auto-updates

Set the `DISABLE_AUTOUPDATER` environment variable in your shell or [settings.json file](settings.md):

Copy

Ask AI

```shiki
export DISABLE_AUTOUPDATER=1
```

### [​](#update-manually) Update manually

Copy

Ask AI

```shiki
claude update
```

## [​](#uninstall-claude-code) Uninstall Claude Code

If you need to uninstall Claude Code, follow the instructions for your installation method.

### [​](#native-installation) Native installation

Remove the Claude Code binary and version files:
**macOS, Linux, WSL:**

Copy

Ask AI

```shiki
rm -f ~/.local/bin/claude
rm -rf ~/.local/share/claude
```

**Windows PowerShell:**

Copy

Ask AI

```shiki
Remove-Item -Path "$env:USERPROFILE\.local\bin\claude.exe" -Force
Remove-Item -Path "$env:USERPROFILE\.local\share\claude" -Recurse -Force
```

**Windows CMD:**

Copy

Ask AI

```shiki
del "%USERPROFILE%\.local\bin\claude.exe"
rmdir /s /q "%USERPROFILE%\.local\share\claude"
```

### [​](#homebrew-installation) Homebrew installation

Copy

Ask AI

```shiki
brew uninstall --cask claude-code
```

### [​](#winget-installation) WinGet installation

Copy

Ask AI

```shiki
winget uninstall Anthropic.ClaudeCode
```

### [​](#npm-installation) NPM installation

Copy

Ask AI

```shiki
npm uninstall -g @anthropic-ai/claude-code
```

### [​](#clean-up-configuration-files-optional) Clean up configuration files (optional)

Removing configuration files will delete all your settings, allowed tools, MCP server configurations, and session history.

To remove Claude Code settings and cached data:
**macOS, Linux, WSL:**

Copy

Ask AI

```shiki
# Remove user settings and state
rm -rf ~/.claude
rm ~/.claude.json

# Remove project-specific settings (run from your project directory)
rm -rf .claude
rm -f .mcp.json
```

**Windows PowerShell:**

Copy

Ask AI

```shiki
# Remove user settings and state
Remove-Item -Path "$env:USERPROFILE\.claude" -Recurse -Force
Remove-Item -Path "$env:USERPROFILE\.claude.json" -Force

# Remove project-specific settings (run from your project directory)
Remove-Item -Path ".claude" -Recurse -Force
Remove-Item -Path ".mcp.json" -Force
```

**Windows CMD:**

Copy

Ask AI

```shiki
REM Remove user settings and state
rmdir /s /q "%USERPROFILE%\.claude"
del "%USERPROFILE%\.claude.json"

REM Remove project-specific settings (run from your project directory)
rmdir /s /q ".claude"
del ".mcp.json"
```

---

*Copyright © Anthropic. All rights reserved.*
