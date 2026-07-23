# Parallel tool use

Copy page



By default, Claude may call multiple tools in a single response. This page covers how to run those calls, how to format the message history so parallelism keeps working, and how to disable parallel tool use when you need to. For the single-call flow, see [Handle tool calls](agents-and-tools/tool-use/handle-tool-calls.md).

##  Execution semantics

When Claude calls tools, the response has a `stop_reason` of `tool_use` and can contain several `tool_use` blocks in a single assistant turn. How you run those calls is your decision. The API doesn't prescribe an execution order: you can run the calls concurrently (`Promise.all`, `asyncio.gather`), sequentially in the order they appear, or in any combination that suits your tools.

Choose the strategy based on what your tools do. Independent, read-only operations are usually safe to run in parallel for lower latency. Tools with side effects, shared state, or ordering requirements might be better run sequentially.

Whichever strategy you use, return one `tool_result` for each `tool_use` block, all together in the next user message. Match each result to its call with `tool_use_id`, and put every `tool_result` block before any text content in that message. See [Handle tool calls](agents-and-tools/tool-use/handle-tool-calls.md) for the full formatting rules. If you choose not to run a particular call (for example, because you ran the batch sequentially and an earlier call failed), still return a `tool_result` for it with `is_error: true` and a brief explanation.

```shiki
{
  "type": "tool_result",
  "tool_use_id": "toolu_02",
  "is_error": true,
  "content": "Not executed: the preceding write_file call failed."
}
```



##  Test parallel tool calls



**Use the Tool Runner for most applications:** the SDK [Tool Runner](agents-and-tools/tool-use/tool-runner.md) handles responses with multiple tool calls and formats the results for you, so you don't write this handling yourself. Use the manual pattern on this page when you need direct control over how the calls run, such as custom batching, ordering, or error handling.

The following script sends a request that should trigger parallel tool calls, verifies the response contains them, and formats the tool results so parallelism keeps working. Run it with `ANTHROPIC_API_KEY` set in your environment:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = Anthropic()

# Define tools
tools = [
    {
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                }
            },
            "required": ["location"],
        },
    },
    {
        "name": "get_time",
        "description": "Get the current time in a given timezone",
        "input_schema": {
            "type": "object",
            "properties": {
                "timezone": {
                    "type": "string",
                    "description": "The timezone, e.g. America/New_York",
                }
            },
            "required": ["timezone"],
        },
    },
]

# Test conversation with parallel tool calls
messages = [
    {
        "role": "user",
        "content": "What's the weather in SF and NYC, and what time is it there?",
    }
]

# Make initial request
print("Requesting parallel tool calls...")
response = client.messages.create(
    model="claude-opus-4-8", max_tokens=1024, messages=messages, tools=tools
)

# Check for parallel tool calls
tool_uses = [block for block in response.content if block.type == "tool_use"]
print(f"\n✓ Claude made {len(tool_uses)} tool calls")

if len(tool_uses) > 1:
    print("✓ Parallel tool calls detected!")
    for tool in tool_uses:
        print(f"  - {tool.name}: {tool.input}")
else:
    print("✗ No parallel tool calls detected")

# Simulate tool execution and format results correctly
tool_results = []
for tool_use in tool_uses:
    if tool_use.name == "get_weather":
        if "San Francisco" in str(tool_use.input):
            result = "San Francisco: 68°F, partly cloudy"
        else:
            result = "New York: 45°F, clear skies"
    else:  # get_time
        if "Los_Angeles" in str(tool_use.input):
            result = "2:30 PM PST"
        else:
            result = "5:30 PM EST"

    tool_results.append(
        {"type": "tool_result", "tool_use_id": tool_use.id, "content": result}
    )

# Continue conversation with tool results
messages.extend(
    [
        {"role": "assistant", "content": response.content},
        {"role": "user", "content": tool_results},  # All results in one message!
    ]
)

# Get final response
print("\nGetting final response...")
final_response = client.messages.create(
    model="claude-opus-4-8", max_tokens=1024, messages=messages, tools=tools
)

final_text = next(
    block.text for block in final_response.content if block.type == "text"
)
print(f"\nClaude's response:\n{final_text}")

# Verify formatting
print("\n--- Verification ---")
print(f"✓ Tool results sent in single user message: {len(tool_results)} results")
print("✓ No text before tool results in content array")
print("✓ Conversation formatted correctly for future parallel tool use")
```

The summary lines at the end restate the two formatting rules that keep parallelism working: every tool result returns in a single user message, and no text content appears before the tool results in that message.

##  Maximizing parallel tool use

Claude 4 models make parallel tool calls by default when a request benefits from multiple tools. For all models, you can increase the likelihood of parallel tool calls with targeted prompting:

### System prompts for parallel tool use

### User message prompting

##  Disable parallel tool use

Parallel tool use is on by default. To turn it off, set `disable_parallel_tool_use: true` inside the [`tool_choice`](agents-and-tools/tool-use/define-tools.md) object. It is not a top-level request parameter. The effect depends on the `tool_choice` type.

###  At most one tool call

When `tool_choice` type is `auto` (the default), setting `disable_parallel_tool_use: true` means Claude calls at most one tool per response. Claude can still answer in plain text without calling any tool. The highlighted lines are the only change from a standard tool use request:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[
        {
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    }
                },
                "required": ["location"],
            },
        }
    ],
    tool_choice={"type": "auto", "disable_parallel_tool_use": True},
    messages=[
        {
            "role": "user",
            "content": "What is the weather in San Francisco and New York?",
        }
    ],
)
print(response.content)
```

###  Exactly one tool call

When `tool_choice` type is `any` or `tool`, setting `disable_parallel_tool_use: true` means Claude calls exactly one tool. The following example uses `any`. The same field works with `tool`:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[
        {
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    }
                },
                "required": ["location"],
            },
        }
    ],
    tool_choice={"type": "any", "disable_parallel_tool_use": True},
    messages=[
        {
            "role": "user",
            "content": "What is the weather in San Francisco and New York?",
        }
    ],
)
print(response.content)
```

##  Troubleshooting

If Claude isn't making parallel tool calls when expected, check these common issues:

**1. Incorrect tool result formatting**

The most common issue is formatting tool results incorrectly in the conversation history. This "teaches" Claude to avoid parallel calls.

Specifically for parallel tool use:

- **Wrong:** a separate user message for each tool result
- **Correct:** all tool results together in a single user message

```shiki
// Wrong: separate user messages reduce parallel tool use
[
  {"role": "assistant", "content": [tool_use_1, tool_use_2]},
  {"role": "user", "content": [tool_result_1]},
  {"role": "user", "content": [tool_result_2]}  // Separate message
]

// Correct: one user message with all results maintains parallel tool use
[
  {"role": "assistant", "content": [tool_use_1, tool_use_2]},
  {"role": "user", "content": [tool_result_1, tool_result_2]}  // Single message
]
```



See [Handle tool calls](agents-and-tools/tool-use/handle-tool-calls.md) for other formatting rules.

**2. Weak prompting**

Default prompting might not be sufficient. Use the stronger system prompt from [Maximizing parallel tool use](#maximizing-parallel-tool-use).

**3. Measuring parallel tool usage**

To verify parallel tool calls are working:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
messages = []  # Message objects returned by client.messages.create across your run

tool_call_messages = [
    msg for msg in messages if any(block.type == "tool_use" for block in msg.content)
]
total_tool_calls = sum(
    len([block for block in msg.content if block.type == "tool_use"])
    for msg in tool_call_messages
)
avg_tools_per_message = (
    total_tool_calls / len(tool_call_messages) if tool_call_messages else 0.0
)
print(f"Average tools per message: {avg_tools_per_message}")
# Should be > 1.0 if parallel calls are working
```

**4. Calls in a batch appear to depend on each other**

Execution order is your choice. If your tools have ordering dependencies, running the batch sequentially and stopping on the first failure is a valid strategy: return `is_error: true` for any call you didn't run. If you run in parallel and a call fails because its prerequisite hadn't completed, return `is_error: true` with the natural error message. Claude will reissue the call on the next turn. To reduce dependent calls appearing together, add this to your system prompt: "Only batch tool calls that are independent of each other."

##  Next steps

[

Tool Runner (SDK)

Use the SDK's Tool Runner abstraction to handle the agentic loop, error wrapping, and type safety automatically.](agents-and-tools/tool-use/tool-runner.md)[Handle tool calls

Parse tool\_use blocks, format tool\_result responses, and handle errors with is\_error.](agents-and-tools/tool-use/handle-tool-calls.md)[Define tools

Specify tool schemas, write effective descriptions, and control when Claude calls your tools.](agents-and-tools/tool-use/define-tools.md)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
