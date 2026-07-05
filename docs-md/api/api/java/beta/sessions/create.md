# Create Session

Copy page



Java

# Create Session

[BetaManagedAgentsSession](api/beta/sessions.md) beta().sessions().create(SessionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions

Create Session

##### ParametersExpand Collapse



SessionCreateParams params



Optional<List<AnthropicBeta>> betas

Optional header to specify the beta version(s) you want to use.

MESSAGE\_BATCHES\_2024\_09\_24("message-batches-2024-09-24")

PROMPT\_CACHING\_2024\_07\_31("prompt-caching-2024-07-31")

COMPUTER\_USE\_2024\_10\_22("computer-use-2024-10-22")

COMPUTER\_USE\_2025\_01\_24("computer-use-2025-01-24")

PDFS\_2024\_09\_25("pdfs-2024-09-25")

TOKEN\_COUNTING\_2024\_11\_01("token-counting-2024-11-01")

TOKEN\_EFFICIENT\_TOOLS\_2025\_02\_19("token-efficient-tools-2025-02-19")

OUTPUT\_128K\_2025\_02\_19("output-128k-2025-02-19")

FILES\_API\_2025\_04\_14("files-api-2025-04-14")

MCP\_CLIENT\_2025\_04\_04("mcp-client-2025-04-04")

MCP\_CLIENT\_2025\_11\_20("mcp-client-2025-11-20")

DEV\_FULL\_THINKING\_2025\_05\_14("dev-full-thinking-2025-05-14")

INTERLEAVED\_THINKING\_2025\_05\_14("interleaved-thinking-2025-05-14")

CODE\_EXECUTION\_2025\_05\_22("code-execution-2025-05-22")

EXTENDED\_CACHE\_TTL\_2025\_04\_11("extended-cache-ttl-2025-04-11")

CONTEXT\_1M\_2025\_08\_07("context-1m-2025-08-07")

CONTEXT\_MANAGEMENT\_2025\_06\_27("context-management-2025-06-27")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED\_2025\_08\_26("model-context-window-exceeded-2025-08-26")

SKILLS\_2025\_10\_02("skills-2025-10-02")

FAST\_MODE\_2026\_02\_01("fast-mode-2026-02-01")

OUTPUT\_300K\_2026\_03\_24("output-300k-2026-03-24")

USER\_PROFILES\_2026\_03\_24("user-profiles-2026-03-24")

ADVISOR\_TOOL\_2026\_03\_01("advisor-tool-2026-03-01")

MANAGED\_AGENTS\_2026\_04\_01("managed-agents-2026-04-01")

CACHE\_DIAGNOSIS\_2026\_04\_07("cache-diagnosis-2026-04-07")

THINKING\_TOKEN\_COUNT\_2026\_05\_13("thinking-token-count-2026-05-13")

SERVER\_SIDE\_FALLBACK\_2026\_06\_01("server-side-fallback-2026-06-01")

FALLBACK\_CREDIT\_2026\_06\_01("fallback-credit-2026-06-01")



Agent agent

Agent identifier. Accepts the `agent` ID string, which pins the latest version for the session, or an `agent` object with both id and version specified.

String



class BetaManagedAgentsAgentParams:

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

String id

The `agent` ID.

Type type

Optional<Long> version

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



class BetaManagedAgentsAgentWithOverridesParams:

Reference to an `agent` plus optional configuration overrides. Each provided field replaces the agent's value for the caller's use; the agent resource is unchanged.

String id

The `agent` ID.

Type type



Optional<List<[BetaManagedAgentsUrlMcpServerParams](api/beta/agents.md)>> mcpServers

Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

String name

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

Type type

String url

Endpoint URL for the MCP server.



Optional<Model> model

Replacement model. Accepts the model string, e.g. `claude-opus-4-6`, or a `model_config` object. Omit to use the agent's model.

One of the following:



enum BetaManagedAgentsModel:

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



class BetaManagedAgentsModelConfigParams:

An object that defines additional configuration control over model use



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")



Optional<List<[BetaManagedAgentsSkillParams](api/beta/agents.md)>> skills

Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

One of the following:



class BetaManagedAgentsAnthropicSkillParams:

An Anthropic-managed skill.

String skillId

Identifier of the Anthropic skill (e.g., "xlsx").

Type type

Optional<String> version

Version to pin. Defaults to latest if omitted.



class BetaManagedAgentsCustomSkillParams:

A user-created custom skill.

String skillId

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

Type type

Optional<String> version

Version to pin. Defaults to latest if omitted.

Optional<String> system

Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.



Optional<List<Tool>> tools

Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

One of the following:



class BetaManagedAgentsAgentToolset20260401Params:

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

Type type



Optional<List<[BetaManagedAgentsAgentToolConfigParams](api/beta/agents.md)>> configs

Per-tool configuration overrides.



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")

Optional<Boolean> enabled

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.



Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



Optional<[BetaManagedAgentsAgentToolsetDefaultConfigParams](api/beta/agents.md)> defaultConfig

Default configuration for all tools in a toolset.

Optional<Boolean> enabled

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.



Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



class BetaManagedAgentsMcpToolsetParams:

Configuration for tools from an MCP server defined in `mcp_servers`.

String mcpServerName

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

Type type



Optional<List<[BetaManagedAgentsMcpToolConfigParams](api/beta/agents.md)>> configs

Per-tool configuration overrides.

String name

Name of the MCP tool to configure. 1-128 characters.

Optional<Boolean> enabled

Whether this tool is enabled. Overrides the `default_config` setting.



Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



Optional<[BetaManagedAgentsMcpToolsetDefaultConfigParams](api/beta/agents.md)> defaultConfig

Default configuration for all tools from an MCP server.

Optional<Boolean> enabled

Whether tools are enabled by default. Defaults to true if not specified.



Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



class BetaManagedAgentsCustomToolParams:

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

String description

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.



[BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

Type type

Optional<Long> version

The specific `agent` version to use. Omit to use the latest version.

String environmentId

ID of the `environment` defining the container configuration for this session.

Optional<Metadata> metadata

Arbitrary key-value metadata attached to the session. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.



Optional<List<Resource>> resources

Resources (e.g. repositories, files) to mount into the session's container.



class BetaManagedAgentsGitHubRepositoryResourceParams:

Mount a GitHub repository into the session's container.

String authorizationToken

GitHub authorization token used to clone the repository.

Type type

String url

Github URL of the repository



Optional<Checkout> checkout

Branch or commit to check out. Defaults to the repository's default branch.

One of the following:



class BetaManagedAgentsBranchCheckout:

String name

Branch name to check out.

Type type



class BetaManagedAgentsCommitCheckout:

String sha

Full commit SHA to check out.

Type type

Optional<String> mountPath

Mount path in the container. Defaults to `/workspace/<repo-name>`.



class BetaManagedAgentsFileResourceParams:

Mount a file uploaded via the Files API into the session.

String fileId

ID of a previously uploaded file.

Type type

Optional<String> mountPath

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



class BetaManagedAgentsMemoryStoreResourceParam:

Parameters for attaching a memory store to an agent session.

String memoryStoreId

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type



Optional<Access> access

Access mode for an attached memory store.

One of the following:

READ\_WRITE("read\_write")

READ\_ONLY("read\_only")

Optional<String> instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

Optional<String> title

Human-readable session title.

Optional<List<String>> vaultIds

Vault IDs for stored credentials the agent can use during the session.

##### ReturnsExpand Collapse



class BetaManagedAgentsSession:

A Managed Agents `session`.

String id



[BetaManagedAgentsSessionAgent](api/beta/sessions.md) agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

String id

Optional<String> description



List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta/agents.md)> mcpServers

String name

Type type

String url



[BetaManagedAgentsModelConfig](api/beta/agents.md) model

Model identifier and configuration.



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")



Optional<[BetaManagedAgentsSessionMultiagentCoordinator](api/beta/sessions.md)> multiagent

Resolved coordinator topology with full agent definitions for each roster member.



List<[BetaManagedAgentsSessionThreadAgent](api/beta/agents.md)> agents

Full `agent` definitions the coordinator may spawn as session threads.

String id

Optional<String> description



List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta/agents.md)> mcpServers

String name

Type type

String url



[BetaManagedAgentsModelConfig](api/beta/agents.md) model

Model identifier and configuration.



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")

String name



List<Skill> skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system



List<Tool> tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



List<[BetaManagedAgentsAgentToolConfig](api/beta/agents.md)> configs

boolean enabled



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type



class BetaManagedAgentsMcpToolset:



List<[BetaManagedAgentsMcpToolConfig](api/beta/agents.md)> configs

boolean enabled

String name



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta/agents.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description



[BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Type type

Type type

long version

Type type

String name



List<Skill> skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system



List<Tool> tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



List<[BetaManagedAgentsAgentToolConfig](api/beta/agents.md)> configs

boolean enabled



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type



class BetaManagedAgentsMcpToolset:



List<[BetaManagedAgentsMcpToolConfig](api/beta/agents.md)> configs

boolean enabled

String name



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta/agents.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description



[BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Type type

Type type

long version

Optional<LocalDateTime> archivedAt

A timestamp in RFC 3339 format

LocalDateTime createdAt

A timestamp in RFC 3339 format

String environmentId

Metadata metadata



List<[BetaManagedAgentsOutcomeEvaluationResource](api/beta/sessions.md)> outcomeEvaluations

Per-outcome evaluation state. One entry per define\_outcome event sent to the session.

Optional<LocalDateTime> completedAt

A timestamp in RFC 3339 format

String description

What the agent should produce.

Optional<String> explanation

Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs\_revision (intermediate), what's missing; for failed, why unrecoverable.

long iteration

0-indexed revision cycle the outcome is currently on.

String outcomeId

Server-generated outc\_ ID for this outcome.

String result

Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

Type type



List<[BetaManagedAgentsSessionResource](api/beta/sessions/resources.md)> resources

One of the following:



class BetaManagedAgentsGitHubRepositoryResource:

String id

LocalDateTime createdAt

A timestamp in RFC 3339 format

String mountPath

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

String url



Optional<Checkout> checkout

One of the following:



class BetaManagedAgentsBranchCheckout:

String name

Branch name to check out.

Type type



class BetaManagedAgentsCommitCheckout:

String sha

Full commit SHA to check out.

Type type



class BetaManagedAgentsFileResource:

String id

LocalDateTime createdAt

A timestamp in RFC 3339 format

String fileId

String mountPath

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsMemoryStoreResource:

A memory store attached to an agent session.

String memoryStoreId

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type



Optional<Access> access

Access mode for an attached memory store.

One of the following:

READ\_WRITE("read\_write")

READ\_ONLY("read\_only")

Optional<String> description

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

Optional<String> instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

Optional<String> mountPath

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

Optional<String> name

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.



[BetaManagedAgentsSessionStats](api/beta/sessions.md) stats

Timing statistics for a session.

Optional<Double> activeSeconds

Cumulative time in seconds the session spent in running status. Excludes idle time.

Optional<Double> durationSeconds

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.



Status status

SessionStatus enum

One of the following:

RESCHEDULING("rescheduling")

RUNNING("running")

IDLE("idle")

TERMINATED("terminated")

Optional<String> title

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format



[BetaManagedAgentsSessionUsage](api/beta/sessions.md) usage

Cumulative token usage for a session across all turns.



Optional<[BetaManagedAgentsCacheCreationUsage](api/beta/sessions.md)> cacheCreation

Prompt-cache creation token usage broken down by cache lifetime.

Optional<Long> ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

Optional<Long> ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.

Optional<Long> cacheReadInputTokens

Total tokens read from prompt cache.

Optional<Long> inputTokens

Total input tokens consumed across all turns.

Optional<Long> outputTokens

Total output tokens generated across all turns.

List<String> vaultIds

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

Optional<String> deploymentId

Deployment ID when the session was created from a deployment reference. Null otherwise.

Create Session

Java

```shiki
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.BetaManagedAgentsSession;
import com.anthropic.models.beta.sessions.SessionCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        SessionCreateParams params = SessionCreateParams.builder()
            .agent("agent_011CZkYpogX7uDKUyvBTophP")
            .environmentId("env_011CZkZ9X2dpNyB7HsEFoRfW")
            .build();
        BetaManagedAgentsSession betaManagedAgentsSession = client.beta().sessions().create(params);
    }
}
```

Response 200



```shiki
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-sonnet-4-6",
      "speed": "standard"
    },
    "multiagent": {
      "agents": [
        {
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "description": "A focused research subagent.",
          "mcp_servers": [
            {
              "name": "example-mcp",
              "type": "url",
              "url": "https://example-server.modelcontextprotocol.io/sse"
            }
          ],
          "model": {
            "id": "claude-sonnet-4-6",
            "speed": "standard"
          },
          "name": "Researcher",
          "skills": [
            {
              "skill_id": "xlsx",
              "type": "anthropic",
              "version": "1"
            }
          ],
          "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
          "tools": [
            {
              "configs": [
                {
                  "enabled": true,
                  "name": "bash",
                  "permission_policy": {
                    "type": "always_allow"
                  }
                }
              ],
              "default_config": {
                "enabled": true,
                "permission_policy": {
                  "type": "always_ask"
                }
              },
              "type": "agent_toolset_20260401"
            }
          ],
          "type": "agent",
          "version": 1
        }
      ],
      "type": "coordinator"
    },
    "name": "My First Agent",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      },
      {
        "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
        "type": "custom",
        "version": "2"
      }
    ],
    "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            }
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
    {
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
    }
  ],
  "resources": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  },
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  },
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "deployment_id": "deployment_id"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-sonnet-4-6",
      "speed": "standard"
    },
    "multiagent": {
      "agents": [
        {
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "description": "A focused research subagent.",
          "mcp_servers": [
            {
              "name": "example-mcp",
              "type": "url",
              "url": "https://example-server.modelcontextprotocol.io/sse"
            }
          ],
          "model": {
            "id": "claude-sonnet-4-6",
            "speed": "standard"
          },
          "name": "Researcher",
          "skills": [
            {
              "skill_id": "xlsx",
              "type": "anthropic",
              "version": "1"
            }
          ],
          "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
          "tools": [
            {
              "configs": [
                {
                  "enabled": true,
                  "name": "bash",
                  "permission_policy": {
                    "type": "always_allow"
                  }
                }
              ],
              "default_config": {
                "enabled": true,
                "permission_policy": {
                  "type": "always_ask"
                }
              },
              "type": "agent_toolset_20260401"
            }
          ],
          "type": "agent",
          "version": 1
        }
      ],
      "type": "coordinator"
    },
    "name": "My First Agent",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      },
      {
        "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
        "type": "custom",
        "version": "2"
      }
    ],
    "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            }
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
    {
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
    }
  ],
  "resources": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  },
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  },
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "deployment_id": "deployment_id"
}
```

---

*Copyright © Anthropic. All rights reserved.*
