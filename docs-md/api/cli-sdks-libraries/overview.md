# CLI, SDKs, and libraries

Copy page



Anthropic provides three kinds of official tooling for building with the Claude API:

- **CLI:** The `ant` command-line tool for shell scripting and interactive use.
- **Client SDKs:** General-purpose Messages API clients for Python, TypeScript, C#, Go, Java, PHP, and Ruby. Each SDK provides idiomatic interfaces, type safety, and built-in support for streaming, retries, and error handling.
- **Libraries and integrations:** Packages and compatibility layers that expose Claude inside another framework's API surface rather than the Messages API directly.

##  CLI

[ant CLI](cli-sdks-libraries/cli/quickstart.md)

Shell scripting, typed flags, response transforms

##  Client SDKs

[Python](cli-sdks-libraries/sdks/python.md)

Sync and async clients, Pydantic models

[TypeScript](cli-sdks-libraries/sdks/typescript.md)

Node.js, Deno, Bun, and browser support

[C#](cli-sdks-libraries/sdks/csharp.md)

.NET Standard 2.0+, IChatClient integration

[Go](cli-sdks-libraries/sdks/go.md)

Context-based cancellation, functional options

[Java](cli-sdks-libraries/sdks/java.md)

Builder pattern, CompletableFuture async

[PHP](cli-sdks-libraries/sdks/php.md)

Value objects, builder pattern

[Ruby](cli-sdks-libraries/sdks/ruby.md)

Sorbet types, streaming helpers

##  Libraries and integrations

Libraries and integrations expose Claude through another framework's API surface. They are not general-purpose Messages API clients.

[Apple Foundation Models](cli-sdks-libraries/libraries/apple-foundation-models.md)

Swift package for Apple's `LanguageModelSession` API

[OpenAI SDK compatibility](cli-sdks-libraries/libraries/openai-sdk.md)

Use Claude through the OpenAI SDK surface

##  Building agents or using Claude Code?

The CLI, client SDKs, and libraries are for calling the Claude API yourself: you send each request and handle each response. Claude Code, the Claude Agent SDK, and Claude Managed Agents work at a higher level, providing the agent loop, tool execution, and runtime.

[Claude Code](overview.md)



Agentic coding tool for delegating coding tasks to Claude

[Claude Agent SDK](agent-sdk/overview.md)



Build agents that run in a process you operate

[Claude Managed Agents](managed-agents/overview.md)

Run agents in Anthropic's managed infrastructure

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
