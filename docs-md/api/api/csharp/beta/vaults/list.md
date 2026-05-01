# List Vaults

Copy page

C#

# List Vaults

[VaultListPageResponse](api/beta.md) Beta.Vaults.List(VaultListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/vaults

List Vaults

##### ParametersExpand Collapse

VaultListParams parameters

Boolean includeArchived

Query param: Whether to include archived vaults in the results.

Int limit

Query param: Maximum number of vaults to return per page. Defaults to 20, maximum 100.

string page

Query param: Opaque pagination token from a previous `list_vaults` response.

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

"advisor-tool-2026-03-01"AdvisorTool2026\_03\_01

##### ReturnsExpand Collapse

class VaultListPageResponse:

Response containing a paginated list of vaults.

IReadOnlyList<[BetaManagedAgentsVault](api/beta.md)> Data

List of vaults.

required string ID

Unique identifier for the vault.

required DateTimeOffset? ArchivedAt

A timestamp in RFC 3339 format

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string DisplayName

Human-readable name for the vault.

required IReadOnlyDictionary<string, string> Metadata

Arbitrary key-value metadata attached to the vault.

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

string? NextPage

Pagination token for the next page, or null if no more results.

List Vaults

C#

```shiki
VaultListParams parameters = new();

var page = await client.Beta.Vaults.List(parameters);
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
      "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "display_name": "Example vault",
      "metadata": {
        "environment": "production"
      },
      "type": "vault",
      "updated_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200

```shiki
{
  "data": [
    {
      "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "display_name": "Example vault",
      "metadata": {
        "environment": "production"
      },
      "type": "vault",
      "updated_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
