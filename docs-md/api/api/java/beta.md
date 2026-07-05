# Beta

Copy page



Java

# Beta

##### ModelsExpand Collapse



enum AnthropicBeta:

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

class BetaApiError:

String message

JsonValue; type "api\_error"constant"api\_error"constant



class BetaAuthenticationError:

String message

JsonValue; type "authentication\_error"constant"authentication\_error"constant



class BetaBillingError:

String message

JsonValue; type "billing\_error"constant"billing\_error"constant



class BetaError: A class that can be one of several variants.union 



class BetaInvalidRequestError:

String message

JsonValue; type "invalid\_request\_error"constant"invalid\_request\_error"constant



class BetaAuthenticationError:

String message

JsonValue; type "authentication\_error"constant"authentication\_error"constant



class BetaBillingError:

String message

JsonValue; type "billing\_error"constant"billing\_error"constant



class BetaPermissionError:

String message

JsonValue; type "permission\_error"constant"permission\_error"constant



class BetaNotFoundError:

String message

JsonValue; type "not\_found\_error"constant"not\_found\_error"constant



class BetaRateLimitError:

String message

JsonValue; type "rate\_limit\_error"constant"rate\_limit\_error"constant



class BetaGatewayTimeoutError:

String message

JsonValue; type "timeout\_error"constant"timeout\_error"constant



class BetaApiError:

String message

JsonValue; type "api\_error"constant"api\_error"constant



class BetaOverloadedError:

String message

JsonValue; type "overloaded\_error"constant"overloaded\_error"constant



class BetaErrorResponse:



[BetaError](api/beta.md) error

One of the following:



class BetaInvalidRequestError:

String message

JsonValue; type "invalid\_request\_error"constant"invalid\_request\_error"constant



class BetaAuthenticationError:

String message

JsonValue; type "authentication\_error"constant"authentication\_error"constant



class BetaBillingError:

String message

JsonValue; type "billing\_error"constant"billing\_error"constant



class BetaPermissionError:

String message

JsonValue; type "permission\_error"constant"permission\_error"constant



class BetaNotFoundError:

String message

JsonValue; type "not\_found\_error"constant"not\_found\_error"constant



class BetaRateLimitError:

String message

JsonValue; type "rate\_limit\_error"constant"rate\_limit\_error"constant



class BetaGatewayTimeoutError:

String message

JsonValue; type "timeout\_error"constant"timeout\_error"constant



class BetaApiError:

String message

JsonValue; type "api\_error"constant"api\_error"constant



class BetaOverloadedError:

String message

JsonValue; type "overloaded\_error"constant"overloaded\_error"constant

Optional<String> requestId

JsonValue; type "error"constant"error"constant



class BetaGatewayTimeoutError:

String message

JsonValue; type "timeout\_error"constant"timeout\_error"constant



class BetaInvalidRequestError:

String message

JsonValue; type "invalid\_request\_error"constant"invalid\_request\_error"constant



class BetaNotFoundError:

String message

JsonValue; type "not\_found\_error"constant"not\_found\_error"constant



class BetaOverloadedError:

String message

JsonValue; type "overloaded\_error"constant"overloaded\_error"constant



class BetaPermissionError:

String message

JsonValue; type "permission\_error"constant"permission\_error"constant



class BetaRateLimitError:

String message

JsonValue; type "rate\_limit\_error"constant"rate\_limit\_error"constant

#### BetaModels

##### [List Models](api/beta/models/list.md)

ModelListPage beta().models().list(ModelListParamsparams = ModelListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

[BetaModelInfo](api/beta/models.md) beta().models().retrieve(ModelRetrieveParamsparams = ModelRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/models/{model\_id}

#### BetaMessages

##### [Create a Message](api/beta/messages/create.md)

[BetaMessage](api/beta/messages.md) beta().messages().create(MessageCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

[BetaMessageTokensCount](api/beta/messages.md) beta().messages().countTokens(MessageCountTokensParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages/count\_tokens

#### BetaMessagesBatches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

[BetaMessageBatch](api/beta/messages/batches.md) beta().messages().batches().create(BatchCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

[BetaMessageBatch](api/beta/messages/batches.md) beta().messages().batches().retrieve(BatchRetrieveParamsparams = BatchRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

BatchListPage beta().messages().batches().list(BatchListParamsparams = BatchListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

[BetaMessageBatch](api/beta/messages/batches.md) beta().messages().batches().cancel(BatchCancelParamsparams = BatchCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

[BetaDeletedMessageBatch](api/beta/messages/batches.md) beta().messages().batches().delete(BatchDeleteParamsparams = BatchDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

[BetaMessageBatchIndividualResponse](api/beta/messages/batches.md) beta().messages().batches().resultsStreaming(BatchResultsParamsparams = BatchResultsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/messages/batches/{message\_batch\_id}/results

#### BetaAgents

##### [Create Agent](api/beta/agents/create.md)

[BetaManagedAgentsAgent](api/beta/agents.md) beta().agents().create(AgentCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

AgentListPage beta().agents().list(AgentListParamsparams = AgentListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

[BetaManagedAgentsAgent](api/beta/agents.md) beta().agents().retrieve(AgentRetrieveParamsparams = AgentRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

[BetaManagedAgentsAgent](api/beta/agents.md) beta().agents().update(AgentUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

[BetaManagedAgentsAgent](api/beta/agents.md) beta().agents().archive(AgentArchiveParamsparams = AgentArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/agents/{agent\_id}/archive

#### BetaAgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

VersionListPage beta().agents().versions().list(VersionListParamsparams = VersionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/agents/{agent\_id}/versions

#### BetaEnvironments

##### [Create Environment](api/beta/environments/create.md)

[BetaEnvironment](api/beta/environments.md) beta().environments().create(EnvironmentCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

EnvironmentListPage beta().environments().list(EnvironmentListParamsparams = EnvironmentListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

[BetaEnvironment](api/beta/environments.md) beta().environments().retrieve(EnvironmentRetrieveParamsparams = EnvironmentRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

[BetaEnvironment](api/beta/environments.md) beta().environments().update(EnvironmentUpdateParamsparams = EnvironmentUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

[BetaEnvironmentDeleteResponse](api/beta/environments.md) beta().environments().delete(EnvironmentDeleteParamsparams = EnvironmentDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

[BetaEnvironment](api/beta/environments.md) beta().environments().archive(EnvironmentArchiveParamsparams = EnvironmentArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments/{environment\_id}/archive

#### BetaEnvironmentsWork

##### [Get Work Item](api/beta/environments/work/retrieve.md)

[BetaSelfHostedWork](api/beta/environments/work.md) beta().environments().work().retrieve(WorkRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

[BetaSelfHostedWork](api/beta/environments/work.md) beta().environments().work().poll(WorkPollParamsparams = WorkPollParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

[BetaSelfHostedWork](api/beta/environments/work.md) beta().environments().work().ack(WorkAckParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

[BetaSelfHostedWorkHeartbeatResponse](api/beta/environments/work.md) beta().environments().work().heartbeat(WorkHeartbeatParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

[BetaSelfHostedWork](api/beta/environments/work.md) beta().environments().work().stop(WorkStopParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

WorkListPage beta().environments().work().list(WorkListParamsparams = WorkListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

[BetaSelfHostedWork](api/beta/environments/work.md) beta().environments().work().update(WorkUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

[BetaSelfHostedWorkQueueStats](api/beta/environments/work.md) beta().environments().work().stats(WorkStatsParamsparams = WorkStatsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/environments/{environment\_id}/work/stats

#### BetaSessions

##### [Create Session](api/beta/sessions/create.md)

[BetaManagedAgentsSession](api/beta/sessions.md) beta().sessions().create(SessionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

SessionListPage beta().sessions().list(SessionListParamsparams = SessionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

[BetaManagedAgentsSession](api/beta/sessions.md) beta().sessions().retrieve(SessionRetrieveParamsparams = SessionRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

[BetaManagedAgentsSession](api/beta/sessions.md) beta().sessions().update(SessionUpdateParamsparams = SessionUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

[BetaManagedAgentsDeletedSession](api/beta/sessions.md) beta().sessions().delete(SessionDeleteParamsparams = SessionDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

[BetaManagedAgentsSession](api/beta/sessions.md) beta().sessions().archive(SessionArchiveParamsparams = SessionArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions/{session\_id}/archive

#### BetaSessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

EventListPage beta().sessions().events().list(EventListParamsparams = EventListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

[BetaManagedAgentsSendSessionEvents](api/beta/sessions/events.md) beta().sessions().events().send(EventSendParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

[BetaManagedAgentsStreamSessionEvents](api/beta/sessions/events.md) beta().sessions().events().streamStreaming(EventStreamParamsparams = EventStreamParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/events/stream

#### BetaSessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

[BetaManagedAgentsFileResource](api/beta/sessions/resources.md) beta().sessions().resources().add(ResourceAddParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

ResourceListPage beta().sessions().resources().list(ResourceListParamsparams = ResourceListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

[ResourceRetrieveResponse](api/beta/sessions/resources.md) beta().sessions().resources().retrieve(ResourceRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

[ResourceUpdateResponse](api/beta/sessions/resources.md) beta().sessions().resources().update(ResourceUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

[BetaManagedAgentsDeleteSessionResource](api/beta/sessions/resources.md) beta().sessions().resources().delete(ResourceDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

#### BetaSessionsThreads

##### [List Session Threads](api/beta/sessions/threads/list.md)

ThreadListPage beta().sessions().threads().list(ThreadListParamsparams = ThreadListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/beta/sessions/threads/retrieve.md)

[BetaManagedAgentsSessionThread](api/beta/sessions/threads.md) beta().sessions().threads().retrieve(ThreadRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/beta/sessions/threads/archive.md)

[BetaManagedAgentsSessionThread](api/beta/sessions/threads.md) beta().sessions().threads().archive(ThreadArchiveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

#### BetaSessionsThreadsEvents

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

EventListPage beta().sessions().threads().events().list(EventListParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

[BetaManagedAgentsStreamSessionThreadEvents](api/beta/sessions/threads.md) beta().sessions().threads().events().streamStreaming(EventStreamParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

#### BetaDeployments

##### [Create Deployment](api/beta/deployments/create.md)

[BetaManagedAgentsDeployment](api/beta/deployments.md) beta().deployments().create(DeploymentCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/deployments

##### [List Deployments](api/beta/deployments/list.md)

DeploymentListPage beta().deployments().list(DeploymentListParamsparams = DeploymentListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/deployments

##### [Get Deployment](api/beta/deployments/retrieve.md)

[BetaManagedAgentsDeployment](api/beta/deployments.md) beta().deployments().retrieve(DeploymentRetrieveParamsparams = DeploymentRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/deployments/{deployment\_id}

##### [Update Deployment](api/beta/deployments/update.md)

[BetaManagedAgentsDeployment](api/beta/deployments.md) beta().deployments().update(DeploymentUpdateParamsparams = DeploymentUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/deployments/{deployment\_id}

##### [Archive Deployment](api/beta/deployments/archive.md)

[BetaManagedAgentsDeployment](api/beta/deployments.md) beta().deployments().archive(DeploymentArchiveParamsparams = DeploymentArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/deployments/{deployment\_id}/archive

##### [Run Deployment Now](api/beta/deployments/run.md)

[BetaManagedAgentsDeploymentRun](api/beta/deployment_runs.md) beta().deployments().run(DeploymentRunParamsparams = DeploymentRunParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/deployments/{deployment\_id}/run

##### [Pause Deployment](api/beta/deployments/pause.md)

[BetaManagedAgentsDeployment](api/beta/deployments.md) beta().deployments().pause(DeploymentPauseParamsparams = DeploymentPauseParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/deployments/{deployment\_id}/pause

##### [Unpause Deployment](api/beta/deployments/unpause.md)

[BetaManagedAgentsDeployment](api/beta/deployments.md) beta().deployments().unpause(DeploymentUnpauseParamsparams = DeploymentUnpauseParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/deployments/{deployment\_id}/unpause

#### BetaDeployment Runs

##### [List Deployment Runs](api/beta/deployment_runs/list.md)

DeploymentRunListPage beta().deploymentRuns().list(DeploymentRunListParamsparams = DeploymentRunListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/deployment\_runs

##### [Get Deployment Run](api/beta/deployment_runs/retrieve.md)

[BetaManagedAgentsDeploymentRun](api/beta/deployment_runs.md) beta().deploymentRuns().retrieve(DeploymentRunRetrieveParamsparams = DeploymentRunRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/deployment\_runs/{deployment\_run\_id}

#### BetaVaults

##### [Create Vault](api/beta/vaults/create.md)

[BetaManagedAgentsVault](api/beta/vaults.md) beta().vaults().create(VaultCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

VaultListPage beta().vaults().list(VaultListParamsparams = VaultListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

[BetaManagedAgentsVault](api/beta/vaults.md) beta().vaults().retrieve(VaultRetrieveParamsparams = VaultRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

[BetaManagedAgentsVault](api/beta/vaults.md) beta().vaults().update(VaultUpdateParamsparams = VaultUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

[BetaManagedAgentsDeletedVault](api/beta/vaults.md) beta().vaults().delete(VaultDeleteParamsparams = VaultDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

[BetaManagedAgentsVault](api/beta/vaults.md) beta().vaults().archive(VaultArchiveParamsparams = VaultArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults/{vault\_id}/archive

#### BetaVaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

[BetaManagedAgentsCredential](api/beta/vaults/credentials.md) beta().vaults().credentials().create(CredentialCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

CredentialListPage beta().vaults().credentials().list(CredentialListParamsparams = CredentialListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

[BetaManagedAgentsCredential](api/beta/vaults/credentials.md) beta().vaults().credentials().retrieve(CredentialRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

[BetaManagedAgentsCredential](api/beta/vaults/credentials.md) beta().vaults().credentials().update(CredentialUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

[BetaManagedAgentsDeletedCredential](api/beta/vaults/credentials.md) beta().vaults().credentials().delete(CredentialDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

[BetaManagedAgentsCredential](api/beta/vaults/credentials.md) beta().vaults().credentials().archive(CredentialArchiveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

[BetaManagedAgentsCredentialValidation](api/beta/vaults/credentials.md) beta().vaults().credentials().mcpOAuthValidate(CredentialMcpOAuthValidateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

#### BetaMemory Stores

##### [Create a memory store](api/beta/memory_stores/create.md)

[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) beta().memoryStores().create(MemoryStoreCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/memory\_stores

##### [List memory stores](api/beta/memory_stores/list.md)

MemoryStoreListPage beta().memoryStores().list(MemoryStoreListParamsparams = MemoryStoreListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/memory\_stores

##### [Retrieve a memory store](api/beta/memory_stores/retrieve.md)

[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) beta().memoryStores().retrieve(MemoryStoreRetrieveParamsparams = MemoryStoreRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/memory\_stores/{memory\_store\_id}

##### [Update a memory store](api/beta/memory_stores/update.md)

[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) beta().memoryStores().update(MemoryStoreUpdateParamsparams = MemoryStoreUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/memory\_stores/{memory\_store\_id}

##### [Delete a memory store](api/beta/memory_stores/delete.md)

[BetaManagedAgentsDeletedMemoryStore](api/beta/memory_stores.md) beta().memoryStores().delete(MemoryStoreDeleteParamsparams = MemoryStoreDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [Archive a memory store](api/beta/memory_stores/archive.md)

[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) beta().memoryStores().archive(MemoryStoreArchiveParamsparams = MemoryStoreArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/memory\_stores/{memory\_store\_id}/archive

#### BetaMemory StoresMemories

##### [Create a memory](api/beta/memory_stores/memories/create.md)

[BetaManagedAgentsMemory](api/beta/memory_stores/memories.md) beta().memoryStores().memories().create(MemoryCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/beta/memory_stores/memories/list.md)

MemoryListPage beta().memoryStores().memories().list(MemoryListParamsparams = MemoryListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/beta/memory_stores/memories/retrieve.md)

[BetaManagedAgentsMemory](api/beta/memory_stores/memories.md) beta().memoryStores().memories().retrieve(MemoryRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/beta/memory_stores/memories/update.md)

[BetaManagedAgentsMemory](api/beta/memory_stores/memories.md) beta().memoryStores().memories().update(MemoryUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/beta/memory_stores/memories/delete.md)

[BetaManagedAgentsDeletedMemory](api/beta/memory_stores/memories.md) beta().memoryStores().memories().delete(MemoryDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

#### BetaMemory StoresMemory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

MemoryVersionListPage beta().memoryStores().memoryVersions().list(MemoryVersionListParamsparams = MemoryVersionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

[BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md) beta().memoryStores().memoryVersions().retrieve(MemoryVersionRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

[BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md) beta().memoryStores().memoryVersions().redact(MemoryVersionRedactParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

#### BetaFiles

##### [Upload File](api/beta/files/upload.md)

[FileMetadata](api/beta/files.md) beta().files().upload(FileUploadParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/files

##### [List Files](api/beta/files/list.md)

FileListPage beta().files().list(FileListParamsparams = FileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/files

##### [Download File](api/beta/files/download.md)

HttpResponse beta().files().download(FileDownloadParamsparams = FileDownloadParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

[FileMetadata](api/beta/files.md) beta().files().retrieveMetadata(FileRetrieveMetadataParamsparams = FileRetrieveMetadataParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

[DeletedFile](api/beta/files.md) beta().files().delete(FileDeleteParamsparams = FileDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/files/{file\_id}

#### BetaSkills

##### [Create Skill](api/beta/skills/create.md)

[SkillCreateResponse](api/beta/skills.md) beta().skills().create(SkillCreateParamsparams = SkillCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

SkillListPage beta().skills().list(SkillListParamsparams = SkillListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

[SkillRetrieveResponse](api/beta/skills.md) beta().skills().retrieve(SkillRetrieveParamsparams = SkillRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

[SkillDeleteResponse](api/beta/skills.md) beta().skills().delete(SkillDeleteParamsparams = SkillDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/skills/{skill\_id}

#### BetaSkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

[VersionCreateResponse](api/beta/skills/versions.md) beta().skills().versions().create(VersionCreateParamsparams = VersionCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

VersionListPage beta().skills().versions().list(VersionListParamsparams = VersionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/skills/{skill\_id}/versions

##### [Download Skill Version Content](api/beta/skills/versions/download.md)

HttpResponse beta().skills().versions().download(VersionDownloadParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/skills/{skill\_id}/versions/{version}/content

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

[VersionRetrieveResponse](api/beta/skills/versions.md) beta().skills().versions().retrieve(VersionRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

[VersionDeleteResponse](api/beta/skills/versions.md) beta().skills().versions().delete(VersionDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/skills/{skill\_id}/versions/{version}

#### BetaUser Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

[BetaUserProfile](api/beta/user_profiles.md) beta().userProfiles().create(UserProfileCreateParamsparams = UserProfileCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

UserProfileListPage beta().userProfiles().list(UserProfileListParamsparams = UserProfileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

[BetaUserProfile](api/beta/user_profiles.md) beta().userProfiles().retrieve(UserProfileRetrieveParamsparams = UserProfileRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/user\_profiles/{user\_profile\_id}

##### [Update User Profile](api/beta/user_profiles/update.md)

[BetaUserProfile](api/beta/user_profiles.md) beta().userProfiles().update(UserProfileUpdateParamsparams = UserProfileUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/user\_profiles/{user\_profile\_id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

[BetaUserProfileEnrollmentUrl](api/beta/user_profiles.md) beta().userProfiles().createEnrollmentUrl(UserProfileCreateEnrollmentUrlParamsparams = UserProfileCreateEnrollmentUrlParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

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
