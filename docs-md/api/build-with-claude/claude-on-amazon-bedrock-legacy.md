# Claude on Amazon Bedrock (legacy)

Copy page





This page covers the legacy Amazon Bedrock integration: the `InvokeModel` and `Converse` APIs with ARN-versioned model identifiers and AWS event-stream encoding. For models available on the Messages-API Bedrock endpoint, see [Claude in Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md), which uses the Messages API at `/anthropic/v1/messages` with SSE streaming. For an Anthropic-operated alternative with AWS Marketplace billing and typically same-day feature access, see [Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md). Existing Bedrock users can follow the [migration guide](build-with-claude/claude-platform-on-aws.md).

Calling Claude through Bedrock slightly differs from how you would call Claude on the Claude API directly. This guide walks you through completing an API call to Claude on Bedrock using one of Anthropic's [client SDKs](cli-sdks-libraries/overview.md).

Note that this guide assumes you have already signed up for an [AWS account](https://portal.aws.amazon.com/billing/signup) and configured programmatic access.

##  Install and configure the AWS CLI

1. [Install a version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) at or newer than version `2.13.23`
2. Configure your AWS credentials using the AWS configure command (see [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)) or find your credentials by navigating to "Command line or programmatic access" within your AWS dashboard and following the directions in the popup modal.
3. Verify that your credentials are working:

AWS CLI



```shiki
aws sts get-caller-identity
```

##  Install an SDK for accessing Bedrock

Anthropic's [client SDKs](cli-sdks-libraries/overview.md) support Bedrock. You can also use an AWS SDK like `boto3` directly.

Python

Python

TypeScript

TypeScript

C#

C#

Go

Go

Java

Java

PHP

PHP

Ruby

Ruby

Boto3 (Python)

Boto3 (Python)

```shiki
pip install -U "anthropic[bedrock]"
```



##  Accessing Bedrock

###  Subscribe to Anthropic models

Go to the [AWS Console > Bedrock > Model Access](https://console.aws.amazon.com/bedrock/home?region=us-west-2#/modelaccess) and request access to Anthropic models. Note that Anthropic model availability varies by region. See [AWS documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) for latest information.

####  API model IDs



Claude Fable 5, Claude Opus 4.8, and Claude Opus 4.7 are reachable through `InvokeModel` on `bedrock-runtime`.
These requests are served by the same infrastructure as the
[Claude in Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md)
endpoint. For the native Messages API request shape and full feature
parity, use that page. Claude Fable 5, Claude Opus 4.8, and Claude Opus 4.7 are omitted from the model
table on this page because they do not have ARN-versioned model IDs.

Claude Sonnet 5 is not available on this surface; use [Claude in Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md) or [Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md).

Lifecycle terms (Deprecated, Retired) are defined in [Model deprecations](about-claude/model-deprecations.md). Lifecycle dates on partner-operated platforms are set by the partner and can differ from the Claude API schedule. For the current retirement date of any model on Amazon Bedrock, see [Amazon Bedrock's model lifecycle page](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html).

| Model | Base Bedrock model ID | `global` | `us` | `eu` | `jp` | `apac` |
| --- | --- | --- | --- | --- | --- | --- |
| Claude Opus 4.6 | anthropic.claude-opus-4-6-v1 | Yes | Yes | Yes | Yes | Yes |
| Claude Sonnet 4.6 | anthropic.claude-sonnet-4-6 | Yes | Yes | Yes | Yes | No |
| Claude Sonnet 4.5 | anthropic.claude-sonnet-4-5-20250929-v1:0 | Yes | Yes | Yes | Yes | No |
| Claude Sonnet 4  Deprecated. | anthropic.claude-sonnet-4-20250514-v1:0 | Yes | Yes | Yes | No | Yes |
| Claude Sonnet 3.7  Retired. | anthropic.claude-3-7-sonnet-20250219-v1:0 | No | No | No | No | No |
| Claude Opus 4.5 | anthropic.claude-opus-4-5-20251101-v1:0 | Yes | Yes | Yes | No | No |
| Claude Opus 4.1  Deprecated. | anthropic.claude-opus-4-1-20250805-v1:0 | No | Yes | No | No | No |
| Claude Opus 4  Retired. | anthropic.claude-opus-4-20250514-v1:0 | No | No | No | No | No |
| Claude Haiku 4.5 | anthropic.claude-haiku-4-5-20251001-v1:0 | Yes | Yes | Yes | No | No |
| Claude Haiku 3.5  Deprecated. | anthropic.claude-3-5-haiku-20241022-v1:0 | No | Yes | No | No | No |

For more information about regional vs global model IDs, see the [Global vs regional endpoints](#global-vs-regional-endpoints) section.

###  List available models

The following examples show how to print a list of all the Claude models available through Bedrock:

AWS CLIBoto3 (Python)TypeScriptC#GoJavaPHPRuby



```shiki
import boto3

bedrock = boto3.client(service_name="bedrock")
response = bedrock.list_foundation_models(byProvider="anthropic")

for summary in response["modelSummaries"]:
    print(summary["modelId"])
```

###  Making requests

The following examples show how to generate text from Claude on Bedrock:

CLIPythonTypeScriptC#GoJavaPHPRubyBoto3 (Python)



```shiki
from anthropic import AnthropicBedrock

client = AnthropicBedrock(
    # Authenticate by either providing the keys below or use the default AWS credential providers, such as
    # using ~/.aws/credentials or the "AWS_SECRET_ACCESS_KEY" and "AWS_ACCESS_KEY_ID" environment variables.
    aws_access_key="<access key>",
    aws_secret_key="<secret key>",
    # Temporary credentials can be used with aws_session_token.
    # Read more at https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html.
    aws_session_token="<session_token>",
    # aws_region changes the aws region to which the request is made. By default, the SDK reads AWS_REGION,
    # and if that's not present, defaults to us-east-1. Note that the SDK does not read ~/.aws/config for the region.
    aws_region="us-west-2",
)

message = client.messages.create(
    model="global.anthropic.claude-opus-4-6-v1",
    max_tokens=256,
    messages=[{"role": "user", "content": "Hello, world"}],
)
print(message.content)
```

See the [client SDKs](cli-sdks-libraries/overview.md) for more details, and the [official Bedrock documentation](https://docs.aws.amazon.com/bedrock/).

###  Bearer token authentication

You can authenticate with Bedrock using bearer tokens instead of AWS credentials. This is useful in corporate environments where teams need access to Bedrock without managing AWS credentials, IAM roles, or account-level permissions.

The simplest approach is to set the `AWS_BEARER_TOKEN_BEDROCK` environment variable, which each SDK detects automatically when resolving credentials from the environment.

To provide a token programmatically:

PythonTypeScriptC#GoJavaPHPRuby



```shiki
from anthropic import AnthropicBedrock

client = AnthropicBedrock(
    api_key="your-bearer-token",
    aws_region="us-west-2",
)

message = client.messages.create(
    model="us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}],
)
print(message.content)
```

##  Activity logging

Bedrock provides an [invocation logging service](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) that allows customers to log the prompts and completions associated with your usage.

Anthropic recommends that you log your activity on at least a 30-day rolling basis to understand your activity and investigate any potential misuse.



Turning on this service does not give AWS or Anthropic any access to your content.

##  Feature support

For the full feature list with Amazon Bedrock availability, see [Features overview](build-with-claude/overview.md).

###  Supported feature highlights

- [Messages API](api/messages/create.md)
- [Prompt caching](build-with-claude/prompt-caching.md)
- [Extended thinking](build-with-claude/extended-thinking.md)
- [Tool use](agents-and-tools/tool-use/overview.md), including the [Bash tool](agents-and-tools/tool-use/bash-tool.md), [Computer use tool](agents-and-tools/tool-use/computer-use-tool.md), [Memory tool](agents-and-tools/tool-use/memory-tool.md), and [Text editor tool](agents-and-tools/tool-use/text-editor-tool.md)
- [Citations](build-with-claude/citations.md)
- [Structured outputs](build-with-claude/structured-outputs.md)

###  Features not supported

- Input sources (URL sources for images and documents, Files API)
- Server-side tools (code execution, web search, web fetch, advisor)
- Agent infrastructure (Agent Skills, MCP connector, programmatic tool calling)
- API endpoints (Message Batches, Models, Admin, Compliance, Usage and Cost)
- Claude Managed Agents
- Server-side fallback (the [`fallbacks` parameter](build-with-claude/refusals-and-fallback.md); use the [client-side fallback pattern](build-with-claude/refusals-and-fallback.md) instead)

###  PDF support on Bedrock

PDF support is available on Bedrock through both the Converse API and InvokeModel API. For detailed information about PDF processing capabilities and limitations, see [Amazon Bedrock PDF support](build-with-claude/pdf-support.md).

**Important considerations for Converse API users:**

- Visual PDF analysis (charts, images, layouts) requires citations to be enabled
- Without citations, only basic text extraction is available
- For full control without forced citations, use the InvokeModel API

###  Context window

Claude Fable 5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6 have a [1M-token context window](build-with-claude/context-windows.md) on Amazon Bedrock. Other Claude models, including Sonnet 4.5 and Sonnet 4 (deprecated), have a 200k-token context window.

Bedrock limits request payloads to 20 MB. When sending large documents or many images, you may reach this limit before the token limit.

##  Global vs regional endpoints

Starting with **Claude Sonnet 4.5 and all future models**, Bedrock offers two endpoint types:

- **Global endpoints:** Dynamic routing for maximum availability
- **Regional endpoints:** Guaranteed data routing through specific geographic regions

Regional endpoints include a 10% pricing premium over global endpoints.



This applies to Claude Sonnet 4.5 and future models only. Older models (Claude Sonnet 4 (deprecated) and earlier) maintain their existing pricing structures.

###  When to use each option

**Global endpoints (recommended):**

- Provide maximum availability and uptime
- Dynamically route requests to regions with available capacity
- No pricing premium
- Best for applications where data residency is flexible

**Regional endpoints (CRIS):**

- Route traffic through specific geographic regions
- Required for data residency and compliance requirements
- Available for US, EU, Japan, and Asia-Pacific
- 10% pricing premium reflects infrastructure costs for dedicated regional capacity

###  Implementation

**Using global endpoints (default for Opus 4.6, Sonnet 4.6, and Sonnet 4.5):**

The model IDs for Claude Opus 4.6, Sonnet 4.6, and Sonnet 4.5 already include the `global.` prefix:

CLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
from anthropic import AnthropicBedrock

client = AnthropicBedrock(aws_region="us-west-2")

message = client.messages.create(
    model="global.anthropic.claude-opus-4-6-v1",
    max_tokens=256,
    messages=[{"role": "user", "content": "Hello, world"}],
)
```

**Using regional endpoints (CRIS):**

To use regional endpoints, replace the `global.` prefix with a regional prefix such as `us.`:

CLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
from anthropic import AnthropicBedrock

client = AnthropicBedrock(aws_region="us-west-2")

# Using US regional endpoint (CRIS)
message = client.messages.create(
    model="us.anthropic.claude-opus-4-6-v1",  # Regional prefix
    max_tokens=256,
    messages=[{"role": "user", "content": "Hello, world"}],
)
```



**Claude Mythos Preview** is a research preview model available to invited customers on Amazon Bedrock. For more information, see [Project Glasswing](https://anthropic.com/glasswing).

##  Additional resources

- **Bedrock pricing:** [aws.amazon.com/bedrock/pricing](https://aws.amazon.com/bedrock/pricing/)
- **AWS pricing documentation:** [Bedrock pricing guide](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-pricing.html)
- **AWS blog post:** [Introducing Claude Sonnet 4.5 in Amazon Bedrock](https://aws.amazon.com/blogs/aws/introducing-claude-sonnet-4-5-in-amazon-bedrock-anthropics-most-intelligent-model-best-for-coding-and-complex-agents/)
- **Anthropic pricing details:** [Cloud platform pricing](about-claude/pricing.md)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
