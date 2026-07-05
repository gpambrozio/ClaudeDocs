# Beta

Copy page



TypeScript

# Beta

##### ModelsExpand Collapse



AnthropicBeta = (string & {}) | "message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 25 more

One of the following:

(string & {})



"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 25 more

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"fallback-credit-2026-06-01"



BetaAPIError { message, type } 

message: string

type: "api\_error"



BetaAuthenticationError { message, type } 

message: string

type: "authentication\_error"



BetaBillingError { message, type } 

message: string

type: "billing\_error"



BetaError = [BetaInvalidRequestError](api/beta.md) { message, type }  | [BetaAuthenticationError](api/beta.md) { message, type }  | [BetaBillingError](api/beta.md) { message, type }  | 6 more

One of the following:



BetaInvalidRequestError { message, type } 

message: string

type: "invalid\_request\_error"



BetaAuthenticationError { message, type } 

message: string

type: "authentication\_error"



BetaBillingError { message, type } 

message: string

type: "billing\_error"



BetaPermissionError { message, type } 

message: string

type: "permission\_error"



BetaNotFoundError { message, type } 

message: string

type: "not\_found\_error"



BetaRateLimitError { message, type } 

message: string

type: "rate\_limit\_error"



BetaGatewayTimeoutError { message, type } 

message: string

type: "timeout\_error"



BetaAPIError { message, type } 

message: string

type: "api\_error"



BetaOverloadedError { message, type } 

message: string

type: "overloaded\_error"



BetaErrorResponse { error, request\_id, type } 



error: [BetaError](api/beta.md)

One of the following:



BetaInvalidRequestError { message, type } 

message: string

type: "invalid\_request\_error"



BetaAuthenticationError { message, type } 

message: string

type: "authentication\_error"



BetaBillingError { message, type } 

message: string

type: "billing\_error"



BetaPermissionError { message, type } 

message: string

type: "permission\_error"



BetaNotFoundError { message, type } 

message: string

type: "not\_found\_error"



BetaRateLimitError { message, type } 

message: string

type: "rate\_limit\_error"



BetaGatewayTimeoutError { message, type } 

message: string

type: "timeout\_error"



BetaAPIError { message, type } 

message: string

type: "api\_error"



BetaOverloadedError { message, type } 

message: string

type: "overloaded\_error"

request\_id: string | null

type: "error"



BetaGatewayTimeoutError { message, type } 

message: string

type: "timeout\_error"



BetaInvalidRequestError { message, type } 

message: string

type: "invalid\_request\_error"



BetaNotFoundError { message, type } 

message: string

type: "not\_found\_error"



BetaOverloadedError { message, type } 

message: string

type: "overloaded\_error"



BetaPermissionError { message, type } 

message: string

type: "permission\_error"



BetaRateLimitError { message, type } 

message: string

type: "rate\_limit\_error"

#### BetaModels

##### [List Models](api/beta/models/list.md)

client.beta.models.list(ModelListParams { after\_id, before\_id, limit, betas } params?, RequestOptionsoptions?): Page<[BetaModelInfo](api/beta/models.md) { id, allowed\_fallback\_models, capabilities, 5 more } >

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

client.beta.models.retrieve(stringmodelID, ModelRetrieveParams { betas } params?, RequestOptionsoptions?): [BetaModelInfo](api/beta/models.md) { id, allowed\_fallback\_models, capabilities, 5 more }

GET/v1/models/{model\_id}

#### BetaMessages

##### [Create a Message](api/beta/messages/create.md)

client.beta.messages.create(MessageCreateParamsparams, RequestOptionsoptions?): [BetaMessage](api/beta/messages.md) { id, container, content, 9 more }  | Stream<[BetaRawMessageStreamEvent](api/beta/messages.md)>

POST/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

client.beta.messages.countTokens(MessageCountTokensParams { messages, model, cache\_control, 11 more } params, RequestOptionsoptions?): [BetaMessageTokensCount](api/beta/messages.md) { context\_management, input\_tokens }

POST/v1/messages/count\_tokens

#### BetaMessagesBatches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

client.beta.messages.batches.create(BatchCreateParams { requests, betas, user\_profile\_id } params, RequestOptionsoptions?): [BetaMessageBatch](api/beta/messages/batches.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

client.beta.messages.batches.retrieve(stringmessageBatchID, BatchRetrieveParams { betas } params?, RequestOptionsoptions?): [BetaMessageBatch](api/beta/messages/batches.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

client.beta.messages.batches.list(BatchListParams { after\_id, before\_id, limit, betas } params?, RequestOptionsoptions?): Page<[BetaMessageBatch](api/beta/messages/batches.md) { id, archived\_at, cancel\_initiated\_at, 7 more } >

GET/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

client.beta.messages.batches.cancel(stringmessageBatchID, BatchCancelParams { betas } params?, RequestOptionsoptions?): [BetaMessageBatch](api/beta/messages/batches.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

client.beta.messages.batches.delete(stringmessageBatchID, BatchDeleteParams { betas } params?, RequestOptionsoptions?): [BetaDeletedMessageBatch](api/beta/messages/batches.md) { id, type }

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

client.beta.messages.batches.results(stringmessageBatchID, BatchResultsParams { betas } params?, RequestOptionsoptions?): [BetaMessageBatchIndividualResponse](api/beta/messages/batches.md) { custom\_id, result }  | Stream<[BetaMessageBatchIndividualResponse](api/beta/messages/batches.md) { custom\_id, result } >

GET/v1/messages/batches/{message\_batch\_id}/results

#### BetaAgents

##### [Create Agent](api/beta/agents/create.md)

client.beta.agents.create(AgentCreateParams { model, name, description, 7 more } params, RequestOptionsoptions?): [BetaManagedAgentsAgent](api/beta/agents.md) { id, archived\_at, created\_at, 12 more }

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

client.beta.agents.list(AgentListParams { created\_at[gte], created\_at[lte], include\_archived, 3 more } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsAgent](api/beta/agents.md) { id, archived\_at, created\_at, 12 more } >

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

client.beta.agents.retrieve(stringagentID, AgentRetrieveParams { version, betas } params?, RequestOptionsoptions?): [BetaManagedAgentsAgent](api/beta/agents.md) { id, archived\_at, created\_at, 12 more }

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

client.beta.agents.update(stringagentID, AgentUpdateParams { version, description, mcp\_servers, 8 more } params, RequestOptionsoptions?): [BetaManagedAgentsAgent](api/beta/agents.md) { id, archived\_at, created\_at, 12 more }

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

client.beta.agents.archive(stringagentID, AgentArchiveParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsAgent](api/beta/agents.md) { id, archived\_at, created\_at, 12 more }

POST/v1/agents/{agent\_id}/archive

#### BetaAgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

client.beta.agents.versions.list(stringagentID, VersionListParams { limit, page, betas } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsAgent](api/beta/agents.md) { id, archived\_at, created\_at, 12 more } >

GET/v1/agents/{agent\_id}/versions

#### BetaEnvironments

##### [Create Environment](api/beta/environments/create.md)

client.beta.environments.create(EnvironmentCreateParams { name, config, description, 3 more } params, RequestOptionsoptions?): [BetaEnvironment](api/beta/environments.md) { id, archived\_at, config, 7 more }

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

client.beta.environments.list(EnvironmentListParams { include\_archived, limit, page, betas } params?, RequestOptionsoptions?): PageCursor<[BetaEnvironment](api/beta/environments.md) { id, archived\_at, config, 7 more } >

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

client.beta.environments.retrieve(stringenvironmentID, EnvironmentRetrieveParams { betas } params?, RequestOptionsoptions?): [BetaEnvironment](api/beta/environments.md) { id, archived\_at, config, 7 more }

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

client.beta.environments.update(stringenvironmentID, EnvironmentUpdateParams { config, description, metadata, 3 more } params, RequestOptionsoptions?): [BetaEnvironment](api/beta/environments.md) { id, archived\_at, config, 7 more }

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

client.beta.environments.delete(stringenvironmentID, EnvironmentDeleteParams { betas } params?, RequestOptionsoptions?): [BetaEnvironmentDeleteResponse](api/beta/environments.md) { id, type }

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

client.beta.environments.archive(stringenvironmentID, EnvironmentArchiveParams { betas } params?, RequestOptionsoptions?): [BetaEnvironment](api/beta/environments.md) { id, archived\_at, config, 7 more }

POST/v1/environments/{environment\_id}/archive

#### BetaEnvironmentsWork

##### [Get Work Item](api/beta/environments/work/retrieve.md)

client.beta.environments.work.retrieve(stringworkID, WorkRetrieveParams { environment\_id, betas } params, RequestOptionsoptions?): [BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 10 more }

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

client.beta.environments.work.poll(stringenvironmentID, WorkPollParams { block\_ms, reclaim\_older\_than\_ms, betas, Anthropic-Worker-ID } params?, RequestOptionsoptions?): [BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 10 more }  | null

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

client.beta.environments.work.ack(stringworkID, WorkAckParams { environment\_id, betas } params, RequestOptionsoptions?): [BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 10 more }

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

client.beta.environments.work.heartbeat(stringworkID, WorkHeartbeatParams { environment\_id, desired\_ttl\_seconds, expected\_last\_heartbeat, betas } params, RequestOptionsoptions?): [BetaSelfHostedWorkHeartbeatResponse](api/beta/environments/work.md) { last\_heartbeat, lease\_extended, state, 2 more }

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

client.beta.environments.work.stop(stringworkID, WorkStopParams { environment\_id, force, betas } params, RequestOptionsoptions?): [BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 10 more }

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

client.beta.environments.work.list(stringenvironmentID, WorkListParams { limit, page, betas } params?, RequestOptionsoptions?): PageCursor<[BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 10 more } >

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

client.beta.environments.work.update(stringworkID, WorkUpdateParams { environment\_id, metadata, betas } params, RequestOptionsoptions?): [BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 10 more }

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

client.beta.environments.work.stats(stringenvironmentID, WorkStatsParams { betas } params?, RequestOptionsoptions?): [BetaSelfHostedWorkQueueStats](api/beta/environments/work.md) { depth, oldest\_queued\_at, pending, 2 more }

GET/v1/environments/{environment\_id}/work/stats

#### BetaSessions

##### [Create Session](api/beta/sessions/create.md)

client.beta.sessions.create(SessionCreateParams { agent, environment\_id, metadata, 4 more } params, RequestOptionsoptions?): [BetaManagedAgentsSession](api/beta/sessions.md) { id, agent, archived\_at, 13 more }

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

client.beta.sessions.list(SessionListParams { agent\_id, agent\_version, created\_at[gt], 11 more } params?, RequestOptionsoptions?): BidirectionalPageCursor<[BetaManagedAgentsSession](api/beta/sessions.md) { id, agent, archived\_at, 13 more } >

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

client.beta.sessions.retrieve(stringsessionID, SessionRetrieveParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsSession](api/beta/sessions.md) { id, agent, archived\_at, 13 more }

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

client.beta.sessions.update(stringsessionID, SessionUpdateParams { agent, metadata, title, 2 more } params, RequestOptionsoptions?): [BetaManagedAgentsSession](api/beta/sessions.md) { id, agent, archived\_at, 13 more }

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

client.beta.sessions.delete(stringsessionID, SessionDeleteParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsDeletedSession](api/beta/sessions.md) { id, type }

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

client.beta.sessions.archive(stringsessionID, SessionArchiveParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsSession](api/beta/sessions.md) { id, agent, archived\_at, 13 more }

POST/v1/sessions/{session\_id}/archive

#### BetaSessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

client.beta.sessions.events.list(stringsessionID, EventListParams { created\_at[gt], created\_at[gte], created\_at[lt], 6 more } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsSessionEvent](api/beta/sessions/events.md)>

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

client.beta.sessions.events.send(stringsessionID, EventSendParams { events, betas } params, RequestOptionsoptions?): [BetaManagedAgentsSendSessionEvents](api/beta/sessions/events.md) { data }

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

client.beta.sessions.events.stream(stringsessionID, EventStreamParams { event\_deltas, betas } params?, RequestOptionsoptions?): [BetaManagedAgentsStreamSessionEvents](api/beta/sessions/events.md) | Stream<[BetaManagedAgentsStreamSessionEvents](api/beta/sessions/events.md)>

GET/v1/sessions/{session\_id}/events/stream

#### BetaSessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

client.beta.sessions.resources.add(stringsessionID, ResourceAddParams { file\_id, type, mount\_path, betas } params, RequestOptionsoptions?): [BetaManagedAgentsFileResource](api/beta/sessions/resources.md) { id, created\_at, file\_id, 3 more }

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

client.beta.sessions.resources.list(stringsessionID, ResourceListParams { limit, page, betas } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsSessionResource](api/beta/sessions/resources.md)>

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

client.beta.sessions.resources.retrieve(stringresourceID, ResourceRetrieveParams { session\_id, betas } params, RequestOptionsoptions?): [ResourceRetrieveResponse](api/beta/sessions/resources.md)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

client.beta.sessions.resources.update(stringresourceID, ResourceUpdateParams { session\_id, authorization\_token, betas } params, RequestOptionsoptions?): [ResourceUpdateResponse](api/beta/sessions/resources.md)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

client.beta.sessions.resources.delete(stringresourceID, ResourceDeleteParams { session\_id, betas } params, RequestOptionsoptions?): [BetaManagedAgentsDeleteSessionResource](api/beta/sessions/resources.md) { id, type }

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

#### BetaSessionsThreads

##### [List Session Threads](api/beta/sessions/threads/list.md)

client.beta.sessions.threads.list(stringsessionID, ThreadListParams { limit, page, betas } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsSessionThread](api/beta/sessions/threads.md) { id, agent, archived\_at, 8 more } >

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/beta/sessions/threads/retrieve.md)

client.beta.sessions.threads.retrieve(stringthreadID, ThreadRetrieveParams { session\_id, betas } params, RequestOptionsoptions?): [BetaManagedAgentsSessionThread](api/beta/sessions/threads.md) { id, agent, archived\_at, 8 more }

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/beta/sessions/threads/archive.md)

client.beta.sessions.threads.archive(stringthreadID, ThreadArchiveParams { session\_id, betas } params, RequestOptionsoptions?): [BetaManagedAgentsSessionThread](api/beta/sessions/threads.md) { id, agent, archived\_at, 8 more }

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

#### BetaSessionsThreadsEvents

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

client.beta.sessions.threads.events.list(stringthreadID, EventListParams { session\_id, limit, page, betas } params, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsSessionEvent](api/beta/sessions/events.md)>

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

client.beta.sessions.threads.events.stream(stringthreadID, EventStreamParams { session\_id, betas } params, RequestOptionsoptions?): [BetaManagedAgentsStreamSessionThreadEvents](api/beta/sessions/threads.md) | Stream<[BetaManagedAgentsStreamSessionThreadEvents](api/beta/sessions/threads.md)>

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

#### BetaDeployments

##### [Create Deployment](api/beta/deployments/create.md)

client.beta.deployments.create(DeploymentCreateParams { agent, environment\_id, initial\_events, 7 more } params, RequestOptionsoptions?): [BetaManagedAgentsDeployment](api/beta/deployments.md) { id, agent, archived\_at, 13 more }

POST/v1/deployments

##### [List Deployments](api/beta/deployments/list.md)

client.beta.deployments.list(DeploymentListParams { agent\_id, created\_at[gte], created\_at[lte], 5 more } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsDeployment](api/beta/deployments.md) { id, agent, archived\_at, 13 more } >

GET/v1/deployments

##### [Get Deployment](api/beta/deployments/retrieve.md)

client.beta.deployments.retrieve(stringdeploymentID, DeploymentRetrieveParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsDeployment](api/beta/deployments.md) { id, agent, archived\_at, 13 more }

GET/v1/deployments/{deployment\_id}

##### [Update Deployment](api/beta/deployments/update.md)

client.beta.deployments.update(stringdeploymentID, DeploymentUpdateParams { agent, description, environment\_id, 7 more } params, RequestOptionsoptions?): [BetaManagedAgentsDeployment](api/beta/deployments.md) { id, agent, archived\_at, 13 more }

POST/v1/deployments/{deployment\_id}

##### [Archive Deployment](api/beta/deployments/archive.md)

client.beta.deployments.archive(stringdeploymentID, DeploymentArchiveParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsDeployment](api/beta/deployments.md) { id, agent, archived\_at, 13 more }

POST/v1/deployments/{deployment\_id}/archive

##### [Run Deployment Now](api/beta/deployments/run.md)

client.beta.deployments.run(stringdeploymentID, DeploymentRunParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsDeploymentRun](api/beta/deployment_runs.md) { id, agent, created\_at, 5 more }

POST/v1/deployments/{deployment\_id}/run

##### [Pause Deployment](api/beta/deployments/pause.md)

client.beta.deployments.pause(stringdeploymentID, DeploymentPauseParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsDeployment](api/beta/deployments.md) { id, agent, archived\_at, 13 more }

POST/v1/deployments/{deployment\_id}/pause

##### [Unpause Deployment](api/beta/deployments/unpause.md)

client.beta.deployments.unpause(stringdeploymentID, DeploymentUnpauseParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsDeployment](api/beta/deployments.md) { id, agent, archived\_at, 13 more }

POST/v1/deployments/{deployment\_id}/unpause

#### BetaDeployment Runs

##### [List Deployment Runs](api/beta/deployment_runs/list.md)

client.beta.deploymentRuns.list(DeploymentRunListParams { created\_at[gt], created\_at[gte], created\_at[lt], 7 more } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsDeploymentRun](api/beta/deployment_runs.md) { id, agent, created\_at, 5 more } >

GET/v1/deployment\_runs

##### [Get Deployment Run](api/beta/deployment_runs/retrieve.md)

client.beta.deploymentRuns.retrieve(stringdeploymentRunID, DeploymentRunRetrieveParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsDeploymentRun](api/beta/deployment_runs.md) { id, agent, created\_at, 5 more }

GET/v1/deployment\_runs/{deployment\_run\_id}

#### BetaVaults

##### [Create Vault](api/beta/vaults/create.md)

client.beta.vaults.create(VaultCreateParams { display\_name, metadata, betas } params, RequestOptionsoptions?): [BetaManagedAgentsVault](api/beta/vaults.md) { id, archived\_at, created\_at, 4 more }

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

client.beta.vaults.list(VaultListParams { include\_archived, limit, page, betas } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsVault](api/beta/vaults.md) { id, archived\_at, created\_at, 4 more } >

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

client.beta.vaults.retrieve(stringvaultID, VaultRetrieveParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsVault](api/beta/vaults.md) { id, archived\_at, created\_at, 4 more }

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

client.beta.vaults.update(stringvaultID, VaultUpdateParams { display\_name, metadata, betas } params, RequestOptionsoptions?): [BetaManagedAgentsVault](api/beta/vaults.md) { id, archived\_at, created\_at, 4 more }

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

client.beta.vaults.delete(stringvaultID, VaultDeleteParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsDeletedVault](api/beta/vaults.md) { id, type }

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

client.beta.vaults.archive(stringvaultID, VaultArchiveParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsVault](api/beta/vaults.md) { id, archived\_at, created\_at, 4 more }

POST/v1/vaults/{vault\_id}/archive

#### BetaVaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

client.beta.vaults.credentials.create(stringvaultID, CredentialCreateParams { auth, display\_name, metadata, betas } params, RequestOptionsoptions?): [BetaManagedAgentsCredential](api/beta/vaults/credentials.md) { id, archived\_at, auth, 6 more }

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

client.beta.vaults.credentials.list(stringvaultID, CredentialListParams { include\_archived, limit, page, betas } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsCredential](api/beta/vaults/credentials.md) { id, archived\_at, auth, 6 more } >

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

client.beta.vaults.credentials.retrieve(stringcredentialID, CredentialRetrieveParams { vault\_id, betas } params, RequestOptionsoptions?): [BetaManagedAgentsCredential](api/beta/vaults/credentials.md) { id, archived\_at, auth, 6 more }

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

client.beta.vaults.credentials.update(stringcredentialID, CredentialUpdateParams { vault\_id, auth, display\_name, 2 more } params, RequestOptionsoptions?): [BetaManagedAgentsCredential](api/beta/vaults/credentials.md) { id, archived\_at, auth, 6 more }

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

client.beta.vaults.credentials.delete(stringcredentialID, CredentialDeleteParams { vault\_id, betas } params, RequestOptionsoptions?): [BetaManagedAgentsDeletedCredential](api/beta/vaults/credentials.md) { id, type }

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

client.beta.vaults.credentials.archive(stringcredentialID, CredentialArchiveParams { vault\_id, betas } params, RequestOptionsoptions?): [BetaManagedAgentsCredential](api/beta/vaults/credentials.md) { id, archived\_at, auth, 6 more }

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

client.beta.vaults.credentials.mcpOAuthValidate(stringcredentialID, CredentialMCPOAuthValidateParams { vault\_id, betas } params, RequestOptionsoptions?): [BetaManagedAgentsCredentialValidation](api/beta/vaults/credentials.md) { credential\_id, has\_refresh\_token, mcp\_probe, 5 more }

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

#### BetaMemory Stores

##### [Create a memory store](api/beta/memory_stores/create.md)

client.beta.memoryStores.create(MemoryStoreCreateParams { name, description, metadata, betas } params, RequestOptionsoptions?): [BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) { id, created\_at, name, 5 more }

POST/v1/memory\_stores

##### [List memory stores](api/beta/memory_stores/list.md)

client.beta.memoryStores.list(MemoryStoreListParams { created\_at[gte], created\_at[lte], include\_archived, 3 more } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) { id, created\_at, name, 5 more } >

GET/v1/memory\_stores

##### [Retrieve a memory store](api/beta/memory_stores/retrieve.md)

client.beta.memoryStores.retrieve(stringmemoryStoreID, MemoryStoreRetrieveParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) { id, created\_at, name, 5 more }

GET/v1/memory\_stores/{memory\_store\_id}

##### [Update a memory store](api/beta/memory_stores/update.md)

client.beta.memoryStores.update(stringmemoryStoreID, MemoryStoreUpdateParams { description, metadata, name, betas } params, RequestOptionsoptions?): [BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) { id, created\_at, name, 5 more }

POST/v1/memory\_stores/{memory\_store\_id}

##### [Delete a memory store](api/beta/memory_stores/delete.md)

client.beta.memoryStores.delete(stringmemoryStoreID, MemoryStoreDeleteParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsDeletedMemoryStore](api/beta/memory_stores.md) { id, type }

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [Archive a memory store](api/beta/memory_stores/archive.md)

client.beta.memoryStores.archive(stringmemoryStoreID, MemoryStoreArchiveParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) { id, created\_at, name, 5 more }

POST/v1/memory\_stores/{memory\_store\_id}/archive

#### BetaMemory StoresMemories

##### [Create a memory](api/beta/memory_stores/memories/create.md)

client.beta.memoryStores.memories.create(stringmemoryStoreID, MemoryCreateParams { content, path, view, betas } params, RequestOptionsoptions?): [BetaManagedAgentsMemory](api/beta/memory_stores/memories.md) { id, content\_sha256, content\_size\_bytes, 7 more }

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/beta/memory_stores/memories/list.md)

client.beta.memoryStores.memories.list(stringmemoryStoreID, MemoryListParams { depth, limit, order, 5 more } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsMemoryListItem](api/beta/memory_stores/memories.md)>

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/beta/memory_stores/memories/retrieve.md)

client.beta.memoryStores.memories.retrieve(stringmemoryID, MemoryRetrieveParams { memory\_store\_id, view, betas } params, RequestOptionsoptions?): [BetaManagedAgentsMemory](api/beta/memory_stores/memories.md) { id, content\_sha256, content\_size\_bytes, 7 more }

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/beta/memory_stores/memories/update.md)

client.beta.memoryStores.memories.update(stringmemoryID, MemoryUpdateParams { memory\_store\_id, view, content, 3 more } params, RequestOptionsoptions?): [BetaManagedAgentsMemory](api/beta/memory_stores/memories.md) { id, content\_sha256, content\_size\_bytes, 7 more }

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/beta/memory_stores/memories/delete.md)

client.beta.memoryStores.memories.delete(stringmemoryID, MemoryDeleteParams { memory\_store\_id, expected\_content\_sha256, betas } params, RequestOptionsoptions?): [BetaManagedAgentsDeletedMemory](api/beta/memory_stores/memories.md) { id, type }

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

#### BetaMemory StoresMemory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

client.beta.memoryStores.memoryVersions.list(stringmemoryStoreID, MemoryVersionListParams { api\_key\_id, created\_at[gte], created\_at[lte], 7 more } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md) { id, created\_at, memory\_id, 10 more } >

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

client.beta.memoryStores.memoryVersions.retrieve(stringmemoryVersionID, MemoryVersionRetrieveParams { memory\_store\_id, view, betas } params, RequestOptionsoptions?): [BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md) { id, created\_at, memory\_id, 10 more }

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

client.beta.memoryStores.memoryVersions.redact(stringmemoryVersionID, MemoryVersionRedactParams { memory\_store\_id, betas } params, RequestOptionsoptions?): [BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md) { id, created\_at, memory\_id, 10 more }

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

#### BetaFiles

##### [Upload File](api/beta/files/upload.md)

client.beta.files.upload(FileUploadParams { file, betas } params, RequestOptionsoptions?): [FileMetadata](api/beta/files.md) { id, created\_at, filename, 5 more }

POST/v1/files

##### [List Files](api/beta/files/list.md)

client.beta.files.list(FileListParams { after\_id, before\_id, limit, 2 more } params?, RequestOptionsoptions?): Page<[FileMetadata](api/beta/files.md) { id, created\_at, filename, 5 more } >

GET/v1/files

##### [Download File](api/beta/files/download.md)

client.beta.files.download(stringfileID, FileDownloadParams { betas } params?, RequestOptionsoptions?): Response

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

client.beta.files.retrieveMetadata(stringfileID, FileRetrieveMetadataParams { betas } params?, RequestOptionsoptions?): [FileMetadata](api/beta/files.md) { id, created\_at, filename, 5 more }

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

client.beta.files.delete(stringfileID, FileDeleteParams { betas } params?, RequestOptionsoptions?): [DeletedFile](api/beta/files.md) { id, type }

DELETE/v1/files/{file\_id}

#### BetaSkills

##### [Create Skill](api/beta/skills/create.md)

client.beta.skills.create(SkillCreateParams { display\_title, files, betas } params?, RequestOptionsoptions?): [SkillCreateResponse](api/beta/skills.md) { id, created\_at, display\_title, 4 more }

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

client.beta.skills.list(SkillListParams { limit, page, source, betas } params?, RequestOptionsoptions?): PageCursor<[SkillListResponse](api/beta/skills.md) { id, created\_at, display\_title, 4 more } >

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

client.beta.skills.retrieve(stringskillID, SkillRetrieveParams { betas } params?, RequestOptionsoptions?): [SkillRetrieveResponse](api/beta/skills.md) { id, created\_at, display\_title, 4 more }

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

client.beta.skills.delete(stringskillID, SkillDeleteParams { betas } params?, RequestOptionsoptions?): [SkillDeleteResponse](api/beta/skills.md) { id, type }

DELETE/v1/skills/{skill\_id}

#### BetaSkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

client.beta.skills.versions.create(stringskillID, VersionCreateParams { files, betas } params?, RequestOptionsoptions?): [VersionCreateResponse](api/beta/skills/versions.md) { id, created\_at, description, 5 more }

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

client.beta.skills.versions.list(stringskillID, VersionListParams { limit, page, betas } params?, RequestOptionsoptions?): PageCursor<[VersionListResponse](api/beta/skills/versions.md) { id, created\_at, description, 5 more } >

GET/v1/skills/{skill\_id}/versions

##### [Download Skill Version Content](api/beta/skills/versions/download.md)

client.beta.skills.versions.download(stringversion, VersionDownloadParams { skill\_id, betas } params, RequestOptionsoptions?): Response

GET/v1/skills/{skill\_id}/versions/{version}/content

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

client.beta.skills.versions.retrieve(stringversion, VersionRetrieveParams { skill\_id, betas } params, RequestOptionsoptions?): [VersionRetrieveResponse](api/beta/skills/versions.md) { id, created\_at, description, 5 more }

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

client.beta.skills.versions.delete(stringversion, VersionDeleteParams { skill\_id, betas } params, RequestOptionsoptions?): [VersionDeleteResponse](api/beta/skills/versions.md) { id, type }

DELETE/v1/skills/{skill\_id}/versions/{version}

#### BetaUser Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

client.beta.userProfiles.create(UserProfileCreateParams { external\_id, metadata, name, 2 more } params, RequestOptionsoptions?): [BetaUserProfile](api/beta/user_profiles.md) { id, created\_at, metadata, 6 more }

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

client.beta.userProfiles.list(UserProfileListParams { limit, order, page, betas } params?, RequestOptionsoptions?): PageCursor<[BetaUserProfile](api/beta/user_profiles.md) { id, created\_at, metadata, 6 more } >

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

client.beta.userProfiles.retrieve(stringuserProfileID, UserProfileRetrieveParams { betas } params?, RequestOptionsoptions?): [BetaUserProfile](api/beta/user_profiles.md) { id, created\_at, metadata, 6 more }

GET/v1/user\_profiles/{user\_profile\_id}

##### [Update User Profile](api/beta/user_profiles/update.md)

client.beta.userProfiles.update(stringuserProfileID, UserProfileUpdateParams { external\_id, metadata, name, 2 more } params, RequestOptionsoptions?): [BetaUserProfile](api/beta/user_profiles.md) { id, created\_at, metadata, 6 more }

POST/v1/user\_profiles/{user\_profile\_id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

client.beta.userProfiles.createEnrollmentURL(stringuserProfileID, UserProfileCreateEnrollmentURLParams { betas } params?, RequestOptionsoptions?): [BetaUserProfileEnrollmentURL](api/beta/user_profiles.md) { expires\_at, type, url }

POST/v1/user\_profiles/{user\_profile\_id}/enrollment\_url

#### BetaTunnels

#### BetaTunnelsCertificates

#### BetaWebhooks

Helpers for receiving and verifying webhook events. Use `unwrap` in your SDK to verify signatures and parse payloads; see the [webhooks guide](managed-agents/webhooks.md) for handler examples.

Possible `data.type` values:

- `agent.archived`
- `agent.created`
- `agent.deleted`
- `agent.updated`
- `deployment.archived`
- `deployment.created`
- `deployment.deleted`
- `deployment.paused`
- `deployment.unpaused`
- `deployment.updated`
- `deployment_run.failed`
- `deployment_run.started`
- `deployment_run.succeeded`
- `environment.archived`
- `environment.created`
- `environment.updated`
- `memory_store.archived`
- `memory_store.created`
- `memory_store.deleted`
- `session.archived`
- `session.created`
- `session.deleted`
- `session.idled`
- `session.outcome_evaluation_ended`
- `session.pending`
- `session.requires_action`
- `session.running`
- `session.status_idled`
- `session.status_rescheduled`
- `session.status_run_started`
- `session.status_terminated`
- `session.thread_created`
- `session.thread_idled`
- `session.thread_terminated`
- `session.updated`
- `vault.archived`
- `vault.created`
- `vault.deleted`
- `vault_credential.archived`
- `vault_credential.created`
- `vault_credential.deleted`
- `vault_credential.refresh_failed`

---

*Copyright © Anthropic. All rights reserved.*
