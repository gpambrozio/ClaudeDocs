# Beta

Copy page



cURL

# Beta

##### ModelsExpand Collapse



AnthropicBeta = string or "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more

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

BetaAPIError object { message, type } 

message: string

type: "api\_error"



BetaAuthenticationError object { message, type } 

message: string

type: "authentication\_error"



BetaBillingError object { message, type } 

message: string

type: "billing\_error"



BetaError = [BetaInvalidRequestError](api/beta.md) { message, type }  or [BetaAuthenticationError](api/beta.md) { message, type }  or [BetaBillingError](api/beta.md) { message, type }  or 6 more

One of the following:



BetaInvalidRequestError object { message, type } 

message: string

type: "invalid\_request\_error"



BetaAuthenticationError object { message, type } 

message: string

type: "authentication\_error"



BetaBillingError object { message, type } 

message: string

type: "billing\_error"



BetaPermissionError object { message, type } 

message: string

type: "permission\_error"



BetaNotFoundError object { message, type } 

message: string

type: "not\_found\_error"



BetaRateLimitError object { message, type } 

message: string

type: "rate\_limit\_error"



BetaGatewayTimeoutError object { message, type } 

message: string

type: "timeout\_error"



BetaAPIError object { message, type } 

message: string

type: "api\_error"



BetaOverloadedError object { message, type } 

message: string

type: "overloaded\_error"



BetaErrorResponse object { error, request\_id, type } 



error: [BetaError](api/beta.md)

One of the following:



BetaInvalidRequestError object { message, type } 

message: string

type: "invalid\_request\_error"



BetaAuthenticationError object { message, type } 

message: string

type: "authentication\_error"



BetaBillingError object { message, type } 

message: string

type: "billing\_error"



BetaPermissionError object { message, type } 

message: string

type: "permission\_error"



BetaNotFoundError object { message, type } 

message: string

type: "not\_found\_error"



BetaRateLimitError object { message, type } 

message: string

type: "rate\_limit\_error"



BetaGatewayTimeoutError object { message, type } 

message: string

type: "timeout\_error"



BetaAPIError object { message, type } 

message: string

type: "api\_error"



BetaOverloadedError object { message, type } 

message: string

type: "overloaded\_error"

request\_id: string

type: "error"



BetaGatewayTimeoutError object { message, type } 

message: string

type: "timeout\_error"



BetaInvalidRequestError object { message, type } 

message: string

type: "invalid\_request\_error"



BetaNotFoundError object { message, type } 

message: string

type: "not\_found\_error"



BetaOverloadedError object { message, type } 

message: string

type: "overloaded\_error"



BetaPermissionError object { message, type } 

message: string

type: "permission\_error"



BetaRateLimitError object { message, type } 

message: string

type: "rate\_limit\_error"

#### BetaModels

##### [List Models](api/beta/models/list.md)

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

GET/v1/models/{model\_id}

#### BetaMessages

##### [Create a Message](api/beta/messages/create.md)

POST/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

POST/v1/messages/count\_tokens

#### BetaMessagesBatches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

GET/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

GET/v1/messages/batches/{message\_batch\_id}/results

#### BetaAgents

##### [Create Agent](api/beta/agents/create.md)

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

POST/v1/agents/{agent\_id}/archive

#### BetaAgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

GET/v1/agents/{agent\_id}/versions

#### BetaEnvironments

##### [Create Environment](api/beta/environments/create.md)

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

POST/v1/environments/{environment\_id}/archive

#### BetaEnvironmentsWork

##### [Get Work Item](api/beta/environments/work/retrieve.md)

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

GET/v1/environments/{environment\_id}/work/stats

#### BetaSessions

##### [Create Session](api/beta/sessions/create.md)

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

POST/v1/sessions/{session\_id}/archive

#### BetaSessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

GET/v1/sessions/{session\_id}/events/stream

#### BetaSessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

#### BetaSessionsThreads

##### [List Session Threads](api/beta/sessions/threads/list.md)

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/beta/sessions/threads/retrieve.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/beta/sessions/threads/archive.md)

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

#### BetaSessionsThreadsEvents

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

#### BetaDeployments

##### [Create Deployment](api/beta/deployments/create.md)

POST/v1/deployments

##### [List Deployments](api/beta/deployments/list.md)

GET/v1/deployments

##### [Get Deployment](api/beta/deployments/retrieve.md)

GET/v1/deployments/{deployment\_id}

##### [Update Deployment](api/beta/deployments/update.md)

POST/v1/deployments/{deployment\_id}

##### [Archive Deployment](api/beta/deployments/archive.md)

POST/v1/deployments/{deployment\_id}/archive

##### [Run Deployment Now](api/beta/deployments/run.md)

POST/v1/deployments/{deployment\_id}/run

##### [Pause Deployment](api/beta/deployments/pause.md)

POST/v1/deployments/{deployment\_id}/pause

##### [Unpause Deployment](api/beta/deployments/unpause.md)

POST/v1/deployments/{deployment\_id}/unpause

#### BetaDeployment Runs

##### [List Deployment Runs](api/beta/deployment_runs/list.md)

GET/v1/deployment\_runs

##### [Get Deployment Run](api/beta/deployment_runs/retrieve.md)

GET/v1/deployment\_runs/{deployment\_run\_id}

#### BetaVaults

##### [Create Vault](api/beta/vaults/create.md)

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

POST/v1/vaults/{vault\_id}/archive

#### BetaVaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

#### BetaMemory Stores

##### [Create a memory store](api/beta/memory_stores/create.md)

POST/v1/memory\_stores

##### [List memory stores](api/beta/memory_stores/list.md)

GET/v1/memory\_stores

##### [Retrieve a memory store](api/beta/memory_stores/retrieve.md)

GET/v1/memory\_stores/{memory\_store\_id}

##### [Update a memory store](api/beta/memory_stores/update.md)

POST/v1/memory\_stores/{memory\_store\_id}

##### [Delete a memory store](api/beta/memory_stores/delete.md)

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [Archive a memory store](api/beta/memory_stores/archive.md)

POST/v1/memory\_stores/{memory\_store\_id}/archive

#### BetaMemory StoresMemories

##### [Create a memory](api/beta/memory_stores/memories/create.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/beta/memory_stores/memories/list.md)

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/beta/memory_stores/memories/retrieve.md)

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/beta/memory_stores/memories/update.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/beta/memory_stores/memories/delete.md)

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

#### BetaMemory StoresMemory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

#### BetaFiles

##### [Upload File](api/beta/files/upload.md)

POST/v1/files

##### [List Files](api/beta/files/list.md)

GET/v1/files

##### [Download File](api/beta/files/download.md)

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

DELETE/v1/files/{file\_id}

#### BetaSkills

##### [Create Skill](api/beta/skills/create.md)

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

DELETE/v1/skills/{skill\_id}

#### BetaSkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

GET/v1/skills/{skill\_id}/versions

##### [Download Skill Version Content](api/beta/skills/versions/download.md)

GET/v1/skills/{skill\_id}/versions/{version}/content

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

DELETE/v1/skills/{skill\_id}/versions/{version}

#### BetaUser Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

GET/v1/user\_profiles/{user\_profile\_id}

##### [Update User Profile](api/beta/user_profiles/update.md)

POST/v1/user\_profiles/{user\_profile\_id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

POST/v1/user\_profiles/{user\_profile\_id}/enrollment\_url

#### BetaTunnels

##### [Create Tunnel](api/beta/tunnels/create.md)

POST/v1/tunnels

##### [Get Tunnel](api/beta/tunnels/retrieve.md)

GET/v1/tunnels/{tunnel\_id}

##### [List Tunnels](api/beta/tunnels/list.md)

GET/v1/tunnels

##### [Archive Tunnel](api/beta/tunnels/archive.md)

POST/v1/tunnels/{tunnel\_id}/archive

##### [Reveal Tunnel Token](api/beta/tunnels/reveal_token.md)

POST/v1/tunnels/{tunnel\_id}/reveal\_token

##### [Rotate Tunnel Token](api/beta/tunnels/rotate_token.md)

POST/v1/tunnels/{tunnel\_id}/rotate\_token

#### BetaTunnelsCertificates

##### [Create Tunnel Certificate](api/beta/tunnels/certificates/create.md)

POST/v1/tunnels/{tunnel\_id}/certificates

##### [Get Tunnel Certificate](api/beta/tunnels/certificates/retrieve.md)

GET/v1/tunnels/{tunnel\_id}/certificates/{certificate\_id}

##### [List Tunnel Certificates](api/beta/tunnels/certificates/list.md)

GET/v1/tunnels/{tunnel\_id}/certificates

##### [Archive Tunnel Certificate](api/beta/tunnels/certificates/archive.md)

POST/v1/tunnels/{tunnel\_id}/certificates/{certificate\_id}/archive

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
