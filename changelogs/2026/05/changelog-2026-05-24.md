# [Claude docs changes for May 24th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/f55061ea2b34f400dcd0873e8ebcf1d5d912269f) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/f55061ea2b34f400dcd0873e8ebcf1d5d912269f)]

## Executive Summary
- The `/code-review` command can now be run locally in any Claude Code session without installing the GitHub App, replacing the previously documented `code-review` plugin approach
- Shell aliases and functions defined in startup files (`~/.zshrc`, `~/.bashrc`, `~/.profile`) are now documented as available to the Bash tool in every command
- Sandbox documentation updated: linked git worktrees allow writes to the main repository's shared `.git` directory (except `hooks/` and `config`)

-----

## Claude Code changes

### Changed documents

#### [Code Review](https://github.com/gpambrozio/ClaudeDocs/blob/f55061ea2b34f400dcd0873e8ebcf1d5d912269f/docs-md/claude-code/code-review.md) [[Source](https://code.claude.com/docs/en/code-review)]

* Added note that the `/code-review` command can be run locally in a terminal session without installing the GitHub App; it reports correctness bugs and can post inline PR comments with `--comment`. Also notes the command was previously named `/simplify` before v2.1.147. [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/f55061ea2b34f400dcd0873e8ebcf1d5d912269f/docs-md/claude-code/code-review.md?plain=1#L23)] [[Source](https://code.claude.com/docs/en/code-review)]
* Updated "See also" section: replaced the "Plugins" link (with `code-review` plugin) with a "Commands" link pointing to the `/code-review` command for local diff checking before pushing. [[line 260](https://github.com/gpambrozio/ClaudeDocs/blob/f55061ea2b34f400dcd0873e8ebcf1d5d912269f/docs-md/claude-code/code-review.md?plain=1#L260)] [[Source](https://code.claude.com/docs/en/code-review#related-resources)]

#### [Sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/f55061ea2b34f400dcd0873e8ebcf1d5d912269f/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Documented git worktree sandbox behavior: when the working directory is a linked git worktree, the sandbox allows writes to the main repository's shared `.git` directory so commands like `git commit` can update refs and the index; writes to `hooks/` and `config` inside that directory remain denied. [[line 177](https://github.com/gpambrozio/ClaudeDocs/blob/f55061ea2b34f400dcd0873e8ebcf1d5d912269f/docs-md/claude-code/sandboxing.md?plain=1#L177)] [[Source](https://code.claude.com/docs/en/sandboxing#filesystem-isolation)]

#### [Tools Reference](https://github.com/gpambrozio/ClaudeDocs/blob/f55061ea2b34f400dcd0873e8ebcf1d5d912269f/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* Added documentation that shell aliases and functions defined in startup files are available in Bash tool commands: Claude Code sources `~/.zshrc`, `~/.bashrc`, or `~/.profile` at session start and applies captured aliases, functions, and shell options to every Bash command. [[line 109](https://github.com/gpambrozio/ClaudeDocs/blob/f55061ea2b34f400dcd0873e8ebcf1d5d912269f/docs-md/claude-code/tools-reference.md?plain=1#L109)] [[Source](https://code.claude.com/docs/en/tools-reference#bash-tool-behavior)]

-----

## API changes

No significant changes today.
