# Beta

Copy page



Ruby

# Beta

##### ModelsExpand Collapse



AnthropicBeta = String | :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 25 more

One of the following:

String = String



AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 25 more

One of the following:

:"message-batches-2024-09-24"

:"prompt-caching-2024-07-31"

:"computer-use-2024-10-22"

:"computer-use-2025-01-24"

:"pdfs-2024-09-25"

:"token-counting-2024-11-01"

:"token-efficient-tools-2025-02-19"

:"output-128k-2025-02-19"

:"files-api-2025-04-14"

:"mcp-client-2025-04-04"

:"mcp-client-2025-11-20"

:"dev-full-thinking-2025-05-14"

:"interleaved-thinking-2025-05-14"

:"code-execution-2025-05-22"

:"extended-cache-ttl-2025-04-11"

:"context-1m-2025-08-07"

:"context-management-2025-06-27"

:"model-context-window-exceeded-2025-08-26"

:"skills-2025-10-02"

:"fast-mode-2026-02-01"

:"output-300k-2026-03-24"

:"user-profiles-2026-03-24"

:"advisor-tool-2026-03-01"

:"managed-agents-2026-04-01"

:"cache-diagnosis-2026-04-07"

:"thinking-token-count-2026-05-13"

:"server-side-fallback-2026-06-01"

:"fallback-credit-2026-06-01"



class BetaAPIError { message, type } 

message: String

type: :api\_error



class BetaAuthenticationError { message, type } 

message: String

type: :authentication\_error



class BetaBillingError { message, type } 

message: String

type: :billing\_error



BetaError = [BetaInvalidRequestError](api/beta.md) { message, type }  | [BetaAuthenticationError](api/beta.md) { message, type }  | [BetaBillingError](api/beta.md) { message, type }  | 6 more

One of the following:



class BetaInvalidRequestError { message, type } 

message: String

type: :invalid\_request\_error



class BetaAuthenticationError { message, type } 

message: String

type: :authentication\_error



class BetaBillingError { message, type } 

message: String

type: :billing\_error



class BetaPermissionError { message, type } 

message: String

type: :permission\_error



class BetaNotFoundError { message, type } 

message: String

type: :not\_found\_error



class BetaRateLimitError { message, type } 

message: String

type: :rate\_limit\_error



class BetaGatewayTimeoutError { message, type } 

message: String

type: :timeout\_error



class BetaAPIError { message, type } 

message: String

type: :api\_error



class BetaOverloadedError { message, type } 

message: String

type: :overloaded\_error



class BetaErrorResponse { error, request\_id, type } 



error: [BetaError](api/beta.md)

One of the following:



class BetaInvalidRequestError { message, type } 

message: String

type: :invalid\_request\_error



class BetaAuthenticationError { message, type } 

message: String

type: :authentication\_error



class BetaBillingError { message, type } 

message: String

type: :billing\_error



class BetaPermissionError { message, type } 

message: String

type: :permission\_error



class BetaNotFoundError { message, type } 

message: String

type: :not\_found\_error



class BetaRateLimitError { message, type } 

message: String

type: :rate\_limit\_error



class BetaGatewayTimeoutError { message, type } 

message: String

type: :timeout\_error



class BetaAPIError { message, type } 

message: String

type: :api\_error



class BetaOverloadedError { message, type } 

message: String

type: :overloaded\_error

request\_id: String

type: :error



class BetaGatewayTimeoutError { message, type } 

message: String

type: :timeout\_error



class BetaInvalidRequestError { message, type } 

message: String

type: :invalid\_request\_error



class BetaNotFoundError { message, type } 

message: String

type: :not\_found\_error



class BetaOverloadedError { message, type } 

message: String

type: :overloaded\_error



class BetaPermissionError { message, type } 

message: String

type: :permission\_error



class BetaRateLimitError { message, type } 

message: String

type: :rate\_limit\_error

#### BetaModels

##### [List Models](api/beta/models/list.md)

beta.models.list(\*\*kwargs) -> Page<[BetaModelInfo](api/beta/models.md) { id, allowed\_fallback\_models, capabilities, 5 more } >

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

beta.models.retrieve(model\_id, \*\*kwargs) -> [BetaModelInfo](api/beta/models.md) { id, allowed\_fallback\_models, capabilities, 5 more }

GET/v1/models/{model\_id}

#### BetaMessages

##### [Create a Message](api/beta/messages/create.md)

beta.messages.create(\*\*kwargs) -> [BetaMessage](api/beta/messages.md) { id, container, content, 9 more }

POST/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

beta.messages.count\_tokens(\*\*kwargs) -> [BetaMessageTokensCount](api/beta/messages.md) { context\_management, input\_tokens }

POST/v1/messages/count\_tokens

#### BetaMessagesBatches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

beta.messages.batches.create(\*\*kwargs) -> [BetaMessageBatch](api/beta/messages/batches.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

beta.messages.batches.retrieve(message\_batch\_id, \*\*kwargs) -> [BetaMessageBatch](api/beta/messages/batches.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

beta.messages.batches.list(\*\*kwargs) -> Page<[BetaMessageBatch](api/beta/messages/batches.md) { id, archived\_at, cancel\_initiated\_at, 7 more } >

GET/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

beta.messages.batches.cancel(message\_batch\_id, \*\*kwargs) -> [BetaMessageBatch](api/beta/messages/batches.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

beta.messages.batches.delete(message\_batch\_id, \*\*kwargs) -> [BetaDeletedMessageBatch](api/beta/messages/batches.md) { id, type }

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

beta.messages.batches.results(message\_batch\_id, \*\*kwargs) -> [BetaMessageBatchIndividualResponse](api/beta/messages/batches.md) { custom\_id, result }

GET/v1/messages/batches/{message\_batch\_id}/results

#### BetaAgents

##### [Create Agent](api/beta/agents/create.md)

beta.agents.create(\*\*kwargs) -> [BetaManagedAgentsAgent](api/beta/agents.md) { id, archived\_at, created\_at, 12 more }

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

beta.agents.list(\*\*kwargs) -> PageCursor<[BetaManagedAgentsAgent](api/beta/agents.md) { id, archived\_at, created\_at, 12 more } >

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

beta.agents.retrieve(agent\_id, \*\*kwargs) -> [BetaManagedAgentsAgent](api/beta/agents.md) { id, archived\_at, created\_at, 12 more }

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

beta.agents.update(agent\_id, \*\*kwargs) -> [BetaManagedAgentsAgent](api/beta/agents.md) { id, archived\_at, created\_at, 12 more }

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

beta.agents.archive(agent\_id, \*\*kwargs) -> [BetaManagedAgentsAgent](api/beta/agents.md) { id, archived\_at, created\_at, 12 more }

POST/v1/agents/{agent\_id}/archive

#### BetaAgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

beta.agents.versions.list(agent\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsAgent](api/beta/agents.md) { id, archived\_at, created\_at, 12 more } >

GET/v1/agents/{agent\_id}/versions

#### BetaEnvironments

##### [Create Environment](api/beta/environments/create.md)

beta.environments.create(\*\*kwargs) -> [BetaEnvironment](api/beta/environments.md) { id, archived\_at, config, 7 more }

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

beta.environments.list(\*\*kwargs) -> PageCursor<[BetaEnvironment](api/beta/environments.md) { id, archived\_at, config, 7 more } >

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

beta.environments.retrieve(environment\_id, \*\*kwargs) -> [BetaEnvironment](api/beta/environments.md) { id, archived\_at, config, 7 more }

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

beta.environments.update(environment\_id, \*\*kwargs) -> [BetaEnvironment](api/beta/environments.md) { id, archived\_at, config, 7 more }

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

beta.environments.delete(environment\_id, \*\*kwargs) -> [BetaEnvironmentDeleteResponse](api/beta/environments.md) { id, type }

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

beta.environments.archive(environment\_id, \*\*kwargs) -> [BetaEnvironment](api/beta/environments.md) { id, archived\_at, config, 7 more }

POST/v1/environments/{environment\_id}/archive

#### BetaEnvironmentsWork

##### [Get Work Item](api/beta/environments/work/retrieve.md)

beta.environments.work.retrieve(work\_id, \*\*kwargs) -> [BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 10 more }

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

beta.environments.work.poll(environment\_id, \*\*kwargs) -> [BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 10 more }

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

beta.environments.work.ack(work\_id, \*\*kwargs) -> [BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 10 more }

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

beta.environments.work.heartbeat(work\_id, \*\*kwargs) -> [BetaSelfHostedWorkHeartbeatResponse](api/beta/environments/work.md) { last\_heartbeat, lease\_extended, state, 2 more }

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

beta.environments.work.stop(work\_id, \*\*kwargs) -> [BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 10 more }

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

beta.environments.work.list(environment\_id, \*\*kwargs) -> PageCursor<[BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 10 more } >

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

beta.environments.work.update(work\_id, \*\*kwargs) -> [BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 10 more }

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

beta.environments.work.stats(environment\_id, \*\*kwargs) -> [BetaSelfHostedWorkQueueStats](api/beta/environments/work.md) { depth, oldest\_queued\_at, pending, 2 more }

GET/v1/environments/{environment\_id}/work/stats

#### BetaSessions

##### [Create Session](api/beta/sessions/create.md)

beta.sessions.create(\*\*kwargs) -> [BetaManagedAgentsSession](api/beta/sessions.md) { id, agent, archived\_at, 13 more }

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

beta.sessions.list(\*\*kwargs) -> BidirectionalPageCursor<[BetaManagedAgentsSession](api/beta/sessions.md) { id, agent, archived\_at, 13 more } >

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

beta.sessions.retrieve(session\_id, \*\*kwargs) -> [BetaManagedAgentsSession](api/beta/sessions.md) { id, agent, archived\_at, 13 more }

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

beta.sessions.update(session\_id, \*\*kwargs) -> [BetaManagedAgentsSession](api/beta/sessions.md) { id, agent, archived\_at, 13 more }

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

beta.sessions.delete(session\_id, \*\*kwargs) -> [BetaManagedAgentsDeletedSession](api/beta/sessions.md) { id, type }

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

beta.sessions.archive(session\_id, \*\*kwargs) -> [BetaManagedAgentsSession](api/beta/sessions.md) { id, agent, archived\_at, 13 more }

POST/v1/sessions/{session\_id}/archive

#### BetaSessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

beta.sessions.events.list(session\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsSessionEvent](api/beta/sessions/events.md)>

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

beta.sessions.events.send\_(session\_id, \*\*kwargs) -> [BetaManagedAgentsSendSessionEvents](api/beta/sessions/events.md) { data }

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

beta.sessions.events.stream(session\_id, \*\*kwargs) -> [BetaManagedAgentsStreamSessionEvents](api/beta/sessions/events.md)

GET/v1/sessions/{session\_id}/events/stream

#### BetaSessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

beta.sessions.resources.add(session\_id, \*\*kwargs) -> [BetaManagedAgentsFileResource](api/beta/sessions/resources.md) { id, created\_at, file\_id, 3 more }

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

beta.sessions.resources.list(session\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsSessionResource](api/beta/sessions/resources.md)>

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

beta.sessions.resources.retrieve(resource\_id, \*\*kwargs) -> [ResourceRetrieveResponse](api/beta/sessions/resources.md)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

beta.sessions.resources.update(resource\_id, \*\*kwargs) -> [ResourceUpdateResponse](api/beta/sessions/resources.md)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

beta.sessions.resources.delete(resource\_id, \*\*kwargs) -> [BetaManagedAgentsDeleteSessionResource](api/beta/sessions/resources.md) { id, type }

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

#### BetaSessionsThreads

##### [List Session Threads](api/beta/sessions/threads/list.md)

beta.sessions.threads.list(session\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsSessionThread](api/beta/sessions/threads.md) { id, agent, archived\_at, 8 more } >

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/beta/sessions/threads/retrieve.md)

beta.sessions.threads.retrieve(thread\_id, \*\*kwargs) -> [BetaManagedAgentsSessionThread](api/beta/sessions/threads.md) { id, agent, archived\_at, 8 more }

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/beta/sessions/threads/archive.md)

beta.sessions.threads.archive(thread\_id, \*\*kwargs) -> [BetaManagedAgentsSessionThread](api/beta/sessions/threads.md) { id, agent, archived\_at, 8 more }

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

#### BetaSessionsThreadsEvents

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

beta.sessions.threads.events.list(thread\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsSessionEvent](api/beta/sessions/events.md)>

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

beta.sessions.threads.events.stream(thread\_id, \*\*kwargs) -> [BetaManagedAgentsStreamSessionThreadEvents](api/beta/sessions/threads.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

#### BetaDeployments

##### [Create Deployment](api/beta/deployments/create.md)

beta.deployments.create(\*\*kwargs) -> [BetaManagedAgentsDeployment](api/beta/deployments.md) { id, agent, archived\_at, 13 more }

POST/v1/deployments

##### [List Deployments](api/beta/deployments/list.md)

beta.deployments.list(\*\*kwargs) -> PageCursor<[BetaManagedAgentsDeployment](api/beta/deployments.md) { id, agent, archived\_at, 13 more } >

GET/v1/deployments

##### [Get Deployment](api/beta/deployments/retrieve.md)

beta.deployments.retrieve(deployment\_id, \*\*kwargs) -> [BetaManagedAgentsDeployment](api/beta/deployments.md) { id, agent, archived\_at, 13 more }

GET/v1/deployments/{deployment\_id}

##### [Update Deployment](api/beta/deployments/update.md)

beta.deployments.update(deployment\_id, \*\*kwargs) -> [BetaManagedAgentsDeployment](api/beta/deployments.md) { id, agent, archived\_at, 13 more }

POST/v1/deployments/{deployment\_id}

##### [Archive Deployment](api/beta/deployments/archive.md)

beta.deployments.archive(deployment\_id, \*\*kwargs) -> [BetaManagedAgentsDeployment](api/beta/deployments.md) { id, agent, archived\_at, 13 more }

POST/v1/deployments/{deployment\_id}/archive

##### [Run Deployment Now](api/beta/deployments/run.md)

beta.deployments.run(deployment\_id, \*\*kwargs) -> [BetaManagedAgentsDeploymentRun](api/beta/deployment_runs.md) { id, agent, created\_at, 5 more }

POST/v1/deployments/{deployment\_id}/run

##### [Pause Deployment](api/beta/deployments/pause.md)

beta.deployments.pause(deployment\_id, \*\*kwargs) -> [BetaManagedAgentsDeployment](api/beta/deployments.md) { id, agent, archived\_at, 13 more }

POST/v1/deployments/{deployment\_id}/pause

##### [Unpause Deployment](api/beta/deployments/unpause.md)

beta.deployments.unpause(deployment\_id, \*\*kwargs) -> [BetaManagedAgentsDeployment](api/beta/deployments.md) { id, agent, archived\_at, 13 more }

POST/v1/deployments/{deployment\_id}/unpause

#### BetaDeployment Runs

##### [List Deployment Runs](api/beta/deployment_runs/list.md)

beta.deployment\_runs.list(\*\*kwargs) -> PageCursor<[BetaManagedAgentsDeploymentRun](api/beta/deployment_runs.md) { id, agent, created\_at, 5 more } >

GET/v1/deployment\_runs

##### [Get Deployment Run](api/beta/deployment_runs/retrieve.md)

beta.deployment\_runs.retrieve(deployment\_run\_id, \*\*kwargs) -> [BetaManagedAgentsDeploymentRun](api/beta/deployment_runs.md) { id, agent, created\_at, 5 more }

GET/v1/deployment\_runs/{deployment\_run\_id}

#### BetaVaults

##### [Create Vault](api/beta/vaults/create.md)

beta.vaults.create(\*\*kwargs) -> [BetaManagedAgentsVault](api/beta/vaults.md) { id, archived\_at, created\_at, 4 more }

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

beta.vaults.list(\*\*kwargs) -> PageCursor<[BetaManagedAgentsVault](api/beta/vaults.md) { id, archived\_at, created\_at, 4 more } >

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

beta.vaults.retrieve(vault\_id, \*\*kwargs) -> [BetaManagedAgentsVault](api/beta/vaults.md) { id, archived\_at, created\_at, 4 more }

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

beta.vaults.update(vault\_id, \*\*kwargs) -> [BetaManagedAgentsVault](api/beta/vaults.md) { id, archived\_at, created\_at, 4 more }

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

beta.vaults.delete(vault\_id, \*\*kwargs) -> [BetaManagedAgentsDeletedVault](api/beta/vaults.md) { id, type }

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

beta.vaults.archive(vault\_id, \*\*kwargs) -> [BetaManagedAgentsVault](api/beta/vaults.md) { id, archived\_at, created\_at, 4 more }

POST/v1/vaults/{vault\_id}/archive

#### BetaVaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

beta.vaults.credentials.create(vault\_id, \*\*kwargs) -> [BetaManagedAgentsCredential](api/beta/vaults/credentials.md) { id, archived\_at, auth, 6 more }

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

beta.vaults.credentials.list(vault\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsCredential](api/beta/vaults/credentials.md) { id, archived\_at, auth, 6 more } >

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

beta.vaults.credentials.retrieve(credential\_id, \*\*kwargs) -> [BetaManagedAgentsCredential](api/beta/vaults/credentials.md) { id, archived\_at, auth, 6 more }

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

beta.vaults.credentials.update(credential\_id, \*\*kwargs) -> [BetaManagedAgentsCredential](api/beta/vaults/credentials.md) { id, archived\_at, auth, 6 more }

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

beta.vaults.credentials.delete(credential\_id, \*\*kwargs) -> [BetaManagedAgentsDeletedCredential](api/beta/vaults/credentials.md) { id, type }

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

beta.vaults.credentials.archive(credential\_id, \*\*kwargs) -> [BetaManagedAgentsCredential](api/beta/vaults/credentials.md) { id, archived\_at, auth, 6 more }

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

beta.vaults.credentials.mcp\_oauth\_validate(credential\_id, \*\*kwargs) -> [BetaManagedAgentsCredentialValidation](api/beta/vaults/credentials.md) { credential\_id, has\_refresh\_token, mcp\_probe, 5 more }

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

#### BetaMemory Stores

##### [Create a memory store](api/beta/memory_stores/create.md)

beta.memory\_stores.create(\*\*kwargs) -> [BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) { id, created\_at, name, 5 more }

POST/v1/memory\_stores

##### [List memory stores](api/beta/memory_stores/list.md)

beta.memory\_stores.list(\*\*kwargs) -> PageCursor<[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) { id, created\_at, name, 5 more } >

GET/v1/memory\_stores

##### [Retrieve a memory store](api/beta/memory_stores/retrieve.md)

beta.memory\_stores.retrieve(memory\_store\_id, \*\*kwargs) -> [BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) { id, created\_at, name, 5 more }

GET/v1/memory\_stores/{memory\_store\_id}

##### [Update a memory store](api/beta/memory_stores/update.md)

beta.memory\_stores.update(memory\_store\_id, \*\*kwargs) -> [BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) { id, created\_at, name, 5 more }

POST/v1/memory\_stores/{memory\_store\_id}

##### [Delete a memory store](api/beta/memory_stores/delete.md)

beta.memory\_stores.delete(memory\_store\_id, \*\*kwargs) -> [BetaManagedAgentsDeletedMemoryStore](api/beta/memory_stores.md) { id, type }

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [Archive a memory store](api/beta/memory_stores/archive.md)

beta.memory\_stores.archive(memory\_store\_id, \*\*kwargs) -> [BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) { id, created\_at, name, 5 more }

POST/v1/memory\_stores/{memory\_store\_id}/archive

#### BetaMemory StoresMemories

##### [Create a memory](api/beta/memory_stores/memories/create.md)

beta.memory\_stores.memories.create(memory\_store\_id, \*\*kwargs) -> [BetaManagedAgentsMemory](api/beta/memory_stores/memories.md) { id, content\_sha256, content\_size\_bytes, 7 more }

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/beta/memory_stores/memories/list.md)

beta.memory\_stores.memories.list(memory\_store\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsMemoryListItem](api/beta/memory_stores/memories.md)>

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/beta/memory_stores/memories/retrieve.md)

beta.memory\_stores.memories.retrieve(memory\_id, \*\*kwargs) -> [BetaManagedAgentsMemory](api/beta/memory_stores/memories.md) { id, content\_sha256, content\_size\_bytes, 7 more }

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/beta/memory_stores/memories/update.md)

beta.memory\_stores.memories.update(memory\_id, \*\*kwargs) -> [BetaManagedAgentsMemory](api/beta/memory_stores/memories.md) { id, content\_sha256, content\_size\_bytes, 7 more }

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/beta/memory_stores/memories/delete.md)

beta.memory\_stores.memories.delete(memory\_id, \*\*kwargs) -> [BetaManagedAgentsDeletedMemory](api/beta/memory_stores/memories.md) { id, type }

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

#### BetaMemory StoresMemory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

beta.memory\_stores.memory\_versions.list(memory\_store\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md) { id, created\_at, memory\_id, 10 more } >

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

beta.memory\_stores.memory\_versions.retrieve(memory\_version\_id, \*\*kwargs) -> [BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md) { id, created\_at, memory\_id, 10 more }

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

beta.memory\_stores.memory\_versions.redact(memory\_version\_id, \*\*kwargs) -> [BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md) { id, created\_at, memory\_id, 10 more }

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

#### BetaFiles

##### [Upload File](api/beta/files/upload.md)

beta.files.upload(\*\*kwargs) -> [FileMetadata](api/beta/files.md) { id, created\_at, filename, 5 more }

POST/v1/files

##### [List Files](api/beta/files/list.md)

beta.files.list(\*\*kwargs) -> Page<[FileMetadata](api/beta/files.md) { id, created\_at, filename, 5 more } >

GET/v1/files

##### [Download File](api/beta/files/download.md)

beta.files.download(file\_id, \*\*kwargs) -> StringIO

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

beta.files.retrieve\_metadata(file\_id, \*\*kwargs) -> [FileMetadata](api/beta/files.md) { id, created\_at, filename, 5 more }

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

beta.files.delete(file\_id, \*\*kwargs) -> [DeletedFile](api/beta/files.md) { id, type }

DELETE/v1/files/{file\_id}

#### BetaSkills

##### [Create Skill](api/beta/skills/create.md)

beta.skills.create(\*\*kwargs) -> [SkillCreateResponse](api/beta/skills.md) { id, created\_at, display\_title, 4 more }

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

beta.skills.list(\*\*kwargs) -> PageCursor<[SkillListResponse](api/beta/skills.md) { id, created\_at, display\_title, 4 more } >

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

beta.skills.retrieve(skill\_id, \*\*kwargs) -> [SkillRetrieveResponse](api/beta/skills.md) { id, created\_at, display\_title, 4 more }

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

beta.skills.delete(skill\_id, \*\*kwargs) -> [SkillDeleteResponse](api/beta/skills.md) { id, type }

DELETE/v1/skills/{skill\_id}

#### BetaSkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

beta.skills.versions.create(skill\_id, \*\*kwargs) -> [VersionCreateResponse](api/beta/skills/versions.md) { id, created\_at, description, 5 more }

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

beta.skills.versions.list(skill\_id, \*\*kwargs) -> PageCursor<[VersionListResponse](api/beta/skills/versions.md) { id, created\_at, description, 5 more } >

GET/v1/skills/{skill\_id}/versions

##### [Download Skill Version Content](api/beta/skills/versions/download.md)

beta.skills.versions.download(version, \*\*kwargs) -> StringIO

GET/v1/skills/{skill\_id}/versions/{version}/content

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

beta.skills.versions.retrieve(version, \*\*kwargs) -> [VersionRetrieveResponse](api/beta/skills/versions.md) { id, created\_at, description, 5 more }

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

beta.skills.versions.delete(version, \*\*kwargs) -> [VersionDeleteResponse](api/beta/skills/versions.md) { id, type }

DELETE/v1/skills/{skill\_id}/versions/{version}

#### BetaUser Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

beta.user\_profiles.create(\*\*kwargs) -> [BetaUserProfile](api/beta/user_profiles.md) { id, created\_at, metadata, 6 more }

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

beta.user\_profiles.list(\*\*kwargs) -> PageCursor<[BetaUserProfile](api/beta/user_profiles.md) { id, created\_at, metadata, 6 more } >

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

beta.user\_profiles.retrieve(user\_profile\_id, \*\*kwargs) -> [BetaUserProfile](api/beta/user_profiles.md) { id, created\_at, metadata, 6 more }

GET/v1/user\_profiles/{user\_profile\_id}

##### [Update User Profile](api/beta/user_profiles/update.md)

beta.user\_profiles.update(user\_profile\_id, \*\*kwargs) -> [BetaUserProfile](api/beta/user_profiles.md) { id, created\_at, metadata, 6 more }

POST/v1/user\_profiles/{user\_profile\_id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

beta.user\_profiles.create\_enrollment\_url(user\_profile\_id, \*\*kwargs) -> [BetaUserProfileEnrollmentURL](api/beta/user_profiles.md) { expires\_at, type, url }

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
