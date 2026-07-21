# CLI quickstart

Copy page



The `ant` CLI provides access to the Claude API from your terminal. Every API resource is exposed as a subcommand, with output formatting, response filtering, and YAML or JSON file input.

[](/docs/videos/ant-cli-demo.webm)

The ant CLI in action.

Compared to `curl`, `ant` builds request bodies from typed flags or piped YAML instead of hand-written JSON, and inlines file contents into string fields with an `@path` reference. It extracts response fields with a built-in `--transform` query, so you don't need a separate tool such as `jq`, and it paginates list endpoints automatically.



For endpoint-specific parameters and response schemas, see the [API reference](api/cli/messages/create.md). This page gets you to a working command. For everything else the CLI does, see [Using the CLI](cli-sdks-libraries/cli/using.md) and [CLI scripting and automation](cli-sdks-libraries/cli/scripting.md).

##  Installation

Homebrew (macOS)

Homebrew (macOS)

curl (Linux/WSL)

curl (Linux/WSL)

Go

Go

```shiki
brew install anthropics/tap/ant
```



Check the installation:

```shiki
ant --version
```



##  Authentication

`ant auth login` opens a browser-based OAuth flow against the Claude Console and stores the resulting credentials locally, so you can call the API without creating or managing an API key.

CLI



```shiki
ant auth login
```



For other ways to authenticate (API key environment variable, headless hosts, multiple workspaces, named profiles, and Workload Identity Federation), see [CLI authentication options](cli-sdks-libraries/cli/authentication.md).

##  Send your first request

With the binary installed and authenticated, call the [Messages API](api/cli/messages/create.md):

```shiki
ant messages create \
  --model claude-opus-4-8 \
  --max-tokens 1024 \
  --message '{role: user, content: "Hello, Claude"}'
```



Output



```shiki
{
  "model": "claude-opus-4-8",
  "id": "msg_01YMmR5XodC5nTqMxLZMKaq6",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Hello! How are you doing today? Is there something I can help you with?"
    }
  ],
  "stop_reason": "end_turn",
  "usage": { "input_tokens": 27, "output_tokens": 20 /*, ... */ }
}
```

The response is the full API object, pretty-printed because stdout is a terminal.

##  Shell completion

The CLI ships completion scripts for bash, zsh, fish, and PowerShell. Generate and install one for your shell:

zsh

zsh

bash

bash

fish

fish

PowerShell

PowerShell

```shiki
ant @completion zsh > "${fpath[1]}/_ant"
# Restart your shell or run: autoload -U compinit && compinit
```



##  Next steps

[

CLI authentication options

API keys, headless hosts, multiple workspaces, and named profiles](cli-sdks-libraries/cli/authentication.md)[Using the CLI

Command structure, output formats, GJSON transforms, and request bodies](cli-sdks-libraries/cli/using.md)[

CLI scripting and automation

Version-control API resources, scripting patterns, and use from Claude Code](cli-sdks-libraries/cli/scripting.md)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
