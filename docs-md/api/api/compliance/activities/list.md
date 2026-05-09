# Query compliance activities

Copy page

The Compliance API is available only on the Claude Enterprise plan and must be enabled before use. See [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Query compliance activities

GET/v1/compliance/activities

List compliance activities for the authenticated parent organization.

Returns a paginated list of compliance activities that can be filtered by various criteria.

##### Query ParametersExpand Collapse

activity\_types: optional array of "account\_deleted" or "admin\_api\_key\_created" or "admin\_api\_key\_deleted" or 292 more

Filter activities by type

Accepts one of the following:

"account\_deleted"

"admin\_api\_key\_created"

"admin\_api\_key\_deleted"

"admin\_api\_key\_updated"

"api\_key\_created"

"scoped\_api\_key\_deleted"

"scoped\_api\_key\_updated"

"claude\_artifact\_access\_failed"

"claude\_published\_artifact\_deleted"

"claude\_artifact\_published"

"claude\_artifact\_sharing\_updated"

"claude\_artifact\_viewed"

"claude\_chat\_access\_failed"

"claude\_chat\_snapshot\_created"

"claude\_chat\_snapshot\_viewed"

"claude\_chat\_created"

"claude\_chat\_deleted"

"claude\_chat\_deletion\_failed"

"claude\_chat\_settings\_updated"

"claude\_chat\_updated"

"desktop\_extension\_allowlisted"

"desktop\_extension\_blocklisted"

"desktop\_extension\_deleted"

"desktop\_extension\_removed\_from\_allowlist"

"desktop\_extension\_unblocked"

"desktop\_extension\_uploaded"

"desktop\_extension\_version\_uploaded"

"plugin\_installation\_preference\_updated"

"claude\_chat\_viewed"

"claude\_code\_review\_config\_updated"

"claude\_code\_review\_repository\_added"

"claude\_code\_review\_repository\_removed"

"claude\_code\_review\_repository\_updated"

"claude\_code\_security\_center\_config\_updated"

"claude\_file\_access\_failed"

"claude\_file\_deleted"

"claude\_file\_uploaded"

"claude\_file\_viewed"

"claude\_gdrive\_integration\_created"

"claude\_gdrive\_integration\_deleted"

"claude\_gdrive\_integration\_updated"

"claude\_github\_integration\_created"

"claude\_github\_integration\_deleted"

"claude\_github\_integration\_updated"

"claude\_project\_archived"

"claude\_project\_created"

"claude\_project\_deleted"

"claude\_project\_document\_access\_failed"

"claude\_project\_document\_deleted"

"claude\_project\_document\_deletion\_failed"

"claude\_project\_document\_uploaded"

"claude\_project\_document\_viewed"

"claude\_project\_file\_access\_failed"

"claude\_project\_file\_deleted"

"claude\_project\_file\_deletion\_failed"

"claude\_project\_file\_uploaded"

"claude\_project\_reported"

"claude\_project\_sharing\_updated"

"claude\_project\_viewed"

"claude\_user\_role\_updated"

"claude\_user\_settings\_updated"

"admin\_request\_created"

"compliance\_api\_accessed"

"domain\_claim\_initiated"

"end\_user\_invite\_requested"

"environment\_archived"

"environment\_created"

"environment\_deleted"

"environment\_token\_minted"

"environment\_token\_revoked"

"environment\_updated"

"group\_created"

"group\_deleted"

"group\_list\_viewed"

"group\_member\_added"

"group\_member\_list\_viewed"

"group\_member\_removed"

"group\_updated"

"group\_viewed"

"magic\_link\_login\_failed"

"magic\_link\_login\_initiated"

"magic\_link\_login\_succeeded"

"social\_login\_succeeded"

"sso\_login\_failed"

"sso\_login\_initiated"

"sso\_login\_succeeded"

"service\_created"

"service\_deleted"

"service\_key\_created"

"service\_key\_revoked"

"platform\_signing\_key\_created"

"platform\_signing\_key\_deleted"

"platform\_signing\_key\_rotated"

"user\_logged\_out"

"age\_verified"

"anonymous\_mobile\_login\_attempted"

"phone\_code\_sent"

"phone\_code\_verified"

"session\_revoked"

"sso\_second\_factor\_magic\_link"

"org\_user\_deleted"

"org\_user\_invite\_accepted"

"org\_user\_invite\_deleted"

"org\_user\_invite\_re\_sent"

"org\_user\_invite\_rejected"

"org\_user\_invite\_sent"

"org\_user\_left"

"org\_domain\_add\_initiated"

"org\_domain\_removed"

"org\_domain\_verified"

"org\_join\_proposal\_decided"

"org\_magic\_link\_second\_factor\_toggled"

"org\_sso\_add\_initiated"

"org\_sso\_connection\_activated"

"org\_sso\_connection\_deactivated"

"org\_sso\_connection\_deleted"

"org\_sso\_group\_role\_mappings\_updated"

"org\_sso\_provisioning\_mode\_changed"

"org\_sso\_seat\_tier\_assignment\_toggled"

"org\_sso\_seat\_tier\_mappings\_updated"

"org\_sso\_toggled"

"org\_directory\_resync\_completed"

"org\_directory\_resync\_failed"

"org\_directory\_resync\_started"

"org\_directory\_sync\_activated"

"org\_directory\_sync\_add\_initiated"

"org\_directory\_sync\_deleted"

"claude\_organization\_settings\_updated"

"org\_claude\_code\_data\_sharing\_disabled"

"org\_claude\_code\_data\_sharing\_enabled"

"org\_analytics\_api\_capability\_updated"

"org\_compliance\_api\_settings\_updated"

"org\_creation\_blocked"

"org\_parent\_join\_proposal\_created"

"org\_parent\_search\_performed"

"org\_sync\_deleting\_synchronized\_files\_started"

"org\_sync\_synchronized\_files\_deleted"

"org\_data\_export\_completed"

"org\_data\_export\_started"

"org\_members\_exported"

"owned\_projects\_access\_restored"

"audit\_log\_export\_accessed"

"audit\_log\_export\_started"

"org\_data\_export\_accessed"

"organization\_address\_updated"

"primary\_owner\_transferred"

"role\_assignment\_granted"

"role\_assignment\_revoked"

"integration\_user\_connected"

"integration\_user\_disconnected"

"billing\_emails\_updated"

"extra\_usage\_billing\_enabled"

"extra\_usage\_credit\_granted"

"extra\_usage\_spend\_limit\_created"

"extra\_usage\_spend\_limit\_deleted"

"extra\_usage\_spend\_limit\_updated"

"invoice\_collection\_method\_updated"

"managed\_organization\_setup\_completed"

"payment\_method\_updated"

"platform\_spend\_limit\_alert\_emails\_updated"

"platform\_spend\_limit\_created"

"platform\_spend\_limit\_deleted"

"platform\_spend\_limit\_updated"

"prepaid\_auto\_recharge\_disabled"

"prepaid\_auto\_recharge\_updated"

"prepaid\_extra\_usage\_auto\_reload\_disabled"

"prepaid\_extra\_usage\_auto\_reload\_enabled"

"prepaid\_extra\_usage\_auto\_reload\_settings\_updated"

"seat\_tier\_changes\_cancelled"

"seat\_tiers\_purchased"

"subscription\_cancellation\_scheduled"

"subscription\_quantity\_updated"

"subscription\_renewed"

"subscription\_resumed"

"subscription\_started"

"subscription\_upgraded"

"tunnel\_token\_minted"

"tunnel\_token\_revoked"

"user\_consent\_recorded"

"user\_consent\_revoked"

"workspace\_member\_spend\_limit\_created"

"workspace\_member\_spend\_limit\_deleted"

"workspace\_member\_spend\_limit\_updated"

"workspace\_spend\_limit\_created"

"workspace\_spend\_limit\_deleted"

"organization\_icon\_deleted"

"organization\_icon\_updated"

"org\_ip\_restriction\_created"

"org\_ip\_restriction\_deleted"

"org\_ip\_restriction\_updated"

"org\_bulk\_delete\_initiated"

"org\_deleted\_via\_bulk"

"claude\_skill\_created"

"claude\_skill\_deleted"

"claude\_skill\_disabled"

"claude\_skill\_enabled"

"claude\_skill\_replaced"

"claude\_command\_created"

"claude\_command\_deleted"

"claude\_command\_replaced"

"claude\_plugin\_created"

"claude\_plugin\_deleted"

"claude\_plugin\_replaced"

"claude\_plugin\_updated"

"session\_share\_accessed"

"session\_share\_created"

"session\_share\_revoked"

"org\_deletion\_requested"

"org\_invite\_link\_disabled"

"org\_invite\_link\_generated"

"org\_invite\_link\_regenerated"

"rbac\_role\_created"

"rbac\_role\_updated"

"rbac\_role\_deleted"

"rbac\_role\_assigned"

"rbac\_role\_unassigned"

"rbac\_role\_permission\_added"

"rbac\_role\_permission\_removed"

"org\_claude\_code\_desktop\_disabled"

"org\_claude\_code\_desktop\_enabled"

"org\_cowork\_disabled"

"org\_cowork\_enabled"

"org\_cowork\_agent\_disabled"

"org\_cowork\_agent\_enabled"

"org\_work\_across\_apps\_disabled"

"org\_work\_across\_apps\_enabled"

"org\_hipaa\_self\_serve\_enabled"

"org\_taint\_added"

"org\_taint\_removed"

"mcp\_server\_created"

"mcp\_server\_deleted"

"mcp\_server\_updated"

"mcp\_tool\_policy\_updated"

"cli\_plugin\_exec\_policy\_updated"

"marketplace\_created"

"marketplace\_deleted"

"marketplace\_updated"

"ghe\_configuration\_created"

"ghe\_configuration\_deleted"

"ghe\_configuration\_updated"

"ghe\_user\_connected"

"ghe\_user\_disconnected"

"ghe\_webhook\_signature\_invalid"

"org\_discoverability\_enabled"

"org\_discoverability\_disabled"

"org\_discoverability\_settings\_updated"

"org\_join\_request\_created"

"org\_join\_request\_approved"

"org\_join\_request\_instant\_approved"

"org\_join\_request\_dismissed"

"org\_join\_requests\_bulk\_dismissed"

"org\_member\_invites\_enabled"

"org\_member\_invites\_disabled"

"lti\_launch\_initiated"

"lti\_launch\_success"

"lti\_platform\_created"

"lti\_platform\_updated"

"org\_users\_listed"

"org\_user\_viewed"

"org\_invites\_listed"

"org\_invite\_viewed"

"org\_external\_key\_created"

"org\_external\_key\_updated"

"org\_external\_key\_deleted"

"org\_external\_key\_validated"

"platform\_workspace\_created"

"platform\_workspace\_updated"

"platform\_workspace\_archived"

"platform\_federation\_issuer\_archived"

"platform\_federation\_issuer\_updated"

"platform\_federation\_rule\_archived"

"platform\_federation\_rule\_updated"

"platform\_service\_account\_archived"

"platform\_service\_account\_updated"

"platform\_workspace\_members\_listed"

"platform\_workspace\_member\_viewed"

"platform\_workspace\_member\_added"

"platform\_workspace\_member\_updated"

"platform\_workspace\_member\_removed"

"platform\_usage\_report\_messages\_viewed"

"platform\_usage\_report\_claude\_code\_viewed"

"platform\_cost\_report\_viewed"

"platform\_api\_key\_updated"

"platform\_api\_key\_created"

"platform\_workspace\_rate\_limit\_updated"

"platform\_workspace\_rate\_limit\_deleted"

"platform\_file\_uploaded"

"platform\_file\_content\_downloaded"

"platform\_file\_deleted"

"platform\_skill\_version\_created"

"platform\_skill\_version\_deleted"

"scim\_user\_created"

"scim\_user\_updated"

"scim\_user\_deleted"

"claude\_pubsec\_identity\_configured"

actor\_ids: optional array of string

Filter activities by actor IDs (currently only `user_...` IDs are supported). Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

after\_id: optional string

Pagination cursor for retrieving the next page of results (heading backwards in time). To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

before\_id: optional string

Pagination cursor for retrieving the previous page of results (heading forwards in time). To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

created\_at: optional object { gt, gte, lt, lte }

gt: optional string

Filter activities created after this time (RFC 3339 format)

gte: optional string

Filter activities created at or after this time (RFC 3339 format)

lt: optional string

Filter activities created before this time (RFC 3339 format)

lte: optional string

Filter activities created at or before this time (RFC 3339 format)

limit: optional number

Maximum results (default: 100, max: 5000)

organization\_ids: optional array of string

Filter activities by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.

##### Header ParametersExpand Collapse

"x-api-key": optional string

##### ReturnsExpand Collapse

data: optional array of map[unknown]

first\_id: optional string

has\_more: optional boolean

last\_id: optional string

Query compliance activities

```shiki
curl https://api.anthropic.com/v1/compliance/activities \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200

```shiki
{
  "data": [
    {
      "foo": "bar"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

##### Returns Examples

Response 200

```shiki
{
  "data": [
    {
      "foo": "bar"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

---

*Copyright © Anthropic. All rights reserved.*
