# Token counting

Copy page



Token counting lets you determine the number of tokens in a message before you send it to Claude. This helps you make informed decisions about your prompts and usage. With token counting, you can:

- Proactively manage rate limits and costs
- Make smart model routing decisions
- Optimize prompts to a specific length

---

##  How to count message tokens

The [token counting](api/messages-count-tokens.md) endpoint accepts the same structured list of inputs for creating a message, including support for system prompts, [tools](agents-and-tools/tool-use/overview.md), [images](build-with-claude/vision.md), and [PDFs](build-with-claude/pdf-support.md). The response contains the total number of input tokens.

###  Supported models

All [active models](about-claude/models/overview.md) support token counting, including Claude Opus 5 and Claude Sonnet 5.

###  Count tokens in basic messages

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-opus-5",
    system="You are a scientist",
    messages=[{"role": "user", "content": "Hello, Claude"}],
)

print(response.json())
```

Output



```shiki
{ "input_tokens": 14 }
```

###  Count tokens in messages with tools

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-opus-5",
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
    messages=[{"role": "user", "content": "What's the weather like in San Francisco?"}],
)

print(response.json())
```

Output



```shiki
{ "input_tokens": 403 }
```

###  Count tokens in messages with images

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
import base64
import httpx

image_url = "https://platform.claude.com/docs/images/vision-example.jpg"
image_media_type = "image/jpeg"
image_data = base64.standard_b64encode(httpx.get(image_url).content).decode("utf-8")

client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-opus-5",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image_media_type,
                        "data": image_data,
                    },
                },
                {"type": "text", "text": "Describe this image"},
            ],
        }
    ],
)
print(response.json())
```

Output



```shiki
{ "input_tokens": 1028 }
```

###  Count tokens in messages with thinking

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-sonnet-4-6",
    thinking={"type": "enabled", "budget_tokens": 16000},
    messages=[
        {
            "role": "user",
            "content": "Are there an infinite number of prime numbers such that n mod 4 == 3?",
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "thinking",
                    "thinking": "This is a nice number theory question. Let's think about it step by step...",
                    "signature": "EuYBCkQYAiJAgCs1le6/Pol5Z4/JMomVOouGrWdhYNsH3ukzUECbB6iWrSQtsQuRHJID6lWV...",
                },
                {
                    "type": "text",
                    "text": "Yes, there are infinitely many prime numbers p such that p mod 4 = 3...",
                },
            ],
        },
        {"role": "user", "content": "Can you write a formal proof?"},
    ],
)

print(response.json())
```

Output



```shiki
{ "input_tokens": 88 }
```

###  Count tokens in messages with PDFs

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
import base64
import anthropic

client = anthropic.Anthropic()

with open("/path/to/document.pdf", "rb") as pdf_file:
    pdf_base64 = base64.standard_b64encode(pdf_file.read()).decode("utf-8")

response = client.messages.count_tokens(
    model="claude-opus-5",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": "application/pdf",
                        "data": pdf_base64,
                    },
                },
                {"type": "text", "text": "Please summarize this document."},
            ],
        }
    ],
)

print(response.json())
```

Output



```shiki
{ "input_tokens": 2188 }
```

---

##  Token counts on Claude Fable 5 and Claude Mythos 5

Claude Fable 5 and Claude Mythos 5 use the tokenizer introduced with Claude Opus 4.7, which produces roughly 30 percent more tokens than models before Claude Opus 4.7 for the same text. The exact increase depends on the content and workload shape. The token counting endpoint returns the count under the tokenizer of the `model` you pass, so to measure the difference for your workload, count the same request twice: once with your current model and once with `model: "claude-fable-5"` (or `"claude-mythos-5"`), and compare the two `input_tokens` values.

---

##  Pricing and rate limits

Token counting is **free to use** but subject to requests per minute rate limits based on your [usage tier](api/rate-limits.md). If you need higher limits, use **Request rate limit increase** on the [Rate limits](/settings/limits) page.

| Usage tier | Requests per minute (RPM) |
| --- | --- |
| Start | 2,000 |
| Build | 4,000 |
| Scale | 8,000 |

---

##  FAQ

### Does token counting use prompt caching?

---

##  Next steps



[Count message tokens](api/messages-count-tokens.md)

Read the full API reference for the token counting endpoint.



[Context windows](build-with-claude/context-windows.md)

Use token counts to keep prompts within a model's context window.



[Rate limits](api/rate-limits.md)

Check token counts before you send a request to stay within your usage tier.



[Prompt caching](build-with-claude/prompt-caching.md)

Reduce cost and latency on repeated prompts by caching prompt prefixes.

## Compatibility

|  |  |
| --- | --- |
| Supported platforms | - Claude API - Claude Platform on AWS - Amazon Bedrock - Google Cloud - Microsoft Foundry |

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
