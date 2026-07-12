# [Claude docs changes for July 12th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/b1db6c5c91508746a465ddc22a811c983ab3e1e1) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/b1db6c5c91508746a465ddc22a811c983ab3e1e1)]

## Executive Summary
- The Claude Code desktop app Linux install docs now include a `curl` command that automatically finds and downloads the latest `.deb` package from the apt repository, plus troubleshooting guidance for when the lookup fails.
- Several pages that link out to Linux desktop downloads (`setup`, `terminal-guide`, `troubleshoot-install`) now point directly to the dedicated Linux install guide instead of a generic download link.
- The Agent SDK MCP guide teases upcoming documentation on MCP output limits, covering `MAX_MCP_OUTPUT_TOKENS`, a persist-to-disk fallback, and the `anthropic/maxResultSizeChars` per-tool annotation.
- The Claude Platform on AWS page now includes an enterprise sales banner for organization-wide deployments (SSO, centralized billing).

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/mcp](https://github.com/gpambrozio/ClaudeDocs/blob/b1db6c5c91508746a465ddc22a811c983ab3e1e1/docs-md/claude-code/agent-sdk/mcp.md) [[Source](https://code.claude.com/docs/en/agent-sdk/mcp)]

* Added a "See also" link teasing coverage of MCP output limits and warnings, covering how the SDK handles tool results that exceed `MAX_MCP_OUTPUT_TOKENS`, a persist-to-disk fallback, and the `anthropic/maxResultSizeChars` per-tool annotation. [[line 769](https://github.com/gpambrozio/ClaudeDocs/blob/b1db6c5c91508746a465ddc22a811c983ab3e1e1/docs-md/claude-code/agent-sdk/mcp.md?plain=1#L769)] [[Source](https://code.claude.com/docs/en/agent-sdk/mcp#related-resources)]

#### [claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/b1db6c5c91508746a465ddc22a811c983ab3e1e1/docs-md/claude-code/claude-platform-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

* Added an enterprise sales banner promoting organization-wide deployment, SSO, and centralized billing, with links to pricing and contact sales. [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/b1db6c5c91508746a465ddc22a811c983ab3e1e1/docs-md/claude-code/claude-platform-on-aws.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

#### [desktop-linux](https://github.com/gpambrozio/ClaudeDocs/blob/b1db6c5c91508746a465ddc22a811c983ab3e1e1/docs-md/claude-code/desktop-linux.md) [[Source](https://code.claude.com/docs/en/desktop-linux)]

* The "Install from a downloaded file" section now provides a `curl` command that looks up and downloads the newest `.deb` package for the user's architecture directly from the apt repository's package pool, replacing the old instruction to manually download from claude.com/download. [[lines 64-70](https://github.com/gpambrozio/ClaudeDocs/blob/b1db6c5c91508746a465ddc22a811c983ab3e1e1/docs-md/claude-code/desktop-linux.md?plain=1#L64-L70)] [[Source](https://code.claude.com/docs/en/desktop-linux#install-from-a-downloaded-file)]
* Added troubleshooting for the `Remote file name has no length` error, explaining it means the package lookup failed (e.g. network blocking `downloads.claude.ai`, or an unsupported architecture) and how to confirm the fix. [[line 72](https://github.com/gpambrozio/ClaudeDocs/blob/b1db6c5c91508746a465ddc22a811c983ab3e1e1/docs-md/claude-code/desktop-linux.md?plain=1#L72)] [[Source](https://code.claude.com/docs/en/desktop-linux#install-from-a-downloaded-file)]
* Clarified that to get updates via apt for a manually-installed `.deb`, users should register the repository from the "Add Anthropic's apt repository" step (or uncomment the `deb` line the package writes). [[line 80](https://github.com/gpambrozio/ClaudeDocs/blob/b1db6c5c91508746a465ddc22a811c983ab3e1e1/docs-md/claude-code/desktop-linux.md?plain=1#L80)] [[Source](https://code.claude.com/docs/en/desktop-linux#install-from-a-downloaded-file)]

#### [setup](https://github.com/gpambrozio/ClaudeDocs/blob/b1db6c5c91508746a465ddc22a811c983ab3e1e1/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* The Linux desktop app download link now points to the dedicated [Linux install guide](https://github.com/gpambrozio/ClaudeDocs/blob/b1db6c5c91508746a465ddc22a811c983ab3e1e1/docs-md/claude-code/desktop-linux.md) instead of the generic claude.com download page. [[line 26](https://github.com/gpambrozio/ClaudeDocs/blob/b1db6c5c91508746a465ddc22a811c983ab3e1e1/docs-md/claude-code/setup.md?plain=1#L26)] [[Source](https://code.claude.com/docs/en/setup#install-claude-code)]

#### [terminal-guide](https://github.com/gpambrozio/ClaudeDocs/blob/b1db6c5c91508746a465ddc22a811c983ab3e1e1/docs-md/claude-code/terminal-guide.md) [[Source](https://code.claude.com/docs/en/terminal-guide)]

* Removed the direct Linux download link in favor of directing Linux users to install the desktop app via apt, referencing the Linux install instructions. [[line 8](https://github.com/gpambrozio/ClaudeDocs/blob/b1db6c5c91508746a465ddc22a811c983ab3e1e1/docs-md/claude-code/terminal-guide.md?plain=1#L8)] [[Source](https://code.claude.com/docs/en/terminal-guide)]

#### [troubleshoot-install](https://github.com/gpambrozio/ClaudeDocs/blob/b1db6c5c91508746a465ddc22a811c983ab3e1e1/docs-md/claude-code/troubleshoot-install.md) [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

* Removed the direct Linux download link in favor of directing Linux users to install the desktop app via apt, referencing the Linux install instructions. [[line 40](https://github.com/gpambrozio/ClaudeDocs/blob/b1db6c5c91508746a465ddc22a811c983ab3e1e1/docs-md/claude-code/troubleshoot-install.md?plain=1#L40)] [[Source](https://code.claude.com/docs/en/troubleshoot-install#find-your-error)]
