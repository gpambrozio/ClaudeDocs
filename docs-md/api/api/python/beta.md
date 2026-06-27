# Beta

Copy page



Python

# Beta

##### ModelsExpand Collapse



Union[str, Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]]

One of the following:

str



Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]

One of the following:

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

class BetaAPIError: …

message: str

type: Literal["api\_error"]



class BetaAuthenticationError: …

message: str

type: Literal["authentication\_error"]



class BetaBillingError: …

message: str

type: Literal["billing\_error"]



[BetaError](api/beta.md)

One of the following:



class BetaInvalidRequestError: …

message: str

type: Literal["invalid\_request\_error"]



class BetaAuthenticationError: …

message: str

type: Literal["authentication\_error"]



class BetaBillingError: …

message: str

type: Literal["billing\_error"]



class BetaPermissionError: …

message: str

type: Literal["permission\_error"]



class BetaNotFoundError: …

message: str

type: Literal["not\_found\_error"]



class BetaRateLimitError: …

message: str

type: Literal["rate\_limit\_error"]



class BetaGatewayTimeoutError: …

message: str

type: Literal["timeout\_error"]



class BetaAPIError: …

message: str

type: Literal["api\_error"]



class BetaOverloadedError: …

message: str

type: Literal["overloaded\_error"]



class BetaErrorResponse: …



error: [BetaError](api/beta.md)

One of the following:



class BetaInvalidRequestError: …

message: str

type: Literal["invalid\_request\_error"]



class BetaAuthenticationError: …

message: str

type: Literal["authentication\_error"]



class BetaBillingError: …

message: str

type: Literal["billing\_error"]



class BetaPermissionError: …

message: str

type: Literal["permission\_error"]



class BetaNotFoundError: …

message: str

type: Literal["not\_found\_error"]



class BetaRateLimitError: …

message: str

type: Literal["rate\_limit\_error"]



class BetaGatewayTimeoutError: …

message: str

type: Literal["timeout\_error"]



class BetaAPIError: …

message: str

type: Literal["api\_error"]



class BetaOverloadedError: …

message: str

type: Literal["overloaded\_error"]

request\_id: Optional[str]

type: Literal["error"]



class BetaGatewayTimeoutError: …

message: str

type: Literal["timeout\_error"]



class BetaInvalidRequestError: …

message: str

type: Literal["invalid\_request\_error"]



class BetaNotFoundError: …

message: str

type: Literal["not\_found\_error"]



class BetaOverloadedError: …

message: str

type: Literal["overloaded\_error"]



class BetaPermissionError: …

message: str

type: Literal["permission\_error"]



class BetaRateLimitError: …

message: str

type: Literal["rate\_limit\_error"]

#### BetaModels

##### [List Models](api/beta/models/list.md)

beta.models.list(ModelListParams\*\*kwargs)  -> SyncPage[[BetaModelInfo](api/beta/models.md)]

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

beta.models.retrieve(strmodel\_id, ModelRetrieveParams\*\*kwargs)  -> [BetaModelInfo](api/beta/models.md)

GET/v1/models/{model\_id}

#### BetaMessages

##### [Create a Message](api/beta/messages/create.md)

beta.messages.create(MessageCreateParams\*\*kwargs)  -> [BetaMessage](api/beta/messages.md)

POST/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

beta.messages.count\_tokens(MessageCountTokensParams\*\*kwargs)  -> [BetaMessageTokensCount](api/beta/messages.md)

POST/v1/messages/count\_tokens

#### BetaMessagesBatches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

beta.messages.batches.create(BatchCreateParams\*\*kwargs)  -> [BetaMessageBatch](api/beta/messages/batches.md)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

beta.messages.batches.retrieve(strmessage\_batch\_id, BatchRetrieveParams\*\*kwargs)  -> [BetaMessageBatch](api/beta/messages/batches.md)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

beta.messages.batches.list(BatchListParams\*\*kwargs)  -> SyncPage[[BetaMessageBatch](api/beta/messages/batches.md)]

GET/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

beta.messages.batches.cancel(strmessage\_batch\_id, BatchCancelParams\*\*kwargs)  -> [BetaMessageBatch](api/beta/messages/batches.md)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

beta.messages.batches.delete(strmessage\_batch\_id, BatchDeleteParams\*\*kwargs)  -> [BetaDeletedMessageBatch](api/beta/messages/batches.md)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

beta.messages.batches.results(strmessage\_batch\_id, BatchResultsParams\*\*kwargs)  -> [BetaMessageBatchIndividualResponse](api/beta/messages/batches.md)

GET/v1/messages/batches/{message\_batch\_id}/results

#### BetaAgents

##### [Create Agent](api/beta/agents/create.md)

beta.agents.create(AgentCreateParams\*\*kwargs)  -> [BetaManagedAgentsAgent](api/beta/agents.md)

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

beta.agents.list(AgentListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsAgent](api/beta/agents.md)]

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

beta.agents.retrieve(stragent\_id, AgentRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsAgent](api/beta/agents.md)

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

beta.agents.update(stragent\_id, AgentUpdateParams\*\*kwargs)  -> [BetaManagedAgentsAgent](api/beta/agents.md)

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

beta.agents.archive(stragent\_id, AgentArchiveParams\*\*kwargs)  -> [BetaManagedAgentsAgent](api/beta/agents.md)

POST/v1/agents/{agent\_id}/archive

#### BetaAgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

beta.agents.versions.list(stragent\_id, VersionListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsAgent](api/beta/agents.md)]

GET/v1/agents/{agent\_id}/versions

#### BetaEnvironments

##### [Create Environment](api/beta/environments/create.md)

beta.environments.create(EnvironmentCreateParams\*\*kwargs)  -> [BetaEnvironment](api/beta/environments.md)

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

beta.environments.list(EnvironmentListParams\*\*kwargs)  -> SyncPageCursor[[BetaEnvironment](api/beta/environments.md)]

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

beta.environments.retrieve(strenvironment\_id, EnvironmentRetrieveParams\*\*kwargs)  -> [BetaEnvironment](api/beta/environments.md)

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

beta.environments.update(strenvironment\_id, EnvironmentUpdateParams\*\*kwargs)  -> [BetaEnvironment](api/beta/environments.md)

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

beta.environments.delete(strenvironment\_id, EnvironmentDeleteParams\*\*kwargs)  -> [BetaEnvironmentDeleteResponse](api/beta/environments.md)

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

beta.environments.archive(strenvironment\_id, EnvironmentArchiveParams\*\*kwargs)  -> [BetaEnvironment](api/beta/environments.md)

POST/v1/environments/{environment\_id}/archive

#### BetaEnvironmentsWork

##### [Get Work Item](api/beta/environments/work/retrieve.md)

beta.environments.work.retrieve(strwork\_id, WorkRetrieveParams\*\*kwargs)  -> [BetaSelfHostedWork](api/beta/environments/work.md)

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

beta.environments.work.poll(strenvironment\_id, WorkPollParams\*\*kwargs)  -> [BetaSelfHostedWork](api/beta/environments/work.md)

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

beta.environments.work.ack(strwork\_id, WorkAckParams\*\*kwargs)  -> [BetaSelfHostedWork](api/beta/environments/work.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

beta.environments.work.heartbeat(strwork\_id, WorkHeartbeatParams\*\*kwargs)  -> [BetaSelfHostedWorkHeartbeatResponse](api/beta/environments/work.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

beta.environments.work.stop(strwork\_id, WorkStopParams\*\*kwargs)  -> [BetaSelfHostedWork](api/beta/environments/work.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

beta.environments.work.list(strenvironment\_id, WorkListParams\*\*kwargs)  -> SyncPageCursor[[BetaSelfHostedWork](api/beta/environments/work.md)]

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

beta.environments.work.update(strwork\_id, WorkUpdateParams\*\*kwargs)  -> [BetaSelfHostedWork](api/beta/environments/work.md)

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

beta.environments.work.stats(strenvironment\_id, WorkStatsParams\*\*kwargs)  -> [BetaSelfHostedWorkQueueStats](api/beta/environments/work.md)

GET/v1/environments/{environment\_id}/work/stats

#### BetaSessions

##### [Create Session](api/beta/sessions/create.md)

beta.sessions.create(SessionCreateParams\*\*kwargs)  -> [BetaManagedAgentsSession](api/beta/sessions.md)

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

beta.sessions.list(SessionListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsSession](api/beta/sessions.md)]

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

#### BetaSessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

beta.sessions.events.list(strsession\_id, EventListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsSessionEvent](api/beta/sessions/events.md)]

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

beta.sessions.events.send(strsession\_id, EventSendParams\*\*kwargs)  -> [BetaManagedAgentsSendSessionEvents](api/beta/sessions/events.md)

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

beta.sessions.events.stream(strsession\_id, EventStreamParams\*\*kwargs)  -> [BetaManagedAgentsStreamSessionEvents](api/beta/sessions/events.md)

GET/v1/sessions/{session\_id}/events/stream

#### BetaSessionsResources

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

#### BetaSessionsThreads

##### [List Session Threads](api/beta/sessions/threads/list.md)

beta.sessions.threads.list(strsession\_id, ThreadListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsSessionThread](api/beta/sessions/threads.md)]

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/beta/sessions/threads/retrieve.md)

beta.sessions.threads.retrieve(strthread\_id, ThreadRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsSessionThread](api/beta/sessions/threads.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/beta/sessions/threads/archive.md)

beta.sessions.threads.archive(strthread\_id, ThreadArchiveParams\*\*kwargs)  -> [BetaManagedAgentsSessionThread](api/beta/sessions/threads.md)

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

#### BetaSessionsThreadsEvents

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

beta.sessions.threads.events.list(strthread\_id, EventListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsSessionEvent](api/beta/sessions/events.md)]

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

beta.sessions.threads.events.stream(strthread\_id, EventStreamParams\*\*kwargs)  -> [BetaManagedAgentsStreamSessionThreadEvents](api/beta/sessions/threads.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

#### BetaDeployments

##### [Create Deployment](api/beta/deployments/create.md)

beta.deployments.create(DeploymentCreateParams\*\*kwargs)  -> [BetaManagedAgentsDeployment](api/beta/deployments.md)

POST/v1/deployments

##### [List Deployments](api/beta/deployments/list.md)

beta.deployments.list(DeploymentListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsDeployment](api/beta/deployments.md)]

GET/v1/deployments

##### [Get Deployment](api/beta/deployments/retrieve.md)

beta.deployments.retrieve(strdeployment\_id, DeploymentRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsDeployment](api/beta/deployments.md)

GET/v1/deployments/{deployment\_id}

##### [Update Deployment](api/beta/deployments/update.md)

beta.deployments.update(strdeployment\_id, DeploymentUpdateParams\*\*kwargs)  -> [BetaManagedAgentsDeployment](api/beta/deployments.md)

POST/v1/deployments/{deployment\_id}

##### [Archive Deployment](api/beta/deployments/archive.md)

beta.deployments.archive(strdeployment\_id, DeploymentArchiveParams\*\*kwargs)  -> [BetaManagedAgentsDeployment](api/beta/deployments.md)

POST/v1/deployments/{deployment\_id}/archive

##### [Run Deployment Now](api/beta/deployments/run.md)

beta.deployments.run(strdeployment\_id, DeploymentRunParams\*\*kwargs)  -> [BetaManagedAgentsDeploymentRun](api/beta/deployment_runs.md)

POST/v1/deployments/{deployment\_id}/run

##### [Pause Deployment](api/beta/deployments/pause.md)

beta.deployments.pause(strdeployment\_id, DeploymentPauseParams\*\*kwargs)  -> [BetaManagedAgentsDeployment](api/beta/deployments.md)

POST/v1/deployments/{deployment\_id}/pause

##### [Unpause Deployment](api/beta/deployments/unpause.md)

beta.deployments.unpause(strdeployment\_id, DeploymentUnpauseParams\*\*kwargs)  -> [BetaManagedAgentsDeployment](api/beta/deployments.md)

POST/v1/deployments/{deployment\_id}/unpause

#### BetaDeployment Runs

##### [List Deployment Runs](api/beta/deployment_runs/list.md)

beta.deployment\_runs.list(DeploymentRunListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsDeploymentRun](api/beta/deployment_runs.md)]

GET/v1/deployment\_runs

##### [Get Deployment Run](api/beta/deployment_runs/retrieve.md)

beta.deployment\_runs.retrieve(strdeployment\_run\_id, DeploymentRunRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsDeploymentRun](api/beta/deployment_runs.md)

GET/v1/deployment\_runs/{deployment\_run\_id}

#### BetaVaults

##### [Create Vault](api/beta/vaults/create.md)

beta.vaults.create(VaultCreateParams\*\*kwargs)  -> [BetaManagedAgentsVault](api/beta/vaults.md)

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

beta.vaults.list(VaultListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsVault](api/beta/vaults.md)]

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

beta.vaults.retrieve(strvault\_id, VaultRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsVault](api/beta/vaults.md)

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

beta.vaults.update(strvault\_id, VaultUpdateParams\*\*kwargs)  -> [BetaManagedAgentsVault](api/beta/vaults.md)

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

beta.vaults.delete(strvault\_id, VaultDeleteParams\*\*kwargs)  -> [BetaManagedAgentsDeletedVault](api/beta/vaults.md)

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

beta.vaults.archive(strvault\_id, VaultArchiveParams\*\*kwargs)  -> [BetaManagedAgentsVault](api/beta/vaults.md)

POST/v1/vaults/{vault\_id}/archive

#### BetaVaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

beta.vaults.credentials.create(strvault\_id, CredentialCreateParams\*\*kwargs)  -> [BetaManagedAgentsCredential](api/beta/vaults/credentials.md)

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

beta.vaults.credentials.list(strvault\_id, CredentialListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsCredential](api/beta/vaults/credentials.md)]

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

beta.vaults.credentials.retrieve(strcredential\_id, CredentialRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsCredential](api/beta/vaults/credentials.md)

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

beta.vaults.credentials.update(strcredential\_id, CredentialUpdateParams\*\*kwargs)  -> [BetaManagedAgentsCredential](api/beta/vaults/credentials.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

beta.vaults.credentials.delete(strcredential\_id, CredentialDeleteParams\*\*kwargs)  -> [BetaManagedAgentsDeletedCredential](api/beta/vaults/credentials.md)

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

beta.vaults.credentials.archive(strcredential\_id, CredentialArchiveParams\*\*kwargs)  -> [BetaManagedAgentsCredential](api/beta/vaults/credentials.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

beta.vaults.credentials.mcp\_oauth\_validate(strcredential\_id, CredentialMCPOAuthValidateParams\*\*kwargs)  -> [BetaManagedAgentsCredentialValidation](api/beta/vaults/credentials.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

#### BetaMemory Stores

##### [Create a memory store](api/beta/memory_stores/create.md)

beta.memory\_stores.create(MemoryStoreCreateParams\*\*kwargs)  -> [BetaManagedAgentsMemoryStore](api/beta/memory_stores.md)

POST/v1/memory\_stores

##### [List memory stores](api/beta/memory_stores/list.md)

beta.memory\_stores.list(MemoryStoreListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md)]

GET/v1/memory\_stores

##### [Retrieve a memory store](api/beta/memory_stores/retrieve.md)

beta.memory\_stores.retrieve(strmemory\_store\_id, MemoryStoreRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsMemoryStore](api/beta/memory_stores.md)

GET/v1/memory\_stores/{memory\_store\_id}

##### [Update a memory store](api/beta/memory_stores/update.md)

beta.memory\_stores.update(strmemory\_store\_id, MemoryStoreUpdateParams\*\*kwargs)  -> [BetaManagedAgentsMemoryStore](api/beta/memory_stores.md)

POST/v1/memory\_stores/{memory\_store\_id}

##### [Delete a memory store](api/beta/memory_stores/delete.md)

beta.memory\_stores.delete(strmemory\_store\_id, MemoryStoreDeleteParams\*\*kwargs)  -> [BetaManagedAgentsDeletedMemoryStore](api/beta/memory_stores.md)

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [Archive a memory store](api/beta/memory_stores/archive.md)

beta.memory\_stores.archive(strmemory\_store\_id, MemoryStoreArchiveParams\*\*kwargs)  -> [BetaManagedAgentsMemoryStore](api/beta/memory_stores.md)

POST/v1/memory\_stores/{memory\_store\_id}/archive

#### BetaMemory StoresMemories

##### [Create a memory](api/beta/memory_stores/memories/create.md)

beta.memory\_stores.memories.create(strmemory\_store\_id, MemoryCreateParams\*\*kwargs)  -> [BetaManagedAgentsMemory](api/beta/memory_stores/memories.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/beta/memory_stores/memories/list.md)

beta.memory\_stores.memories.list(strmemory\_store\_id, MemoryListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsMemoryListItem](api/beta/memory_stores/memories.md)]

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/beta/memory_stores/memories/retrieve.md)

beta.memory\_stores.memories.retrieve(strmemory\_id, MemoryRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsMemory](api/beta/memory_stores/memories.md)

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/beta/memory_stores/memories/update.md)

beta.memory\_stores.memories.update(strmemory\_id, MemoryUpdateParams\*\*kwargs)  -> [BetaManagedAgentsMemory](api/beta/memory_stores/memories.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/beta/memory_stores/memories/delete.md)

beta.memory\_stores.memories.delete(strmemory\_id, MemoryDeleteParams\*\*kwargs)  -> [BetaManagedAgentsDeletedMemory](api/beta/memory_stores/memories.md)

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

#### BetaMemory StoresMemory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

beta.memory\_stores.memory\_versions.list(strmemory\_store\_id, MemoryVersionListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md)]

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

beta.memory\_stores.memory\_versions.retrieve(strmemory\_version\_id, MemoryVersionRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

beta.memory\_stores.memory\_versions.redact(strmemory\_version\_id, MemoryVersionRedactParams\*\*kwargs)  -> [BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

#### BetaFiles

##### [Upload File](api/beta/files/upload.md)

beta.files.upload(FileUploadParams\*\*kwargs)  -> [FileMetadata](api/beta/files.md)

POST/v1/files

##### [List Files](api/beta/files/list.md)

beta.files.list(FileListParams\*\*kwargs)  -> SyncPage[[FileMetadata](api/beta/files.md)]

GET/v1/files

##### [Download File](api/beta/files/download.md)

beta.files.download(strfile\_id, FileDownloadParams\*\*kwargs)  -> BinaryResponseContent

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

beta.files.retrieve\_metadata(strfile\_id, FileRetrieveMetadataParams\*\*kwargs)  -> [FileMetadata](api/beta/files.md)

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

beta.files.delete(strfile\_id, FileDeleteParams\*\*kwargs)  -> [DeletedFile](api/beta/files.md)

DELETE/v1/files/{file\_id}

#### BetaSkills

##### [Create Skill](api/beta/skills/create.md)

beta.skills.create(SkillCreateParams\*\*kwargs)  -> [SkillCreateResponse](api/beta/skills.md)

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

beta.skills.list(SkillListParams\*\*kwargs)  -> SyncPageCursor[[SkillListResponse](api/beta/skills.md)]

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

beta.skills.retrieve(strskill\_id, SkillRetrieveParams\*\*kwargs)  -> [SkillRetrieveResponse](api/beta/skills.md)

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

beta.skills.delete(strskill\_id, SkillDeleteParams\*\*kwargs)  -> [SkillDeleteResponse](api/beta/skills.md)

DELETE/v1/skills/{skill\_id}

#### BetaSkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

beta.skills.versions.create(strskill\_id, VersionCreateParams\*\*kwargs)  -> [VersionCreateResponse](api/beta/skills/versions.md)

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

beta.skills.versions.list(strskill\_id, VersionListParams\*\*kwargs)  -> SyncPageCursor[[VersionListResponse](api/beta/skills/versions.md)]

GET/v1/skills/{skill\_id}/versions

##### [Download Skill Version Content](api/beta/skills/versions/download.md)

beta.skills.versions.download(strversion, VersionDownloadParams\*\*kwargs)  -> BinaryResponseContent

GET/v1/skills/{skill\_id}/versions/{version}/content

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

beta.skills.versions.retrieve(strversion, VersionRetrieveParams\*\*kwargs)  -> [VersionRetrieveResponse](api/beta/skills/versions.md)

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

beta.skills.versions.delete(strversion, VersionDeleteParams\*\*kwargs)  -> [VersionDeleteResponse](api/beta/skills/versions.md)

DELETE/v1/skills/{skill\_id}/versions/{version}

#### BetaUser Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

beta.user\_profiles.create(UserProfileCreateParams\*\*kwargs)  -> [BetaUserProfile](api/beta/user_profiles.md)

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

beta.user\_profiles.list(UserProfileListParams\*\*kwargs)  -> SyncPageCursor[[BetaUserProfile](api/beta/user_profiles.md)]

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

beta.user\_profiles.retrieve(struser\_profile\_id, UserProfileRetrieveParams\*\*kwargs)  -> [BetaUserProfile](api/beta/user_profiles.md)

GET/v1/user\_profiles/{user\_profile\_id}

##### [Update User Profile](api/beta/user_profiles/update.md)

beta.user\_profiles.update(struser\_profile\_id, UserProfileUpdateParams\*\*kwargs)  -> [BetaUserProfile](api/beta/user_profiles.md)

POST/v1/user\_profiles/{user\_profile\_id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

beta.user\_profiles.create\_enrollment\_url(struser\_profile\_id, UserProfileCreateEnrollmentURLParams\*\*kwargs)  -> [BetaUserProfileEnrollmentURL](api/beta/user_profiles.md)

POST/v1/user\_profiles/{user\_profile\_id}/enrollment\_url

#### BetaWebhooks

Helpers for receiving and verifying webhook events. Use `unwrap` in your SDK to verify signatures and parse payloads; see the [webhooks guide](managed-agents/webhooks.md) for handler examples.

Possible `data.type` values:

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
