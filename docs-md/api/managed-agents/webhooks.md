# Subscribe to webhooks

Copy page



Sessions are long-running interactions. While most real-time interactions happen through the [SSE event stream](managed-agents/events-and-streaming.md), webhooks notify you of major state changes.

Webhook events return the event `type` and `id`, not the full object. When you receive a webhook event, you need to fetch the object directly with a `GET` call. This avoids delivering stale data on retries and keeps every delivery small.

##  Supported event types

Session events

Session events

Vault events

Vault events

Agent events

Agent events

Deployment events

Deployment events

Deployment run events

Deployment run events

Environment events

Environment events

Memory store events

Memory store events

| Event | Trigger |
| --- | --- |
| `session.status_run_started` | Agent execution kicked off. This triggers at every session status transition to `running`. |
| `session.status_idled` | Agent awaiting input, for example a tool permission approval or a new user message. |
| `session.status_rescheduled` | A transient error occurred and the session is retrying automatically. |
| `session.status_terminated` | The session terminated, either because of an error or completion. |
| `session.thread_created` | New [multiagent thread](managed-agents/multiagent-orchestration.md) opened, meaning an additional agent called by the coordinator is kicking off work. |
| `session.thread_idled` | An agent in a [multiagent interaction](managed-agents/multiagent-orchestration.md) is waiting for input. |
| `session.thread_terminated` | A [multiagent thread](managed-agents/multiagent-orchestration.md) terminated, either because the child agent completed its work or because the thread was archived. Fires for child threads only; the primary thread's end surfaces as `session.status_terminated`. |
| `session.outcome_evaluation_ended` | [Outcome evaluation](managed-agents/define-outcomes.md) for a single iteration completed. |
| `session.updated` | Session properties changed (for example, its name or configuration was updated). |
| `session.deleted` | Session permanently deleted. There is no object left to fetch, so treat the event itself as final. |

##  Register an endpoint

Visit **Manage > Webhooks** in [Console](https://platform.claude.com/settings/workspaces/default/webhooks).

A webhook endpoint consists of:

- **URL:** Must be HTTPS on port 443 with a publicly resolvable hostname.
- **Event types:** The list of `data.type` values this endpoint receives. An endpoint only receives events it's subscribed to.
- **Signing secret:** A 32-byte `whsec_`-prefixed secret generated at creation. It's shown only once, so store it securely to verify webhook deliveries.

##  Verify the signature

Every delivery carries the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers. Use the SDK's `unwrap()` helper to verify the signature and parse the event in one step. It throws if the signature is invalid or the payload is more than five minutes old.

Set `ANTHROPIC_WEBHOOK_SIGNING_KEY` to the `whsec_`-prefixed secret shown at endpoint creation.

PythonTypeScriptC#GoJavaPHPRuby



```shiki
from flask import Flask, request
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_WEBHOOK_SIGNING_KEY from env
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        # unwrap() raises if the signature is invalid or the payload is stale
        event = client.beta.webhooks.unwrap(
            request.get_data(as_text=True),
            headers=dict(request.headers),
        )
    except Exception:
        return "invalid signature", 400

    if event.data.type == "session.status_idled":
        print("session idled:", event.data.id)
    # handle other event types

    return "", 200
```

##  Handle an event

Parse the body, switch on `data.type`, and fetch the resource by ID. Return any `2xx` to acknowledge. Any other response counts against the endpoint: a `3xx` disables it immediately (redirects are never followed), while other failures are retried; see [Delivery behavior](#delivery-behavior) for the retry and auto-disable rules.

Every event payload has the same structure, including the event type, identifier, and the timestamp of when the event occurred.

```shiki
{
  "type": "event",
  "id": "whe_9d5c1f7e...",
  "created_at": "2026-03-18T14:05:22Z",
  "data": {
    "type": "session.status_idled",
    "id": "sesn_01XYZ...",
    "organization_id": "8a3d2f1e-...",
    "workspace_id": "c7b0e4d9-..."
  }
}
```



PythonTypeScriptC#GoJavaPHPRuby



```shiki
if event.data.type == "session.status_idled":
    session = client.beta.sessions.retrieve(event.data.id)
    notify_user(session)
return "", 204
```

The top-level `event.id` is unique per event, not per delivery. If you receive the same `event.id` twice, it's a retry and you can discard it.

##  Delivery behavior

- **Duplicates:** An endpoint can receive the same event more than once, and every attempt delivers the same top-level `event.id` (the same value as the `webhook-id` header). Deduplicate on it.
- **Subscription scope:** An event is delivered only to endpoints subscribed to its type at the moment it's emitted. An event emitted while no endpoint is subscribed to its type is never delivered, and subscribing later doesn't backfill it, so subscribe to an event type before you need it.
- **Ordering is not guaranteed.** Events aren't delivered in the order they occurred: `session.status_idled` may arrive before `session.outcome_evaluation_ended` even if the outcome was produced first, and a `.deleted` event can arrive before the `.archived` event for the same resource. Drive your state from the resource you fetch, not from the order events arrive in.
- **Retries:** For each endpoint and event, Anthropic makes up to three delivery attempts (a response that triggers auto-disable, described later in this section, is never retried) with jittered exponential backoff between 5 and 120 seconds. Every attempt delivers the same `event.id`. After the last attempt fails, the event is dropped: it isn't queued for later delivery and there's no signal that it was lost. Webhooks aren't a durable log, so if you need to observe every transition, reconcile by listing or fetching the resource through the API.
- **Timestamps:** The `webhook-timestamp` header is stamped when a delivery attempt is signed and is regenerated on every retry, so retries aren't rejected by the SDK's freshness check. It's the clock for the delivery attempt, not for the event: use the event payload's `created_at` for when the event occurred.
- **Auto-disable:** An endpoint is automatically set to `disabled` with a machine-readable `disabled_reason` in three cases:

  - The endpoint returns a `3xx` response. Redirects are never followed; this disables the endpoint immediately, on the first attempt, with the reason `auto-disabled: endpoint URL returned a redirect (3xx)`. If your endpoint moves, update the URL in Console and re-enable the endpoint.
  - The endpoint's URL resolves to a non-public IP address when Anthropic connects. This disables the endpoint immediately, with the reason `auto-disabled: endpoint URL resolved to an invalid address`.
  - Deliveries to the endpoint fail continuously for a sustained period, with the reason `auto-disabled after sustained delivery failures`. The trigger is how long the endpoint has been failing without interruption, not a delivery count. A single `2xx` resets the window, so one flaky event can't disable the endpoint.

  All three are reversible: re-enable the endpoint in Console after you resolve the issue. Events emitted while the endpoint was disabled aren't replayed.

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
