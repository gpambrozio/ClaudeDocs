# Beta

Copy page



CLI

# Beta

##### ModelsExpand Collapse



beta\_api\_error: object { message, type } 

message: string

type: "api\_error"



beta\_authentication\_error: object { message, type } 

message: string

type: "authentication\_error"



beta\_billing\_error: object { message, type } 

message: string

type: "billing\_error"



beta\_error: [BetaInvalidRequestError](api/beta.md) { message, type }  or [BetaAuthenticationError](api/beta.md) { message, type }  or [BetaBillingError](api/beta.md) { message, type }  or 6 more



beta\_invalid\_request\_error: object { message, type } 

message: string

type: "invalid\_request\_error"



beta\_authentication\_error: object { message, type } 

message: string

type: "authentication\_error"



beta\_billing\_error: object { message, type } 

message: string

type: "billing\_error"



beta\_permission\_error: object { message, type } 

message: string

type: "permission\_error"



beta\_not\_found\_error: object { message, type } 

message: string

type: "not\_found\_error"



beta\_rate\_limit\_error: object { message, type } 

message: string

type: "rate\_limit\_error"



beta\_gateway\_timeout\_error: object { message, type } 

message: string

type: "timeout\_error"



beta\_api\_error: object { message, type } 

message: string

type: "api\_error"



beta\_overloaded\_error: object { message, type } 

message: string

type: "overloaded\_error"



beta\_error\_response: object { error, request\_id, type } 



error: [BetaInvalidRequestError](api/beta.md) { message, type }  or [BetaAuthenticationError](api/beta.md) { message, type }  or [BetaBillingError](api/beta.md) { message, type }  or 6 more



beta\_invalid\_request\_error: object { message, type } 

message: string

type: "invalid\_request\_error"



beta\_authentication\_error: object { message, type } 

message: string

type: "authentication\_error"



beta\_billing\_error: object { message, type } 

message: string

type: "billing\_error"



beta\_permission\_error: object { message, type } 

message: string

type: "permission\_error"



beta\_not\_found\_error: object { message, type } 

message: string

type: "not\_found\_error"



beta\_rate\_limit\_error: object { message, type } 

message: string

type: "rate\_limit\_error"



beta\_gateway\_timeout\_error: object { message, type } 

message: string

type: "timeout\_error"



beta\_api\_error: object { message, type } 

message: string

type: "api\_error"



beta\_overloaded\_error: object { message, type } 

message: string

type: "overloaded\_error"

request\_id: string

type: "error"



beta\_gateway\_timeout\_error: object { message, type } 

message: string

type: "timeout\_error"



beta\_invalid\_request\_error: object { message, type } 

message: string

type: "invalid\_request\_error"



beta\_not\_found\_error: object { message, type } 

message: string

type: "not\_found\_error"



beta\_overloaded\_error: object { message, type } 

message: string

type: "overloaded\_error"



beta\_permission\_error: object { message, type } 

message: string

type: "permission\_error"



beta\_rate\_limit\_error: object { message, type } 

message: string

type: "rate\_limit\_error"

#### BetaModels

##### [List Models](api/beta/models/list.md)

$ ant beta:models list

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

$ ant beta:models retrieve

GET/v1/models/{model\_id}

#### BetaMessages

##### [Create a Message](api/beta/messages/create.md)

$ ant beta:messages create

POST/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

$ ant beta:messages count-tokens

POST/v1/messages/count\_tokens

#### BetaMessagesBatches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

$ ant beta:messages:batches create

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

$ ant beta:messages:batches retrieve

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

$ ant beta:messages:batches list

GET/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

$ ant beta:messages:batches cancel

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

$ ant beta:messages:batches delete

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

$ ant beta:messages:batches results

GET/v1/messages/batches/{message\_batch\_id}/results

#### BetaAgents

##### [Create Agent](api/beta/agents/create.md)

$ ant beta:agents create

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

$ ant beta:agents list

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

$ ant beta:agents retrieve

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

$ ant beta:agents update

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

$ ant beta:agents archive

POST/v1/agents/{agent\_id}/archive

#### BetaAgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

$ ant beta:agents:versions list

GET/v1/agents/{agent\_id}/versions

#### BetaEnvironments

##### [Create Environment](api/beta/environments/create.md)

$ ant beta:environments create

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

$ ant beta:environments list

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

$ ant beta:environments retrieve

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

$ ant beta:environments update

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

$ ant beta:environments delete

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

$ ant beta:environments archive

POST/v1/environments/{environment\_id}/archive

#### BetaEnvironmentsWork

##### [Get Work Item](api/beta/environments/work/retrieve.md)

$ ant beta:environments:work retrieve

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

$ ant beta:environments:work poll

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

$ ant beta:environments:work ack

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

$ ant beta:environments:work heartbeat

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

$ ant beta:environments:work stop

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

$ ant beta:environments:work list

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

$ ant beta:environments:work update

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

$ ant beta:environments:work stats

GET/v1/environments/{environment\_id}/work/stats

#### BetaSessions

##### [Create Session](api/beta/sessions/create.md)

$ ant beta:sessions create

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

$ ant beta:sessions list

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

$ ant beta:sessions retrieve

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

$ ant beta:sessions update

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

$ ant beta:sessions delete

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

$ ant beta:sessions archive

POST/v1/sessions/{session\_id}/archive

#### BetaSessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

$ ant beta:sessions:events list

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

$ ant beta:sessions:events send

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

$ ant beta:sessions:events stream

GET/v1/sessions/{session\_id}/events/stream

#### BetaSessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

$ ant beta:sessions:resources add

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

$ ant beta:sessions:resources list

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

$ ant beta:sessions:resources retrieve

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

$ ant beta:sessions:resources update

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

$ ant beta:sessions:resources delete

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

#### BetaSessionsThreads

##### [List Session Threads](api/beta/sessions/threads/list.md)

$ ant beta:sessions:threads list

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/beta/sessions/threads/retrieve.md)

$ ant beta:sessions:threads retrieve

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/beta/sessions/threads/archive.md)

$ ant beta:sessions:threads archive

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

#### BetaSessionsThreadsEvents

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

$ ant beta:sessions:threads:events list

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

$ ant beta:sessions:threads:events stream

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

#### BetaDeployments

##### [Create Deployment](api/beta/deployments/create.md)

$ ant beta:deployments create

POST/v1/deployments

##### [List Deployments](api/beta/deployments/list.md)

$ ant beta:deployments list

GET/v1/deployments

##### [Get Deployment](api/beta/deployments/retrieve.md)

$ ant beta:deployments retrieve

GET/v1/deployments/{deployment\_id}

##### [Update Deployment](api/beta/deployments/update.md)

$ ant beta:deployments update

POST/v1/deployments/{deployment\_id}

##### [Archive Deployment](api/beta/deployments/archive.md)

$ ant beta:deployments archive

POST/v1/deployments/{deployment\_id}/archive

##### [Run Deployment Now](api/beta/deployments/run.md)

$ ant beta:deployments run

POST/v1/deployments/{deployment\_id}/run

##### [Pause Deployment](api/beta/deployments/pause.md)

$ ant beta:deployments pause

POST/v1/deployments/{deployment\_id}/pause

##### [Unpause Deployment](api/beta/deployments/unpause.md)

$ ant beta:deployments unpause

POST/v1/deployments/{deployment\_id}/unpause

#### BetaDeployment Runs

##### [List Deployment Runs](api/beta/deployment_runs/list.md)

$ ant beta:deployment-runs list

GET/v1/deployment\_runs

##### [Get Deployment Run](api/beta/deployment_runs/retrieve.md)

$ ant beta:deployment-runs retrieve

GET/v1/deployment\_runs/{deployment\_run\_id}

#### BetaVaults

##### [Create Vault](api/beta/vaults/create.md)

$ ant beta:vaults create

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

$ ant beta:vaults list

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

$ ant beta:vaults retrieve

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

$ ant beta:vaults update

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

$ ant beta:vaults delete

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

$ ant beta:vaults archive

POST/v1/vaults/{vault\_id}/archive

#### BetaVaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

$ ant beta:vaults:credentials create

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

$ ant beta:vaults:credentials list

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

$ ant beta:vaults:credentials retrieve

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

$ ant beta:vaults:credentials update

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

$ ant beta:vaults:credentials delete

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

$ ant beta:vaults:credentials archive

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

$ ant beta:vaults:credentials mcp-oauth-validate

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

#### BetaMemory Stores

##### [Create a memory store](api/beta/memory_stores/create.md)

$ ant beta:memory-stores create

POST/v1/memory\_stores

##### [List memory stores](api/beta/memory_stores/list.md)

$ ant beta:memory-stores list

GET/v1/memory\_stores

##### [Retrieve a memory store](api/beta/memory_stores/retrieve.md)

$ ant beta:memory-stores retrieve

GET/v1/memory\_stores/{memory\_store\_id}

##### [Update a memory store](api/beta/memory_stores/update.md)

$ ant beta:memory-stores update

POST/v1/memory\_stores/{memory\_store\_id}

##### [Delete a memory store](api/beta/memory_stores/delete.md)

$ ant beta:memory-stores delete

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [Archive a memory store](api/beta/memory_stores/archive.md)

$ ant beta:memory-stores archive

POST/v1/memory\_stores/{memory\_store\_id}/archive

#### BetaMemory StoresMemories

##### [Create a memory](api/beta/memory_stores/memories/create.md)

$ ant beta:memory-stores:memories create

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/beta/memory_stores/memories/list.md)

$ ant beta:memory-stores:memories list

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/beta/memory_stores/memories/retrieve.md)

$ ant beta:memory-stores:memories retrieve

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/beta/memory_stores/memories/update.md)

$ ant beta:memory-stores:memories update

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/beta/memory_stores/memories/delete.md)

$ ant beta:memory-stores:memories delete

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

#### BetaMemory StoresMemory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

$ ant beta:memory-stores:memory-versions list

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

$ ant beta:memory-stores:memory-versions retrieve

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

$ ant beta:memory-stores:memory-versions redact

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

#### BetaFiles

##### [Upload File](api/beta/files/upload.md)

$ ant beta:files upload

POST/v1/files

##### [List Files](api/beta/files/list.md)

$ ant beta:files list

GET/v1/files

##### [Download File](api/beta/files/download.md)

$ ant beta:files download

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

$ ant beta:files retrieve-metadata

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

$ ant beta:files delete

DELETE/v1/files/{file\_id}

#### BetaSkills

##### [Create Skill](api/beta/skills/create.md)

$ ant beta:skills create

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

$ ant beta:skills list

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

$ ant beta:skills retrieve

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

$ ant beta:skills delete

DELETE/v1/skills/{skill\_id}

#### BetaSkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

$ ant beta:skills:versions create

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

$ ant beta:skills:versions list

GET/v1/skills/{skill\_id}/versions

##### [Download Skill Version Content](api/beta/skills/versions/download.md)

$ ant beta:skills:versions download

GET/v1/skills/{skill\_id}/versions/{version}/content

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

$ ant beta:skills:versions retrieve

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

$ ant beta:skills:versions delete

DELETE/v1/skills/{skill\_id}/versions/{version}

#### BetaUser Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

$ ant beta:user-profiles create

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

$ ant beta:user-profiles list

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

$ ant beta:user-profiles retrieve

GET/v1/user\_profiles/{user\_profile\_id}

##### [Update User Profile](api/beta/user_profiles/update.md)

$ ant beta:user-profiles update

POST/v1/user\_profiles/{user\_profile\_id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

$ ant beta:user-profiles create-enrollment-url

POST/v1/user\_profiles/{user\_profile\_id}/enrollment\_url

#### BetaTunnels

#### BetaTunnelsCertificates

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
