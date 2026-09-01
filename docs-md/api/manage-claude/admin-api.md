# Admin API

Copy page



The [Admin API](api/admin.md) lets you manage your organization's members, workspaces, invites, and API keys programmatically instead of by hand in the [Claude Console](/).

## Authentication

Authenticate with any of the three credentials. An Admin API key covers most endpoints. The service-account, federation-issuer, and federation-rule endpoints accept only an `org:admin` OAuth token. Send a personal key or service account key in the `x-api-key` header, as you would an Admin API key. The following examples call the [organization info endpoint](#accessing-organization-info) with an OAuth token and with an Admin API key.

The Python, TypeScript, C#, Go, Java, PHP, and Ruby SDKs expose the Admin API under `client.beta.organization`, and the `ant` CLI under `ant beta:organization`. The examples on this page use the default client, which reads an Admin API key from `ANTHROPIC_API_KEY` or an OAuth bearer token from `ANTHROPIC_AUTH_TOKEN`. SDK list methods in Python, TypeScript, C#, Go, and Java return an iterator that fetches more pages on demand, so `limit` sets the page size, not the total. The PHP, Ruby, and curl examples return one page. In the CLI, `--limit` caps the results on the member, invite, workspace, workspace-member, and API-key lists. For each endpoint's parameters and responses, see the [Admin API reference](api/admin.md).

### OAuth bearer token

Log in with the [`ant` CLI](cli-sdks-libraries/cli/quickstart.md) under a dedicated profile with the `org:admin` scope (see [Admin access](cli-sdks-libraries/cli/authentication.md)), then export the bearer token. `--profile admin` stores the `org:admin` credential under its own profile and makes it the CLI's active profile. The exported variable applies to every SDK and CLI call in that shell. Use a shell you reserve for administration, unset the variable when you're done, and switch the CLI back with `ant profile activate default`:

CLI



```shiki
ant auth login --profile admin --scope "org:admin"
export ANTHROPIC_AUTH_TOKEN=$(ant auth print-credentials --profile admin --access-token)
```

Interactive tokens are short-lived. If requests start returning 401, re-run the `export` command to refresh the token.

The SDKs and the `ant` CLI read `ANTHROPIC_AUTH_TOKEN` automatically. Leave `ANTHROPIC_API_KEY` unset in the same shell so they send the bearer token. Automated workloads skip the login: they authenticate through workload identity federation, and the SDKs and CLI perform the token exchange from the federation environment variables. See [Bootstrap a workload to manage WIF](manage-claude/wif-admin-api.md).

Call the Admin API with the exported token:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

organization = client.beta.organization.retrieve()

print(f"id: {organization.id}")
print(f"name: {organization.name}")
```

An `org:admin` token grants access to the whole organization, regardless of the workspace the underlying profile or [federation rule](#federation-rules) is bound to.

For CI and other non-interactive workloads, mint the token with Workload Identity Federation instead of logging in interactively. See [Manage WIF with the Admin API](manage-claude/wif-admin-api.md).

### Admin API key

To create an Admin API key for your organization type, see [Create an Admin API key](manage-claude/admin-api-keys.md).

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

organization = client.beta.organization.retrieve()

print(f"id: {organization.id}")
print(f"name: {organization.name}")
```

## How the Admin API works

Authenticate with any credential from [Authentication](#authentication), then manage the following resources:

- Organization members and their roles
- Organization invites
- Workspaces and their members
- API keys
- Service accounts, federation issuers, and federation rules (`org:admin` OAuth token only)

Common uses include automating onboarding and offboarding, managing workspace access, and auditing API keys.

## Organization roles and permissions

There are five organization-level roles. For details, see [API Console roles and permissions](https://support.claude.com/en/articles/10186004-api-console-roles-and-permissions).

| Role | Permissions |
| --- | --- |
| user | Can use playground |
| claude\_code\_user | Can use playground and [Claude Code](overview.md) |
| developer | Can use playground and manage API keys |
| billing | Can use playground and manage billing details |
| admin | Can do all of the preceding, plus manage users |

Organization owners and primary owners have all admin permissions and can also manage admins. All references to the admin role on this page also apply to owners and primary owners.

## Key concepts

### Organization members

List [organization members](api/admin-api/users/get-user.md), update their roles, and remove them.

List the members of your organization:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

users = client.beta.organization.users.list(limit=10)

# Automatically fetches more pages as needed.
for user in users:
    print(f"{user.id}: {user.email} ({user.role})")
```

Update a member's role:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

user = client.beta.organization.users.update(
    "user_01XyDMpzjS89pFZXqSFUBDr6", role="developer"
)

print(f"id: {user.id}")
print(f"role: {user.role}")
```

Remove a member from the organization:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

removed_user = client.beta.organization.users.remove("user_01XyDMpzjS89pFZXqSFUBDr6")

print(f"id: {removed_user.id}")
```

### Organization invites

Invite users to your organization and manage pending [invites](api/admin-api/invites/get-invite.md).

Invite a user to your organization:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

invite = client.beta.organization.invites.create(
    email="user@example.com", role="developer"
)

print(f"id: {invite.id}")
print(f"email: {invite.email}")
print(f"status: {invite.status}")
print(f"expires_at: {invite.expires_at}")
```

List pending invites:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

invites = client.beta.organization.invites.list(limit=10)

# Automatically fetches more pages as needed.
for invite in invites:
    print(f"{invite.id}: {invite.email} ({invite.status})")
```

Delete an invite:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

deleted_invite = client.beta.organization.invites.delete(
    "invite_015gWxHNr6h6TdRPZTmuCGnn"
)

print(f"id: {deleted_invite.id}")
```

### Workspaces

See [Workspaces](manage-claude/workspaces.md) for Console and API examples.

### Workspace members

Manage [user access to specific workspaces](api/admin-api/workspace_members/get-workspace-member.md):

Add a member to a workspace:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

member = client.beta.organization.workspaces.members.add(
    "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
    user_id="user_01XyDMpzjS89pFZXqSFUBDr6",
    workspace_role="workspace_developer",
)

print(f"user_id: {member.user_id}")
print(f"workspace_role: {member.workspace_role}")
```

List the members of a workspace:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

members = client.beta.organization.workspaces.members.list(
    "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ", limit=10
)

# Automatically fetches more pages as needed.
for member in members:
    print(f"{member.user_id}: {member.workspace_role}")
```

Update a workspace member's role:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

member = client.beta.organization.workspaces.members.update(
    "user_01XyDMpzjS89pFZXqSFUBDr6",
    workspace_id="wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
    workspace_role="workspace_admin",
)

print(f"user_id: {member.user_id}")
print(f"workspace_role: {member.workspace_role}")
```

Remove a member from a workspace:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

removed_member = client.beta.organization.workspaces.members.remove(
    "user_01XyDMpzjS89pFZXqSFUBDr6", workspace_id="wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
)

print(f"user_id: {removed_member.user_id}")
```

### API keys

Monitor and manage [API keys](api/admin/api_keys/list.md). Each key in the response includes its `expires_at` timestamp (`null` for keys without an [expiration](manage-claude/authentication.md)) and `principal`, the identity it acts as (see [Key types](manage-claude/authentication.md)). For a personal key, `principal` is `{"type": "user_actor", "user_id": "user_..."}`; for a service account key, `{"type": "service_account_actor", "service_account_id": "svac_..."}`; and for a workspace key, `null`. Each key also has a `scope` object: `{"type": "workspace", "workspace_id": "wrkspc_..."}` for a key bound to one workspace, or `{"type": "organization"}` for a key that can work across any workspace the account has access to. The top-level `workspace_id` field is deprecated and is `null` both for keys bound to the Default Workspace and for keys without a workspace scope; use `scope` to tell them apart. Filtering the list by `workspace_id` with the Default Workspace's ID returns only keys bound to the Default Workspace; keys without a workspace scope aren't returned under any `workspace_id` filter.

List the active API keys in a workspace:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

api_keys = client.beta.organization.api_keys.list(
    limit=10, status="active", workspace_id="wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
)

# Automatically fetches more pages as needed.
for api_key in api_keys:
    print(f"{api_key.id}: {api_key.name} ({api_key.status})")
```

Rename or deactivate an API key:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

api_key = client.beta.organization.api_keys.update(
    "apikey_01Rj2N8SVvo6BePZj99NhmiT", status="inactive", name="New Key Name"
)

print(f"id: {api_key.id}")
print(f"name: {api_key.name}")
print(f"status: {api_key.status}")
```

### Service accounts

Create and manage service accounts (`svac_...`), the non-human identities that [service account keys](manage-claude/authentication.md) and [Workload Identity Federation](manage-claude/workload-identity-federation.md) tokens act as. These endpoints, like the federation-issuer and federation-rule endpoints, require an `org:admin` OAuth token. See [Manage WIF with the Admin API](manage-claude/wif-admin-api.md).

### Federation issuers

Register the OIDC identity providers (`fdis_...`) whose tokens may assert workload identity for your organization. See [Manage WIF with the Admin API](manage-claude/wif-admin-api.md).

### Federation rules

Manage the rules (`fdrl_...`) that map issuer tokens to service accounts and scopes. See [Manage WIF with the Admin API](manage-claude/wif-admin-api.md).

## Accessing organization info

The `/v1/organizations/me` endpoint returns the organization that your credential belongs to:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

organization = client.beta.organization.retrieve()

print(f"id: {organization.id}")
print(f"name: {organization.name}")
```

```shiki
{
  "id": "12345678-1234-5678-1234-567812345678",
  "type": "organization",
  "name": "Organization Name"
}
```



For parameter details and response schemas, see the [Organization Info API reference](api/admin-api/organization/get-me.md).

## Usage and cost reports

Track your organization's usage and costs with the [Usage and Cost API](manage-claude/usage-cost-api.md).

## Claude Code analytics

Monitor developer productivity and Claude Code adoption with the [Claude Code Analytics API](manage-claude/claude-code-analytics-api.md).

## Rate limits

Read the rate limits configured for your organization and its workspaces with the [Rate Limits API](manage-claude/rate-limits-api.md).

## Compliance API

Retrieve audit and activity data for your organization with the [Compliance API](manage-claude/compliance-api.md). Admin API keys can read only the Activity Feed. For full access, see [Set up the Compliance API](manage-claude/compliance-api-access.md).

## Best practices

- Use meaningful names and descriptions for workspaces and API keys
- Handle errors from failed operations
- Regularly audit member roles and permissions
- Clean up unused workspaces and expired invites
- Monitor API key usage, audit each key's [`expires_at`](manage-claude/authentication.md), and rotate keys periodically

## FAQ

### What permissions are needed to use the Admin API?

### Can I create new API keys through the Admin API?

### What happens to API keys when removing a user?

### Can organization admins be removed through the API?

### How long do organization invites last?

For workspace-specific questions, see the [Workspaces FAQ](manage-claude/workspaces.md).

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
