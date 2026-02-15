# Get Workspace

Copy page

# Get Workspace

GET/v1/organizations/workspaces/{workspace\_id}

Get Workspace

##### Path ParametersExpand Collapse

workspace\_id: string

ID of the Workspace.

##### ReturnsExpand Collapse

Workspace = object { id, archived\_at, created\_at, 4 more }

id: string

ID of the Workspace.

archived\_at: string

RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

created\_at: string

RFC 3339 datetime string indicating when the Workspace was created.

data\_residency: object { allowed\_inference\_geos, default\_inference\_geo, workspace\_geo }

Data residency configuration.

allowed\_inference\_geos: array of string or "unrestricted"

Permitted inference geo values. 'unrestricted' means all geos are allowed.

Accepts one of the following:

UnionMember0 = array of string

UnionMember1 = "unrestricted"

default\_inference\_geo: string

Default inference geo applied when requests omit the parameter.

workspace\_geo: string

Geographic region for workspace data storage. Immutable after creation.

display\_color: string

Hex color code representing the Workspace in the Anthropic Console.

name: string

Name of the Workspace.

type: "workspace"

Object type.

For Workspaces, this is always `"workspace"`.

Get Workspace

```shiki
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
