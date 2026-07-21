# Claude API errors

Copy page



##  HTTP errors

The API follows a predictable HTTP error code format:

- 400 - `invalid_request_error`: There was an issue with the format or content of your request. This error type may also be used for other 4XX status codes not listed in this section.
- 401 - `authentication_error`: There's an issue with your API key (for example, it's malformed, revoked, or expired; see [Key expiration](manage-claude/authentication.md)). On Claude Platform on AWS, this can also indicate a problem with your AWS credentials or SigV4 signature.
- 402 - `billing_error`: There's an issue with your billing or payment information. Check your payment details in the [Claude Console](https://platform.claude.com), or in AWS Marketplace if you're using Claude Platform on AWS.
- 403 - `permission_error`: Your API key does not have permission to use the specified resource. Check your organization's access and workspace settings in the [Claude Console](https://platform.claude.com).
- 404 - `not_found_error`: The requested resource was not found. Check the endpoint path and any resource IDs in the request URL.
- 409 - `conflict_error`: The request conflicts with the current state of a resource. For example, the resource was modified concurrently, or a value that must be unique is already in use. Resolve the conflict, then retry the request.
- 413 - `request_too_large`: Request exceeds the maximum allowed number of bytes. See [Request size limits](#request-size-limits) for per-endpoint maximums.
- 429 - `rate_limit_error`: Your account has hit a rate limit.
- 500 - `api_error`: An unexpected error has occurred internal to Anthropic's systems. Retry the request with exponential backoff; if the error persists, contact support with the [request ID](#request-id).
- 504 - `timeout_error`: The request timed out while processing. Consider using the [streaming Messages API](build-with-claude/streaming.md) for long-running requests. See [Long requests](#long-requests) for more options.
- 529 - `overloaded_error`: The API is temporarily overloaded.

  

  529 errors can occur when the API experiences high traffic across all users.

  In rare cases, if your organization has a sharp increase in usage, you might see 429 errors because of acceleration limits on the API. To avoid hitting acceleration limits, ramp up your traffic gradually and maintain consistent usage patterns.

The official SDKs automatically retry transient failures (such as connection errors, rate limits, and 5xx server errors) with exponential backoff, twice by default, honoring the `retry-after` header when present. Each SDK client accepts a maximum-retries option to configure or disable this behavior.

When receiving a [streaming](build-with-claude/streaming.md) response over server-sent events (SSE), an error can occur after the API returns a 200 response. In that case, error handling doesn't follow these standard mechanisms. See [Error events](build-with-claude/streaming.md) for the shape of mid-stream errors.

##  Request size limits

The API enforces request size limits:

| Endpoint type | Maximum request size |
| --- | --- |
| Messages API | 32 MB |
| Token Counting API | 32 MB |
| [Batch API](build-with-claude/batch-processing.md) | 256 MB |
| [Files API](build-with-claude/files.md) | 500 MB |

If you exceed these limits, you'll receive a 413 `request_too_large` error. On the direct Claude API, Cloudflare returns this error before the request reaches the API servers.

##  Error shapes

The API always returns errors as JSON, with a top-level `error` object that always includes a `type` and `message` value. The response also includes a `request_id` field for easier tracking and debugging. For example:

JSON



```shiki
{
  "type": "error",
  "error": {
    "type": "not_found_error",
    "message": "The requested resource could not be found."
  },
  "request_id": "req_011CSHoEeqs5C35K2UUqR7Fy"
}
```

In accordance with the [versioning](api/versioning.md) policy, the values within these objects may expand, and it is possible that the `type` values will grow over time.

##  SDK error types

The official SDKs raise typed exceptions for these errors instead of returning raw JSON, and the class names and namespaces differ by language. For example, a 404 surfaces as `anthropic.NotFoundError` in Python, `Anthropic::Errors::NotFoundError` in Ruby, `com.anthropic.errors.NotFoundException` in Java, and as a single `*anthropic.Error` value (branch on `StatusCode`) in Go. Catch the SDK's typed classes rather than string-matching error messages, handling the most specific classes first. Each SDK page documents its full exception hierarchy:

- [Python](cli-sdks-libraries/sdks/python.md) · [TypeScript](cli-sdks-libraries/sdks/typescript.md) · [C#](cli-sdks-libraries/sdks/csharp.md) · [Go](cli-sdks-libraries/sdks/go.md) · [Java](cli-sdks-libraries/sdks/java.md) · [PHP](cli-sdks-libraries/sdks/php.md) · [Ruby](cli-sdks-libraries/sdks/ruby.md)

##  Request ID

Every API response includes a unique `request-id` header. This header contains a value such as `req_018EeWyXxfu5pfWkrYcMdjWG`. The same identifier appears as the `request_id` field in [error response bodies](#error-shapes). When contacting support about a specific request, include this ID to help quickly resolve your issue.

On [Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md), responses include two request IDs: the AWS request ID (`x-amzn-requestid`, primary, indexed in CloudTrail) and the Anthropic request ID (`request-id`, secondary). Use the AWS request ID for CloudTrail lookups and the Anthropic request ID for Anthropic support tickets.

The Python and TypeScript SDKs expose the request ID as a `_request_id` property on top-level response objects. The C#, Go, Java, and PHP SDKs expose it through their raw-response accessors, which also let you read any other response header. On Claude Platform on AWS, use the raw-response accessor to read the AWS request ID (`x-amzn-requestid`) as well:

cURLCLIPythonTypeScriptC#GoJavaPHPRubyPython (Claude Platform on AWS)TypeScript (Claude Platform on AWS)



```shiki
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(f"Request ID: {message._request_id}")
```

For Claude Platform on AWS request-ID examples in other languages, see [Request IDs](build-with-claude/claude-platform-on-aws.md).

##  Long requests



Consider using the [streaming Messages API](build-with-claude/streaming.md) or [Message Batches API](api/messages/batches/create.md) for long-running requests, especially those over 10 minutes.

Avoid setting a large `max_tokens` value without using the [streaming Messages API](build-with-claude/streaming.md)
or [Message Batches API](api/messages/batches/create.md):

- Some networks may drop idle connections after a variable period of time, which
  can cause the request to fail or time out without receiving a response from Anthropic.
- Networks differ in reliability. The [Message Batches API](api/messages/batches/create.md) can help you
  manage the risk of network issues by allowing you to poll for results rather than requiring an uninterrupted network connection.

If you are building a direct API integration, setting a [TCP socket keep-alive](https://tldp.org/HOWTO/TCP-Keepalive-HOWTO/programming.html) can reduce the impact of idle connection timeouts on some networks.

The [SDKs](cli-sdks-libraries/overview.md) validate that your non-streaming Messages API requests are not expected to exceed a 10-minute timeout. They also set a socket option for TCP keep-alive.

If you don't need to process events incrementally, the SDKs can consume the stream for you and return the complete `Message` object, identical to what a non-streaming call returns:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

with client.messages.stream(
    max_tokens=128000,
    messages=[{"role": "user", "content": "Write a detailed analysis..."}],
    model="claude-sonnet-5",
) as stream:
    message = stream.get_final_message()

print(message.content[0].text)
```

See [Streaming Messages](build-with-claude/streaming.md) for more details.

##  Common validation errors

###  Prefill not supported

Claude Fable 5, [Claude Mythos 5](https://anthropic.com/glasswing), [Claude Mythos Preview](https://anthropic.com/glasswing), Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6 do not support prefilling assistant messages. Sending a request with a prefilled last assistant message to any of these models returns a 400 `invalid_request_error`:

```shiki
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "Prefilling assistant messages is not supported for this model."
  }
}
```



Use [structured outputs](build-with-claude/structured-outputs.md) on models that support it, system prompt instructions, or [`output_config.format`](build-with-claude/structured-outputs.md) instead.

###  Thinking blocks cannot be modified

If the most recent assistant message contains `thinking` or `redacted_thinking` blocks that were edited, reordered, filtered out, or reconstructed before being sent back to the API, the request returns a 400 `invalid_request_error`. The error message starts with the position of the offending block (for example, `messages.1.content.0`) and contains:

```block
`thinking` or `redacted_thinking` blocks in the latest assistant message cannot be modified. These blocks must remain as they were in the original response.
```



With tool use, every `thinking` and `redacted_thinking` block from the assistant turn must be passed back exactly as received, including blocks whose `thinking` field is empty. Pass thinking blocks back unchanged, and if your application filters content blocks by type before resending, include both `thinking` and `redacted_thinking`. See [Preserving thinking blocks](build-with-claude/extended-thinking.md) and [Thinking output on Claude Fable 5 and Claude Mythos 5](build-with-claude/adaptive-thinking.md).

###  Outbound web identity federation disabled (Claude Platform on AWS)

If every request to [Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md) returns `"Outbound web identity federation is disabled for your account"`, run `aws iam enable-outbound-web-identity-federation` once per AWS account. See [Enable outbound web identity federation](build-with-claude/claude-platform-on-aws.md) for details.

##  Next steps

[

Trigger a routine through the API

Start a Claude Code routine session on demand by sending an authenticated POST request.](api/claude-code/routines-fire.md)[Rate limits

To mitigate misuse and manage capacity on the API, limits are in place on how much an organization can use the Claude API.](api/rate-limits.md)[

Streaming messages

Stream Messages API responses incrementally with server-sent events, including text, tool use, and extended thinking deltas.](build-with-claude/streaming.md)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
