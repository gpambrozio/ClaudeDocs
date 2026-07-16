# Token counting

Copy page



Token counting lets you determine the number of tokens in a message before you send it to Claude. This helps you make informed decisions about your prompts and usage. With token counting, you can:

- Proactively manage rate limits and costs
- Make smart model routing decisions
- Optimize prompts to a specific length



This feature is eligible for [Zero Data Retention (ZDR)](build-with-claude/api-and-data-retention.md). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.

---

##  How to count message tokens

The [token counting](api/messages-count-tokens.md) endpoint accepts the same structured list of inputs for creating a message, including support for system prompts, [tools](agents-and-tools/tool-use/overview.md), [images](build-with-claude/vision.md), and [PDFs](build-with-claude/pdf-support.md). The response contains the total number of input tokens.



The token count should be considered an **estimate**. In some cases, the actual number of input tokens used when creating a message may differ by a small amount.

Token counts may include tokens added automatically by Anthropic for system optimizations. **You are not billed for system-added tokens**. Billing reflects only your content.

###  Supported models

All [active models](about-claude/models/overview.md) support token counting, including Claude Sonnet 5.



Claude Opus 4.7 and later Opus models, Claude Fable 5, Claude Mythos 5, Claude Mythos Preview, and Claude Sonnet 5 use a newer tokenizer. The same input text produces approximately 30% more tokens than on earlier models. The exact increase depends on the content and workload shape. Recount prompts against the model you plan to use rather than reusing counts measured against earlier models.

###  Count tokens in basic messages

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-opus-4-8",
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



[Server tool](agents-and-tools/tool-use/server-tools.md) token counts only apply to the first sampling call.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-opus-4-8",
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

image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
image_media_type = "image/jpeg"
image_data = base64.standard_b64encode(httpx.get(image_url).content).decode("utf-8")

client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-opus-4-8",
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
{ "input_tokens": 1551 }
```

###  Count tokens in messages with extended thinking



See [how the context window is calculated with extended thinking](build-with-claude/extended-thinking.md) for more details.

- Thinking blocks from **previous** assistant turns are ignored and **do not** count toward your input tokens
- **Current** assistant turn thinking **does** count toward your input tokens

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



Token counting supports PDFs with the same [limitations](build-with-claude/pdf-support.md) as the Messages API.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
import base64
import anthropic

client = anthropic.Anthropic()

with open("/path/to/document.pdf", "rb") as pdf_file:
    pdf_base64 = base64.standard_b64encode(pdf_file.read()).decode("utf-8")

response = client.messages.count_tokens(
    model="claude-opus-4-8",
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

Claude Fable 5 and Claude Mythos 5 use the tokenizer introduced with Claude Opus 4.7, which produces roughly 30% more tokens than models before Claude Opus 4.7 for the same text. The exact increase depends on the content and workload shape. The token counting endpoint returns the count under the tokenizer of the `model` you pass, so to measure the difference for your workload, count the same request twice: once with your current model and once with `model: "claude-fable-5"` (or `"claude-mythos-5"`), and compare the two `input_tokens` values.



**Billing and migration:** Usage and billing on Claude Fable 5 and Claude Mythos 5 reflect this tokenizer's counts. If you're migrating from a model before Claude Opus 4.7, the same content consumes roughly 30% more tokens. The exact increase depends on the content and workload shape. When migrating a workload to Claude Fable 5 and Claude Mythos 5, don't reuse token counts measured on a model before Claude Opus 4.7 to estimate costs or context window fit. Count your prompts with `model: "claude-fable-5"` (or `"claude-mythos-5"`).

---

##  Pricing and rate limits

Token counting is **free to use** but subject to requests per minute rate limits based on your [usage tier](api/rate-limits.md). If you need higher limits, use **Request rate limit increase** on the [Limits](/settings/limits) page.

| Usage tier | Requests per minute (RPM) |
| --- | --- |
| Start | 2,000 |
| Build | 4,000 |
| Scale | 8,000 |



Token counting and message creation have separate and independent rate limits. Usage of one does not count against the limits of the other.

---

##  FAQ

### Does token counting use prompt caching?

---

##  Next steps

[

Count message tokens

Read the full API reference for the token counting endpoint.](api/messages-count-tokens.md)[Context windows

Use token counts to keep prompts within a model's context window.](build-with-claude/context-windows.md)[Rate limits

Check token counts before you send a request to stay within your usage tier.](api/rate-limits.md)[Prompt caching

Reduce cost and latency on repeated prompts by caching prompt prefixes.](build-with-claude/prompt-caching.md)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
