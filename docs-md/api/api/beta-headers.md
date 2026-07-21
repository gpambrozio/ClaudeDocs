# Beta headers

Copy page



Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API.



Each [client SDK](cli-sdks-libraries/overview.md) exposes a `beta` namespace for calling the API with beta features enabled.

##  How to use beta headers

To access beta features, include the `anthropic-beta` header in your API requests:

```shiki
POST /v1/messages
x-api-key: YOUR_API_KEY
anthropic-version: 2023-06-01
anthropic-beta: BETA_FEATURE_NAME
content-type: application/json
```



Each feature's documentation states the exact beta name to send. The [API overview](api/overview.md) lists the APIs currently in beta.

The following examples show the same request with cURL, the `ant` CLI, and the SDKs. The SDKs take beta names in the `betas` parameter and send the `anthropic-beta` header for you:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    betas=["files-api-2025-04-14"],
)

print(response.content)
```



Beta features are experimental and may:

- Have breaking changes with notice
- Be deprecated or removed
- Have different rate limits or pricing
- Not be available in all regions

###  Multiple beta features

To use multiple beta features in a single request, include all feature names in the header separated by commas:

```shiki
anthropic-beta: feature1,feature2,feature3
```



When using an SDK, list each feature in the `betas` parameter (for example, `betas=["feature1", "feature2"]`). With the CLI, pass a single `--beta` flag with the feature names separated by commas (for example, `--beta feature1,feature2`). Avoid repeating the flag: currently only the first flag's value takes effect.

###  Endpoint-specific headers

Some beta APIs are scoped to specific endpoints and require a feature-specific beta header on every request:

| Endpoints | Beta header |
| --- | --- |
| `/v1/agents`, `/v1/sessions`, `/v1/environments` | `managed-agents-2026-04-01` |
| `/v1/tunnels` | `mcp-tunnels-2026-06-22` |
| `/v1/memory_stores` and sub-resources | `agent-memory-2026-07-22` |

The SDKs' `beta` namespaces add these headers automatically. Add them yourself only when making raw HTTP requests. See the [Managed Agents overview](managed-agents/overview.md), [Using agent memory](managed-agents/memory.md), and the [MCP tunnels reference](agents-and-tools/mcp-tunnels/reference.md) for details.

Endpoint-specific headers that apply to the same endpoint aren't always combinable. On memory store endpoints, `agent-memory-2026-07-22` replaces `managed-agents-2026-04-01`: sending both on the same request returns a `400` error. The client SDKs send the correct header for each endpoint automatically.

###  Version naming conventions

Beta feature names typically follow the pattern `feature-name-YYYY-MM-DD`, where the date indicates when the beta was released. Always use the exact beta feature name as documented.

##  Error handling

If you use an invalid beta name, or a beta your organization doesn't have access to, you'll receive a `400` error response:

Output



```shiki
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "Unexpected value(s) `invalid-beta-name` for the `anthropic-beta` header. Please consult our documentation at platform.claude.com/docs or try again without the header."
  },
  "request_id": "req_011CcnGfC9fELffo2EALu4Wd"
}
```

##  Getting help

For updates to beta features, see the [release notes](release-notes/overview.md). For help with production issues, contact [support](https://support.claude.com/).

##  Next steps

[

Errors

Understand the HTTP status codes, error response shape, and request IDs the Claude API returns, and handle errors with the SDKs' typed exceptions.](api/errors.md)[API overview

Explore the Claude API's features, including the APIs currently in beta.](api/overview.md)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
