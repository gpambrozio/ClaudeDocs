# Beta

Copy page



cURL

# Beta

##### Models



AnthropicBeta = string or "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 31 more

One of the following:



BetaAPIError object{ message, type }



message: string

defaultInternal server error



type: "api\_error"

defaultapi\_error



BetaAuthenticationError object{ message, type }



message: string

defaultAuthentication error



type: "authentication\_error"

defaultauthentication\_error



BetaBillingError object{ message, type }



message: string

defaultBilling error



type: "billing\_error"

defaultbilling\_error

BetaCurrency = "USD"



BetaError = [BetaInvalidRequestError](api/http/beta.md) { message, type } or [BetaAuthenticationError](api/http/beta.md) { message, type } or [BetaBillingError](api/http/beta.md) { message, type } or 6 more

One of the following:



BetaErrorResponse object{ error, request\_id, type }



error: [BetaError](api/http/beta.md)

One of the following:

request\_id: string or null



type: "error"

defaulterror



BetaGatewayTimeoutError object{ message, type }



message: string

defaultRequest timeout



type: "timeout\_error"

defaulttimeout\_error



BetaInvalidRequestError object{ message, type }



message: string

defaultInvalid request



type: "invalid\_request\_error"

defaultinvalid\_request\_error



BetaMonetaryAmount object{ amount, currency }

A monetary amount in a specific currency.

amount: string

Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

currency: [BetaCurrency](api/http/beta.md)

Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.



BetaNotFoundError object{ message, type }



message: string

defaultNot found



type: "not\_found\_error"

defaultnot\_found\_error



BetaOverloadedError object{ message, type }



message: string

defaultOverloaded



type: "overloaded\_error"

defaultoverloaded\_error



BetaPermissionError object{ message, type }



message: string

defaultPermission denied



type: "permission\_error"

defaultpermission\_error



BetaRateLimitError object{ message, type }



message: string

defaultRate limited



type: "rate\_limit\_error"

defaultrate\_limit\_error

#### Beta[Models](api/http/beta/models.md)

##### [List Models](api/http/beta/models/list.md)

GET/v1/models

##### [Get a Model](api/http/beta/models/retrieve.md)

GET/v1/models/{model\_id}

#### Beta[Messages](api/http/beta/messages.md)

##### [Create a Message](api/http/beta/messages/create.md)

POST/v1/messages

##### [Count tokens in a Message](api/http/beta/messages/count_tokens.md)

POST/v1/messages/count\_tokens

#### BetaMessages[Batches](api/http/beta/messages/batches.md)

##### [Create a Message Batch](api/http/beta/messages/batches/create.md)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/http/beta/messages/batches/retrieve.md)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/http/beta/messages/batches/list.md)

GET/v1/messages/batches

##### [Cancel a Message Batch](api/http/beta/messages/batches/cancel.md)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/http/beta/messages/batches/delete.md)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/http/beta/messages/batches/results.md)

GET/v1/messages/batches/{message\_batch\_id}/results

#### Beta[Agents](api/http/beta/agents.md)

##### [Create Agent](api/http/beta/agents/create.md)

POST/v1/agents

##### [List Agents](api/http/beta/agents/list.md)

GET/v1/agents

##### [Get Agent](api/http/beta/agents/retrieve.md)

GET/v1/agents/{agent\_id}

##### [Update Agent](api/http/beta/agents/update.md)

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/http/beta/agents/archive.md)

POST/v1/agents/{agent\_id}/archive

#### BetaAgents[Versions](api/http/beta/agents/versions.md)

##### [List Agent Versions](api/http/beta/agents/versions/list.md)

GET/v1/agents/{agent\_id}/versions

#### Beta[Environments](api/http/beta/environments.md)

##### [Create Environment](api/http/beta/environments/create.md)

POST/v1/environments

##### [List Environments](api/http/beta/environments/list.md)

GET/v1/environments

##### [Get Environment](api/http/beta/environments/retrieve.md)

GET/v1/environments/{environment\_id}

##### [Update Environment](api/http/beta/environments/update.md)

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/http/beta/environments/delete.md)

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/http/beta/environments/archive.md)

POST/v1/environments/{environment\_id}/archive

#### BetaEnvironments[Work](api/http/beta/environments/work.md)

##### [Get Work Item](api/http/beta/environments/work/retrieve.md)

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/http/beta/environments/work/poll.md)

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/http/beta/environments/work/ack.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/http/beta/environments/work/heartbeat.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/http/beta/environments/work/stop.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/http/beta/environments/work/list.md)

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/http/beta/environments/work/update.md)

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/http/beta/environments/work/stats.md)

GET/v1/environments/{environment\_id}/work/stats

#### Beta[Sessions](api/http/beta/sessions.md)

##### [Create Session](api/http/beta/sessions/create.md)

POST/v1/sessions

##### [List Sessions](api/http/beta/sessions/list.md)

GET/v1/sessions

##### [Get Session](api/http/beta/sessions/retrieve.md)

GET/v1/sessions/{session\_id}

##### [Update Session](api/http/beta/sessions/update.md)

POST/v1/sessions/{session\_id}

##### [Delete Session](api/http/beta/sessions/delete.md)

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/http/beta/sessions/archive.md)

POST/v1/sessions/{session\_id}/archive

#### BetaSessions[Events](api/http/beta/sessions/events.md)

##### [List Events](api/http/beta/sessions/events/list.md)

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/http/beta/sessions/events/send.md)

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/http/beta/sessions/events/stream.md)

GET/v1/sessions/{session\_id}/events/stream

#### BetaSessions[Resources](api/http/beta/sessions/resources.md)

##### [Add Session Resource](api/http/beta/sessions/resources/add.md)

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/http/beta/sessions/resources/list.md)

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/http/beta/sessions/resources/retrieve.md)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/http/beta/sessions/resources/update.md)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/http/beta/sessions/resources/delete.md)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

#### BetaSessions[Threads](api/http/beta/sessions/threads.md)

##### [List Session Threads](api/http/beta/sessions/threads/list.md)

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/http/beta/sessions/threads/retrieve.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/http/beta/sessions/threads/archive.md)

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

#### BetaSessionsThreads[Events](api/http/beta/sessions/threads/events.md)

##### [List Session Thread Events](api/http/beta/sessions/threads/events/list.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/http/beta/sessions/threads/events/stream.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

#### Beta[Deployments](api/http/beta/deployments.md)

##### [Create Deployment](api/http/beta/deployments/create.md)

POST/v1/deployments

##### [List Deployments](api/http/beta/deployments/list.md)

GET/v1/deployments

##### [Get Deployment](api/http/beta/deployments/retrieve.md)

GET/v1/deployments/{deployment\_id}

##### [Update Deployment](api/http/beta/deployments/update.md)

POST/v1/deployments/{deployment\_id}

##### [Archive Deployment](api/http/beta/deployments/archive.md)

POST/v1/deployments/{deployment\_id}/archive

##### [Run Deployment Now](api/http/beta/deployments/run.md)

POST/v1/deployments/{deployment\_id}/run

##### [Pause Deployment](api/http/beta/deployments/pause.md)

POST/v1/deployments/{deployment\_id}/pause

##### [Unpause Deployment](api/http/beta/deployments/unpause.md)

POST/v1/deployments/{deployment\_id}/unpause

#### Beta[Deployment Runs](api/http/beta/deployment_runs.md)

##### [List Deployment Runs](api/http/beta/deployment_runs/list.md)

GET/v1/deployment\_runs

##### [Get Deployment Run](api/http/beta/deployment_runs/retrieve.md)

GET/v1/deployment\_runs/{deployment\_run\_id}

#### Beta[Vaults](api/http/beta/vaults.md)

##### [Create Vault](api/http/beta/vaults/create.md)

POST/v1/vaults

##### [List Vaults](api/http/beta/vaults/list.md)

GET/v1/vaults

##### [Get Vault](api/http/beta/vaults/retrieve.md)

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/http/beta/vaults/update.md)

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/http/beta/vaults/delete.md)

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/http/beta/vaults/archive.md)

POST/v1/vaults/{vault\_id}/archive

#### BetaVaults[Credentials](api/http/beta/vaults/credentials.md)

##### [Create Credential](api/http/beta/vaults/credentials/create.md)

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/http/beta/vaults/credentials/list.md)

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/http/beta/vaults/credentials/retrieve.md)

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/http/beta/vaults/credentials/update.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/http/beta/vaults/credentials/delete.md)

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/http/beta/vaults/credentials/archive.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/http/beta/vaults/credentials/mcp_oauth_validate.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

#### Beta[Memory Stores](api/http/beta/memory_stores.md)

##### [Create a memory store](api/http/beta/memory_stores/create.md)

POST/v1/memory\_stores

##### [List memory stores](api/http/beta/memory_stores/list.md)

GET/v1/memory\_stores

##### [Retrieve a memory store](api/http/beta/memory_stores/retrieve.md)

GET/v1/memory\_stores/{memory\_store\_id}

##### [Update a memory store](api/http/beta/memory_stores/update.md)

POST/v1/memory\_stores/{memory\_store\_id}

##### [Delete a memory store](api/http/beta/memory_stores/delete.md)

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [Archive a memory store](api/http/beta/memory_stores/archive.md)

POST/v1/memory\_stores/{memory\_store\_id}/archive

#### BetaMemory Stores[Memories](api/http/beta/memory_stores/memories.md)

##### [Create a memory](api/http/beta/memory_stores/memories/create.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/http/beta/memory_stores/memories/list.md)

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/http/beta/memory_stores/memories/retrieve.md)

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/http/beta/memory_stores/memories/update.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/http/beta/memory_stores/memories/delete.md)

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

#### BetaMemory Stores[Memory Versions](api/http/beta/memory_stores/memory_versions.md)

##### [List memory versions](api/http/beta/memory_stores/memory_versions/list.md)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/http/beta/memory_stores/memory_versions/retrieve.md)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/http/beta/memory_stores/memory_versions/redact.md)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

#### Beta[Files](api/http/beta/files.md)

##### [Upload File](api/http/beta/files/upload.md)

POST/v1/files

##### [List Files](api/http/beta/files/list.md)

GET/v1/files

##### [Download File](api/http/beta/files/download.md)

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/http/beta/files/retrieve_metadata.md)

GET/v1/files/{file\_id}

##### [Delete File](api/http/beta/files/delete.md)

DELETE/v1/files/{file\_id}

#### Beta[Skills](api/http/beta/skills.md)

##### [Create Skill](api/http/beta/skills/create.md)

POST/v1/skills

##### [List Skills](api/http/beta/skills/list.md)

GET/v1/skills

##### [Get Skill](api/http/beta/skills/retrieve.md)

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/http/beta/skills/delete.md)

DELETE/v1/skills/{skill\_id}

#### BetaSkills[Versions](api/http/beta/skills/versions.md)

##### [Create Skill Version](api/http/beta/skills/versions/create.md)

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/http/beta/skills/versions/list.md)

GET/v1/skills/{skill\_id}/versions

##### [Download Skill Version Content](api/http/beta/skills/versions/download.md)

GET/v1/skills/{skill\_id}/versions/{version}/content

##### [Get Skill Version](api/http/beta/skills/versions/retrieve.md)

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/http/beta/skills/versions/delete.md)

DELETE/v1/skills/{skill\_id}/versions/{version}

#### Beta[Webhooks](api/http/beta/webhooks.md)

##### [Unwrap](api/http/beta/webhooks/unwrap.md)

#### Beta[User Profiles](api/http/beta/user_profiles.md)

##### [Create User Profile](api/http/beta/user_profiles/create.md)

POST/v1/user\_profiles

##### [List User Profiles](api/http/beta/user_profiles/list.md)

GET/v1/user\_profiles

##### [Get User Profile](api/http/beta/user_profiles/retrieve.md)

GET/v1/user\_profiles/{user\_profile\_id}

##### [Update User Profile](api/http/beta/user_profiles/update.md)

POST/v1/user\_profiles/{user\_profile\_id}

##### [Create Enrollment URL](api/http/beta/user_profiles/create_enrollment_url.md)

POST/v1/user\_profiles/{user\_profile\_id}/enrollment\_url

#### Beta[Dreams](api/http/beta/dreams.md)

##### [Create a Dream](api/http/beta/dreams/create.md)

POST/v1/dreams

##### [List Dreams](api/http/beta/dreams/list.md)

GET/v1/dreams

##### [Get a Dream](api/http/beta/dreams/retrieve.md)

GET/v1/dreams/{dream\_id}

##### [Cancel a Dream](api/http/beta/dreams/cancel.md)

POST/v1/dreams/{dream\_id}/cancel

##### [Archive a Dream](api/http/beta/dreams/archive.md)

POST/v1/dreams/{dream\_id}/archive

#### Beta[Tunnels](api/http/beta/tunnels.md)

##### [Create Tunnel](api/http/beta/tunnels/create.md)

POST/v1/tunnels

##### [Get Tunnel](api/http/beta/tunnels/retrieve.md)

GET/v1/tunnels/{tunnel\_id}

##### [List Tunnels](api/http/beta/tunnels/list.md)

GET/v1/tunnels

##### [Archive Tunnel](api/http/beta/tunnels/archive.md)

POST/v1/tunnels/{tunnel\_id}/archive

##### [Reveal Tunnel Token](api/http/beta/tunnels/reveal_token.md)

POST/v1/tunnels/{tunnel\_id}/reveal\_token

##### [Rotate Tunnel Token](api/http/beta/tunnels/rotate_token.md)

POST/v1/tunnels/{tunnel\_id}/rotate\_token

#### BetaTunnels[Certificates](api/http/beta/tunnels/certificates.md)

##### [Create Tunnel Certificate](api/http/beta/tunnels/certificates/create.md)

POST/v1/tunnels/{tunnel\_id}/certificates

##### [Get Tunnel Certificate](api/http/beta/tunnels/certificates/retrieve.md)

GET/v1/tunnels/{tunnel\_id}/certificates/{certificate\_id}

##### [List Tunnel Certificates](api/http/beta/tunnels/certificates/list.md)

GET/v1/tunnels/{tunnel\_id}/certificates

##### [Archive Tunnel Certificate](api/http/beta/tunnels/certificates/archive.md)

POST/v1/tunnels/{tunnel\_id}/certificates/{certificate\_id}/archive

---

*Copyright © Anthropic. All rights reserved.*
