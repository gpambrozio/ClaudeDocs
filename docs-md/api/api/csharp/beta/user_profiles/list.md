# List User Profiles

Copy page

C#

# List User Profiles

[UserProfileListPageResponse](api/beta.md) Beta.UserProfiles.List(UserProfileListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/user\_profiles

List User Profiles

##### ParametersExpand Collapse

UserProfileListParams parameters

Int limit

Query param: Query parameter for limit

[Order](api/beta/user_profiles/list.md) order

Query param: Query parameter for order

"asc"Asc

"desc"Desc

string page

Query param: Query parameter for page

IReadOnlyList<[AnthropicBeta](api/beta.md)> betas

Header param: Optional header to specify the beta version(s) you want to use.

"message-batches-2024-09-24"MessageBatches2024\_09\_24

"prompt-caching-2024-07-31"PromptCaching2024\_07\_31

"computer-use-2024-10-22"ComputerUse2024\_10\_22

"computer-use-2025-01-24"ComputerUse2025\_01\_24

"pdfs-2024-09-25"Pdfs2024\_09\_25

"token-counting-2024-11-01"TokenCounting2024\_11\_01

"token-efficient-tools-2025-02-19"TokenEfficientTools2025\_02\_19

"output-128k-2025-02-19"Output128k2025\_02\_19

"files-api-2025-04-14"FilesApi2025\_04\_14

"mcp-client-2025-04-04"McpClient2025\_04\_04

"mcp-client-2025-11-20"McpClient2025\_11\_20

"dev-full-thinking-2025-05-14"DevFullThinking2025\_05\_14

"interleaved-thinking-2025-05-14"InterleavedThinking2025\_05\_14

"code-execution-2025-05-22"CodeExecution2025\_05\_22

"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025\_04\_11

"context-1m-2025-08-07"Context1m2025\_08\_07

"context-management-2025-06-27"ContextManagement2025\_06\_27

"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025\_08\_26

"skills-2025-10-02"Skills2025\_10\_02

"fast-mode-2026-02-01"FastMode2026\_02\_01

"output-300k-2026-03-24"Output300k2026\_03\_24

"user-profiles-2026-03-24"UserProfiles2026\_03\_24

##### ReturnsExpand Collapse

class UserProfileListPageResponse:

required IReadOnlyList<[BetaUserProfile](api/beta.md)> Data

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required IReadOnlyDictionary<string, string> Metadata

required IReadOnlyDictionary<string, [BetaUserProfileTrustGrant](api/beta.md)> TrustGrants

required string Status

required string Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

string? ExternalID

string? NextPage

List User Profiles

C#

```shiki
UserProfileListParams parameters = new();

var page = await client.Beta.UserProfiles.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

Response 200

```shiki
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "metadata": {
        "foo": "string"
      },
      "trust_grants": {
        "foo": {
          "status": "status"
        }
      },
      "type": "type",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "external_id": "external_id"
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200

```shiki
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "metadata": {
        "foo": "string"
      },
      "trust_grants": {
        "foo": {
          "status": "status"
        }
      },
      "type": "type",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "external_id": "external_id"
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
