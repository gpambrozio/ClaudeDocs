# Events

Copy page

Go

# Events

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

client.Beta.Sessions.Threads.Events.List(ctx, threadID, params) (\*PageCursor[[BetaManagedAgentsSessionEventUnion](api/beta.md)], error)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

client.Beta.Sessions.Threads.Events.Stream(ctx, threadID, params) (\*[BetaManagedAgentsStreamSessionThreadEventsUnion](api/beta.md), error)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

---

*Copyright © Anthropic. All rights reserved.*
