# Compaction

Copy page

This feature is eligible for [Zero Data Retention (ZDR)](build-with-claude/api-and-data-retention.md). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.

Server-side compaction is the recommended strategy for managing context in long-running conversations and agentic workflows. It handles context management automatically with minimal integration work.

Compaction extends the effective context length for long-running conversations and tasks by automatically summarizing older context when approaching the context window limit. This isn't just about staying under a token cap. As conversations get longer, models struggle to maintain focus across the full history. Compaction keeps the active context focused and performant by replacing stale content with concise summaries.

For a deeper look at why long contexts degrade and how compaction helps, see
[Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).

This is ideal for:

- Chat-based, multi-turn conversations where you want users to use one chat for a long period of time
- Task-oriented prompts that require a lot of follow-up work (often tool use) that may exceed the context window

Compaction is in beta. Include the [beta header](api/beta-headers.md) `compact-2026-01-12` in your API requests to use this feature.

## Supported models

Compaction is supported on the following models:

- [Claude Mythos Preview](https://anthropic.com/glasswing) (`claude-mythos-preview`)
- Claude Opus 4.6 (`claude-opus-4-6`)
- Claude Sonnet 4.6 (`claude-sonnet-4-6`)

## How compaction works

When compaction is enabled, Claude automatically summarizes your conversation when it approaches the configured token threshold. The API:

1. Detects when input tokens exceed your specified trigger threshold.
2. Generates a summary of the current conversation.
3. Creates a `compaction` block containing the summary.
4. Continues the response with the compacted context.

On subsequent requests, append the response to your messages. The API automatically drops all message blocks prior to the `compaction` block, continuing the conversation from the summary.

![Flow diagram showing the compaction process: when input tokens exceed the trigger threshold, Claude generates a summary in a compaction block and continues the response with the compacted context](/docs/images/compaction-flow.svg)

## Basic usage

Enable compaction by adding the `compact_20260112` strategy to `context_management.edits` in your Messages API request.

Shell

```shiki
curl https://api.anthropic.com/v1/messages \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "anthropic-beta: compact-2026-01-12" \
     --header "content-type: application/json" \
     --data \
'{
    "model": "claude-opus-4-6",
    "max_tokens": 4096,
    "messages": [
        {
            "role": "user",
            "content": "Help me build a website"
        }
    ],
    "context_management": {
        "edits": [
            {
                "type": "compact_20260112"
            }
        ]
    }
}'
```

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `type` | string | Required | Must be `"compact_20260112"` |
| `trigger` | object | 150,000 tokens | When to trigger compaction. Must be at least 50,000 tokens. |
| `pause_after_compaction` | boolean | `false` | Whether to pause after generating the compaction summary |
| `instructions` | string | `null` | Custom summarization prompt. Completely replaces the default prompt when provided. |

### Trigger configuration

Configure when compaction triggers using the `trigger` parameter:

CLI

```shiki
ant beta:messages create --beta compact-2026-01-12 <<'YAML'
model: claude-opus-4-6
max_tokens: 4096
messages:
  - role: user
    content: Hello, Claude
context_management:
  edits:
    - type: compact_20260112
      trigger:
        type: input_tokens
        value: 150000
YAML
```

### Custom summarization instructions

By default, compaction uses the following summarization prompt:

```inline-block
You have written a partial transcript for the initial task above. Please write a summary of the transcript. The purpose of this summary is to provide continuity so you can continue to make progress towards solving the task in a future context, where the raw history above may not be accessible and will be replaced with this summary. Write down anything that would be helpful, including the state, next steps, learnings etc. You must wrap your summary in a <summary></summary> block.
```

You can provide custom instructions via the `instructions` parameter to replace this prompt entirely. Custom instructions don't supplement the default; they completely replace it:

CLI

```shiki
ant beta:messages create --beta compact-2026-01-12 <<'YAML'
model: claude-opus-4-6
max_tokens: 4096
messages:
  - role: user
    content: Hello, Claude
context_management:
  edits:
    - type: compact_20260112
      instructions: >-
        Focus on preserving code snippets, variable names, and
        technical decisions.
YAML
```

### Pausing after compaction

Use `pause_after_compaction` to pause the API after generating the compaction summary. This allows you to add additional content blocks (such as preserving recent messages or specific instruction-oriented messages) before the API continues with the response.

When enabled, the API returns a message with the `compaction` stop reason after generating the compaction block:

CLI

```shiki
ant beta:messages create --beta compact-2026-01-12 \
  --transform '{stop_reason,content}' --format jsonl <<'YAML' > resp.json
model: claude-opus-4-6
max_tokens: 4096
messages:
  - role: user
    content: "Hello, Claude"
context_management:
  edits:
    - type: compact_20260112
      pause_after_compaction: true
YAML

# Check if compaction triggered a pause
if grep -q '"stop_reason":"compaction"' resp.json; then
  # Response contains only the compaction block
  RESP=$(cat resp.json)
  CONTENT="${RESP#*\"content\":}"
  printf '%s' "${CONTENT%\}}" > content.json

  # Continue the request
  ant beta:messages create --beta compact-2026-01-12 <<YAML > /dev/null
model: claude-opus-4-6
max_tokens: 4096
messages:
  - role: user
    content: "Hello, Claude"
  - role: assistant
    content: $(cat content.json)
context_management:
  edits:
    - type: compact_20260112
YAML
fi
```

#### Enforcing a total token budget

When a model works on long tasks with many tool-use iterations, total token consumption can grow significantly. You can combine `pause_after_compaction` with a compaction counter to estimate cumulative usage and gracefully wrap up the task once a budget is reached:

Python

```shiki
client = anthropic.Anthropic()
messages = [{"role": "user", "content": "Hello, Claude"}]
TRIGGER_THRESHOLD = 100_000
TOTAL_TOKEN_BUDGET = 3_000_000
n_compactions = 0

response = client.beta.messages.create(
    betas=["compact-2026-01-12"],
    model="claude-opus-4-6",
    max_tokens=4096,
    messages=messages,
    context_management={
        "edits": [
            {
                "type": "compact_20260112",
                "trigger": {"type": "input_tokens", "value": TRIGGER_THRESHOLD},
                "pause_after_compaction": True,
            }
        ]
    },
)

if response.stop_reason == "compaction":
    n_compactions += 1
    messages.append({"role": "assistant", "content": response.content})

    # Estimate total tokens consumed; prompt wrap-up if over budget
    if n_compactions * TRIGGER_THRESHOLD >= TOTAL_TOKEN_BUDGET:
        messages.append(
            {
                "role": "user",
                "content": "Please wrap up your current work and summarize the final state.",
            }
        )
```

## Working with compaction blocks

When compaction is triggered, the API returns a `compaction` block at the start of the assistant response.

A long-running conversation may result in multiple compactions. The last compaction block reflects the final state of the prompt, replacing content prior to it with the generated summary.

Output

```shiki
{
  "content": [
    {
      "type": "compaction",
      "content": "Summary of the conversation: The user requested help building a web scraper..."
    },
    {
      "type": "text",
      "text": "Based on our conversation so far..."
    }
  ]
}
```

### Passing compaction blocks back

You must pass the `compaction` block back to the API on subsequent requests to continue the conversation with the shortened prompt. The simplest approach is to append the entire response content to your messages:

CLI

```shiki
ant beta:messages create --beta compact-2026-01-12 \
  --transform content --format jsonl <<'YAML' > content.json
model: claude-opus-4-6
max_tokens: 4096
messages:
  - role: user
    content: Hello, Claude
context_management:
  edits:
    - type: compact_20260112
YAML

# After receiving a response with a compaction block, append it as the
# assistant turn and continue the conversation
ant beta:messages create --beta compact-2026-01-12 <<YAML
model: claude-opus-4-6
max_tokens: 4096
messages:
  - role: user
    content: Hello, Claude
  - role: assistant
    content: $(cat content.json)
  - role: user
    content: Now add error handling
context_management:
  edits:
    - type: compact_20260112
YAML
```

When the API receives a `compaction` block, all content blocks before it are ignored. You can either:

- Keep the original messages in your list and let the API handle removing the compacted content
- Manually drop the compacted messages and only include the compaction block onwards

### Streaming

When streaming responses with compaction enabled, you'll receive a `content_block_start` event when compaction begins. The compaction block streams differently from text blocks. You'll receive a `content_block_start` event, followed by a single `content_block_delta` with the complete summary content (no intermediate streaming), and then a `content_block_stop` event.

CLI

```shiki
ant beta:messages create --stream --format jsonl \
  --beta compact-2026-01-12 <<'YAML'
model: claude-opus-4-6
max_tokens: 4096
messages:
  - role: user
    content: Hello, Claude
context_management:
  edits:
    - type: compact_20260112
YAML
```

### Prompt caching

Compaction works well with [prompt caching](build-with-claude/prompt-caching.md). You can add a `cache_control` breakpoint on compaction blocks to cache the summarized content. The original compacted content is ignored.

```shiki
{
  "role": "assistant",
  "content": [
    {
      "type": "compaction",
      "content": "[summary text]",
      "cache_control": { "type": "ephemeral" }
    },
    {
      "type": "text",
      "text": "Based on our conversation..."
    }
  ]
}
```

#### Maximizing cache hits with system prompts

When compaction occurs, the summary becomes new content that needs to be written to the cache. Without additional cache breakpoints, this would also invalidate any cached system prompt, requiring it to be re-cached along with the compaction summary.

To maximize cache hit rates, add a `cache_control` breakpoint at the end of your system prompt. This keeps the system prompt cached separately from the conversation, so when compaction occurs:

- The system prompt cache remains valid and is read from cache
- Only the compaction summary needs to be written as a new cache entry

CLI

```shiki
ant beta:messages create --beta compact-2026-01-12 <<'YAML'
model: claude-opus-4-6
max_tokens: 4096
system:
  - type: text
    text: You are a helpful coding assistant...
    cache_control:
      type: ephemeral
messages:
  - role: user
    content: Hello, Claude
context_management:
  edits:
    - type: compact_20260112
YAML
```

This approach is particularly beneficial for long system prompts, as they remain cached even across multiple compaction events throughout a conversation.

## Understanding usage

Compaction requires an additional sampling step, which contributes to rate limits and billing. The API returns detailed usage information in the response:

Output

```shiki
{
  "usage": {
    "input_tokens": 23000,
    "output_tokens": 1000,
    "iterations": [
      {
        "type": "compaction",
        "input_tokens": 180000,
        "output_tokens": 3500
      },
      {
        "type": "message",
        "input_tokens": 23000,
        "output_tokens": 1000
      }
    ]
  }
}
```

The `iterations` array shows usage for each sampling iteration. When compaction occurs, you'll see a `compaction` iteration followed by the main `message` iteration. The top-level `input_tokens` and `output_tokens` match the `message` iteration exactly in this example because there is only one non-compaction iteration. The final iteration's token counts reflect the effective context size after compaction.

The top-level `input_tokens` and `output_tokens` do not include compaction iteration usage. They reflect the sum of all non-compaction iterations. To calculate total tokens consumed and billed for a request, sum across all entries in the `usage.iterations` array.

If you previously relied on `usage.input_tokens` and `usage.output_tokens` for cost tracking or auditing, you'll need to update your tracking logic to aggregate across `usage.iterations` when compaction is enabled. The `iterations` array is only populated when a new compaction is triggered during the request. Re-applying a previous `compaction` block incurs no additional compaction cost, and the top-level usage fields remain accurate in that case.

## Combining with other features

### Server tools

When using server tools (like web search), the compaction trigger is checked at the start of each sampling iteration. Compaction may occur multiple times within a single request depending on your trigger threshold and the amount of output generated.

### Token counting

The token counting endpoint (`/v1/messages/count_tokens`) applies existing `compaction` blocks in your prompt but does not trigger new compactions. Use it to check your effective token count after previous compactions:

CLI

```shiki
cat > request.yaml <<'YAML'
model: claude-opus-4-6
messages:
  - role: user
    content: Hello, Claude
context_management:
  edits:
    - type: compact_20260112
YAML

CURRENT=$(ant beta:messages count-tokens \
  --beta compact-2026-01-12 \
  --transform input_tokens --format yaml < request.yaml)

ORIGINAL=$(ant beta:messages count-tokens \
  --beta compact-2026-01-12 \
  --transform context_management.original_input_tokens \
  --format yaml < request.yaml)

printf 'Current tokens: %s\n' "$CURRENT"
printf 'Original tokens: %s\n' "$ORIGINAL"
```

## Examples

Here's a complete example of a long-running conversation with compaction:

CLI

```shiki
# The CLI handles individual turns; maintain the messages array in the
# calling script. See the SDK tabs for the full chat() loop. Single-turn
# request shape:
ant beta:messages create --beta compact-2026-01-12 \
  --transform 'content.#(type=="text").text' --format yaml <<'YAML'
model: claude-opus-4-6
max_tokens: 4096
messages:
  - role: user
    content: Help me build a Python web scraper
context_management:
  edits:
    - type: compact_20260112
      trigger:
        type: input_tokens
        value: 100000
YAML
```

Here's an example that uses `pause_after_compaction` to preserve the prior exchange and the current user message (three messages total) verbatim instead of summarizing them:

CLI

```shiki
# The CLI handles individual turns; maintain the messages array in the
# calling script. See the SDK tabs for the full chat() loop with
# pause-and-preserve handling. Single-turn request shape:
ant beta:messages create --beta compact-2026-01-12 \
  --transform 'content.#(type=="text").text' --format yaml <<'YAML'
model: claude-opus-4-6
max_tokens: 4096
messages:
  - role: user
    content: Help me build a Python web scraper
context_management:
  edits:
    - type: compact_20260112
      trigger:
        type: input_tokens
        value: 100000
      pause_after_compaction: true
YAML
```

## Current limitations

- **Same model for summarization:** The model specified in your request is used for summarization. There is no option to use a different (for example, cheaper) model for the summary.

## Next steps

[Session memory compaction cookbook

Explore a practical implementation that manages long-running conversations with instant session memory compaction using background threading and prompt caching.](https://platform.claude.com/cookbook/misc-session-memory-compaction)[Context windows

Learn about context window sizes and management strategies.](build-with-claude/context-windows.md)[Context editing

Explore other strategies for managing conversation context like tool result clearing and thinking block clearing.](build-with-claude/context-editing.md)

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
