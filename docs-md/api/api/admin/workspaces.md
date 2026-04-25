# Workspaces

Copy page

# Workspaces

##### [Create Workspace](api/admin/workspaces/create.md)

POST/v1/organizations/workspaces

##### [Get Workspace](api/admin/workspaces/retrieve.md)

GET/v1/organizations/workspaces/{workspace\_id}

##### [List Workspaces](api/admin/workspaces/list.md)

GET/v1/organizations/workspaces

##### [Update Workspace](api/admin/workspaces/update.md)

POST/v1/organizations/workspaces/{workspace\_id}

##### [Archive Workspace](api/admin/workspaces/archive.md)

POST/v1/organizations/workspaces/{workspace\_id}/archive

#### WorkspacesMembers

##### [Create Workspace Member](api/admin/workspaces/members/create.md)

POST/v1/organizations/workspaces/{workspace\_id}/members

##### [Get Workspace Member](api/admin/workspaces/members/retrieve.md)

GET/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### [List Workspace Members](api/admin/workspaces/members/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/members

##### [Update Workspace Member](api/admin/workspaces/members/update.md)

POST/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### [Delete Workspace Member](api/admin/workspaces/members/delete.md)

DELETE/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### ModelsExpand Collapse

WorkspaceMember = object { type, user\_id, workspace\_id, workspace\_role }

type: "workspace\_member"

Object type.

For Workspace Members, this is always `"workspace_member"`.

user\_id: string

ID of the User.

workspace\_id: string

ID of the Workspace.

workspace\_role: "workspace\_user" or "workspace\_developer" or "workspace\_restricted\_developer" or 2 more

Role of the Workspace Member.

Accepts one of the following:

"workspace\_user"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_admin"

"workspace\_billing"

MemberDeleteResponse = object { type, user\_id, workspace\_id }

type: "workspace\_member\_deleted"

Deleted object type.

For Workspace Members, this is always `"workspace_member_deleted"`.

user\_id: string

ID of the User.

workspace\_id: string

ID of the Workspace.

#### WorkspacesRate Limits

##### [List Workspace Rate Limits](api/admin/workspaces/rate_limits/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/rate\_limits

##### ModelsExpand Collapse

RateLimitListResponse = object { data, next\_page }

data: array of object { group\_type, limits, models, type }

Rate-limit entries for the workspace, one per group that has at least one override.

group\_type: "model\_group" or "batch" or "token\_count" or 3 more

The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

Accepts one of the following:

"model\_group"

"batch"

"token\_count"

"files"

"skills"

"web\_search"

limits: array of object { org\_limit, type, value }

The limiter values overridden for this group in this workspace. Limiter types without a workspace override are omitted and inherit the organization value.

org\_limit: number

The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

type: string

The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

value: number

The workspace-level override value for this limiter type.

models: array of string

Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

type: "workspace\_rate\_limit"

Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

next\_page: string

Token to provide in as `page` in the subsequent request to retrieve the next page of data.

---

*Copyright © Anthropic. All rights reserved.*
