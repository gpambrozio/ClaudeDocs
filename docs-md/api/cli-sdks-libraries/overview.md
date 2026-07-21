# CLI, SDKs, and libraries

Copy page



Anthropic provides three kinds of official tooling for building with the Claude API:

- **CLI:** The `ant` command-line tool for shell scripting and interactive use.
- **Client SDKs:** General-purpose Messages API clients for Python, TypeScript, C#, Go, Java, PHP, and Ruby. Each SDK provides idiomatic interfaces, type safety, and built-in support for streaming, retries, and error handling.
- **Libraries and integrations:** Packages and compatibility layers that expose Claude inside another framework's API surface rather than the Messages API directly.



For the full API specification, see the [API reference](api/overview.md).

##  CLI

[ant CLI

Shell scripting, typed flags, response transforms](cli-sdks-libraries/cli/quickstart.md)

##  Client SDKs

[Python

Sync and async clients, Pydantic models](cli-sdks-libraries/sdks/python.md)[TypeScript

Node.js, Deno, Bun, and browser support](cli-sdks-libraries/sdks/typescript.md)[C#

.NET Standard 2.0+, IChatClient integration](cli-sdks-libraries/sdks/csharp.md)[Go

Context-based cancellation, functional options](cli-sdks-libraries/sdks/go.md)[Java

Builder pattern, CompletableFuture async](cli-sdks-libraries/sdks/java.md)[PHP

Value objects, builder pattern](cli-sdks-libraries/sdks/php.md)[Ruby

Sorbet types, streaming helpers](cli-sdks-libraries/sdks/ruby.md)

##  Libraries and integrations

Libraries and integrations expose Claude through another framework's API surface. They are not general-purpose Messages API clients.

[Apple Foundation Models

Swift package for Apple's `LanguageModelSession` API](cli-sdks-libraries/libraries/apple-foundation-models.md)[OpenAI SDK compatibility

Use Claude through the OpenAI SDK surface](cli-sdks-libraries/libraries/openai-sdk.md)

##  Building agents or using Claude Code?

The CLI, client SDKs, and libraries are for calling the Claude API yourself: you send each request and handle each response. Claude Code, the Claude Agent SDK, and Claude Managed Agents work at a higher level, providing the agent loop, tool execution, and runtime.

[Claude Code



Agentic coding tool for delegating coding tasks to Claude](overview.md)[Claude Agent SDK



Build agents that run in a process you operate](agent-sdk/overview.md)[Claude Managed Agents

Run agents in Anthropic's managed infrastructure](managed-agents/overview.md)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
