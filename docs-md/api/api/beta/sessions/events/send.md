# Send Events

Copy page



cURL

# Send Events

POST/v1/sessions/{session\_id}/events

Send Events

##### Path parameters

session\_id: string

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](api/http/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more

One of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"user-profiles-2026-08-18"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"dreaming-2026-04-21"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"server-side-fallback-2026-07-01"

"fallback-credit-2026-06-01"

"fallback-credit-2026-07-01"

"agent-memory-2026-07-22"

"mid-conversation-tool-changes-2026-07-01"

"compact-2026-01-12"

"computer-use-2025-11-24"

"mcp-tunnels-2026-06-22"

"structured-outputs-2025-11-13"

"task-budgets-2026-03-13"

"thinking-display-updates-2026-08-18"

"ce-user-management-2026-07-13"

##### Body



events: array of [BetaManagedAgentsEventParams](api/http/beta/sessions/events.md)

Events to send to the `session`.

One of the following:



BetaManagedAgentsUserMessageEventParams object{ content, type }

Parameters for sending a user message to the session.



BetaManagedAgentsUserInterruptEventParams object{ type, session\_thread\_id }

Parameters for sending an interrupt to pause the agent.

type: "user.interrupt"

session\_thread\_id: optional string or null

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



BetaManagedAgentsUserToolConfirmationEventParams object{ result, tool\_use\_id, type, deny\_message }

Parameters for confirming or denying a tool execution request.



result: "allow" or "deny"

UserToolConfirmationResult enum

One of the following:

"allow"

"deny"



tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

minLength1

maxLength128

type: "user.tool\_confirmation"



deny\_message: optional string or null

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

maxLength10000



BetaManagedAgentsUserCustomToolResultEventParams object{ custom\_tool\_use\_id, type, content, is\_error }

Parameters for providing the result of a custom tool execution.



BetaManagedAgentsUserDefineOutcomeEventParams object{ description, rubric, type, max\_iterations }

Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.



BetaManagedAgentsUserToolResultEventParams object{ tool\_use\_id, type, content, is\_error }

Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.



BetaManagedAgentsSystemMessageEventParams object{ content, type }

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.



content: array of [BetaManagedAgentsSystemContentBlock](api/http/beta/sessions.md) { text, type }

System content blocks to append. Text-only.



text: string

The text content.

minLength1

type: "text"

type: "system.message"

##### Returns



BetaManagedAgentsSendSessionEvents object{ data }

Events that were successfully sent to the session.

Send Events

cURL

```shiki
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/events \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "events": [
            {
              "content": [
                {
                  "text": "Where is my order #1234?",
                  "type": "text"
                }
              ],
              "type": "user.message"
            }
          ]
        }'
```

Response 200



```shiki
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ]
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ]
}
```

---

*Copyright © Anthropic. All rights reserved.*
