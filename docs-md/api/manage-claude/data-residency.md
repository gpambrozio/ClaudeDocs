# Check where inference actually ran

---
title: Data residency
url: https://platform.claude.com/docs/en/manage-claude/data-residency
description: Manage where model inference runs and where data is stored with geographic controls.
featureMetadata:
  status: ga
  zdr:
    eligibility: eligible
    note: Excludes [Covered Models](api-and-data-retention.md#model-specific-data-retention-requirements).
  supportedModels:
    - claude-fable-5-1
    - claude-mythos-5-1
    - claude-fable-5
    - claude-mythos-5
    - claude-mythos-preview
    - claude-opus-5-5
    - claude-opus-5
    - claude-sonnet-5-5
    - claude-sonnet-5
    - claude-haiku-5-5
    - claude-opus-4-8
    - claude-opus-4-7
    - claude-opus-4-6
    - claude-sonnet-4-6
  supportedPlatforms:
    Claude API: ga
    Claude Platform on AWS:
      availability: ga
      note: Workspace geo is not configurable; Managed Agents sessions there run with workspace geo "us".
    Claude Models on Google Cloud (Anthropic managed):
      availability: ga
      note: Workspace geo is not configurable.
---

**API support**: Usage differs by product.

* **Messages API**: Set `inference_geo` on each request, or set a default for the workspace.
* **Managed Agents**: Pin `inference_geo` in the agent’s model configuration; override it at session creation.

Data residency controls let you manage where your data is processed and stored. Two independent settings govern this:

* **Inference geo:** Controls where model inference runs, on a per-request basis. Set through the `inference_geo` API parameter or as a workspace default.
* **Workspace geo:** Controls where data is stored at rest and where endpoint processing (such as image transcoding and code execution) occurs. Configured at the workspace level in the [Claude Console](https://platform.claude.com/).

[Claude Managed Agents](../managed-agents/overview.md) supports geographic pinning at the agent level: `inference_geo` on an [agent’s model configuration](../managed-agents/agent-setup.md#pin-the-inference-geo) pins the geography that serves model requests for sessions running that agent, with [per-session overrides](../managed-agents/sessions.md#pin-the-inference-geo-for-a-session) at session create. Agents without a pin follow the workspace’s default inference geo on each request. Managed Agents also respects the Workspace geo configured in Console, and with [self-hosted sandboxes](../managed-agents/self-hosted-sandboxes.md), tool execution and the sandbox filesystem stay on infrastructure you control; the contents of attached [memory stores](../managed-agents/self-hosted-sandboxes-memory.md) remain stored by Anthropic and are copied to your sandbox for the session.

## Inference geo

The `inference_geo` parameter controls where model inference runs for a specific API request. Add it to any `POST /v1/messages` call.

| Value      | Description                                                                                     |
| ---------- | ----------------------------------------------------------------------------------------------- |
| `"global"` | Default. Inference may run in any available geography for optimal performance and availability. |
| `"us"`     | Inference runs only in US-based infrastructure.                                                 |

### API usage

```bash cURL
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-opus-5-5",
    "max_tokens": 1024,
    "inference_geo": "us",
    "messages": [{
      "role": "user",
      "content": "Summarize the key points of this document."
    }]
  }'
```

```bash CLI
ant messages create \
  --model claude-opus-5-5 \
  --max-tokens 1024 \
  --inference-geo us \
  --message '{role: user, content: "Summarize the key points of this document."}'
```

```python Python
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    inference_geo="us",
    messages=[
        {"role": "user", "content": "Summarize the key points of this document."}
    ],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
# Check where inference actually ran
print(f"Inference geo: {response.usage.inference_geo}")
```

```typescript TypeScript
const client = new Anthropic();

const response = await client.messages.create({
  model: "claude-opus-5-5",
  max_tokens: 1024,
  inference_geo: "us",
  messages: [
    {
      role: "user",
      content: "Summarize the key points of this document."
    }
  ]
});

const textBlock = response.content.find((block) => block.type === "text");
console.log(textBlock?.text);
// Check where inference actually ran
console.log(`Inference geo: ${response.usage.inference_geo}`);
```

```csharp C#
var client = new AnthropicClient();

var response = await client.Messages.Create(
    new MessageCreateParams
    {
        Model = Model.ClaudeOpus5_5,
        MaxTokens = 1024,
        InferenceGeo = "us",
        Messages =
        [
            new UserMessageParam { Content = "Summarize the key points of this document." },
        ],
    }
);

foreach (var block in response.Content)
{
    if (block.TryPickText(out var textBlock))
    {
        Console.WriteLine(textBlock.Text);
    }
}

// Check where inference actually ran
Console.WriteLine($"Inference geo: {response.Usage.InferenceGeo}");
```

```go Go
client := anthropic.NewClient()

message, err := client.Messages.New(context.Background(), anthropic.MessageNewParams{
	Model:        anthropic.ModelClaudeOpus5_5,
	MaxTokens:    1024,
	InferenceGeo: anthropic.String("us"),
	Messages: []anthropic.MessageParam{
		anthropic.NewUserMessage(anthropic.NewTextBlock("Summarize the key points of this document.")),
	},
})
if err != nil {
	log.Fatal(err)
}

for _, block := range message.Content {
	if textBlock, ok := block.AsAny().(anthropic.TextBlock); ok {
		fmt.Println(textBlock.Text)
	}
}
// Check where inference actually ran
fmt.Printf("Inference geo: %s\n", message.Usage.InferenceGeo)
```

```java Java
AnthropicClient client = AnthropicOkHttpClient.fromEnv();

Message response = client.messages().create(
    MessageCreateParams.builder()
        .model(Model.CLAUDE_OPUS_5_5)
        .maxTokens(1024L)
        .inferenceGeo("us")
        .addUserMessage("Summarize the key points of this document.")
        .build());

response.content().stream()
    .flatMap(block -> block.text().stream())
    .forEach(textBlock -> IO.println(textBlock.text()));
// Check where inference actually ran
IO.println("Inference geo: " + response.usage().inferenceGeo().get());
```

```php PHP
$client = new Client();

$response = $client->messages->create(
    model: 'claude-opus-5-5',
    maxTokens: 1024,
    inferenceGeo: 'us',
    messages: [
        ['role' => 'user', 'content' => 'Summarize the key points of this document.'],
    ],
);

foreach ($response->content as $block) {
    if ($block->type === 'text') {
        echo $block->text, PHP_EOL;
    }
}
// Check where inference actually ran
echo "Inference geo: {$response->usage->inferenceGeo}\n";
```

```ruby Ruby
client = Anthropic::Client.new

response = client.messages.create(
  model: Anthropic::Model::CLAUDE_OPUS_5_5,
  max_tokens: 1024,
  inference_geo: "us",
  messages: [
    {role: "user", content: "Summarize the key points of this document."}
  ]
)

response.content.each do |block|
  puts block.text if block.type == :text
end
# Check where inference actually ran
puts "Inference geo: #{response.usage.inference_geo}"
```

### Response

The response `usage` object includes an `inference_geo` field indicating where inference ran:

```json Output
{
  "usage": {
    "input_tokens": 25,
    "output_tokens": 150,
    "inference_geo": "us"
  }
}
```

### Model availability

The `inference_geo` parameter is supported on Claude 4.6 and later models. Requests with `inference_geo` on Claude Opus 4.5, Claude Sonnet 4.5 (deprecated), Claude Haiku 4.5, or earlier models return a 400 error.

The `inference_geo` parameter is available on the Claude API (first-party), [Claude Platform on AWS](../build-with-claude/claude-platform-on-aws.md), and [Claude Models on Google Cloud (Anthropic managed)](../build-with-claude/claude-models-on-google-cloud/anthropic-managed.md). On Amazon Bedrock and Claude Models on Google Cloud (Google managed), the inference region is determined by the endpoint URL or inference profile, so `inference_geo` is not applicable. On [Claude in Microsoft Foundry](../build-with-claude/claude-in-microsoft-foundry.md), `inference_geo` is likewise not applicable: deployments hosted on Azure can instead use the US Data Zone Standard deployment type, which keeps inference within the United States. The `inference_geo` parameter is also not available through the [OpenAI SDK compatibility endpoint](../cli-sdks-libraries/libraries/openai-sdk.md).

### Workspace-level restrictions

Workspace settings also support restricting which inference geos are available:

* **`allowed_inference_geos`:** Restricts which geos a workspace can use. If a request specifies an `inference_geo` not in this list, the API returns an error.
* **`default_inference_geo`:** Sets the fallback geo when `inference_geo` is omitted from a request. Individual requests can override this by setting `inference_geo` explicitly.

These settings can be configured through the Console or the [Admin API](admin-api.md) under the `data_residency` field.

**Claude Models on Google Cloud (Anthropic managed):** Every workspace allows all inference geos and uses `"global"` as its default inference geo. The Claude Console shows both settings as read-only. For US-only inference, set `inference_geo: "us"` on each request.

## Workspace geo

Workspace geo is set when you create a workspace and can’t be changed afterward. Currently, `"us"` is the only available workspace geo.

To set workspace geo, create a new workspace in the [Console](https://platform.claude.com/):

1. Go to [Workspaces in the Claude Console](https://platform.claude.com/settings/workspaces) (`platform.claude.com/settings/workspaces`).
2. Click **Create workspace** to open the [Create workspace](https://platform.claude.com/settings/workspaces/new) page (`platform.claude.com/settings/workspaces/new`) in the Console.
3. Enter a name, confirm the value in the **Workspace geo** field, and click **Create workspace**.

**Claude Platform on AWS:** Workspace geo is not configurable. Claude Managed Agents sessions on this platform run with an effective Workspace geo of `"us"`, which is currently the only available workspace geo. See [Claude Platform on AWS](../build-with-claude/claude-platform-on-aws.md) for data residency considerations specific to that platform.

**Claude Models on Google Cloud (Anthropic managed):** Workspace geo is not configurable. Every workspace uses `"us"` as its workspace geo, and the **Workspace geo** field doesn’t appear in the Claude Console.

## Pricing

Data residency pricing varies by model generation:

* **Claude 4.6 and later models:** US-only inference (`inference_geo: "us"`) is priced at 1.1x the standard rate across all token pricing categories (input tokens, output tokens, cache writes, and cache reads). On Claude Haiku 5.5, the multiplier also applies to the higher prices for prompts over 100,000 tokens (see [Long context pricing](../about-claude/pricing.md#long-context-pricing)).
* **Global routing (`inference_geo: "global"`):** Standard pricing applies.
* **Older models:** Don’t support `inference_geo` (see [Model availability](data-residency.md#model-availability)). Standard pricing applies. Requests that include the parameter return a 400 error.

This pricing applies to the Claude API (first-party), Claude Platform on AWS, and Claude Models on Google Cloud (Anthropic managed). On Claude in Microsoft Foundry, the same 1.1x multiplier applies to deployments hosted on Azure that use the US Data Zone Standard deployment type. Partner-operated platforms, Bedrock and Claude Models on Google Cloud (Google managed), have their own regional pricing. See [Data residency pricing](../about-claude/pricing.md#data-residency-pricing) for details.

The same multiplier applies to [Claude Managed Agents](../managed-agents/overview.md): when an agent’s [model configuration](../managed-agents/agent-setup.md) pins `inference_geo` to `"us"`, model requests in sessions running that agent are priced at 1.1x the standard rate.

If you have a [Priority Tier](../api/service-tiers.md) commitment, the 1.1x multiplier for US-only inference also affects how tokens are counted against your Priority Tier capacity. Each token consumed with `inference_geo: "us"` draws down 1.1 tokens from your committed TPM, consistent with how other pricing multipliers (such as prompt caching) affect burndown rates.

## Batch API support

The `inference_geo` parameter is supported on the [Batch API](../build-with-claude/batch-processing.md). Each request in a batch can specify its own `inference_geo` value.

## Migration from legacy opt-outs

If your organization previously opted out of global routing to keep inference in the US, your workspace has been automatically configured with `allowed_inference_geos: ["us"]` and `default_inference_geo: "us"`. No code changes are needed. Your existing data residency requirements continue to be enforced through the new geo controls.

### What changed

The legacy opt-out was an organization-level setting that restricted all requests to US-based infrastructure. The new data residency controls replace this with two mechanisms:

* **Per-request control:** The `inference_geo` parameter lets you specify `"us"` or `"global"` on each API call, giving you request-level flexibility.
* **Workspace controls:** The `default_inference_geo` and `allowed_inference_geos` settings in the Console let you enforce geo policies across all keys in a workspace.

### What happened to your workspace

Your workspace was migrated automatically:

| Legacy setting                   | New equivalent                                                  |
| -------------------------------- | --------------------------------------------------------------- |
| Global routing opt-out (US only) | `allowed_inference_geos: ["us"]`, `default_inference_geo: "us"` |

All API requests using keys from your workspace continue to run on US-based infrastructure. No action is needed to maintain your current behavior.

### If you want to use global routing

If your data residency requirements have changed and you want to take advantage of global routing for better performance and availability, update your workspace’s inference geo settings to include `"global"` in the allowed geos and set `default_inference_geo` to `"global"`. See [Workspace-level restrictions](data-residency.md#workspace-level-restrictions) for details.

### Pricing impact

Legacy models are unaffected by this migration. For current pricing on newer models, see [Pricing](data-residency.md#pricing).

## Current limitations

* **Shared rate limits:** Rate limits are shared across all geos.
* **Inference geo:** Only `"us"` and `"global"` are available.
* **Workspace geo:** Only `"us"` is currently available. Workspace geo can’t be changed after workspace creation.

## Next steps

**Data residency pricing**

View data residency pricing details.

**Workspaces**

Learn about workspace configuration.

**Usage and Cost Analytics API**

Track usage and costs by inference geo.

## Availability

Data residency is available on select models and eligible for zero data retention and HIPAA readiness.

### API support

#### [Messages API](../build-with-claude/working-with-messages.md)

* Availability: Available
* Usage: Set `inference_geo` on each request, or set a default for the workspace.

| Status                | Cloud platforms                                                                                                                                            | Models                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Available             | Claude API                                                                                                                                                 | [Claude Fable 5.1](../models/fable-5-1/overview.md), [Claude Mythos 5.1](../models/mythos-5-1/overview.md), [Claude Fable 5](../models/fable-5/overview.md), [Claude Mythos 5](../models/mythos-5/overview.md), Claude Mythos Preview, [Claude Opus 5.5](../models/opus-5-5/overview.md), [Claude Opus 5](../models/opus-5/overview.md), [Claude Sonnet 5.5](../models/sonnet-5-5/overview.md), [Claude Sonnet 5](../models/sonnet-5/overview.md), [Claude Haiku 5.5](../models/haiku-5-5/overview.md), [Claude Opus 4.8](../models/opus-4-8/overview.md), [Claude Opus 4.7](../models/opus-4-7/overview.md), [Claude Opus 4.6](../models/opus-4-6/overview.md), [Claude Sonnet 4.6](../models/sonnet-4-6/overview.md) |
| Available<sup>1</sup> | [Claude Platform on AWS](../build-with-claude/claude-platform-on-aws.md)                                                     | [Claude Fable 5.1](../models/fable-5-1/overview.md), [Claude Fable 5](../models/fable-5/overview.md), [Claude Opus 5.5](../models/opus-5-5/overview.md), [Claude Opus 5](../models/opus-5/overview.md), [Claude Sonnet 5.5](../models/sonnet-5-5/overview.md), [Claude Sonnet 5](../models/sonnet-5/overview.md), [Claude Haiku 5.5](../models/haiku-5-5/overview.md), [Claude Opus 4.8](../models/opus-4-8/overview.md), [Claude Opus 4.7](../models/opus-4-7/overview.md), [Claude Opus 4.6](../models/opus-4-6/overview.md), [Claude Sonnet 4.6](../models/sonnet-4-6/overview.md)                                                                                                                                                                                              |
| Available<sup>1</sup> | [Claude Models on Google Cloud (Anthropic managed)](../build-with-claude/claude-models-on-google-cloud/anthropic-managed.md) | [Claude Fable 5.1](../models/fable-5-1/overview.md), [Claude Fable 5](../models/fable-5/overview.md), [Claude Opus 5.5](../models/opus-5-5/overview.md), [Claude Opus 5](../models/opus-5/overview.md), [Claude Sonnet 5.5](../models/sonnet-5-5/overview.md), [Claude Sonnet 5](../models/sonnet-5/overview.md), [Claude Haiku 5.5](../models/haiku-5-5/overview.md), [Claude Opus 4.8](../models/opus-4-8/overview.md), [Claude Opus 4.7](../models/opus-4-7/overview.md), [Claude Opus 4.6](../models/opus-4-6/overview.md), [Claude Sonnet 4.6](../models/sonnet-4-6/overview.md)                                                                                                                                                                                              |

1. Workspace geo is not configurable.

#### [Managed Agents](../managed-agents/overview.md)

* Availability: Available
* Usage: Pin `inference_geo` in the agent’s model configuration, and override it per session at session creation. An agent with no pin follows the workspace default.

| Status                | Cloud platforms                                                                                        | Models                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Available             | Claude API                                                                                             | [Claude Fable 5.1](../models/fable-5-1/overview.md), [Claude Mythos 5.1](../models/mythos-5-1/overview.md), [Claude Fable 5](../models/fable-5/overview.md), [Claude Mythos 5](../models/mythos-5/overview.md), Claude Mythos Preview, [Claude Opus 5.5](../models/opus-5-5/overview.md), [Claude Opus 5](../models/opus-5/overview.md), [Claude Sonnet 5.5](../models/sonnet-5-5/overview.md), [Claude Sonnet 5](../models/sonnet-5/overview.md), [Claude Haiku 5.5](../models/haiku-5-5/overview.md), [Claude Opus 4.8](../models/opus-4-8/overview.md), [Claude Opus 4.7](../models/opus-4-7/overview.md), [Claude Opus 4.6](../models/opus-4-6/overview.md), [Claude Sonnet 4.6](../models/sonnet-4-6/overview.md) |
| Available<sup>1</sup> | [Claude Platform on AWS](../build-with-claude/claude-platform-on-aws.md) | [Claude Fable 5.1](../models/fable-5-1/overview.md), [Claude Fable 5](../models/fable-5/overview.md), [Claude Opus 5.5](../models/opus-5-5/overview.md), [Claude Opus 5](../models/opus-5/overview.md), [Claude Sonnet 5.5](../models/sonnet-5-5/overview.md), [Claude Sonnet 5](../models/sonnet-5/overview.md), [Claude Haiku 5.5](../models/haiku-5-5/overview.md), [Claude Opus 4.8](../models/opus-4-8/overview.md), [Claude Opus 4.7](../models/opus-4-7/overview.md), [Claude Opus 4.6](../models/opus-4-6/overview.md), [Claude Sonnet 4.6](../models/sonnet-4-6/overview.md)                                                                                                                                                                                              |

1. Workspace geo is not configurable; Managed Agents sessions there run with workspace geo “us”.

### Data handling

[Data handling overview](api-and-data-retention.md#feature-eligibility)

| Item   | Zero data retention                                                                                                                                       | HIPAA    |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Status | Eligible (excludes [Covered Models](api-and-data-retention.md#model-specific-data-retention-requirements)) | Eligible |

Applicable endpoints:

* `/v1/messages` with `inference_geo`

---

*Copyright © Anthropic. All rights reserved.*
