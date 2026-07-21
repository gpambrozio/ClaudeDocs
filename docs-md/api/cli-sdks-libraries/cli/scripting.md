# CLI scripting and automation

Copy page



This page covers task-oriented workflows built on the `ant` CLI. For the underlying flags and output options, see [Using the CLI](cli-sdks-libraries/cli/using.md).

##  Version-controlling API resources

You can use the CLI to version control API resources such as skills, agents, environments, or deployments as YAML files in your repository and keep them in sync with the Claude API.



For more information on these resources, see [Managed Agents](managed-agents/overview.md).

1. 1

   Define your agent

   Write the agent definition to `summarizer.agent.yaml`:

   summarizer.agent.yaml

   

   ```shiki
   name: Summarizer
   model: claude-opus-4-8
   system: |
     You are a helpful assistant that writes concise summaries.
   tools:
     - type: agent_toolset_20260401
   ```
2. 2

   Create the agent

   ```shiki
   ant beta:agents create < summarizer.agent.yaml
   ```

   

   Output

   

   ```shiki
   {
     "id": "agent_011CYm1BLqPXpQRk5khsSXrs",
     "version": 1,
     "name": "Summarizer",
     "model": "claude-opus-4-8"
     /* ... */
   }
   ```

   Note the `id` from the response. You'll pass it to the session create command in a later step.

   

   Check `summarizer.agent.yaml` into your repository and keep it in sync with the API in your CI pipeline. The update command needs the agent ID and current version as flags:

   CLI

   

   ```shiki
   ant beta:agents update --agent-id agent_011CYm1BLqPXpQRk5khsSXrs --version 1 < summarizer.agent.yaml
   ```
3. 3

   Define the environment

   A session runs in an [environment](api/cli/beta/environments.md), which defines the sandbox it executes in. Write the environment definition to `summarizer.environment.yaml`:

   summarizer.environment.yaml

   

   ```shiki
   name: summarizer-env
   config:
     type: cloud
     networking:
       type: unrestricted
   ```
4. 4

   Create the environment

   ```shiki
   ant beta:environments create < summarizer.environment.yaml
   ```

   

   Output

   

   ```shiki
   {
     "id": "env_01595EKxaaTTGwwY3kyXdtbs",
     "name": "summarizer-env"
     /* ... */
   }
   ```

   Note the `id` from the response. You'll pass it to the session create command in a later step.

   

   Check `summarizer.environment.yaml` into your repository and keep it in sync with the API in your CI pipeline. The update command needs the environment ID as a flag:

   CLI

   

   ```shiki
   ant beta:environments update --environment-id env_01595EKxaaTTGwwY3kyXdtbs < summarizer.environment.yaml
   ```
5. 5

   Start a session

   Paste the agent `id` and environment `id` from the previous outputs into the session create command:

   ```shiki
   ant beta:sessions create \
     --agent agent_011CYm1BLqPXpQRk5khsSXrs \
     --environment-id env_01595EKxaaTTGwwY3kyXdtbs \
     --title "Summarization task"
   ```

   

   Output

   

   ```shiki
   {
     "id": "session_01JZCh78XvmxJjiXVy3oSi7K",
     "status": "running"
     /* ... */
   }
   ```
6. 6

   Send a user message

   Copy the session `id` from the previous output into `--session-id`:

   ```shiki
   ant beta:sessions:events send \
     --session-id session_01JZCh78XvmxJjiXVy3oSi7K \
     --event '{type: user.message, content: [{type: text, text: "Summarize the benefits of type safety in one sentence."}]}'
   ```

   
7. 7

   Read the conversation

   `--transform` runs against each listed event, so this prints the text of every message in order. `--format auto` overrides the interactive explorer that list commands open by default in a terminal:

   ```shiki
   ant beta:sessions:events list \
     --session-id session_01JZCh78XvmxJjiXVy3oSi7K \
     --transform 'content.0.text' --format auto --raw-output
   ```

   

   Output

   

   ```block
   Summarize the benefits of type safety in one sentence.
   Type safety catches errors at compile time rather than runtime, reducing bugs, improving code clarity, enabling better tooling support, and making codebases easier to maintain and refactor with confidence.
   ```

   

   To watch a session as it runs, use `ant beta:sessions:events stream --session-id session_01JZCh78XvmxJjiXVy3oSi7K`. Events are written to stdout as they arrive.

##  Scripting patterns

The CLI is designed to compose with standard shell tooling.

###  Chain list output into a second command

`--transform id --raw-output` on a list endpoint emits one bare ID per line, so standard tools such as `head` and `xargs` apply directly. Capture the first result, then pass it to a follow-up command:

```shiki
FIRST_AGENT=$(ant beta:agents list \
  --transform id --raw-output | head -1)

ant beta:agents:versions list \
  --agent-id "$FIRST_AGENT" \
  --transform "{version,created_at}" --format jsonl
```



###  Inspect errors

The `--transform-error` and `--format-error` flags apply the same filtering to error responses. `--raw-output` does not apply to errors, so use `--format-error yaml` for an unquoted scalar. Extract only the error message:

```shiki
ant beta:agents retrieve --agent-id bogus \
  --transform-error error.message --format-error yaml 2>&1
```



Output



```block
GET "https://api.anthropic.com/v1/agents/bogus?beta=true": 404 Not Found
Agent not found.
```

##  Use the CLI from Claude Code

[Claude Code](overview.md) can use the `ant` CLI out of the box. With the CLI installed and authenticated, you can ask Claude Code to operate on your API resources directly. For example:

- "List my recent agent sessions and summarize which ones errored."
- "Upload every PDF in `./reports` to the Files API and print the resulting IDs."
- "Pull the events for session `session_01...` and tell me where the agent got stuck."

Claude Code shells out to `ant`, parses the structured output, and reasons over the results (no custom integration code required).

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
