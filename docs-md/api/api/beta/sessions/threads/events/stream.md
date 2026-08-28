# Stream Session Thread Events

Copy page



cURL

# Stream Session Thread Events

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

Stream Session Thread Events

##### Path parameters

session\_id: string

thread\_id: string

##### Query parameters



event\_deltas: optional array of [BetaManagedAgentsDeltaType](api/http/beta/sessions.md)

When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

One of the following:

"agent.message"

"agent.thinking"

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](api/http/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more

One of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"user-profiles-2026-08-18"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"dreaming-2026-04-21"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"server-side-fallback-2026-07-01"

"fallback-credit-2026-06-01"

"fallback-credit-2026-07-01"

"agent-memory-2026-07-22"

"mid-conversation-tool-changes-2026-07-01"

"compact-2026-01-12"

"computer-use-2025-11-24"

"mcp-tunnels-2026-06-22"

"structured-outputs-2025-11-13"

"task-budgets-2026-03-13"

"thinking-display-updates-2026-08-18"

"ce-user-management-2026-07-13"

##### Returns



BetaManagedAgentsStreamSessionThreadEvents = [BetaManagedAgentsUserMessageEvent](api/http/beta/sessions/events.md) { id, content, type, processed\_at } or [BetaManagedAgentsUserInterruptEvent](api/http/beta/sessions/events.md) { id, type, processed\_at, session\_thread\_id } or [BetaManagedAgentsUserToolConfirmationEvent](api/http/beta/sessions/events.md) { id, result, tool\_use\_id, 4 more } or 34 more

Server-sent event in a single thread's stream.

One of the following:



BetaManagedAgentsStreamSessionThreadEvents = [BetaManagedAgentsUserMessageEvent](api/http/beta/sessions/events.md) { id, content, type, processed\_at } or [BetaManagedAgentsUserInterruptEvent](api/http/beta/sessions/events.md) { id, type, processed\_at, session\_thread\_id } or [BetaManagedAgentsUserToolConfirmationEvent](api/http/beta/sessions/events.md) { id, result, tool\_use\_id, 4 more } or 34 more

Server-sent event in a single thread's stream.

One of the following:



### Stream Session Thread Events

cURL



```shiki
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/threads/$THREAD_ID/stream \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```shiki
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
```

##### Returns Examples

Response 200



```shiki
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
```

---

*Copyright © Anthropic. All rights reserved.*
