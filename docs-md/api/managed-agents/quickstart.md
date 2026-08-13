# Get started with Claude Managed Agents

Copy page



This guide walks you through creating an agent, setting up an environment, starting a session, and streaming agent responses.

##  Core concepts

| Concept | Description |
| --- | --- |
| **Agent** | The model, system prompt, tools, MCP servers, and skills |
| **Environment** | Configuration for where sessions run: an Anthropic-managed cloud sandbox, or a self-hosted sandbox on your own infrastructure |
| **Session** | A running agent instance within an environment, performing a specific task and generating outputs |
| **Events** | Messages exchanged between your application and the agent (user turns, tool results, status updates) |

##  Prerequisites

- A [Claude Console account](https://platform.claude.com)
- An [API key](/settings/keys)

##  Install the CLI

Homebrew (macOS)curl (Linux/WSL)Go

```shiki
brew install anthropics/tap/ant
```



Check the installation:

```shiki
ant --version
```



##  Install the SDK

PythonTypeScriptJavaGoC#RubyPHP

```shiki
pip install anthropic
```



Set your API key as an environment variable:

```shiki
export ANTHROPIC_API_KEY="your-api-key-here"
```



##  Create your first session

1. 1

   Create an agent

   Create an agent that defines the model, system prompt, and available tools.

   cURLCLIPythonTypeScriptC#GoJavaPHPRuby

   

   ```shiki
   AGENT_ID=$(ant beta:agents create \
     --name "Coding Assistant" \
     --model '{id: claude-opus-5}' \
     --system "You are a helpful coding assistant. Write clean, well-documented code." \
     --tool '{type: agent_toolset_20260401}' \
     --transform id --raw-output)

   echo "Agent ID: $AGENT_ID"
   ```

   The `agent_toolset_20260401` tool type enables the full set of pre-built agent tools (bash, file operations, web search, and more). See [Tools](managed-agents/tools.md) for the complete list and per-tool configuration options.

   Save the returned `agent.id`. You'll reference it in every session you create.
2. 2

   Create an environment

   An environment defines the sandbox where your agent runs.

   cURLCLIPythonTypeScriptC#GoJavaPHPRuby

   

   ```shiki
   ENVIRONMENT_ID=$(ant beta:environments create \
     --name "quickstart-env" \
     --config '{type: cloud, networking: {type: unrestricted}}' \
     --transform id --raw-output)

   echo "Environment ID: $ENVIRONMENT_ID"
   ```

   Save the returned `environment.id`. You'll reference it in every session you create.
3. 3

   Start a session

   Create a session that references your agent and environment.

   cURLCLIPythonTypeScriptC#GoJavaPHPRuby

   

   ```shiki
   session = client.beta.sessions.create(
       agent=agent.id,
       environment_id=environment.id,
       title="Quickstart session",
   )

   print(f"Session ID: {session.id}")
   ```
4. 4

   Send a message and stream the response

   Open a stream, send a user event, then process events as they arrive:

   cURLCLIPythonTypeScriptC#GoJavaPHPRuby

   

   ```shiki
   with client.beta.sessions.events.stream(session.id) as stream:
       # Send the user message after the stream opens
       client.beta.sessions.events.send(
           session.id,
           events=[
               {
                   "type": "user.message",
                   "content": [
                       {
                           "type": "text",
                           "text": "Create a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt",
                       },
                   ],
               },
           ],
       )

       # Process streaming events
       for event in stream:
           match event.type:
               case "agent.message":
                   for block in event.content:
                       print(block.text, end="")
               case "agent.tool_use":
                   print(f"\n[Using tool: {event.name}]")
               case "session.status_idle":
                   print("\n\nAgent finished.")
                   break
   ```

   The agent writes a Python script, runs it in the sandbox, and verifies the output file was created. Your output looks similar to this:

   ```block
   I'll create a Python script that generates the first 20 Fibonacci numbers and saves them to a file.
   [Using tool: write]
   [Using tool: bash]
   The script ran successfully. Let me verify the output file.
   [Using tool: bash]
   fibonacci.txt contains the first 20 Fibonacci numbers (0 through 4181).

   Agent finished.
   ```

   

##  What's happening

When you send a user event, Claude Managed Agents:

1. **Provisions a sandbox:** Your environment configuration determines how it's built.
2. **Runs the agent loop:** Claude determines which tools to use based on your message.
3. **Runs tools:** File writes, bash commands, and other tool calls run inside the sandbox.
4. **Streams events:** You receive real-time updates as the agent works.
5. **Goes idle:** The agent emits a `session.status_idle` event when it has nothing more to do.

##  Build a complete app

Each of these quickstarts pairs Claude Managed Agents with a popular chat framework to make a complete, runnable application. In each one, the framework renders the chat surface while a managed session runs the agent loop server-side: the session holds the transcript, runs tools in a sandbox, and streams events that the front end renders.

[Chat SDK](https://github.com/anthropics/claude-quickstarts/tree/main/managed-agents/chat-sdk)



A research analyst in a browser chat built with Vercel's Chat SDK. Each conversation is one persistent session that streams its reply while a live feed shows the tool calls. Swapping the Chat SDK adapter moves the same handler to Slack, Teams, Discord, or WhatsApp.

[assistant-ui](https://github.com/anthropics/claude-quickstarts/tree/main/managed-agents/assistant-ui)



A spreadsheet analyst in a chat built from assistant-ui primitives. Sessions are the thread list, one reducer turns the session event log into messages and tool cards, and each bash command renders an inline Allow/Deny gate before it runs.

[CopilotKit (AG-UI)](https://github.com/anthropics/claude-quickstarts/tree/main/managed-agents/copilot-kit-ag-ui)



A personal finance assistant in a CopilotKit chat. The AG-UI adapter for Claude Managed Agents maps each chat thread to a managed session and streams replies token by token, and custom tools render interactive charts inline in the conversation.

##  Next steps



[Define your agent](managed-agents/agent-setup.md)

Create reusable, versioned agent configurations



[Configure environments](managed-agents/environments.md)

Customize networking and sandbox settings



[Agent tools](managed-agents/tools.md)

Enable specific tools for your agent



[Session event stream](managed-agents/events-and-streaming.md)

Handle events and steer the agent mid-execution



[Scheduled deployments](managed-agents/scheduled-deployments.md)

Run your agent on a recurring cron schedule

[Knowledge wiki quickstart](https://github.com/anthropics/claude-quickstarts/tree/main/managed-agents/knowledge-wiki)



Distill a document corpus once into a knowledge wiki, then answer repeated questions from it at a fraction of the cost

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
