# Start building
with Claude

Claude Platform

# Start building with Claude

Everything you need to integrate Claude into your applications. From first API call to production.

Search`Ctrl``K`

[Quickstart](get-started.md)[Get API key](/settings/keys)[API reference](api/overview.md)

PythonTypeScriptGoJavaRubyPHPC#cURLCLI



```shiki
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
  model="claude-opus-5",
  max_tokens=1024,
  messages=[{
    "role": "user",
    "content": "Hello, Claude"
  }]
)
for block in message.content:
    if block.type == "text":
        print(block.text)
```

Platform

## Choose how you build

Pick the developer surface that matches your approach, and the infrastructure that fits your stack.

### Messages

Direct model access. You construct every turn, manage conversation state, and write your own tool loop.

[Quickstart](get-started.md)[API reference](api/messages/create.md)[Client SDKs](cli-sdks-libraries/overview.md)

### Managed Agents

Fully managed agent infrastructure. Deploy and manage autonomous agents in stateful sessions with persistent event history.

[Quickstart](managed-agents/quickstart.md)[API reference](api/beta/sessions.md)[Define your agent](managed-agents/agent-setup.md)

Claude is also available on these cloud platforms:

[Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md)

[Google Cloud](build-with-claude/claude-on-vertex-ai.md)

[Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md)

Developer journey

## From idea to production

Follow the lifecycle or jump to what you need.

MessagesManaged Agents

1. 1

   ### Get started

   [Quickstart](get-started.md)

   [Get API key](/settings/keys)

   [Choose a model](models/overview.md)

   [Install an SDK](cli-sdks-libraries/overview.md)

   [Try the API in playground](/playground)
2. 2

   ### Build

   [Messages API](api/messages/create.md)

   [Thinking](build-with-claude/thinking.md)

   [Vision](build-with-claude/vision.md)

   [Tool use](agents-and-tools/tool-use/overview.md)

   [Web search](agents-and-tools/tool-use/web-search-tool.md)

   [Code execution](agents-and-tools/tool-use/code-execution-tool.md)

   [Structured outputs](build-with-claude/structured-outputs.md)

   [Prompt caching](build-with-claude/prompt-caching.md)

   [Streaming](build-with-claude/streaming.md)
3. 3

   ### Evaluate and ship

   [Prompting best practices](build-with-claude/prompt-engineering/overview.md)

   [Run evals](test-and-evaluate/develop-tests.md)

   [Batch testing](build-with-claude/batch-processing.md)

   [Safety and guardrails](test-and-evaluate/strengthen-guardrails/increase-consistency.md)

   [Rate limits and errors](api/rate-limits.md)

   [Cost optimization](about-claude/pricing.md)
4. 4

   ### Operate

   [Workspaces and admin](build-with-claude/workspaces.md)

   [API key management](/settings/keys)

   [Usage monitoring](build-with-claude/usage-cost-api.md)

   [Model migration](about-claude/models/migration-guide.md)

Models

## The Claude model family

Choose the right model for your use case.

![](/images/dashboard-discovery/head.svg)

![](/images/dashboard-discovery/head.svg)

### [Fable 5.1](models/fable-5-1/overview.md)

New

Most capableResearchMulti-day tasks

For demanding reasoning and long-horizon agentic work

![](/images/dashboard-discovery/cursor.svg)

![](/images/dashboard-discovery/cursor.svg)

### [Opus 5](models/opus-5/overview.md)

Complex projectsAgentsCoding

For complex agentic coding and enterprise work

![](/images/dashboard-discovery/bubble.svg)

![](/images/dashboard-discovery/bubble.svg)

### [Sonnet 5](models/sonnet-5/overview.md)

Everyday tasksWritingCost-efficient

The best combination of speed and intelligence

![](/images/dashboard-discovery/bird.svg)

![](/images/dashboard-discovery/bird.svg)

### [Haiku 4.5](models/haiku-4-5/overview.md)

FastestLowest costHigh volume

The fastest model with near-frontier intelligence

Resources

## Keep learning



[Courses](https://academy.claude.com/courses)

Interactive courses to master Claude.



[Cookbook](https://platform.claude.com/cookbook)

Code samples and patterns.



[Quickstarts](https://github.com/anthropics/anthropic-quickstarts)

Deployable starter apps.



[What's new](release-notes/overview.md)

Latest features and updates.



[Claude Code](https://code.claude.com/docs)

An agentic coding assistant in your terminal.

---

*Copyright © Anthropic. All rights reserved.*
