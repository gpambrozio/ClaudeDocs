# Threads

Copy page



cURL

# Threads

##### [List Session Threads](api/http/beta/sessions/threads/list.md)

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/http/beta/sessions/threads/retrieve.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/http/beta/sessions/threads/archive.md)

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

##### Models



BetaManagedAgentsSessionThread object{ id, agent, archived\_at, 8 more }

An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.



BetaManagedAgentsSessionThreadStats object{ active\_seconds, duration\_seconds, startup\_seconds }

Timing statistics for a session thread.



active\_seconds: optional number

Cumulative time in seconds the thread spent actively running. Excludes idle time.

formatdouble



duration\_seconds: optional number

Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

formatdouble



startup\_seconds: optional number

Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

formatdouble



BetaManagedAgentsSessionThreadStatus = "running" or "idle" or "rescheduling" or "terminated"

SessionThreadStatus enum

One of the following:

"running"

"idle"

"rescheduling"

"terminated"



BetaManagedAgentsSessionThreadUsage object{ active\_seconds, cache\_creation, cache\_read\_input\_tokens, 4 more }

Cumulative token usage for a session thread across all turns.



BetaManagedAgentsStreamSessionThreadEvents = [BetaManagedAgentsUserMessageEvent](api/http/beta/sessions/events.md) { id, content, type, processed\_at } or [BetaManagedAgentsUserInterruptEvent](api/http/beta/sessions/events.md) { id, type, processed\_at, session\_thread\_id } or [BetaManagedAgentsUserToolConfirmationEvent](api/http/beta/sessions/events.md) { id, result, tool\_use\_id, 4 more } or 34 more

Server-sent event in a single thread's stream.

One of the following:

#### Threads[Events](api/http/beta/sessions/threads/events.md)

##### [List Session Thread Events](api/http/beta/sessions/threads/events/list.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/http/beta/sessions/threads/events/stream.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

---

*Copyright © Anthropic. All rights reserved.*
