# Beta

Copy page



C#

# Beta

##### ModelsExpand Collapse



class BetaApiError:

required string Message

JsonElement Type "api\_error"constant



class BetaAuthenticationError:

required string Message

JsonElement Type "authentication\_error"constant



class BetaBillingError:

required string Message

JsonElement Type "billing\_error"constant



class BetaError: A class that can be one of several variants.union 



class BetaInvalidRequestError:

required string Message

JsonElement Type "invalid\_request\_error"constant



class BetaAuthenticationError:

required string Message

JsonElement Type "authentication\_error"constant



class BetaBillingError:

required string Message

JsonElement Type "billing\_error"constant



class BetaPermissionError:

required string Message

JsonElement Type "permission\_error"constant



class BetaNotFoundError:

required string Message

JsonElement Type "not\_found\_error"constant



class BetaRateLimitError:

required string Message

JsonElement Type "rate\_limit\_error"constant



class BetaGatewayTimeoutError:

required string Message

JsonElement Type "timeout\_error"constant



class BetaApiError:

required string Message

JsonElement Type "api\_error"constant



class BetaOverloadedError:

required string Message

JsonElement Type "overloaded\_error"constant



class BetaErrorResponse:



required [BetaError](api/beta.md) Error

One of the following:



class BetaInvalidRequestError:

required string Message

JsonElement Type "invalid\_request\_error"constant



class BetaAuthenticationError:

required string Message

JsonElement Type "authentication\_error"constant



class BetaBillingError:

required string Message

JsonElement Type "billing\_error"constant



class BetaPermissionError:

required string Message

JsonElement Type "permission\_error"constant



class BetaNotFoundError:

required string Message

JsonElement Type "not\_found\_error"constant



class BetaRateLimitError:

required string Message

JsonElement Type "rate\_limit\_error"constant



class BetaGatewayTimeoutError:

required string Message

JsonElement Type "timeout\_error"constant



class BetaApiError:

required string Message

JsonElement Type "api\_error"constant



class BetaOverloadedError:

required string Message

JsonElement Type "overloaded\_error"constant

required string? RequestID

JsonElement Type "error"constant



class BetaGatewayTimeoutError:

required string Message

JsonElement Type "timeout\_error"constant



class BetaInvalidRequestError:

required string Message

JsonElement Type "invalid\_request\_error"constant



class BetaNotFoundError:

required string Message

JsonElement Type "not\_found\_error"constant



class BetaOverloadedError:

required string Message

JsonElement Type "overloaded\_error"constant



class BetaPermissionError:

required string Message

JsonElement Type "permission\_error"constant



class BetaRateLimitError:

required string Message

JsonElement Type "rate\_limit\_error"constant

#### BetaModels

##### [List Models](api/beta/models/list.md)

[ModelListPageResponse](api/beta/models.md) Beta.Models.List(ModelListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

[BetaModelInfo](api/beta/models.md) Beta.Models.Retrieve(ModelRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/models/{model\_id}

#### BetaMessages

##### [Create a Message](api/beta/messages/create.md)

[BetaMessage](api/beta/messages.md) Beta.Messages.Create(MessageCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

[BetaMessageTokensCount](api/beta/messages.md) Beta.Messages.CountTokens(MessageCountTokensParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages/count\_tokens

#### BetaMessagesBatches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

[BetaMessageBatch](api/beta/messages/batches.md) Beta.Messages.Batches.Create(BatchCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

[BetaMessageBatch](api/beta/messages/batches.md) Beta.Messages.Batches.Retrieve(BatchRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

[BatchListPageResponse](api/beta/messages/batches.md) Beta.Messages.Batches.List(BatchListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

[BetaMessageBatch](api/beta/messages/batches.md) Beta.Messages.Batches.Cancel(BatchCancelParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

[BetaDeletedMessageBatch](api/beta/messages/batches.md) Beta.Messages.Batches.Delete(BatchDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

[BetaMessageBatchIndividualResponse](api/beta/messages/batches.md) Beta.Messages.Batches.ResultsStreaming(BatchResultsParamsparameters, CancellationTokencancellationToken = default)

GET/v1/messages/batches/{message\_batch\_id}/results

#### BetaAgents

##### [Create Agent](api/beta/agents/create.md)

[BetaManagedAgentsAgent](api/beta/agents.md) Beta.Agents.Create(AgentCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

[AgentListPageResponse](api/beta/agents.md) Beta.Agents.List(AgentListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

[BetaManagedAgentsAgent](api/beta/agents.md) Beta.Agents.Retrieve(AgentRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

[BetaManagedAgentsAgent](api/beta/agents.md) Beta.Agents.Update(AgentUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

[BetaManagedAgentsAgent](api/beta/agents.md) Beta.Agents.Archive(AgentArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/agents/{agent\_id}/archive

#### BetaAgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

[VersionListPageResponse](api/beta/agents/versions.md) Beta.Agents.Versions.List(VersionListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/agents/{agent\_id}/versions

#### BetaEnvironments

##### [Create Environment](api/beta/environments/create.md)

[BetaEnvironment](api/beta/environments.md) Beta.Environments.Create(EnvironmentCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

[EnvironmentListPageResponse](api/beta/environments.md) Beta.Environments.List(EnvironmentListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

[BetaEnvironment](api/beta/environments.md) Beta.Environments.Retrieve(EnvironmentRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

[BetaEnvironment](api/beta/environments.md) Beta.Environments.Update(EnvironmentUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

[BetaEnvironmentDeleteResponse](api/beta/environments.md) Beta.Environments.Delete(EnvironmentDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

[BetaEnvironment](api/beta/environments.md) Beta.Environments.Archive(EnvironmentArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments/{environment\_id}/archive

#### BetaEnvironmentsWork

##### [Get Work Item](api/beta/environments/work/retrieve.md)

[BetaSelfHostedWork](api/beta/environments/work.md) Beta.Environments.Work.Retrieve(WorkRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

[BetaSelfHostedWork](api/beta/environments/work.md)? Beta.Environments.Work.Poll(WorkPollParamsparameters, CancellationTokencancellationToken = default)

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

[BetaSelfHostedWork](api/beta/environments/work.md) Beta.Environments.Work.Ack(WorkAckParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

[BetaSelfHostedWorkHeartbeatResponse](api/beta/environments/work.md) Beta.Environments.Work.Heartbeat(WorkHeartbeatParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

[BetaSelfHostedWork](api/beta/environments/work.md) Beta.Environments.Work.Stop(WorkStopParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

[BetaSelfHostedWorkListResponse](api/beta/environments/work.md) Beta.Environments.Work.List(WorkListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

[BetaSelfHostedWork](api/beta/environments/work.md) Beta.Environments.Work.Update(WorkUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

[BetaSelfHostedWorkQueueStats](api/beta/environments/work.md) Beta.Environments.Work.Stats(WorkStatsParamsparameters, CancellationTokencancellationToken = default)

GET/v1/environments/{environment\_id}/work/stats

#### BetaSessions

##### [Create Session](api/beta/sessions/create.md)

[BetaManagedAgentsSession](api/beta/sessions.md) Beta.Sessions.Create(SessionCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

[SessionListPageResponse](api/beta/sessions.md) Beta.Sessions.List(SessionListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

[BetaManagedAgentsSession](api/beta/sessions.md) Beta.Sessions.Retrieve(SessionRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

[BetaManagedAgentsSession](api/beta/sessions.md) Beta.Sessions.Update(SessionUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

[BetaManagedAgentsDeletedSession](api/beta/sessions.md) Beta.Sessions.Delete(SessionDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

[BetaManagedAgentsSession](api/beta/sessions.md) Beta.Sessions.Archive(SessionArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/archive

#### BetaSessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

[EventListPageResponse](api/beta/sessions/events.md) Beta.Sessions.Events.List(EventListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

[BetaManagedAgentsSendSessionEvents](api/beta/sessions/events.md) Beta.Sessions.Events.Send(EventSendParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

[BetaManagedAgentsStreamSessionEvents](api/beta/sessions/events.md) Beta.Sessions.Events.StreamStreaming(EventStreamParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/events/stream

#### BetaSessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

[BetaManagedAgentsFileResource](api/beta/sessions/resources.md) Beta.Sessions.Resources.Add(ResourceAddParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

[ResourceListPageResponse](api/beta/sessions/resources.md) Beta.Sessions.Resources.List(ResourceListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

[ResourceRetrieveResponse](api/beta/sessions/resources.md) Beta.Sessions.Resources.Retrieve(ResourceRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

[ResourceUpdateResponse](api/beta/sessions/resources.md) Beta.Sessions.Resources.Update(ResourceUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

[BetaManagedAgentsDeleteSessionResource](api/beta/sessions/resources.md) Beta.Sessions.Resources.Delete(ResourceDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

#### BetaSessionsThreads

##### [List Session Threads](api/beta/sessions/threads/list.md)

[ThreadListPageResponse](api/beta/sessions/threads.md) Beta.Sessions.Threads.List(ThreadListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/beta/sessions/threads/retrieve.md)

[BetaManagedAgentsSessionThread](api/beta/sessions/threads.md) Beta.Sessions.Threads.Retrieve(ThreadRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/beta/sessions/threads/archive.md)

[BetaManagedAgentsSessionThread](api/beta/sessions/threads.md) Beta.Sessions.Threads.Archive(ThreadArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

#### BetaSessionsThreadsEvents

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

[EventListPageResponse](api/beta/sessions/threads/events.md) Beta.Sessions.Threads.Events.List(EventListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

[BetaManagedAgentsStreamSessionThreadEvents](api/beta/sessions/threads.md) Beta.Sessions.Threads.Events.StreamStreaming(EventStreamParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

#### BetaDeployments

##### [Create Deployment](api/beta/deployments/create.md)

[BetaManagedAgentsDeployment](api/beta/deployments.md) Beta.Deployments.Create(DeploymentCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/deployments

##### [List Deployments](api/beta/deployments/list.md)

[DeploymentListPageResponse](api/beta/deployments.md) Beta.Deployments.List(DeploymentListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/deployments

##### [Get Deployment](api/beta/deployments/retrieve.md)

[BetaManagedAgentsDeployment](api/beta/deployments.md) Beta.Deployments.Retrieve(DeploymentRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/deployments/{deployment\_id}

##### [Update Deployment](api/beta/deployments/update.md)

[BetaManagedAgentsDeployment](api/beta/deployments.md) Beta.Deployments.Update(DeploymentUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/deployments/{deployment\_id}

##### [Archive Deployment](api/beta/deployments/archive.md)

[BetaManagedAgentsDeployment](api/beta/deployments.md) Beta.Deployments.Archive(DeploymentArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/deployments/{deployment\_id}/archive

##### [Run Deployment Now](api/beta/deployments/run.md)

[BetaManagedAgentsDeploymentRun](api/beta/deployment_runs.md) Beta.Deployments.Run(DeploymentRunParamsparameters, CancellationTokencancellationToken = default)

POST/v1/deployments/{deployment\_id}/run

##### [Pause Deployment](api/beta/deployments/pause.md)

[BetaManagedAgentsDeployment](api/beta/deployments.md) Beta.Deployments.Pause(DeploymentPauseParamsparameters, CancellationTokencancellationToken = default)

POST/v1/deployments/{deployment\_id}/pause

##### [Unpause Deployment](api/beta/deployments/unpause.md)

[BetaManagedAgentsDeployment](api/beta/deployments.md) Beta.Deployments.Unpause(DeploymentUnpauseParamsparameters, CancellationTokencancellationToken = default)

POST/v1/deployments/{deployment\_id}/unpause

#### BetaDeployment Runs

##### [List Deployment Runs](api/beta/deployment_runs/list.md)

[DeploymentRunListPageResponse](api/beta/deployment_runs.md) Beta.DeploymentRuns.List(DeploymentRunListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/deployment\_runs

##### [Get Deployment Run](api/beta/deployment_runs/retrieve.md)

[BetaManagedAgentsDeploymentRun](api/beta/deployment_runs.md) Beta.DeploymentRuns.Retrieve(DeploymentRunRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/deployment\_runs/{deployment\_run\_id}

#### BetaVaults

##### [Create Vault](api/beta/vaults/create.md)

[BetaManagedAgentsVault](api/beta/vaults.md) Beta.Vaults.Create(VaultCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

[VaultListPageResponse](api/beta/vaults.md) Beta.Vaults.List(VaultListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

[BetaManagedAgentsVault](api/beta/vaults.md) Beta.Vaults.Retrieve(VaultRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

[BetaManagedAgentsVault](api/beta/vaults.md) Beta.Vaults.Update(VaultUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

[BetaManagedAgentsDeletedVault](api/beta/vaults.md) Beta.Vaults.Delete(VaultDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

[BetaManagedAgentsVault](api/beta/vaults.md) Beta.Vaults.Archive(VaultArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}/archive

#### BetaVaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

[BetaManagedAgentsCredential](api/beta/vaults/credentials.md) Beta.Vaults.Credentials.Create(CredentialCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

[CredentialListPageResponse](api/beta/vaults/credentials.md) Beta.Vaults.Credentials.List(CredentialListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

[BetaManagedAgentsCredential](api/beta/vaults/credentials.md) Beta.Vaults.Credentials.Retrieve(CredentialRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

[BetaManagedAgentsCredential](api/beta/vaults/credentials.md) Beta.Vaults.Credentials.Update(CredentialUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

[BetaManagedAgentsDeletedCredential](api/beta/vaults/credentials.md) Beta.Vaults.Credentials.Delete(CredentialDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

[BetaManagedAgentsCredential](api/beta/vaults/credentials.md) Beta.Vaults.Credentials.Archive(CredentialArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

[BetaManagedAgentsCredentialValidation](api/beta/vaults/credentials.md) Beta.Vaults.Credentials.McpOAuthValidate(CredentialMcpOAuthValidateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

#### BetaMemory Stores

##### [Create a memory store](api/beta/memory_stores/create.md)

[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) Beta.MemoryStores.Create(MemoryStoreCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/memory\_stores

##### [List memory stores](api/beta/memory_stores/list.md)

[MemoryStoreListPageResponse](api/beta/memory_stores.md) Beta.MemoryStores.List(MemoryStoreListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/memory\_stores

##### [Retrieve a memory store](api/beta/memory_stores/retrieve.md)

[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) Beta.MemoryStores.Retrieve(MemoryStoreRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/memory\_stores/{memory\_store\_id}

##### [Update a memory store](api/beta/memory_stores/update.md)

[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) Beta.MemoryStores.Update(MemoryStoreUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/memory\_stores/{memory\_store\_id}

##### [Delete a memory store](api/beta/memory_stores/delete.md)

[BetaManagedAgentsDeletedMemoryStore](api/beta/memory_stores.md) Beta.MemoryStores.Delete(MemoryStoreDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [Archive a memory store](api/beta/memory_stores/archive.md)

[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) Beta.MemoryStores.Archive(MemoryStoreArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/memory\_stores/{memory\_store\_id}/archive

#### BetaMemory StoresMemories

##### [Create a memory](api/beta/memory_stores/memories/create.md)

[BetaManagedAgentsMemory](api/beta/memory_stores/memories.md) Beta.MemoryStores.Memories.Create(MemoryCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/beta/memory_stores/memories/list.md)

[MemoryListPageResponse](api/beta/memory_stores/memories.md) Beta.MemoryStores.Memories.List(MemoryListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/beta/memory_stores/memories/retrieve.md)

[BetaManagedAgentsMemory](api/beta/memory_stores/memories.md) Beta.MemoryStores.Memories.Retrieve(MemoryRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/beta/memory_stores/memories/update.md)

[BetaManagedAgentsMemory](api/beta/memory_stores/memories.md) Beta.MemoryStores.Memories.Update(MemoryUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/beta/memory_stores/memories/delete.md)

[BetaManagedAgentsDeletedMemory](api/beta/memory_stores/memories.md) Beta.MemoryStores.Memories.Delete(MemoryDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

#### BetaMemory StoresMemory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

[MemoryVersionListPageResponse](api/beta/memory_stores/memory_versions.md) Beta.MemoryStores.MemoryVersions.List(MemoryVersionListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

[BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md) Beta.MemoryStores.MemoryVersions.Retrieve(MemoryVersionRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

[BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md) Beta.MemoryStores.MemoryVersions.Redact(MemoryVersionRedactParamsparameters, CancellationTokencancellationToken = default)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

#### BetaFiles

##### [Upload File](api/beta/files/upload.md)

[FileMetadata](api/beta/files.md) Beta.Files.Upload(FileUploadParamsparameters, CancellationTokencancellationToken = default)

POST/v1/files

##### [List Files](api/beta/files/list.md)

[FileListPageResponse](api/beta/files.md) Beta.Files.List(FileListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/files

##### [Download File](api/beta/files/download.md)

HttpResponse Beta.Files.Download(FileDownloadParamsparameters, CancellationTokencancellationToken = default)

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

[FileMetadata](api/beta/files.md) Beta.Files.RetrieveMetadata(FileRetrieveMetadataParamsparameters, CancellationTokencancellationToken = default)

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

[DeletedFile](api/beta/files.md) Beta.Files.Delete(FileDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/files/{file\_id}

#### BetaSkills

##### [Create Skill](api/beta/skills/create.md)

[SkillCreateResponse](api/beta/skills.md) Beta.Skills.Create(SkillCreateParams?parameters, CancellationTokencancellationToken = default)

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

[SkillListPageResponse](api/beta/skills.md) Beta.Skills.List(SkillListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

[SkillRetrieveResponse](api/beta/skills.md) Beta.Skills.Retrieve(SkillRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

[SkillDeleteResponse](api/beta/skills.md) Beta.Skills.Delete(SkillDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/skills/{skill\_id}

#### BetaSkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

[VersionCreateResponse](api/beta/skills/versions.md) Beta.Skills.Versions.Create(VersionCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

[VersionListPageResponse](api/beta/skills/versions.md) Beta.Skills.Versions.List(VersionListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/skills/{skill\_id}/versions

##### [Download Skill Version Content](api/beta/skills/versions/download.md)

HttpResponse Beta.Skills.Versions.Download(VersionDownloadParamsparameters, CancellationTokencancellationToken = default)

GET/v1/skills/{skill\_id}/versions/{version}/content

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

[VersionRetrieveResponse](api/beta/skills/versions.md) Beta.Skills.Versions.Retrieve(VersionRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

[VersionDeleteResponse](api/beta/skills/versions.md) Beta.Skills.Versions.Delete(VersionDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/skills/{skill\_id}/versions/{version}

#### BetaUser Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

[BetaUserProfile](api/beta/user_profiles.md) Beta.UserProfiles.Create(UserProfileCreateParams?parameters, CancellationTokencancellationToken = default)

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

[UserProfileListPageResponse](api/beta/user_profiles.md) Beta.UserProfiles.List(UserProfileListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

[BetaUserProfile](api/beta/user_profiles.md) Beta.UserProfiles.Retrieve(UserProfileRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/user\_profiles/{user\_profile\_id}

##### [Update User Profile](api/beta/user_profiles/update.md)

[BetaUserProfile](api/beta/user_profiles.md) Beta.UserProfiles.Update(UserProfileUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/user\_profiles/{user\_profile\_id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

[BetaUserProfileEnrollmentUrl](api/beta/user_profiles.md) Beta.UserProfiles.CreateEnrollmentUrl(UserProfileCreateEnrollmentUrlParamsparameters, CancellationTokencancellationToken = default)

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
