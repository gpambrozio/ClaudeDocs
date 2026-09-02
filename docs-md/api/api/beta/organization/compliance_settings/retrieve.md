# Get Compliance Settings

Copy page



cURL

# Get Compliance Settings

GET/v1/organizations/compliance\_settings

Retrieve your organization's Compliance Settings.

Compliance Settings is a singleton resource: there is exactly one per
organization, addressed without an identifier. The `state` field reflects
whether the Compliance API is enabled. An organization with a parent
organization reads the state inherited from the parent's configuration.

##### Returns



BetaComplianceSettings object{ state, type }



state: [BetaComplianceSettingsStateEnabled](api/http/beta/organization/compliance_settings.md) { type } or [BetaComplianceSettingsStateDisabled](api/http/beta/organization/compliance_settings.md) { type }

Whether the Compliance API is enabled for this organization.

One of the following:



BetaComplianceSettingsStateEnabled object{ type }



type: "enabled"

defaultenabled



BetaComplianceSettingsStateDisabled object{ type }



type: "disabled"

defaultdisabled



type: "compliance\_settings"

defaultcompliance\_settings

Get Compliance Settings

cURL

```shiki
curl https://api.anthropic.com/v1/organizations/compliance_settings \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```shiki
{
  "state": {
    "type": "enabled"
  },
  "type": "compliance_settings"
}
```

##### Returns Examples

Response 200



```shiki
{
  "state": {
    "type": "enabled"
  },
  "type": "compliance_settings"
}
```

---

*Copyright © Anthropic. All rights reserved.*
