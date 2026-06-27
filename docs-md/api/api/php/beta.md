# Beta

Copy page



PHP

# Beta

##### ModelsExpand Collapse



AnthropicBeta

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

[BetaAPIError](api/beta.md)

string message

"api\_error" type



[BetaAuthenticationError](api/beta.md)

string message

"authentication\_error" type



[BetaBillingError](api/beta.md)

string message

"billing\_error" type



[BetaError](api/beta.md)

One of the following:



[BetaInvalidRequestError](api/beta.md)

string message

"invalid\_request\_error" type



[BetaAuthenticationError](api/beta.md)

string message

"authentication\_error" type



[BetaBillingError](api/beta.md)

string message

"billing\_error" type



[BetaPermissionError](api/beta.md)

string message

"permission\_error" type



[BetaNotFoundError](api/beta.md)

string message

"not\_found\_error" type



[BetaRateLimitError](api/beta.md)

string message

"rate\_limit\_error" type



[BetaGatewayTimeoutError](api/beta.md)

string message

"timeout\_error" type



[BetaAPIError](api/beta.md)

string message

"api\_error" type



[BetaOverloadedError](api/beta.md)

string message

"overloaded\_error" type



[BetaErrorResponse](api/beta.md)

[BetaError](api/beta.md) error

?string requestID

"error" type



[BetaGatewayTimeoutError](api/beta.md)

string message

"timeout\_error" type



[BetaInvalidRequestError](api/beta.md)

string message

"invalid\_request\_error" type



[BetaNotFoundError](api/beta.md)

string message

"not\_found\_error" type



[BetaOverloadedError](api/beta.md)

string message

"overloaded\_error" type



[BetaPermissionError](api/beta.md)

string message

"permission\_error" type



[BetaRateLimitError](api/beta.md)

string message

"rate\_limit\_error" type

#### BetaModels

##### [List Models](api/beta/models/list.md)

$client->beta->models->list(?string afterID, ?string beforeID, ?int limit, ?list<AnthropicBeta> betas): Page<[BetaModelInfo](api/beta/models.md)>

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

$client->beta->models->retrieve(string modelID, ?list<AnthropicBeta> betas): [BetaModelInfo](api/beta/models.md)

GET/v1/models/{model\_id}

#### BetaMessages

##### [Create a Message](api/beta/messages/create.md)

$client->beta->messages->create(int maxTokens, list<[BetaMessageParam](api/beta/messages.md)> messages, Model model, ?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl, ?[Container](api/beta/messages/create.md) container, ?[BetaContextManagementConfig](api/beta/messages.md) contextManagement, ?[BetaDiagnosticsParam](api/beta/messages.md) diagnostics, ?string fallbackCreditToken, ?list<[BetaFallbackParam](api/beta/messages.md)> fallbacks, ?string inferenceGeo, ?list<[BetaRequestMCPServerURLDefinition](api/beta/messages.md)> mcpServers, ?[BetaMetadata](api/beta/messages.md) metadata, ?[BetaOutputConfig](api/beta/messages.md) outputConfig, ?[BetaJSONOutputFormat](api/beta/messages.md) outputFormat, ?[ServiceTier](api/beta/messages/create.md) serviceTier, ?[Speed](api/beta/messages/create.md) speed, ?list<string> stopSequences, ?[System](api/beta/messages/create.md) system, ?float temperature, ?[BetaThinkingConfigParam](api/beta/messages.md) thinking, ?[BetaToolChoice](api/beta/messages.md) toolChoice, ?list<[BetaToolUnion](api/beta/messages.md)> tools, ?int topK, ?float topP, ?string userProfileID, ?list<AnthropicBeta> betas): [BetaMessage](api/beta/messages.md)

POST/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

$client->beta->messages->countTokens(list<[BetaMessageParam](api/beta/messages.md)> messages, Model model, ?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl, ?[BetaContextManagementConfig](api/beta/messages.md) contextManagement, ?list<[BetaRequestMCPServerURLDefinition](api/beta/messages.md)> mcpServers, ?[BetaOutputConfig](api/beta/messages.md) outputConfig, ?[BetaJSONOutputFormat](api/beta/messages.md) outputFormat, ?[Speed](api/beta/messages/count_tokens.md) speed, ?[System](api/beta/messages/count_tokens.md) system, ?[BetaThinkingConfigParam](api/beta/messages.md) thinking, ?[BetaToolChoice](api/beta/messages.md) toolChoice, ?list<Tool> tools, ?list<AnthropicBeta> betas): [BetaMessageTokensCount](api/beta/messages.md)

POST/v1/messages/count\_tokens

#### BetaMessagesBatches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

$client->beta->messages->batches->create(list<Request> requests, ?list<AnthropicBeta> betas): [MessageBatch](api/beta/messages/batches.md)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

$client->beta->messages->batches->retrieve(string messageBatchID, ?list<AnthropicBeta> betas): [MessageBatch](api/beta/messages/batches.md)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

$client->beta->messages->batches->list(?string afterID, ?string beforeID, ?int limit, ?list<AnthropicBeta> betas): Page<[MessageBatch](api/beta/messages/batches.md)>

GET/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

$client->beta->messages->batches->cancel(string messageBatchID, ?list<AnthropicBeta> betas): [MessageBatch](api/beta/messages/batches.md)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

$client->beta->messages->batches->delete(string messageBatchID, ?list<AnthropicBeta> betas): [DeletedMessageBatch](api/beta/messages/batches.md)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

$client->beta->messages->batches->results(string messageBatchID, ?list<AnthropicBeta> betas): [MessageBatchIndividualResponse](api/beta/messages/batches.md)

GET/v1/messages/batches/{message\_batch\_id}/results

#### BetaAgents

##### [Create Agent](api/beta/agents/create.md)

$client->beta->agents->create([Model](api/beta/agents/create.md) model, string name, ?string description, ?list<[BetaManagedAgentsURLMCPServerParams](api/beta/agents.md)> mcpServers, ?array<string,string> metadata, ?[BetaManagedAgentsMultiagentParams](api/beta/sessions.md) multiagent, ?list<[BetaManagedAgentsSkillParams](api/beta/agents.md)> skills, ?string system, ?list<Tool> tools, ?list<AnthropicBeta> betas): [BetaManagedAgentsAgent](api/beta/agents.md)

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

$client->beta->agents->list(?\Datetime createdAtGte, ?\Datetime createdAtLte, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsAgent](api/beta/agents.md)>

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

$client->beta->agents->retrieve(string agentID, ?int version, ?list<AnthropicBeta> betas): [BetaManagedAgentsAgent](api/beta/agents.md)

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

$client->beta->agents->update(string agentID, int version, ?string description, ?list<[BetaManagedAgentsURLMCPServerParams](api/beta/agents.md)> mcpServers, ?array<string,string> metadata, ?[Model](api/beta/agents/update.md) model, ?[BetaManagedAgentsMultiagentParams](api/beta/sessions.md) multiagent, ?string name, ?list<[BetaManagedAgentsSkillParams](api/beta/agents.md)> skills, ?string system, ?list<Tool> tools, ?list<AnthropicBeta> betas): [BetaManagedAgentsAgent](api/beta/agents.md)

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

$client->beta->agents->archive(string agentID, ?list<AnthropicBeta> betas): [BetaManagedAgentsAgent](api/beta/agents.md)

POST/v1/agents/{agent\_id}/archive

#### BetaAgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

$client->beta->agents->versions->list(string agentID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsAgent](api/beta/agents.md)>

GET/v1/agents/{agent\_id}/versions

#### BetaEnvironments

##### [Create Environment](api/beta/environments/create.md)

$client->beta->environments->create(string name, ?[Config](api/beta/environments/create.md) config, ?string description, ?array<string,string> metadata, ?[Scope](api/beta/environments/create.md) scope, ?list<AnthropicBeta> betas): [BetaEnvironment](api/beta/environments.md)

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

$client->beta->environments->list(?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[BetaEnvironment](api/beta/environments.md)>

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

$client->beta->environments->retrieve(string environmentID, ?list<AnthropicBeta> betas): [BetaEnvironment](api/beta/environments.md)

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

$client->beta->environments->update(string environmentID, ?[Config](api/beta/environments/update.md) config, ?string description, ?array<string,string> metadata, ?string name, ?[Scope](api/beta/environments/update.md) scope, ?list<AnthropicBeta> betas): [BetaEnvironment](api/beta/environments.md)

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

$client->beta->environments->delete(string environmentID, ?list<AnthropicBeta> betas): [BetaEnvironmentDeleteResponse](api/beta/environments.md)

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

$client->beta->environments->archive(string environmentID, ?list<AnthropicBeta> betas): [BetaEnvironment](api/beta/environments.md)

POST/v1/environments/{environment\_id}/archive

#### BetaEnvironmentsWork

##### [Get Work Item](api/beta/environments/work/retrieve.md)

$client->beta->environments->work->retrieve(string workID, string environmentID, ?list<AnthropicBeta> betas): [SelfHostedWork](api/beta/environments/work.md)

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

$client->beta->environments->work->poll(string environmentID, ?int blockMs, ?int reclaimOlderThanMs, ?list<AnthropicBeta> betas, ?string anthropicWorkerID): [SelfHostedWork](api/beta/environments/work.md)

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

$client->beta->environments->work->ack(string workID, string environmentID, ?list<AnthropicBeta> betas): [SelfHostedWork](api/beta/environments/work.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

$client->beta->environments->work->heartbeat(string workID, string environmentID, ?int desiredTTLSeconds, ?string expectedLastHeartbeat, ?list<AnthropicBeta> betas): [SelfHostedWorkHeartbeatResponse](api/beta/environments/work.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

$client->beta->environments->work->stop(string workID, string environmentID, ?bool force, ?list<AnthropicBeta> betas): [SelfHostedWork](api/beta/environments/work.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

$client->beta->environments->work->list(string environmentID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[SelfHostedWork](api/beta/environments/work.md)>

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

$client->beta->environments->work->update(string workID, string environmentID, array<string,string> metadata, ?list<AnthropicBeta> betas): [SelfHostedWork](api/beta/environments/work.md)

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

$client->beta->environments->work->stats(string environmentID, ?list<AnthropicBeta> betas): [SelfHostedWorkQueueStats](api/beta/environments/work.md)

GET/v1/environments/{environment\_id}/work/stats

#### BetaSessions

##### [Create Session](api/beta/sessions/create.md)

$client->beta->sessions->create([Agent](api/beta/sessions/create.md) agent, string environmentID, ?array<string,string> metadata, ?list<Resource> resources, ?string title, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): [BetaManagedAgentsSession](api/beta/sessions.md)

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

$client->beta->sessions->list(?string agentID, ?int agentVersion, ?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?string deploymentID, ?bool includeArchived, ?int limit, ?string memoryStoreID, ?[Order](api/beta/sessions/list.md) order, ?string page, ?list<Status> statuses, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsSession](api/beta/sessions.md)>

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

$client->beta->sessions->retrieve(string sessionID, ?list<AnthropicBeta> betas): [BetaManagedAgentsSession](api/beta/sessions.md)

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

$client->beta->sessions->update(string sessionID, ?[BetaManagedAgentsSessionAgentUpdate](api/beta/sessions.md) agent, ?array<string,string> metadata, ?string title, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): [BetaManagedAgentsSession](api/beta/sessions.md)

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

$client->beta->sessions->delete(string sessionID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeletedSession](api/beta/sessions.md)

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

$client->beta->sessions->archive(string sessionID, ?list<AnthropicBeta> betas): [BetaManagedAgentsSession](api/beta/sessions.md)

POST/v1/sessions/{session\_id}/archive

#### BetaSessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

$client->beta->sessions->events->list(string sessionID, ?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?int limit, ?[Order](api/beta/sessions/events/list.md) order, ?string page, ?list<string> types, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsSessionEvent](api/beta/sessions/events.md)>

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

$client->beta->sessions->events->send(string sessionID, list<[ManagedAgentsEventParams](api/beta/sessions/events.md)> events, ?list<AnthropicBeta> betas): [ManagedAgentsSendSessionEvents](api/beta/sessions/events.md)

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

$client->beta->sessions->events->stream(string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsStreamSessionEvents](api/beta/sessions/events.md)

GET/v1/sessions/{session\_id}/events/stream

#### BetaSessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

$client->beta->sessions->resources->add(string sessionID, string fileID, [Type](api/beta/sessions/resources/add.md) type, ?string mountPath, ?list<AnthropicBeta> betas): [ManagedAgentsFileResource](api/beta/sessions/resources.md)

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

$client->beta->sessions->resources->list(string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsSessionResource](api/beta/sessions/resources.md)>

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

$client->beta->sessions->resources->retrieve(string resourceID, string sessionID, ?list<AnthropicBeta> betas): [ResourceGetResponse](api/beta/sessions/resources.md)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

$client->beta->sessions->resources->update(string resourceID, string sessionID, string authorizationToken, ?list<AnthropicBeta> betas): [ResourceUpdateResponse](api/beta/sessions/resources.md)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

$client->beta->sessions->resources->delete(string resourceID, string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsDeleteSessionResource](api/beta/sessions/resources.md)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

#### BetaSessionsThreads

##### [List Session Threads](api/beta/sessions/threads/list.md)

$client->beta->sessions->threads->list(string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsSessionThread](api/beta/sessions/threads.md)>

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/beta/sessions/threads/retrieve.md)

$client->beta->sessions->threads->retrieve(string threadID, string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsSessionThread](api/beta/sessions/threads.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/beta/sessions/threads/archive.md)

$client->beta->sessions->threads->archive(string threadID, string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsSessionThread](api/beta/sessions/threads.md)

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

#### BetaSessionsThreadsEvents

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

$client->beta->sessions->threads->events->list(string threadID, string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsSessionEvent](api/beta/sessions/events.md)>

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

$client->beta->sessions->threads->events->stream(string threadID, string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsStreamSessionThreadEvents](api/beta/sessions/threads.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

#### BetaDeployments

##### [Create Deployment](api/beta/deployments/create.md)

$client->beta->deployments->create([Agent](api/beta/deployments/create.md) agent, string environmentID, list<[BetaManagedAgentsDeploymentInitialEventParams](api/beta/deployments.md)> initialEvents, string name, ?string description, ?array<string,string> metadata, ?list<Resource> resources, ?[BetaManagedAgentsScheduleParams](api/beta/deployments.md) schedule, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeployment](api/beta/deployments.md)

POST/v1/deployments

##### [List Deployments](api/beta/deployments/list.md)

$client->beta->deployments->list(?string agentID, ?\Datetime createdAtGte, ?\Datetime createdAtLte, ?bool includeArchived, ?int limit, ?string page, ?[BetaManagedAgentsDeploymentStatus](api/beta/deployments.md) status, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsDeployment](api/beta/deployments.md)>

GET/v1/deployments

##### [Get Deployment](api/beta/deployments/retrieve.md)

$client->beta->deployments->retrieve(string deploymentID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeployment](api/beta/deployments.md)

GET/v1/deployments/{deployment\_id}

##### [Update Deployment](api/beta/deployments/update.md)

$client->beta->deployments->update(string deploymentID, ?[Agent](api/beta/deployments/update.md) agent, ?string description, ?string environmentID, ?list<[BetaManagedAgentsDeploymentInitialEventParams](api/beta/deployments.md)> initialEvents, ?array<string,string> metadata, ?string name, ?list<Resource> resources, ?[BetaManagedAgentsScheduleParams](api/beta/deployments.md) schedule, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeployment](api/beta/deployments.md)

POST/v1/deployments/{deployment\_id}

##### [Archive Deployment](api/beta/deployments/archive.md)

$client->beta->deployments->archive(string deploymentID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeployment](api/beta/deployments.md)

POST/v1/deployments/{deployment\_id}/archive

##### [Run Deployment Now](api/beta/deployments/run.md)

$client->beta->deployments->run(string deploymentID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeploymentRun](api/beta/deployment_runs.md)

POST/v1/deployments/{deployment\_id}/run

##### [Pause Deployment](api/beta/deployments/pause.md)

$client->beta->deployments->pause(string deploymentID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeployment](api/beta/deployments.md)

POST/v1/deployments/{deployment\_id}/pause

##### [Unpause Deployment](api/beta/deployments/unpause.md)

$client->beta->deployments->unpause(string deploymentID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeployment](api/beta/deployments.md)

POST/v1/deployments/{deployment\_id}/unpause

#### BetaDeployment Runs

##### [List Deployment Runs](api/beta/deployment_runs/list.md)

$client->beta->deploymentRuns->list(?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?string deploymentID, ?bool hasError, ?int limit, ?string page, ?[BetaManagedAgentsTriggerType](api/beta/deployment_runs.md) triggerType, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsDeploymentRun](api/beta/deployment_runs.md)>

GET/v1/deployment\_runs

##### [Get Deployment Run](api/beta/deployment_runs/retrieve.md)

$client->beta->deploymentRuns->retrieve(string deploymentRunID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeploymentRun](api/beta/deployment_runs.md)

GET/v1/deployment\_runs/{deployment\_run\_id}

#### BetaVaults

##### [Create Vault](api/beta/vaults/create.md)

$client->beta->vaults->create(string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): [BetaManagedAgentsVault](api/beta/vaults.md)

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

$client->beta->vaults->list(?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsVault](api/beta/vaults.md)>

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

$client->beta->vaults->retrieve(string vaultID, ?list<AnthropicBeta> betas): [BetaManagedAgentsVault](api/beta/vaults.md)

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

$client->beta->vaults->update(string vaultID, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): [BetaManagedAgentsVault](api/beta/vaults.md)

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

$client->beta->vaults->delete(string vaultID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeletedVault](api/beta/vaults.md)

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

$client->beta->vaults->archive(string vaultID, ?list<AnthropicBeta> betas): [BetaManagedAgentsVault](api/beta/vaults.md)

POST/v1/vaults/{vault\_id}/archive

#### BetaVaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

$client->beta->vaults->credentials->create(string vaultID, [Auth](api/beta/vaults/credentials/create.md) auth, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): [ManagedAgentsCredential](api/beta/vaults/credentials.md)

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

$client->beta->vaults->credentials->list(string vaultID, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsCredential](api/beta/vaults/credentials.md)>

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

$client->beta->vaults->credentials->retrieve(string credentialID, string vaultID, ?list<AnthropicBeta> betas): [ManagedAgentsCredential](api/beta/vaults/credentials.md)

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

$client->beta->vaults->credentials->update(string credentialID, string vaultID, ?[Auth](api/beta/vaults/credentials/update.md) auth, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): [ManagedAgentsCredential](api/beta/vaults/credentials.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

$client->beta->vaults->credentials->delete(string credentialID, string vaultID, ?list<AnthropicBeta> betas): [ManagedAgentsDeletedCredential](api/beta/vaults/credentials.md)

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

$client->beta->vaults->credentials->archive(string credentialID, string vaultID, ?list<AnthropicBeta> betas): [ManagedAgentsCredential](api/beta/vaults/credentials.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

$client->beta->vaults->credentials->mcpOAuthValidate(string credentialID, string vaultID, ?list<AnthropicBeta> betas): [ManagedAgentsCredentialValidation](api/beta/vaults/credentials.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

#### BetaMemory Stores

##### [Create a memory store](api/beta/memory_stores/create.md)

$client->beta->memoryStores->create(string name, ?string description, ?array<string,string> metadata, ?list<AnthropicBeta> betas): [BetaManagedAgentsMemoryStore](api/beta/memory_stores.md)

POST/v1/memory\_stores

##### [List memory stores](api/beta/memory_stores/list.md)

$client->beta->memoryStores->list(?\Datetime createdAtGte, ?\Datetime createdAtLte, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md)>

GET/v1/memory\_stores

##### [Retrieve a memory store](api/beta/memory_stores/retrieve.md)

$client->beta->memoryStores->retrieve(string memoryStoreID, ?list<AnthropicBeta> betas): [BetaManagedAgentsMemoryStore](api/beta/memory_stores.md)

GET/v1/memory\_stores/{memory\_store\_id}

##### [Update a memory store](api/beta/memory_stores/update.md)

$client->beta->memoryStores->update(string memoryStoreID, ?string description, ?array<string,string> metadata, ?string name, ?list<AnthropicBeta> betas): [BetaManagedAgentsMemoryStore](api/beta/memory_stores.md)

POST/v1/memory\_stores/{memory\_store\_id}

##### [Delete a memory store](api/beta/memory_stores/delete.md)

$client->beta->memoryStores->delete(string memoryStoreID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeletedMemoryStore](api/beta/memory_stores.md)

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [Archive a memory store](api/beta/memory_stores/archive.md)

$client->beta->memoryStores->archive(string memoryStoreID, ?list<AnthropicBeta> betas): [BetaManagedAgentsMemoryStore](api/beta/memory_stores.md)

POST/v1/memory\_stores/{memory\_store\_id}/archive

#### BetaMemory StoresMemories

##### [Create a memory](api/beta/memory_stores/memories/create.md)

$client->beta->memoryStores->memories->create(string memoryStoreID, ?string content, string path, ?[ManagedAgentsMemoryView](api/beta/memory_stores/memories.md) view, ?list<AnthropicBeta> betas): [ManagedAgentsMemory](api/beta/memory_stores/memories.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/beta/memory_stores/memories/list.md)

$client->beta->memoryStores->memories->list(string memoryStoreID, ?int depth, ?int limit, ?[Order](api/beta/memory_stores/memories/list.md) order, ?string orderBy, ?string page, ?string pathPrefix, ?[ManagedAgentsMemoryView](api/beta/memory_stores/memories.md) view, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsMemoryListItem](api/beta/memory_stores/memories.md)>

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/beta/memory_stores/memories/retrieve.md)

$client->beta->memoryStores->memories->retrieve(string memoryID, string memoryStoreID, ?[ManagedAgentsMemoryView](api/beta/memory_stores/memories.md) view, ?list<AnthropicBeta> betas): [ManagedAgentsMemory](api/beta/memory_stores/memories.md)

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/beta/memory_stores/memories/update.md)

$client->beta->memoryStores->memories->update(string memoryID, string memoryStoreID, ?[ManagedAgentsMemoryView](api/beta/memory_stores/memories.md) view, ?string content, ?string path, ?[ManagedAgentsPrecondition](api/beta/memory_stores/memories.md) precondition, ?list<AnthropicBeta> betas): [ManagedAgentsMemory](api/beta/memory_stores/memories.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/beta/memory_stores/memories/delete.md)

$client->beta->memoryStores->memories->delete(string memoryID, string memoryStoreID, ?string expectedContentSha256, ?list<AnthropicBeta> betas): [ManagedAgentsDeletedMemory](api/beta/memory_stores/memories.md)

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

#### BetaMemory StoresMemory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

$client->beta->memoryStores->memoryVersions->list(string memoryStoreID, ?string apiKeyID, ?\Datetime createdAtGte, ?\Datetime createdAtLte, ?int limit, ?string memoryID, ?[ManagedAgentsMemoryVersionOperation](api/beta/memory_stores/memory_versions.md) operation, ?string page, ?string sessionID, ?[ManagedAgentsMemoryView](api/beta/memory_stores/memories.md) view, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md)>

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

$client->beta->memoryStores->memoryVersions->retrieve(string memoryVersionID, string memoryStoreID, ?[ManagedAgentsMemoryView](api/beta/memory_stores/memories.md) view, ?list<AnthropicBeta> betas): [ManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

$client->beta->memoryStores->memoryVersions->redact(string memoryVersionID, string memoryStoreID, ?list<AnthropicBeta> betas): [ManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

#### BetaFiles

##### [Upload File](api/beta/files/upload.md)

$client->beta->files->upload(string file, ?list<AnthropicBeta> betas): [FileMetadata](api/beta/files.md)

POST/v1/files

##### [List Files](api/beta/files/list.md)

$client->beta->files->list(?string afterID, ?string beforeID, ?int limit, ?string scopeID, ?list<AnthropicBeta> betas): Page<[FileMetadata](api/beta/files.md)>

GET/v1/files

##### [Download File](api/beta/files/download.md)

$client->beta->files->download(string fileID, ?list<AnthropicBeta> betas): download

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

$client->beta->files->retrieveMetadata(string fileID, ?list<AnthropicBeta> betas): [FileMetadata](api/beta/files.md)

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

$client->beta->files->delete(string fileID, ?list<AnthropicBeta> betas): [DeletedFile](api/beta/files.md)

DELETE/v1/files/{file\_id}

#### BetaSkills

##### [Create Skill](api/beta/skills/create.md)

$client->beta->skills->create(?string displayTitle, ?list<string> files, ?list<AnthropicBeta> betas): [SkillNewResponse](api/beta/skills.md)

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

$client->beta->skills->list(?int limit, ?string page, ?string source, ?list<AnthropicBeta> betas): PageCursor<[SkillListResponse](api/beta/skills.md)>

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

$client->beta->skills->retrieve(string skillID, ?list<AnthropicBeta> betas): [SkillGetResponse](api/beta/skills.md)

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

$client->beta->skills->delete(string skillID, ?list<AnthropicBeta> betas): [SkillDeleteResponse](api/beta/skills.md)

DELETE/v1/skills/{skill\_id}

#### BetaSkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

$client->beta->skills->versions->create(string skillID, ?list<string> files, ?list<AnthropicBeta> betas): [VersionNewResponse](api/beta/skills/versions.md)

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

$client->beta->skills->versions->list(string skillID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[VersionListResponse](api/beta/skills/versions.md)>

GET/v1/skills/{skill\_id}/versions

##### [Download Skill Version Content](api/beta/skills/versions/download.md)

$client->beta->skills->versions->download(string version, string skillID, ?list<AnthropicBeta> betas): download

GET/v1/skills/{skill\_id}/versions/{version}/content

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

$client->beta->skills->versions->retrieve(string version, string skillID, ?list<AnthropicBeta> betas): [VersionGetResponse](api/beta/skills/versions.md)

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

$client->beta->skills->versions->delete(string version, string skillID, ?list<AnthropicBeta> betas): [VersionDeleteResponse](api/beta/skills/versions.md)

DELETE/v1/skills/{skill\_id}/versions/{version}

#### BetaUser Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

$client->beta->userProfiles->create(?string externalID, ?array<string,string> metadata, ?string name, ?[Relationship](api/beta/user_profiles/create.md) relationship, ?list<AnthropicBeta> betas): [BetaUserProfile](api/beta/user_profiles.md)

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

$client->beta->userProfiles->list(?int limit, ?[Order](api/beta/user_profiles/list.md) order, ?string page, ?list<AnthropicBeta> betas): PageCursor<[BetaUserProfile](api/beta/user_profiles.md)>

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

$client->beta->userProfiles->retrieve(string userProfileID, ?list<AnthropicBeta> betas): [BetaUserProfile](api/beta/user_profiles.md)

GET/v1/user\_profiles/{user\_profile\_id}

##### [Update User Profile](api/beta/user_profiles/update.md)

$client->beta->userProfiles->update(string userProfileID, ?string externalID, ?array<string,string> metadata, ?string name, ?[Relationship](api/beta/user_profiles/update.md) relationship, ?list<AnthropicBeta> betas): [BetaUserProfile](api/beta/user_profiles.md)

POST/v1/user\_profiles/{user\_profile\_id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

$client->beta->userProfiles->createEnrollmentURL(string userProfileID, ?list<AnthropicBeta> betas): [BetaUserProfileEnrollmentURL](api/beta/user_profiles.md)

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
