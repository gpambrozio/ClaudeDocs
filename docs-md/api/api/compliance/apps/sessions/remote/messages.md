# Messages

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](manage-claude/compliance-api-access.md)

Copy page



# Messages

##### [Retrieve remote session messages](api/http/compliance/apps/sessions/remote/messages/list.md)

GET/v1/compliance/apps/sessions/remote/{claude\_remote\_session\_id}/messages

##### Models



MessageListResponse object{ id, content, content\_unavailable, 3 more }

A single user or assistant turn in a remote session transcript.

`content` is a discriminated union of `text`, `tool_use`, and
`tool_result` blocks.

---

*Copyright © Anthropic. All rights reserved.*
