# Define outcomes

Copy page

Outcomes is a Research Preview feature. [Request access](https://claude.com/form/claude-managed-agents) to try it.

The `outcome` elevates a session from *conversation* to *work*. You define what the end result should look like and how to measure quality. The agent works toward that target, self-evaluating and iterating until the outcome is met.

When you define an outcome, the harness automatically provisions a *grader* to evaluate the artifact against a rubric. It leverages a separate context window to avoid being influenced by the main agent's implementation choices.

The grader returns a per-criterion breakdown: either confirmation that the artifact satisfies the rubric, or the specific gaps between the current work and the requirements. That feedback is handed back to the agent for the next iteration.

All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. Research preview features additionally require `managed-agents-2026-04-01-research-preview`. The SDK sets these beta headers automatically.

## Create a rubric

A rubric is a markdown document describing per-criterion scoring. The rubric is required.

### Tips for writing effective rubrics

Example rubric:

```shiki
# DCF Model Rubric

## Revenue Projections
- Uses historical revenue data from the last 5 fiscal years
- Projects revenue for at least 5 years forward
- Growth rate assumptions are explicitly stated and reasonable

## Cost Structure
- COGS and operating expenses are modeled separately
- Margins are consistent with historical trends or deviations are justified

## Discount Rate
- WACC is calculated with stated assumptions for cost of equity and cost of debt
- Beta, risk-free rate, and equity risk premium are sourced or justified

## Terminal Value
- Uses either perpetuity growth or exit multiple method (stated which)
- Terminal growth rate does not exceed long-term GDP growth

## Output Quality
- All figures are in a single .xlsx file with clearly labeled sheets
- Key assumptions are on a separate "Assumptions" sheet
- Sensitivity analysis on WACC and terminal growth rate is included
```

Pass the rubric as inline text on `user.define_outcome` (shown in the next section), or upload it via the Files API for reuse across sessions:

**Requires beta header `files-api-2025-04-14`.**

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
rubric=$(curl -fsSL https://api.anthropic.com/v1/files \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01,files-api-2025-04-14" \
  -F file=@/path/to/pr_review_rubric.md)
rubric_id=$(jq -r '.id' <<<"$rubric")
printf 'Uploaded rubric: %s\n' "$rubric_id"
```

## Create a session with an outcome

After creating a session, send a `user.define_outcome` event. The agent begins work immediately; no additional user message event is required.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
# Create a session
session=$(curl -fsSL https://api.anthropic.com/v1/sessions \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01-research-preview" \
  --json @- <<EOF
{
  "agent": "$agent_id",
  "environment_id": "$environment_id",
  "title": "Financial analysis on Costco"
}
EOF
)
session_id=$(jq -r '.id' <<<"$session")

# Define the outcome — agent starts working on receipt
curl -fsSL "https://api.anthropic.com/v1/sessions/$session_id/events" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01-research-preview" \
  --json @- >/dev/null <<EOF
{
  "events": [
    {
      "type": "user.define_outcome",
      "description": "Build a DCF model for Costco in .xlsx",
      "rubric": {"type": "text", "content": "# DCF Model Rubric\n..."},
      "max_iterations": 5
    }
  ]
}
EOF
# or: "rubric": {"type": "file", "file_id": "$rubric_id"}
# "max_iterations" is optional; default 3, max 20
```

## Outcome events

Progress on an outcome-oriented session is surfaced on the events [stream](managed-agents/events-and-streaming.md).

- `agent.*` events (messages, tool use, etc.) show progress towards the outcome.
- `span.outcome_evaluation_*` events are only emitted for outcome-oriented sessions and show the number of iteration loops and the grader's feedback process.
- You can also send `user.message` [events](managed-agents/events-and-streaming.md) to an outcome-oriented session, to direct the agent's work as it progresses, but these are not as necessary; the agent knows to work until it has exhausted its iterations or achieved the outcome.
- A `user.interrupt` event will pause work on the current outcome and mark the `span.outcome_evaluation_end.result` as `interrupted`, allowing you to kick off a new outcome.
- After the final outcome evaluation, the session can be continued as a conversational session, or a new outcome can be kicked off. The session will retain history of the prior outcome.

### Define outcome user event

Only one outcome supported at a time, but you may chain together outcomes in sequence. To do this, send a new `user.define_outcome` event after the terminal event of the previous outcome.

This is the event you send to initiate an outcome. It is echoed back on receipt, including a `processed_at` timestamp and `outcome_id`.

```shiki
{
  "type": "user.define_outcome",
  "description": "Build a DCF model for Costco in .xlsx",
  "rubric": { "type": "file", "file_id": "file_01..." },
  "max_iterations": 5
}
```

### Outcome evaluation start

Emitted once the grader starts an evaluation over one iteration loop. The `iteration` field is a 0-indexed revision counter: `0` is the first evaluation, `1` is the re-evaluation after the first revision, and so on.

```shiki
{
  "type": "span.outcome_evaluation_start",
  "id": "sevt_01def...",
  "outcome_id": "outc_01a...",
  "iteration": 0,
  "processed_at": "2026-03-25T14:01:45Z"
}
```

### Outcome evaluation ongoing

Heartbeat emitted while the grader runs. The grader's internal reasoning is opaque: you see that it's working, not what it's thinking.

```shiki
{
  "type": "span.outcome_evaluation_ongoing",
  "id": "sevt_01ghi...",
  "outcome_id": "outc_01a...",
  "processed_at": "2026-03-25T14:02:10Z"
}
```

### Outcome evaluation end

Emitted after the grader finishes evaluating one iteration. The `result` field indicates what happens next.

| Result | Next |
| --- | --- |
| `satisfied` | Session transitions to `idle`. |
| `needs_revision` | Agent starts a new iteration cycle. |
| `max_iterations_reached` | No further evaluation cycles. The agent may run one final revision before the session transitions to `idle`. |
| `failed` | Session transitions to `idle`. Returned when the rubric fundamentally does not match the task, for example if the description and rubric contradict each other. |
| `interrupted` | Only emitted if `outcome_evaluation_start` already fired before the interrupt. |

```shiki
{
  "type": "span.outcome_evaluation_end",
  "id": "sevt_01jkl...",
  "outcome_evaluation_start_id": "sevt_01def...",
  "outcome_id": "outc_01a...",
  "result": "satisfied",
  "explanation": "All 12 criteria met: revenue projections use 5 years of historical data, WACC assumptions are stated, sensitivity table is included...",
  "iteration": 0,
  "usage": {
    "input_tokens": 2400,
    "output_tokens": 350,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 1800
  },
  "processed_at": "2026-03-25T14:03:00Z"
}
```

## Checking on outcome status

You can either listen on the [event stream](managed-agents/events-and-streaming.md) for `span.outcome_evaluation_end`, or poll `GET /v1/sessions/:id` and read `outcome_evaluations[].result`:

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
session=$(curl -fsSL "https://api.anthropic.com/v1/sessions/$session_id" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01-research-preview")

jq -r '.outcome_evaluations[] | "\(.outcome_id): \(.result)"' <<<"$session"
# outc_01a...: satisfied
```

## Retrieving deliverables

The agent writes output files to `/mnt/session/outputs/` inside the container. Once the session is idle, fetch them via the [Files API](build-with-claude/files.md) scoped to the session:

curlPython

```shiki
# List files produced by this session
curl -fsSL "https://api.anthropic.com/v1/files?scope_id=$session_id" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14,managed-agents-2026-04-01-research-preview" \
| jq '.data[] | {id, filename, size_bytes}'

# Download by file_id
curl -fsSL "https://api.anthropic.com/v1/files/$file_id/content" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14" \
  -o costco_dcf.xlsx
```

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
