# Beta

Copy page



Go

# Beta

##### ModelsExpand Collapse



type AnthropicBeta interface{…}

One of the following:

string



type AnthropicBeta string

One of the following:

const AnthropicBetaMessageBatches2024\_09\_24 AnthropicBeta = "message-batches-2024-09-24"

const AnthropicBetaPromptCaching2024\_07\_31 AnthropicBeta = "prompt-caching-2024-07-31"

const AnthropicBetaComputerUse2024\_10\_22 AnthropicBeta = "computer-use-2024-10-22"

const AnthropicBetaComputerUse2025\_01\_24 AnthropicBeta = "computer-use-2025-01-24"

const AnthropicBetaPDFs2024\_09\_25 AnthropicBeta = "pdfs-2024-09-25"

const AnthropicBetaTokenCounting2024\_11\_01 AnthropicBeta = "token-counting-2024-11-01"

const AnthropicBetaTokenEfficientTools2025\_02\_19 AnthropicBeta = "token-efficient-tools-2025-02-19"

const AnthropicBetaOutput128k2025\_02\_19 AnthropicBeta = "output-128k-2025-02-19"

const AnthropicBetaFilesAPI2025\_04\_14 AnthropicBeta = "files-api-2025-04-14"

const AnthropicBetaMCPClient2025\_04\_04 AnthropicBeta = "mcp-client-2025-04-04"

const AnthropicBetaMCPClient2025\_11\_20 AnthropicBeta = "mcp-client-2025-11-20"

const AnthropicBetaDevFullThinking2025\_05\_14 AnthropicBeta = "dev-full-thinking-2025-05-14"

const AnthropicBetaInterleavedThinking2025\_05\_14 AnthropicBeta = "interleaved-thinking-2025-05-14"

const AnthropicBetaCodeExecution2025\_05\_22 AnthropicBeta = "code-execution-2025-05-22"

const AnthropicBetaExtendedCacheTTL2025\_04\_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"

const AnthropicBetaContext1m2025\_08\_07 AnthropicBeta = "context-1m-2025-08-07"

const AnthropicBetaContextManagement2025\_06\_27 AnthropicBeta = "context-management-2025-06-27"

const AnthropicBetaModelContextWindowExceeded2025\_08\_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"

const AnthropicBetaSkills2025\_10\_02 AnthropicBeta = "skills-2025-10-02"

const AnthropicBetaFastMode2026\_02\_01 AnthropicBeta = "fast-mode-2026-02-01"

const AnthropicBetaOutput300k2026\_03\_24 AnthropicBeta = "output-300k-2026-03-24"

const AnthropicBetaUserProfiles2026\_03\_24 AnthropicBeta = "user-profiles-2026-03-24"

const AnthropicBetaAdvisorTool2026\_03\_01 AnthropicBeta = "advisor-tool-2026-03-01"

const AnthropicBetaManagedAgents2026\_04\_01 AnthropicBeta = "managed-agents-2026-04-01"

const AnthropicBetaCacheDiagnosis2026\_04\_07 AnthropicBeta = "cache-diagnosis-2026-04-07"

const AnthropicBetaThinkingTokenCount2026\_05\_13 AnthropicBeta = "thinking-token-count-2026-05-13"

const AnthropicBetaServerSideFallback2026\_06\_01 AnthropicBeta = "server-side-fallback-2026-06-01"

const AnthropicBetaFallbackCredit2026\_06\_01 AnthropicBeta = "fallback-credit-2026-06-01"



type BetaAPIError struct{…}

Message string

Type APIError



type BetaAuthenticationError struct{…}

Message string

Type AuthenticationError



type BetaBillingError struct{…}

Message string

Type BillingError



type BetaErrorUnion interface{…}

One of the following:



type BetaInvalidRequestError struct{…}

Message string

Type InvalidRequestError



type BetaAuthenticationError struct{…}

Message string

Type AuthenticationError



type BetaBillingError struct{…}

Message string

Type BillingError



type BetaPermissionError struct{…}

Message string

Type PermissionError



type BetaNotFoundError struct{…}

Message string

Type NotFoundError



type BetaRateLimitError struct{…}

Message string

Type RateLimitError



type BetaGatewayTimeoutError struct{…}

Message string

Type TimeoutError



type BetaAPIError struct{…}

Message string

Type APIError



type BetaOverloadedError struct{…}

Message string

Type OverloadedError



type BetaErrorResponse struct{…}



Error [BetaErrorUnion](api/beta.md)

One of the following:



type BetaInvalidRequestError struct{…}

Message string

Type InvalidRequestError



type BetaAuthenticationError struct{…}

Message string

Type AuthenticationError



type BetaBillingError struct{…}

Message string

Type BillingError



type BetaPermissionError struct{…}

Message string

Type PermissionError



type BetaNotFoundError struct{…}

Message string

Type NotFoundError



type BetaRateLimitError struct{…}

Message string

Type RateLimitError



type BetaGatewayTimeoutError struct{…}

Message string

Type TimeoutError



type BetaAPIError struct{…}

Message string

Type APIError



type BetaOverloadedError struct{…}

Message string

Type OverloadedError

RequestID string

Type Error



type BetaGatewayTimeoutError struct{…}

Message string

Type TimeoutError



type BetaInvalidRequestError struct{…}

Message string

Type InvalidRequestError



type BetaNotFoundError struct{…}

Message string

Type NotFoundError



type BetaOverloadedError struct{…}

Message string

Type OverloadedError



type BetaPermissionError struct{…}

Message string

Type PermissionError



type BetaRateLimitError struct{…}

Message string

Type RateLimitError

#### BetaModels

##### [List Models](api/beta/models/list.md)

client.Beta.Models.List(ctx, params) (\*Page[[BetaModelInfo](api/beta/models.md)], error)

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

client.Beta.Models.Get(ctx, modelID, query) (\*[BetaModelInfo](api/beta/models.md), error)

GET/v1/models/{model\_id}

#### BetaMessages

##### [Create a Message](api/beta/messages/create.md)

client.Beta.Messages.New(ctx, params) (\*[BetaMessage](api/beta/messages.md), error)

POST/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

client.Beta.Messages.CountTokens(ctx, params) (\*[BetaMessageTokensCount](api/beta/messages.md), error)

POST/v1/messages/count\_tokens

#### BetaMessagesBatches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

client.Beta.Messages.Batches.New(ctx, params) (\*[BetaMessageBatch](api/beta/messages/batches.md), error)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

client.Beta.Messages.Batches.Get(ctx, messageBatchID, query) (\*[BetaMessageBatch](api/beta/messages/batches.md), error)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

client.Beta.Messages.Batches.List(ctx, params) (\*Page[[BetaMessageBatch](api/beta/messages/batches.md)], error)

GET/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

client.Beta.Messages.Batches.Cancel(ctx, messageBatchID, body) (\*[BetaMessageBatch](api/beta/messages/batches.md), error)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

client.Beta.Messages.Batches.Delete(ctx, messageBatchID, body) (\*[BetaDeletedMessageBatch](api/beta/messages/batches.md), error)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

client.Beta.Messages.Batches.Results(ctx, messageBatchID, query) (\*[BetaMessageBatchIndividualResponse](api/beta/messages/batches.md), error)

GET/v1/messages/batches/{message\_batch\_id}/results

#### BetaAgents

##### [Create Agent](api/beta/agents/create.md)

client.Beta.Agents.New(ctx, params) (\*[BetaManagedAgentsAgent](api/beta/agents.md), error)

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

client.Beta.Agents.List(ctx, params) (\*PageCursor[[BetaManagedAgentsAgent](api/beta/agents.md)], error)

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

client.Beta.Agents.Get(ctx, agentID, params) (\*[BetaManagedAgentsAgent](api/beta/agents.md), error)

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

client.Beta.Agents.Update(ctx, agentID, params) (\*[BetaManagedAgentsAgent](api/beta/agents.md), error)

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

client.Beta.Agents.Archive(ctx, agentID, body) (\*[BetaManagedAgentsAgent](api/beta/agents.md), error)

POST/v1/agents/{agent\_id}/archive

#### BetaAgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

client.Beta.Agents.Versions.List(ctx, agentID, params) (\*PageCursor[[BetaManagedAgentsAgent](api/beta/agents.md)], error)

GET/v1/agents/{agent\_id}/versions

#### BetaEnvironments

##### [Create Environment](api/beta/environments/create.md)

client.Beta.Environments.New(ctx, params) (\*[BetaEnvironment](api/beta/environments.md), error)

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

client.Beta.Environments.List(ctx, params) (\*PageCursor[[BetaEnvironment](api/beta/environments.md)], error)

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

client.Beta.Environments.Get(ctx, environmentID, query) (\*[BetaEnvironment](api/beta/environments.md), error)

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

client.Beta.Environments.Update(ctx, environmentID, params) (\*[BetaEnvironment](api/beta/environments.md), error)

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

client.Beta.Environments.Delete(ctx, environmentID, body) (\*[BetaEnvironmentDeleteResponse](api/beta/environments.md), error)

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

client.Beta.Environments.Archive(ctx, environmentID, body) (\*[BetaEnvironment](api/beta/environments.md), error)

POST/v1/environments/{environment\_id}/archive

#### BetaEnvironmentsWork

##### [Get Work Item](api/beta/environments/work/retrieve.md)

client.Beta.Environments.Work.Get(ctx, workID, params) (\*[BetaSelfHostedWork](api/beta/environments/work.md), error)

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

client.Beta.Environments.Work.Poll(ctx, environmentID, params) (\*[BetaSelfHostedWork](api/beta/environments/work.md), error)

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

client.Beta.Environments.Work.Ack(ctx, workID, params) (\*[BetaSelfHostedWork](api/beta/environments/work.md), error)

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

client.Beta.Environments.Work.Heartbeat(ctx, workID, params) (\*[BetaSelfHostedWorkHeartbeatResponse](api/beta/environments/work.md), error)

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

client.Beta.Environments.Work.Stop(ctx, workID, params) (\*[BetaSelfHostedWork](api/beta/environments/work.md), error)

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

client.Beta.Environments.Work.List(ctx, environmentID, params) (\*PageCursor[[BetaSelfHostedWork](api/beta/environments/work.md)], error)

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

client.Beta.Environments.Work.Update(ctx, workID, params) (\*[BetaSelfHostedWork](api/beta/environments/work.md), error)

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

client.Beta.Environments.Work.Stats(ctx, environmentID, query) (\*[BetaSelfHostedWorkQueueStats](api/beta/environments/work.md), error)

GET/v1/environments/{environment\_id}/work/stats

#### BetaSessions

##### [Create Session](api/beta/sessions/create.md)

client.Beta.Sessions.New(ctx, params) (\*[BetaManagedAgentsSession](api/beta/sessions.md), error)

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

client.Beta.Sessions.List(ctx, params) (\*BidirectionalPageCursor[[BetaManagedAgentsSession](api/beta/sessions.md)], error)

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

client.Beta.Sessions.Get(ctx, sessionID, query) (\*[BetaManagedAgentsSession](api/beta/sessions.md), error)

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

client.Beta.Sessions.Update(ctx, sessionID, params) (\*[BetaManagedAgentsSession](api/beta/sessions.md), error)

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

client.Beta.Sessions.Delete(ctx, sessionID, body) (\*[BetaManagedAgentsDeletedSession](api/beta/sessions.md), error)

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

client.Beta.Sessions.Archive(ctx, sessionID, body) (\*[BetaManagedAgentsSession](api/beta/sessions.md), error)

POST/v1/sessions/{session\_id}/archive

#### BetaSessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

client.Beta.Sessions.Events.List(ctx, sessionID, params) (\*PageCursor[[BetaManagedAgentsSessionEventUnion](api/beta/sessions/events.md)], error)

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

client.Beta.Sessions.Events.Send(ctx, sessionID, params) (\*[BetaManagedAgentsSendSessionEvents](api/beta/sessions/events.md), error)

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

client.Beta.Sessions.Events.Stream(ctx, sessionID, params) (\*[BetaManagedAgentsStreamSessionEventsUnion](api/beta/sessions/events.md), error)

GET/v1/sessions/{session\_id}/events/stream

#### BetaSessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

client.Beta.Sessions.Resources.Add(ctx, sessionID, params) (\*[BetaManagedAgentsFileResource](api/beta/sessions/resources.md), error)

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

client.Beta.Sessions.Resources.List(ctx, sessionID, params) (\*PageCursor[[BetaManagedAgentsSessionResourceUnion](api/beta/sessions/resources.md)], error)

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

client.Beta.Sessions.Resources.Get(ctx, resourceID, params) (\*[BetaSessionResourceGetResponseUnion](api/beta/sessions/resources.md), error)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

client.Beta.Sessions.Resources.Update(ctx, resourceID, params) (\*[BetaSessionResourceUpdateResponseUnion](api/beta/sessions/resources.md), error)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

client.Beta.Sessions.Resources.Delete(ctx, resourceID, params) (\*[BetaManagedAgentsDeleteSessionResource](api/beta/sessions/resources.md), error)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

#### BetaSessionsThreads

##### [List Session Threads](api/beta/sessions/threads/list.md)

client.Beta.Sessions.Threads.List(ctx, sessionID, params) (\*PageCursor[[BetaManagedAgentsSessionThread](api/beta/sessions/threads.md)], error)

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/beta/sessions/threads/retrieve.md)

client.Beta.Sessions.Threads.Get(ctx, threadID, params) (\*[BetaManagedAgentsSessionThread](api/beta/sessions/threads.md), error)

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/beta/sessions/threads/archive.md)

client.Beta.Sessions.Threads.Archive(ctx, threadID, params) (\*[BetaManagedAgentsSessionThread](api/beta/sessions/threads.md), error)

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

#### BetaSessionsThreadsEvents

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

client.Beta.Sessions.Threads.Events.List(ctx, threadID, params) (\*PageCursor[[BetaManagedAgentsSessionEventUnion](api/beta/sessions/events.md)], error)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

client.Beta.Sessions.Threads.Events.Stream(ctx, threadID, params) (\*[BetaManagedAgentsStreamSessionThreadEventsUnion](api/beta/sessions/threads.md), error)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

#### BetaDeployments

##### [Create Deployment](api/beta/deployments/create.md)

client.Beta.Deployments.New(ctx, params) (\*[BetaManagedAgentsDeployment](api/beta/deployments.md), error)

POST/v1/deployments

##### [List Deployments](api/beta/deployments/list.md)

client.Beta.Deployments.List(ctx, params) (\*PageCursor[[BetaManagedAgentsDeployment](api/beta/deployments.md)], error)

GET/v1/deployments

##### [Get Deployment](api/beta/deployments/retrieve.md)

client.Beta.Deployments.Get(ctx, deploymentID, query) (\*[BetaManagedAgentsDeployment](api/beta/deployments.md), error)

GET/v1/deployments/{deployment\_id}

##### [Update Deployment](api/beta/deployments/update.md)

client.Beta.Deployments.Update(ctx, deploymentID, params) (\*[BetaManagedAgentsDeployment](api/beta/deployments.md), error)

POST/v1/deployments/{deployment\_id}

##### [Archive Deployment](api/beta/deployments/archive.md)

client.Beta.Deployments.Archive(ctx, deploymentID, body) (\*[BetaManagedAgentsDeployment](api/beta/deployments.md), error)

POST/v1/deployments/{deployment\_id}/archive

##### [Run Deployment Now](api/beta/deployments/run.md)

client.Beta.Deployments.Run(ctx, deploymentID, body) (\*[BetaManagedAgentsDeploymentRun](api/beta/deployment_runs.md), error)

POST/v1/deployments/{deployment\_id}/run

##### [Pause Deployment](api/beta/deployments/pause.md)

client.Beta.Deployments.Pause(ctx, deploymentID, body) (\*[BetaManagedAgentsDeployment](api/beta/deployments.md), error)

POST/v1/deployments/{deployment\_id}/pause

##### [Unpause Deployment](api/beta/deployments/unpause.md)

client.Beta.Deployments.Unpause(ctx, deploymentID, body) (\*[BetaManagedAgentsDeployment](api/beta/deployments.md), error)

POST/v1/deployments/{deployment\_id}/unpause

#### BetaDeployment Runs

##### [List Deployment Runs](api/beta/deployment_runs/list.md)

client.Beta.DeploymentRuns.List(ctx, params) (\*PageCursor[[BetaManagedAgentsDeploymentRun](api/beta/deployment_runs.md)], error)

GET/v1/deployment\_runs

##### [Get Deployment Run](api/beta/deployment_runs/retrieve.md)

client.Beta.DeploymentRuns.Get(ctx, deploymentRunID, query) (\*[BetaManagedAgentsDeploymentRun](api/beta/deployment_runs.md), error)

GET/v1/deployment\_runs/{deployment\_run\_id}

#### BetaVaults

##### [Create Vault](api/beta/vaults/create.md)

client.Beta.Vaults.New(ctx, params) (\*[BetaManagedAgentsVault](api/beta/vaults.md), error)

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

client.Beta.Vaults.List(ctx, params) (\*PageCursor[[BetaManagedAgentsVault](api/beta/vaults.md)], error)

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

client.Beta.Vaults.Get(ctx, vaultID, query) (\*[BetaManagedAgentsVault](api/beta/vaults.md), error)

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

client.Beta.Vaults.Update(ctx, vaultID, params) (\*[BetaManagedAgentsVault](api/beta/vaults.md), error)

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

client.Beta.Vaults.Delete(ctx, vaultID, body) (\*[BetaManagedAgentsDeletedVault](api/beta/vaults.md), error)

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

client.Beta.Vaults.Archive(ctx, vaultID, body) (\*[BetaManagedAgentsVault](api/beta/vaults.md), error)

POST/v1/vaults/{vault\_id}/archive

#### BetaVaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

client.Beta.Vaults.Credentials.New(ctx, vaultID, params) (\*[BetaManagedAgentsCredential](api/beta/vaults/credentials.md), error)

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

client.Beta.Vaults.Credentials.List(ctx, vaultID, params) (\*PageCursor[[BetaManagedAgentsCredential](api/beta/vaults/credentials.md)], error)

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

client.Beta.Vaults.Credentials.Get(ctx, credentialID, params) (\*[BetaManagedAgentsCredential](api/beta/vaults/credentials.md), error)

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

client.Beta.Vaults.Credentials.Update(ctx, credentialID, params) (\*[BetaManagedAgentsCredential](api/beta/vaults/credentials.md), error)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

client.Beta.Vaults.Credentials.Delete(ctx, credentialID, params) (\*[BetaManagedAgentsDeletedCredential](api/beta/vaults/credentials.md), error)

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

client.Beta.Vaults.Credentials.Archive(ctx, credentialID, params) (\*[BetaManagedAgentsCredential](api/beta/vaults/credentials.md), error)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

client.Beta.Vaults.Credentials.MCPOAuthValidate(ctx, credentialID, params) (\*[BetaManagedAgentsCredentialValidation](api/beta/vaults/credentials.md), error)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

#### BetaMemory Stores

##### [Create a memory store](api/beta/memory_stores/create.md)

client.Beta.MemoryStores.New(ctx, params) (\*[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md), error)

POST/v1/memory\_stores

##### [List memory stores](api/beta/memory_stores/list.md)

client.Beta.MemoryStores.List(ctx, params) (\*PageCursor[[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md)], error)

GET/v1/memory\_stores

##### [Retrieve a memory store](api/beta/memory_stores/retrieve.md)

client.Beta.MemoryStores.Get(ctx, memoryStoreID, query) (\*[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md), error)

GET/v1/memory\_stores/{memory\_store\_id}

##### [Update a memory store](api/beta/memory_stores/update.md)

client.Beta.MemoryStores.Update(ctx, memoryStoreID, params) (\*[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md), error)

POST/v1/memory\_stores/{memory\_store\_id}

##### [Delete a memory store](api/beta/memory_stores/delete.md)

client.Beta.MemoryStores.Delete(ctx, memoryStoreID, body) (\*[BetaManagedAgentsDeletedMemoryStore](api/beta/memory_stores.md), error)

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [Archive a memory store](api/beta/memory_stores/archive.md)

client.Beta.MemoryStores.Archive(ctx, memoryStoreID, body) (\*[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md), error)

POST/v1/memory\_stores/{memory\_store\_id}/archive

#### BetaMemory StoresMemories

##### [Create a memory](api/beta/memory_stores/memories/create.md)

client.Beta.MemoryStores.Memories.New(ctx, memoryStoreID, params) (\*[BetaManagedAgentsMemory](api/beta/memory_stores/memories.md), error)

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/beta/memory_stores/memories/list.md)

client.Beta.MemoryStores.Memories.List(ctx, memoryStoreID, params) (\*PageCursor[[BetaManagedAgentsMemoryListItemUnion](api/beta/memory_stores/memories.md)], error)

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/beta/memory_stores/memories/retrieve.md)

client.Beta.MemoryStores.Memories.Get(ctx, memoryID, params) (\*[BetaManagedAgentsMemory](api/beta/memory_stores/memories.md), error)

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/beta/memory_stores/memories/update.md)

client.Beta.MemoryStores.Memories.Update(ctx, memoryID, params) (\*[BetaManagedAgentsMemory](api/beta/memory_stores/memories.md), error)

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/beta/memory_stores/memories/delete.md)

client.Beta.MemoryStores.Memories.Delete(ctx, memoryID, params) (\*[BetaManagedAgentsDeletedMemory](api/beta/memory_stores/memories.md), error)

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

#### BetaMemory StoresMemory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

client.Beta.MemoryStores.MemoryVersions.List(ctx, memoryStoreID, params) (\*PageCursor[[BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md)], error)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

client.Beta.MemoryStores.MemoryVersions.Get(ctx, memoryVersionID, params) (\*[BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md), error)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

client.Beta.MemoryStores.MemoryVersions.Redact(ctx, memoryVersionID, params) (\*[BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md), error)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

#### BetaFiles

##### [Upload File](api/beta/files/upload.md)

client.Beta.Files.Upload(ctx, params) (\*[FileMetadata](api/beta/files.md), error)

POST/v1/files

##### [List Files](api/beta/files/list.md)

client.Beta.Files.List(ctx, params) (\*Page[[FileMetadata](api/beta/files.md)], error)

GET/v1/files

##### [Download File](api/beta/files/download.md)

client.Beta.Files.Download(ctx, fileID, query) (\*Response, error)

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

client.Beta.Files.GetMetadata(ctx, fileID, query) (\*[FileMetadata](api/beta/files.md), error)

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

client.Beta.Files.Delete(ctx, fileID, body) (\*[DeletedFile](api/beta/files.md), error)

DELETE/v1/files/{file\_id}

#### BetaSkills

##### [Create Skill](api/beta/skills/create.md)

client.Beta.Skills.New(ctx, params) (\*[BetaSkillNewResponse](api/beta/skills.md), error)

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

client.Beta.Skills.List(ctx, params) (\*PageCursor[[BetaSkillListResponse](api/beta/skills.md)], error)

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

client.Beta.Skills.Get(ctx, skillID, query) (\*[BetaSkillGetResponse](api/beta/skills.md), error)

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

client.Beta.Skills.Delete(ctx, skillID, body) (\*[BetaSkillDeleteResponse](api/beta/skills.md), error)

DELETE/v1/skills/{skill\_id}

#### BetaSkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

client.Beta.Skills.Versions.New(ctx, skillID, params) (\*[BetaSkillVersionNewResponse](api/beta/skills/versions.md), error)

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

client.Beta.Skills.Versions.List(ctx, skillID, params) (\*PageCursor[[BetaSkillVersionListResponse](api/beta/skills/versions.md)], error)

GET/v1/skills/{skill\_id}/versions

##### [Download Skill Version Content](api/beta/skills/versions/download.md)

client.Beta.Skills.Versions.Download(ctx, version, params) (\*Response, error)

GET/v1/skills/{skill\_id}/versions/{version}/content

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

client.Beta.Skills.Versions.Get(ctx, version, params) (\*[BetaSkillVersionGetResponse](api/beta/skills/versions.md), error)

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

client.Beta.Skills.Versions.Delete(ctx, version, params) (\*[BetaSkillVersionDeleteResponse](api/beta/skills/versions.md), error)

DELETE/v1/skills/{skill\_id}/versions/{version}

#### BetaUser Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

client.Beta.UserProfiles.New(ctx, params) (\*[BetaUserProfile](api/beta/user_profiles.md), error)

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

client.Beta.UserProfiles.List(ctx, params) (\*PageCursor[[BetaUserProfile](api/beta/user_profiles.md)], error)

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

client.Beta.UserProfiles.Get(ctx, userProfileID, query) (\*[BetaUserProfile](api/beta/user_profiles.md), error)

GET/v1/user\_profiles/{user\_profile\_id}

##### [Update User Profile](api/beta/user_profiles/update.md)

client.Beta.UserProfiles.Update(ctx, userProfileID, params) (\*[BetaUserProfile](api/beta/user_profiles.md), error)

POST/v1/user\_profiles/{user\_profile\_id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

client.Beta.UserProfiles.NewEnrollmentURL(ctx, userProfileID, body) (\*[BetaUserProfileEnrollmentURL](api/beta/user_profiles.md), error)

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
