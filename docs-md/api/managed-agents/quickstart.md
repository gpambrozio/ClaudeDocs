# Get started with Claude Managed Agents

Copy page

This guide walks you through creating an agent, setting up an environment, starting a session, and streaming agent responses.

## Core concepts

| Concept | Description |
| --- | --- |
| **Agent** | The model, system prompt, tools, MCP servers, and skills |
| **Environment** | A configured container template (packages, network access) |
| **Session** | A running agent instance within an environment, performing a specific task and generating outputs |
| **Events** | Messages exchanged between your application and the agent (user turns, tool results, status updates) |

## Prerequisites

- An Anthropic [Console account](/)
- An [API key](/settings/keys)

## Install the CLI

Homebrew (macOS)

Homebrew (macOS)

curl (Linux/WSL)

curl (Linux/WSL)

Go

Go

```shiki
brew install anthropics/tap/ant
```

On macOS, unquarantine the binary:

```shiki
xattr -d com.apple.quarantine "$(brew --prefix)/bin/ant"
```

Check the installation:

```shiki
ant --version
```

## Install the SDK

Python

Python

TypeScript

TypeScript

Java

Java

Go

Go

C#

C#

Ruby

Ruby

PHP

PHP

```shiki
pip install anthropic
```

Set your API key as an environment variable:

```shiki
export ANTHROPIC_API_KEY="your-api-key-here"
```

## Create your first session

All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.

1. 1

   Create an agent

   Create an agent that defines the model, system prompt, and available tools.

   CLI

   ```shiki
   ant beta:agents create \
     --name "Coding Assistant" \
     --model claude-sonnet-4-6 \
     --system "You are a helpful coding assistant. Write clean, well-documented code." \
     --tool '{type: agent_toolset_20260401}'
   ```

   The `agent_toolset_20260401` tool type enables the full set of pre-built agent tools (bash, file operations, web search, and more). See [Tools](managed-agents/tools.md) for the complete list and per-tool configuration options.

   Save the returned `agent.id`. You'll reference it in every session you create.
2. 2

   Create an environment

   An environment defines the container where your agent runs.

   CLI

   ```shiki
   ant beta:environments create \
     --name "quickstart-env" \
     --config '{type: cloud, networking: {type: unrestricted}}'
   ```

   Save the returned `environment.id`. You'll reference it in every session you create.
3. 3

   Start a session

   Create a session that references your agent and environment.

   curl

   ```shiki
   session=$(
     curl -sS --fail-with-body https://api.anthropic.com/v1/sessions \
       -H "x-api-key: $ANTHROPIC_API_KEY" \
       -H "anthropic-version: 2023-06-01" \
       -H "anthropic-beta: managed-agents-2026-04-01" \
       -H "content-type: application/json" \
       -d @- <<EOF
   {
     "agent": "$AGENT_ID",
     "environment_id": "$ENVIRONMENT_ID",
     "title": "Quickstart session"
   }
   EOF
   )

   SESSION_ID=$(jq -er '.id' <<<"$session")

   echo "Session ID: $SESSION_ID"
   ```
4. 4

   Send a message and stream the response

   Open a stream, send a user event, then process events as they arrive:

   curl

   ```shiki
   # Send the user message first; the API buffers events until the stream attaches
   curl -sS --fail-with-body \
     "https://api.anthropic.com/v1/sessions/$SESSION_ID/events" \
     -H "x-api-key: $ANTHROPIC_API_KEY" \
     -H "anthropic-version: 2023-06-01" \
     -H "anthropic-beta: managed-agents-2026-04-01" \
     -H "content-type: application/json" \
     -d @- >/dev/null <<'EOF'
   {
     "events": [
       {
         "type": "user.message",
         "content": [
           {
             "type": "text",
             "text": "Create a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt"
           }
         ]
       }
     ]
   }
   EOF

   # Open the SSE stream and process events as they arrive
   while IFS= read -r line; do
     [[ $line == data:* ]] || continue
     json=${line#data: }
     case $(jq -r '.type' <<<"$json") in
       agent.message)
         jq -j '.content[] | select(.type == "text") | .text' <<<"$json"
         ;;
       agent.tool_use)
         printf '\n[Using tool: %s]\n' "$(jq -r '.name' <<<"$json")"
         ;;
       session.status_idle)
         printf '\n\nAgent finished.\n'
         break
         ;;
     esac
   done < <(
     curl -sS -N --fail-with-body \
       "https://api.anthropic.com/v1/sessions/$SESSION_ID/stream" \
       -H "x-api-key: $ANTHROPIC_API_KEY" \
       -H "anthropic-version: 2023-06-01" \
       -H "anthropic-beta: managed-agents-2026-04-01" \
       -H "Accept: text/event-stream"
   )
   ```

   The agent will write a Python script, execute it in the container, and verify the output file was created. Your output will look similar to this:

   ```inline-block
   I'll create a Python script that generates the first 20 Fibonacci numbers and saves them to a file.
   [Using tool: write]
   [Using tool: bash]
   The script ran successfully. Let me verify the output file.
   [Using tool: bash]
   fibonacci.txt contains the first 20 Fibonacci numbers (0 through 4181).

   Agent finished.
   ```

## What's happening

When you send a user event, Claude Managed Agents:

1. **Provisions a container:** Your environment configuration determines how it's built.
2. **Runs the agent loop:** Claude decides which tools to use based on your message
3. **Executes tools:** File writes, bash commands, and other tool calls run inside the container
4. **Streams events:** You receive real-time updates as the agent works
5. **Goes idle:** The agent emits a `session.status_idle` event when it has nothing more to do

## Next steps

[Define your agent

Create reusable, versioned agent configurations](managed-agents/agent-setup.md)[Configure environments

Customize networking and container settings](managed-agents/environments.md)[Agent tools

Enable specific tools for your agent](managed-agents/tools.md)[Events and streaming

Handle events and steer the agent mid-execution](managed-agents/events-and-streaming.md)

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
