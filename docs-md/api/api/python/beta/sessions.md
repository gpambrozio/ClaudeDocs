# Sessions

Copy page



Python

# Sessions

##### [Create Session](api/beta/sessions/create.md)

beta.sessions.create(SessionCreateParams\*\*kwargs)  -> [BetaManagedAgentsSession](api/beta/sessions.md)

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

beta.sessions.list(SessionListParams\*\*kwargs)  -> SyncBidirectionalPageCursor[[BetaManagedAgentsSession](api/beta/sessions.md)]

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

beta.sessions.retrieve(strsession\_id, SessionRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsSession](api/beta/sessions.md)

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

beta.sessions.update(strsession\_id, SessionUpdateParams\*\*kwargs)  -> [BetaManagedAgentsSession](api/beta/sessions.md)

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

beta.sessions.delete(strsession\_id, SessionDeleteParams\*\*kwargs)  -> [BetaManagedAgentsDeletedSession](api/beta/sessions.md)

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

beta.sessions.archive(strsession\_id, SessionArchiveParams\*\*kwargs)  -> [BetaManagedAgentsSession](api/beta/sessions.md)

POST/v1/sessions/{session\_id}/archive

##### ModelsExpand Collapse



class BetaManagedAgentsAgentMessagePreview: …

id: str

The id the buffered agent.message will carry if it is emitted. Matches the event\_id on this preview's event\_delta events.

type: Literal["agent.message"]



class BetaManagedAgentsAgentParams: …

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: str

The `agent` ID.

type: Literal["agent"]

version: Optional[int]

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



class BetaManagedAgentsAgentThinkingPreview: …

id: str

The id the buffered agent.thinking will carry if it is emitted. Start-only — no event\_delta events follow.

type: Literal["agent.thinking"]



class BetaManagedAgentsAgentWithOverridesParams: …

Reference to an `agent` plus optional configuration overrides. Each provided field replaces the agent's value for the caller's use; the agent resource is unchanged.

id: str

The `agent` ID.

type: Literal["agent\_with\_overrides"]



mcp\_servers: Optional[List[[BetaManagedAgentsURLMCPServerParams](api/beta/agents.md)]]

Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

name: str

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

type: Literal["url"]

url: str

Endpoint URL for the MCP server.



model: Optional[Model]

Replacement model. Accepts the model string, e.g. `claude-opus-4-6`, or a `model_config` object. Omit to use the agent's model.

One of the following:



Union[Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more], str]

One of the following:



Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-sonnet-5` - High-performance model for coding and agents
- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

One of the following:

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

str



class BetaManagedAgentsModelConfigParams: …

An object that defines additional configuration control over model use



id: [BetaManagedAgentsModel](api/beta/agents.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-sonnet-5` - High-performance model for coding and agents
- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

One of the following:

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

str



speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



skills: Optional[List[[BetaManagedAgentsSkillParams](api/beta/agents.md)]]

Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

One of the following:



class BetaManagedAgentsAnthropicSkillParams: …

An Anthropic-managed skill.

skill\_id: str

Identifier of the Anthropic skill (e.g., "xlsx").

type: Literal["anthropic"]

version: Optional[str]

Version to pin. Defaults to latest if omitted.



class BetaManagedAgentsCustomSkillParams: …

A user-created custom skill.

skill\_id: str

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

type: Literal["custom"]

version: Optional[str]

Version to pin. Defaults to latest if omitted.

system: Optional[str]

Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.



tools: Optional[List[Tool]]

Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

One of the following:



class BetaManagedAgentsAgentToolset20260401Params: …

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

type: Literal["agent\_toolset\_20260401"]



configs: Optional[List[[BetaManagedAgentsAgentToolConfigParams](api/beta/agents.md)]]

Per-tool configuration overrides.



name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

enabled: Optional[bool]

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.



permission\_policy: Optional[PermissionPolicy]

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: Optional[BetaManagedAgentsAgentToolsetDefaultConfigParams]

Default configuration for all tools in a toolset.

enabled: Optional[bool]

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.



permission\_policy: Optional[PermissionPolicy]

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



class BetaManagedAgentsMCPToolsetParams: …

Configuration for tools from an MCP server defined in `mcp_servers`.

mcp\_server\_name: str

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

type: Literal["mcp\_toolset"]



configs: Optional[List[[BetaManagedAgentsMCPToolConfigParams](api/beta/agents.md)]]

Per-tool configuration overrides.

name: str

Name of the MCP tool to configure. 1-128 characters.

enabled: Optional[bool]

Whether this tool is enabled. Overrides the `default_config` setting.



permission\_policy: Optional[PermissionPolicy]

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: Optional[BetaManagedAgentsMCPToolsetDefaultConfigParams]

Default configuration for all tools from an MCP server.

enabled: Optional[bool]

Whether tools are enabled by default. Defaults to true if not specified.



permission\_policy: Optional[PermissionPolicy]

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



class BetaManagedAgentsCustomToolParams: …

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

description: str

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md)

JSON Schema for custom tool input parameters.

type: Literal["object"]

properties: Optional[Dict[str, object]]

required: Optional[List[str]]

name: str

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

type: Literal["custom"]

version: Optional[int]

The specific `agent` version to use. Omit to use the latest version.



class BetaManagedAgentsBranchCheckout: …

name: str

Branch name to check out.

type: Literal["branch"]



class BetaManagedAgentsCacheCreationUsage: …

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: Optional[int]

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: Optional[int]

Tokens used to create 5-minute ephemeral cache entries.



class BetaManagedAgentsCommitCheckout: …

sha: str

Full commit SHA to check out.

type: Literal["commit"]



class BetaManagedAgentsDeletedSession: …

Confirmation that a `session` has been permanently deleted.

id: str

type: Literal["session\_deleted"]



class BetaManagedAgentsDeltaContent: …



content: [BetaManagedAgentsTextBlock](api/beta/sessions/events.md)

Regular text content.

text: str

The text content.

type: Literal["text"]

type: Literal["content\_delta"]

index: Optional[int]

Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.



class BetaManagedAgentsDeltaEvent: …

An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event\_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model\_request\_end closes the preview. Only sent on stream connections that opt in via event\_deltas; never appears in event history.



delta: [BetaManagedAgentsDeltaContent](api/beta/sessions.md)

One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content\_delta fragments, each a partial element of the content array.



content: [BetaManagedAgentsTextBlock](api/beta/sessions/events.md)

Regular text content.

text: str

The text content.

type: Literal["text"]

type: Literal["content\_delta"]

index: Optional[int]

Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

event\_id: str

The id of the event being previewed. Matches event.id on the corresponding event\_start and the buffered event that reconciles the preview.

type: Literal["event\_delta"]



Literal["agent.message", "agent.thinking"]

EventDeltaType enum

One of the following:

"agent.message"

"agent.thinking"



class BetaManagedAgentsFileResourceParams: …

Mount a file uploaded via the Files API into the session.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

mount\_path: Optional[str]

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



class BetaManagedAgentsGitHubRepositoryResourceParams: …

Mount a GitHub repository into the session's container.

authorization\_token: str

GitHub authorization token used to clone the repository.

type: Literal["github\_repository"]

url: str

Github URL of the repository



checkout: Optional[Checkout]

Branch or commit to check out. Defaults to the repository's default branch.

One of the following:



class BetaManagedAgentsBranchCheckout: …

name: str

Branch name to check out.

type: Literal["branch"]



class BetaManagedAgentsCommitCheckout: …

sha: str

Full commit SHA to check out.

type: Literal["commit"]

mount\_path: Optional[str]

Mount path in the container. Defaults to `/workspace/<repo-name>`.



class BetaManagedAgentsMemoryStoreResourceParam: …

Parameters for attaching a memory store to an agent session.

memory\_store\_id: str

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: Literal["memory\_store"]



access: Optional[Literal["read\_write", "read\_only"]]

Access mode for an attached memory store.

One of the following:

"read\_write"

"read\_only"

instructions: Optional[str]

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.



class BetaManagedAgentsMultiagent: …

Resolved coordinator topology with a concrete agent roster.



agents: List[[BetaManagedAgentsAgentReference](api/beta/agents.md)]

Agents the coordinator may spawn as session threads, each resolved to a specific version.

id: str

type: Literal["agent"]

version: int

type: Literal["coordinator"]



class BetaManagedAgentsMultiagentParams: …

A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.



agents: Sequence[[BetaManagedAgentsMultiagentRosterEntryParams](api/beta/sessions.md)]

Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

One of the following:

str



class BetaManagedAgentsAgentParams: …

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: str

The `agent` ID.

type: Literal["agent"]

version: Optional[int]

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



class BetaManagedAgentsMultiagentSelfParams: …

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

type: Literal["self"]

type: Literal["coordinator"]



[BetaManagedAgentsMultiagentRosterEntryParams](api/beta/sessions.md)

An entry in a multiagent roster: an agent ID string, a versioned agent reference, or `self`.

One of the following:

str



class BetaManagedAgentsAgentParams: …

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: str

The `agent` ID.

type: Literal["agent"]

version: Optional[int]

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



class BetaManagedAgentsMultiagentSelfParams: …

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

type: Literal["self"]



class BetaManagedAgentsOutcomeEvaluationResource: …

Evaluation state for a single outcome defined via a define\_outcome event.

completed\_at: Optional[datetime]

A timestamp in RFC 3339 format

description: str

What the agent should produce.

explanation: Optional[str]

Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs\_revision (intermediate), what's missing; for failed, why unrecoverable.

iteration: int

0-indexed revision cycle the outcome is currently on.

outcome\_id: str

Server-generated outc\_ ID for this outcome.

result: str

Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

type: Literal["outcome\_evaluation"]



class BetaManagedAgentsSession: …

A Managed Agents `session`.

id: str



agent: [BetaManagedAgentsSessionAgent](api/beta/sessions.md)

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: str

description: Optional[str]



mcp\_servers: List[[BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md)]

name: str

type: Literal["url"]

url: str



model: [BetaManagedAgentsModelConfig](api/beta/agents.md)

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta/agents.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-sonnet-5` - High-performance model for coding and agents
- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

One of the following:

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

str



speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]

Resolved coordinator topology with full agent definitions for each roster member.



agents: List[[BetaManagedAgentsSessionThreadAgent](api/beta/agents.md)]

Full `agent` definitions the coordinator may spawn as session threads.

id: str

description: Optional[str]



mcp\_servers: List[[BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md)]

name: str

type: Literal["url"]

url: str



model: [BetaManagedAgentsModelConfig](api/beta/agents.md)

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta/agents.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-sonnet-5` - High-performance model for coding and agents
- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

One of the following:

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

str



speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

name: str



skills: List[Skill]

One of the following:



class BetaManagedAgentsAnthropicSkill: …

A resolved Anthropic-managed skill.

skill\_id: str

type: Literal["anthropic"]

version: str



class BetaManagedAgentsCustomSkill: …

A resolved user-created custom skill.

skill\_id: str

type: Literal["custom"]

version: str

system: Optional[str]



tools: List[Tool]

One of the following:



class BetaManagedAgentsAgentToolset20260401: …



configs: List[[BetaManagedAgentsAgentToolConfig](api/beta/agents.md)]

enabled: bool



name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md)

Resolved default configuration for agent tools.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

type: Literal["agent\_toolset\_20260401"]



class BetaManagedAgentsMCPToolset: …



configs: List[[BetaManagedAgentsMCPToolConfig](api/beta/agents.md)]

enabled: bool

name: str



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta/agents.md)

Resolved default configuration for all tools from an MCP server.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

mcp\_server\_name: str

type: Literal["mcp\_toolset"]



class BetaManagedAgentsCustomTool: …

A custom tool as returned in API responses.

description: str



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md)

JSON Schema for custom tool input parameters.

type: Literal["object"]

properties: Optional[Dict[str, object]]

required: Optional[List[str]]

name: str

type: Literal["custom"]

type: Literal["agent"]

version: int

type: Literal["coordinator"]

name: str



skills: List[Skill]

One of the following:



class BetaManagedAgentsAnthropicSkill: …

A resolved Anthropic-managed skill.

skill\_id: str

type: Literal["anthropic"]

version: str



class BetaManagedAgentsCustomSkill: …

A resolved user-created custom skill.

skill\_id: str

type: Literal["custom"]

version: str

system: Optional[str]



tools: List[Tool]

One of the following:



class BetaManagedAgentsAgentToolset20260401: …



configs: List[[BetaManagedAgentsAgentToolConfig](api/beta/agents.md)]

enabled: bool



name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md)

Resolved default configuration for agent tools.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

type: Literal["agent\_toolset\_20260401"]



class BetaManagedAgentsMCPToolset: …



configs: List[[BetaManagedAgentsMCPToolConfig](api/beta/agents.md)]

enabled: bool

name: str



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta/agents.md)

Resolved default configuration for all tools from an MCP server.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

mcp\_server\_name: str

type: Literal["mcp\_toolset"]



class BetaManagedAgentsCustomTool: …

A custom tool as returned in API responses.

description: str



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md)

JSON Schema for custom tool input parameters.

type: Literal["object"]

properties: Optional[Dict[str, object]]

required: Optional[List[str]]

name: str

type: Literal["custom"]

type: Literal["agent"]

version: int

archived\_at: Optional[datetime]

A timestamp in RFC 3339 format

created\_at: datetime

A timestamp in RFC 3339 format

environment\_id: str

metadata: Dict[str, str]



outcome\_evaluations: List[[BetaManagedAgentsOutcomeEvaluationResource](api/beta/sessions.md)]

Per-outcome evaluation state. One entry per define\_outcome event sent to the session.

completed\_at: Optional[datetime]

A timestamp in RFC 3339 format

description: str

What the agent should produce.

explanation: Optional[str]

Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs\_revision (intermediate), what's missing; for failed, why unrecoverable.

iteration: int

0-indexed revision cycle the outcome is currently on.

outcome\_id: str

Server-generated outc\_ ID for this outcome.

result: str

Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

type: Literal["outcome\_evaluation"]



resources: List[[BetaManagedAgentsSessionResource](api/beta/sessions/resources.md)]

One of the following:



class BetaManagedAgentsGitHubRepositoryResource: …

id: str

created\_at: datetime

A timestamp in RFC 3339 format

mount\_path: str

type: Literal["github\_repository"]

updated\_at: datetime

A timestamp in RFC 3339 format

url: str



checkout: Optional[Checkout]

One of the following:



class BetaManagedAgentsBranchCheckout: …

name: str

Branch name to check out.

type: Literal["branch"]



class BetaManagedAgentsCommitCheckout: …

sha: str

Full commit SHA to check out.

type: Literal["commit"]



class BetaManagedAgentsFileResource: …

id: str

created\_at: datetime

A timestamp in RFC 3339 format

file\_id: str

mount\_path: str

type: Literal["file"]

updated\_at: datetime

A timestamp in RFC 3339 format



class BetaManagedAgentsMemoryStoreResource: …

A memory store attached to an agent session.

memory\_store\_id: str

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: Literal["memory\_store"]



access: Optional[Literal["read\_write", "read\_only"]]

Access mode for an attached memory store.

One of the following:

"read\_write"

"read\_only"

description: Optional[str]

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: Optional[str]

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: Optional[str]

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: Optional[str]

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.



stats: [BetaManagedAgentsSessionStats](api/beta/sessions.md)

Timing statistics for a session.

active\_seconds: Optional[float]

Cumulative time in seconds the session spent in running status. Excludes idle time.

duration\_seconds: Optional[float]

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.



status: Literal["rescheduling", "running", "idle", "terminated"]

SessionStatus enum

One of the following:

"rescheduling"

"running"

"idle"

"terminated"

title: Optional[str]

type: Literal["session"]

updated\_at: datetime

A timestamp in RFC 3339 format



usage: [BetaManagedAgentsSessionUsage](api/beta/sessions.md)

Cumulative token usage for a session across all turns.



cache\_creation: Optional[BetaManagedAgentsCacheCreationUsage]

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: Optional[int]

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: Optional[int]

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens: Optional[int]

Total tokens read from prompt cache.

input\_tokens: Optional[int]

Total input tokens consumed across all turns.

output\_tokens: Optional[int]

Total output tokens generated across all turns.

vault\_ids: List[str]

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

deployment\_id: Optional[str]

Deployment ID when the session was created from a deployment reference. Null otherwise.



class BetaManagedAgentsSessionAgent: …

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: str

description: Optional[str]



mcp\_servers: List[[BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md)]

name: str

type: Literal["url"]

url: str



model: [BetaManagedAgentsModelConfig](api/beta/agents.md)

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta/agents.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-sonnet-5` - High-performance model for coding and agents
- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

One of the following:

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

str



speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]

Resolved coordinator topology with full agent definitions for each roster member.



agents: List[[BetaManagedAgentsSessionThreadAgent](api/beta/agents.md)]

Full `agent` definitions the coordinator may spawn as session threads.

id: str

description: Optional[str]



mcp\_servers: List[[BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md)]

name: str

type: Literal["url"]

url: str



model: [BetaManagedAgentsModelConfig](api/beta/agents.md)

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta/agents.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-sonnet-5` - High-performance model for coding and agents
- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

One of the following:

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

str



speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

name: str



skills: List[Skill]

One of the following:



class BetaManagedAgentsAnthropicSkill: …

A resolved Anthropic-managed skill.

skill\_id: str

type: Literal["anthropic"]

version: str



class BetaManagedAgentsCustomSkill: …

A resolved user-created custom skill.

skill\_id: str

type: Literal["custom"]

version: str

system: Optional[str]



tools: List[Tool]

One of the following:



class BetaManagedAgentsAgentToolset20260401: …



configs: List[[BetaManagedAgentsAgentToolConfig](api/beta/agents.md)]

enabled: bool



name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md)

Resolved default configuration for agent tools.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

type: Literal["agent\_toolset\_20260401"]



class BetaManagedAgentsMCPToolset: …



configs: List[[BetaManagedAgentsMCPToolConfig](api/beta/agents.md)]

enabled: bool

name: str



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta/agents.md)

Resolved default configuration for all tools from an MCP server.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

mcp\_server\_name: str

type: Literal["mcp\_toolset"]



class BetaManagedAgentsCustomTool: …

A custom tool as returned in API responses.

description: str



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md)

JSON Schema for custom tool input parameters.

type: Literal["object"]

properties: Optional[Dict[str, object]]

required: Optional[List[str]]

name: str

type: Literal["custom"]

type: Literal["agent"]

version: int

type: Literal["coordinator"]

name: str



skills: List[Skill]

One of the following:



class BetaManagedAgentsAnthropicSkill: …

A resolved Anthropic-managed skill.

skill\_id: str

type: Literal["anthropic"]

version: str



class BetaManagedAgentsCustomSkill: …

A resolved user-created custom skill.

skill\_id: str

type: Literal["custom"]

version: str

system: Optional[str]



tools: List[Tool]

One of the following:



class BetaManagedAgentsAgentToolset20260401: …



configs: List[[BetaManagedAgentsAgentToolConfig](api/beta/agents.md)]

enabled: bool



name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md)

Resolved default configuration for agent tools.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

type: Literal["agent\_toolset\_20260401"]



class BetaManagedAgentsMCPToolset: …



configs: List[[BetaManagedAgentsMCPToolConfig](api/beta/agents.md)]

enabled: bool

name: str



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta/agents.md)

Resolved default configuration for all tools from an MCP server.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

mcp\_server\_name: str

type: Literal["mcp\_toolset"]



class BetaManagedAgentsCustomTool: …

A custom tool as returned in API responses.

description: str



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md)

JSON Schema for custom tool input parameters.

type: Literal["object"]

properties: Optional[Dict[str, object]]

required: Optional[List[str]]

name: str

type: Literal["custom"]

type: Literal["agent"]

version: int



class BetaManagedAgentsSessionAgentUpdate: …

Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.



mcp\_servers: Optional[List[[BetaManagedAgentsURLMCPServerParams](api/beta/agents.md)]]

Replacement MCP server list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

name: str

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

type: Literal["url"]

url: str

Endpoint URL for the MCP server.



tools: Optional[List[Tool]]

Replacement tool list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

One of the following:



class BetaManagedAgentsAgentToolset20260401Params: …

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

type: Literal["agent\_toolset\_20260401"]



configs: Optional[List[[BetaManagedAgentsAgentToolConfigParams](api/beta/agents.md)]]

Per-tool configuration overrides.



name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

enabled: Optional[bool]

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.



permission\_policy: Optional[PermissionPolicy]

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: Optional[BetaManagedAgentsAgentToolsetDefaultConfigParams]

Default configuration for all tools in a toolset.

enabled: Optional[bool]

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.



permission\_policy: Optional[PermissionPolicy]

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



class BetaManagedAgentsMCPToolsetParams: …

Configuration for tools from an MCP server defined in `mcp_servers`.

mcp\_server\_name: str

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

type: Literal["mcp\_toolset"]



configs: Optional[List[[BetaManagedAgentsMCPToolConfigParams](api/beta/agents.md)]]

Per-tool configuration overrides.

name: str

Name of the MCP tool to configure. 1-128 characters.

enabled: Optional[bool]

Whether this tool is enabled. Overrides the `default_config` setting.



permission\_policy: Optional[PermissionPolicy]

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: Optional[BetaManagedAgentsMCPToolsetDefaultConfigParams]

Default configuration for all tools from an MCP server.

enabled: Optional[bool]

Whether tools are enabled by default. Defaults to true if not specified.



permission\_policy: Optional[PermissionPolicy]

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



class BetaManagedAgentsCustomToolParams: …

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

description: str

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md)

JSON Schema for custom tool input parameters.

type: Literal["object"]

properties: Optional[Dict[str, object]]

required: Optional[List[str]]

name: str

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

type: Literal["custom"]



class BetaManagedAgentsSessionMultiagentCoordinator: …

Resolved coordinator topology with full agent definitions for each roster member.



agents: List[[BetaManagedAgentsSessionThreadAgent](api/beta/agents.md)]

Full `agent` definitions the coordinator may spawn as session threads.

id: str

description: Optional[str]



mcp\_servers: List[[BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md)]

name: str

type: Literal["url"]

url: str



model: [BetaManagedAgentsModelConfig](api/beta/agents.md)

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta/agents.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-sonnet-5` - High-performance model for coding and agents
- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

One of the following:

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

str



speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

name: str



skills: List[Skill]

One of the following:



class BetaManagedAgentsAnthropicSkill: …

A resolved Anthropic-managed skill.

skill\_id: str

type: Literal["anthropic"]

version: str



class BetaManagedAgentsCustomSkill: …

A resolved user-created custom skill.

skill\_id: str

type: Literal["custom"]

version: str

system: Optional[str]



tools: List[Tool]

One of the following:



class BetaManagedAgentsAgentToolset20260401: …



configs: List[[BetaManagedAgentsAgentToolConfig](api/beta/agents.md)]

enabled: bool



name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md)

Resolved default configuration for agent tools.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

type: Literal["agent\_toolset\_20260401"]



class BetaManagedAgentsMCPToolset: …



configs: List[[BetaManagedAgentsMCPToolConfig](api/beta/agents.md)]

enabled: bool

name: str



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta/agents.md)

Resolved default configuration for all tools from an MCP server.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

mcp\_server\_name: str

type: Literal["mcp\_toolset"]



class BetaManagedAgentsCustomTool: …

A custom tool as returned in API responses.

description: str



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md)

JSON Schema for custom tool input parameters.

type: Literal["object"]

properties: Optional[Dict[str, object]]

required: Optional[List[str]]

name: str

type: Literal["custom"]

type: Literal["agent"]

version: int

type: Literal["coordinator"]



class BetaManagedAgentsSessionStats: …

Timing statistics for a session.

active\_seconds: Optional[float]

Cumulative time in seconds the session spent in running status. Excludes idle time.

duration\_seconds: Optional[float]

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.



class BetaManagedAgentsSessionUpdatedEvent: …

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.updated"]



agent: Optional[BetaManagedAgentsSessionAgent]

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: str

description: Optional[str]



mcp\_servers: List[[BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md)]

name: str

type: Literal["url"]

url: str



model: [BetaManagedAgentsModelConfig](api/beta/agents.md)

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta/agents.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-sonnet-5` - High-performance model for coding and agents
- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

One of the following:

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

str



speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]

Resolved coordinator topology with full agent definitions for each roster member.



agents: List[[BetaManagedAgentsSessionThreadAgent](api/beta/agents.md)]

Full `agent` definitions the coordinator may spawn as session threads.

id: str

description: Optional[str]



mcp\_servers: List[[BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md)]

name: str

type: Literal["url"]

url: str



model: [BetaManagedAgentsModelConfig](api/beta/agents.md)

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta/agents.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-sonnet-5` - High-performance model for coding and agents
- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

One of the following:

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

str



speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

name: str



skills: List[Skill]

One of the following:



class BetaManagedAgentsAnthropicSkill: …

A resolved Anthropic-managed skill.

skill\_id: str

type: Literal["anthropic"]

version: str



class BetaManagedAgentsCustomSkill: …

A resolved user-created custom skill.

skill\_id: str

type: Literal["custom"]

version: str

system: Optional[str]



tools: List[Tool]

One of the following:



class BetaManagedAgentsAgentToolset20260401: …



configs: List[[BetaManagedAgentsAgentToolConfig](api/beta/agents.md)]

enabled: bool



name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md)

Resolved default configuration for agent tools.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

type: Literal["agent\_toolset\_20260401"]



class BetaManagedAgentsMCPToolset: …



configs: List[[BetaManagedAgentsMCPToolConfig](api/beta/agents.md)]

enabled: bool

name: str



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta/agents.md)

Resolved default configuration for all tools from an MCP server.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

mcp\_server\_name: str

type: Literal["mcp\_toolset"]



class BetaManagedAgentsCustomTool: …

A custom tool as returned in API responses.

description: str



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md)

JSON Schema for custom tool input parameters.

type: Literal["object"]

properties: Optional[Dict[str, object]]

required: Optional[List[str]]

name: str

type: Literal["custom"]

type: Literal["agent"]

version: int

type: Literal["coordinator"]

name: str



skills: List[Skill]

One of the following:



class BetaManagedAgentsAnthropicSkill: …

A resolved Anthropic-managed skill.

skill\_id: str

type: Literal["anthropic"]

version: str



class BetaManagedAgentsCustomSkill: …

A resolved user-created custom skill.

skill\_id: str

type: Literal["custom"]

version: str

system: Optional[str]



tools: List[Tool]

One of the following:



class BetaManagedAgentsAgentToolset20260401: …



configs: List[[BetaManagedAgentsAgentToolConfig](api/beta/agents.md)]

enabled: bool



name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md)

Resolved default configuration for agent tools.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

type: Literal["agent\_toolset\_20260401"]



class BetaManagedAgentsMCPToolset: …



configs: List[[BetaManagedAgentsMCPToolConfig](api/beta/agents.md)]

enabled: bool

name: str



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta/agents.md)

Resolved default configuration for all tools from an MCP server.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

mcp\_server\_name: str

type: Literal["mcp\_toolset"]



class BetaManagedAgentsCustomTool: …

A custom tool as returned in API responses.

description: str



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md)

JSON Schema for custom tool input parameters.

type: Literal["object"]

properties: Optional[Dict[str, object]]

required: Optional[List[str]]

name: str

type: Literal["custom"]

type: Literal["agent"]

version: int

metadata: Optional[Dict[str, str]]

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

title: Optional[str]

The session's new title. Present only when the update changed it.



class BetaManagedAgentsSessionUsage: …

Cumulative token usage for a session across all turns.



cache\_creation: Optional[BetaManagedAgentsCacheCreationUsage]

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: Optional[int]

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: Optional[int]

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens: Optional[int]

Total tokens read from prompt cache.

input\_tokens: Optional[int]

Total input tokens consumed across all turns.

output\_tokens: Optional[int]

Total output tokens generated across all turns.



class BetaManagedAgentsStartEvent: …

Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event\_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model\_request\_end closes the preview. Only sent on stream connections that opt in via event\_deltas; never appears in event history.



event: [BetaManagedAgentsStartEventPreview](api/beta/sessions.md)

The previewed event's type and id. The event type determines which delta types the preview's event\_delta events carry: agent.message events stream content\_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

One of the following:



class BetaManagedAgentsAgentMessagePreview: …

id: str

The id the buffered agent.message will carry if it is emitted. Matches the event\_id on this preview's event\_delta events.

type: Literal["agent.message"]



class BetaManagedAgentsAgentThinkingPreview: …

id: str

The id the buffered agent.thinking will carry if it is emitted. Start-only — no event\_delta events follow.

type: Literal["agent.thinking"]

type: Literal["event\_start"]



[BetaManagedAgentsStartEventPreview](api/beta/sessions.md)

One of the following:



class BetaManagedAgentsAgentMessagePreview: …

id: str

The id the buffered agent.message will carry if it is emitted. Matches the event\_id on this preview's event\_delta events.

type: Literal["agent.message"]



class BetaManagedAgentsAgentThinkingPreview: …

id: str

The id the buffered agent.thinking will carry if it is emitted. Start-only — no event\_delta events follow.

type: Literal["agent.thinking"]



class BetaManagedAgentsSystemContentBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]



class BetaManagedAgentsSystemMessageEvent: …

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

id: str

Unique identifier for this event.



content: List[[BetaManagedAgentsSystemContentBlock](api/beta/sessions.md)]

System content blocks. Text-only.

text: str

The text content.

type: Literal["text"]

type: Literal["system.message"]

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format



class BetaManagedAgentsUserToolResultEvent: …

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

id: str

Unique identifier for this event.

tool\_use\_id: str

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: Literal["user.tool\_result"]



content: Optional[List[Content]]

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]



class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.



source: Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]



class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.



class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]



class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]



class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]



class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.



class BetaManagedAgentsSearchResultBlock: …

A block containing a web search result.



citations: [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md)

Citation settings for a search result.

enabled: bool

Whether citations are enabled for this search result.



content: List[[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md)]

Array of text content blocks from the search result.

text: str

The text content.

type: Literal["text"]

source: str

The URL source of the search result.

title: str

The title of the search result.

type: Literal["search\_result"]

is\_error: Optional[bool]

Whether the tool execution resulted in an error.

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format

session\_thread\_id: Optional[str]

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

#### SessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

beta.sessions.events.list(strsession\_id, EventListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsSessionEvent](api/beta/sessions/events.md)]

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

beta.sessions.events.send(strsession\_id, EventSendParams\*\*kwargs)  -> [BetaManagedAgentsSendSessionEvents](api/beta/sessions/events.md)

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

beta.sessions.events.stream(strsession\_id, EventStreamParams\*\*kwargs)  -> [BetaManagedAgentsStreamSessionEvents](api/beta/sessions/events.md)

GET/v1/sessions/{session\_id}/events/stream

#### SessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

beta.sessions.resources.add(strsession\_id, ResourceAddParams\*\*kwargs)  -> [BetaManagedAgentsFileResource](api/beta/sessions/resources.md)

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

beta.sessions.resources.list(strsession\_id, ResourceListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsSessionResource](api/beta/sessions/resources.md)]

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

beta.sessions.resources.retrieve(strresource\_id, ResourceRetrieveParams\*\*kwargs)  -> [ResourceRetrieveResponse](api/beta/sessions/resources.md)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

beta.sessions.resources.update(strresource\_id, ResourceUpdateParams\*\*kwargs)  -> [ResourceUpdateResponse](api/beta/sessions/resources.md)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

beta.sessions.resources.delete(strresource\_id, ResourceDeleteParams\*\*kwargs)  -> [BetaManagedAgentsDeleteSessionResource](api/beta/sessions/resources.md)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

#### SessionsThreads

##### [List Session Threads](api/beta/sessions/threads/list.md)

beta.sessions.threads.list(strsession\_id, ThreadListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsSessionThread](api/beta/sessions/threads.md)]

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/beta/sessions/threads/retrieve.md)

beta.sessions.threads.retrieve(strthread\_id, ThreadRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsSessionThread](api/beta/sessions/threads.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/beta/sessions/threads/archive.md)

beta.sessions.threads.archive(strthread\_id, ThreadArchiveParams\*\*kwargs)  -> [BetaManagedAgentsSessionThread](api/beta/sessions/threads.md)

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

#### SessionsThreadsEvents

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

beta.sessions.threads.events.list(strthread\_id, EventListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsSessionEvent](api/beta/sessions/events.md)]

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

beta.sessions.threads.events.stream(strthread\_id, EventStreamParams\*\*kwargs)  -> [BetaManagedAgentsStreamSessionThreadEvents](api/beta/sessions/threads.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

---

*Copyright © Anthropic. All rights reserved.*
