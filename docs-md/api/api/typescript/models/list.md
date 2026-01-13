# List Models

Copy page

TypeScript

# List Models

client.models.list(ModelListParams { after\_id, before\_id, limit, betas } params?, RequestOptionsoptions?): Page<[ModelInfo](api/models.md) { id, created\_at, display\_name, type } >

get/v1/models

List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.

##### ParametersExpand Collapse

params: ModelListParams { after\_id, before\_id, limit, betas }

after\_id?: string

Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

before\_id?: string

Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

limit?: number

Query param: Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

maximum1000

minimum1

betas?: Array<[AnthropicBeta](api/beta.md)>

Header param: Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

(string & {})

"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 16 more

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

##### ReturnsExpand Collapse

ModelInfo { id, created\_at, display\_name, type }

id: string

Unique model identifier.

created\_at: string

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

formatdate-time

display\_name: string

A human-readable name for the model.

type: "model"

Object type.

For Models, this is always `"model"`.

Accepts one of the following:

"model"

List Models

TypeScript

```shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const modelInfo of client.models.list()) {
  console.log(modelInfo.id);
}
```

Response 200

```shiki
{
  "data": [
    {
      "id": "claude-sonnet-4-20250514",
      "created_at": "2025-02-19T00:00:00Z",
      "display_name": "Claude Sonnet 4",
      "type": "model"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

##### Returns Examples

Response 200

```shiki
{
  "data": [
    {
      "id": "claude-sonnet-4-20250514",
      "created_at": "2025-02-19T00:00:00Z",
      "display_name": "Claude Sonnet 4",
      "type": "model"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```