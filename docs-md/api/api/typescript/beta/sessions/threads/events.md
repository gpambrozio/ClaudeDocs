# Events

Copy page



TypeScript

# Events

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

client.beta.sessions.threads.events.list(stringthreadID, EventListParams { session\_id, limit, page, betas } params, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsSessionEvent](api/beta/sessions/events.md)>

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

client.beta.sessions.threads.events.stream(stringthreadID, EventStreamParams { session\_id, betas } params, RequestOptionsoptions?): [BetaManagedAgentsStreamSessionThreadEvents](api/beta/sessions/threads.md) | Stream<[BetaManagedAgentsStreamSessionThreadEvents](api/beta/sessions/threads.md)>

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

---

*Copyright © Anthropic. All rights reserved.*
