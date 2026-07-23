# Thinking in tool and multi-turn workflows

Copy page





For how zero data retention (ZDR) applies to this feature, see [API and data retention](manage-claude/api-and-data-retention.md).

This page walks through a complete two-turn tool-use round trip with thinking enabled: Claude thinks, requests a tool call, receives the result, and finishes its answer, with the thinking blocks handled correctly at every step. The full rules live on the [Thinking](build-with-claude/thinking.md) page, in [Thinking with tool use](build-with-claude/thinking.md) and [Preserving thinking blocks](build-with-claude/thinking.md); this page shows those rules applied in runnable code.

##  The rules this walkthrough applies

Each link leads to the full statement on the Thinking page:

- [Limit tool choice to `auto` or `none`](build-with-claude/thinking.md): `tool_choice` options that force tool use return an error while thinking is on.
- [Keep one thinking configuration per assistant turn](build-with-claude/thinking.md): a tool-use loop is one assistant turn, so change the configuration only between turns.
- [Pass thinking blocks back complete and unmodified](build-with-claude/thinking.md): when you return a tool result, the thinking blocks from the assistant message must come back with it.
- [Echo the assistant message exactly as received](build-with-claude/thinking.md): rebuilding the message or filtering out `redacted_thinking` blocks triggers a 400 error.

The samples use adaptive thinking; on models that support only extended thinking, substitute `thinking: {type: "enabled", budget_tokens: N}`. The round-trip rules are identical.

##  Walk through a two-turn tool-use round trip

The example defines a `get_weather` tool, lets Claude think and request a tool call, then returns the tool result along with the assistant turn echoed exactly as received, thinking block included.

1. 1

   Make the first request with a tool available

   Send a request with adaptive thinking enabled and the tool defined. Apart from the `thinking` parameter, this is a standard [tool use](agents-and-tools/tool-use/overview.md) request:

   CLIPythonTypeScriptC#GoJavaPHPRuby

   

   ```shiki
   client = anthropic.Anthropic()

   weather_tool = {
       "name": "get_weather",
       "description": "Get current weather for a location",
       "input_schema": {
           "type": "object",
           "properties": {"location": {"type": "string", "description": "City name"}},
           "required": ["location"],
       },
   }

   # First request - Claude responds with thinking and tool request
   response = client.messages.create(
       model="claude-opus-4-8",
       max_tokens=16000,
       thinking={"type": "adaptive"},
       tools=[weather_tool],
       messages=[{"role": "user", "content": "What's the weather in Paris?"}],
   )
   print(response)
   ```
2. 2

   Capture the content array to echo back

   You should see `thinking`, `text`, and `tool_use` blocks in the response content on a run where Claude chose to think (on simpler requests, adaptive mode may skip the thinking block). Keep this content array intact: the next step sends it back verbatim.

   

   To see thinking text like this output, add `display: "summarized"` to the request. On models where display defaults to omitted, including claude-opus-4-8, the `thinking` field otherwise comes back as an empty string with only the `signature` populated. Either way, echo the content array back unchanged; see [Controlling thinking display](build-with-claude/thinking.md).

   Output

   

   ```shiki
   {
     "content": [
       {
         "type": "thinking",
         "thinking": "The user wants to know the current weather in Paris. I have access to a function `get_weather`...",
         "signature": "BDaL4VrbR2Oj0hO4XpJxT28J5T...."
       },
       {
         "type": "text",
         "text": "I can help you get the current weather information for Paris. Let me check that for you"
       },
       {
         "type": "tool_use",
         "id": "toolu_01CswdEQBMshySk6Y9DFKrfq",
         "name": "get_weather",
         "input": {
           "location": "Paris"
         }
       }
     ]
   }
   ```
3. 3

   Return the tool result, echoing the assistant turn verbatim

   Run the tool on your side, then send a second request that appends two messages to the conversation. The first is the assistant content echoed back exactly as received, so the thinking block stays unchanged alongside the `tool_use` block. The second is a user message carrying the `tool_result`.

   Each sample is a self-contained script: it repeats the first request, then immediately sends the follow-up using the response it just received.

   CLIPythonTypeScriptC#GoJavaPHPRuby

   

   ```shiki
   client = anthropic.Anthropic()
   weather_tool = {
       "name": "get_weather",
       "description": "Get current weather for a location",
       "input_schema": {
           "type": "object",
           "properties": {"location": {"type": "string", "description": "City name"}},
           "required": ["location"],
       },
   }
   response = client.messages.create(
       model="claude-opus-4-8",
       max_tokens=16000,
       thinking={"type": "adaptive"},
       tools=[weather_tool],
       messages=[{"role": "user", "content": "What's the weather in Paris?"}],
   )
   # Extract the tool use block to get its ID for the tool result
   tool_use_block = next(block for block in response.content if block.type == "tool_use")

   # Call your actual weather API, here is where your actual API call would go
   # Let's pretend this is what we get back
   weather_data = {"temperature": 88}

   # Second request - Include the assistant turn and the tool result
   continuation = client.messages.create(
       model="claude-opus-4-8",
       max_tokens=16000,
       thinking={"type": "adaptive"},
       tools=[weather_tool],
       messages=[
           {"role": "user", "content": "What's the weather in Paris?"},
           # Echo the assistant content exactly as received. When a thinking
           # block is present, it must accompany the tool_use block.
           {"role": "assistant", "content": response.content},
           {
               "role": "user",
               "content": [
                   {
                       "type": "tool_result",
                       "tool_use_id": tool_use_block.id,
                       "content": f"Current temperature: {weather_data['temperature']}°F",
                   }
               ],
           },
       ],
   )
   print(continuation)
   ```
4. 4

   Read the final response

   You should see Claude complete the turn with text. Because [interleaved thinking](build-with-claude/thinking.md) is automatic in adaptive mode, the continuation can also open with a new thinking block before the final text:

   Output

   

   ```shiki
   {
     "content": [
       {
         "type": "text",
         "text": "Currently in Paris, the temperature is 88°F (31°C)"
       }
     ]
   }
   ```

##  How interleaved thinking changes the flow

Interleaved thinking lets Claude think between tool calls, reasoning about each tool result before acting on it. The concept and per-model availability are covered in [Interleaved thinking](build-with-claude/thinking.md) on the Thinking page; interleaving changes where thinking blocks appear, not whether tool calls can chain. The following comparison shows what interleaved thinking changes in a two-tool workflow:

### Tool use without interleaved thinking

### Tool use with interleaved thinking

##  Next steps

[Thinking

The overview: turn thinking on, read thinking output, and review the full rules for tool use, caching, and streaming.](build-with-claude/thinking.md)[Steering thinking

Steer how often and how deeply Claude thinks with effort levels and prompt-based guidance.](build-with-claude/thinking-steering-and-cost.md)[Extended thinking

Manual thinking budgets on older models: `budget_tokens` mechanics and migration to adaptive.](build-with-claude/extended-thinking.md)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
