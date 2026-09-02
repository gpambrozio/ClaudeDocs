# Update Compliance Settings

Copy page



cURL

# Update Compliance Settings

POST/v1/organizations/compliance\_settings

Update your organization's Compliance Settings.

Setting `state` to `enabled` turns on the Compliance API and begins
capturing organization activity events. Setting it to `disabled` turns
both off. `state` reflects whether the Compliance API is enabled.

A request that sets `state` to its current value succeeds and leaves the
resource unchanged. A `disabled` request stays in effect until a later
`enabled` request or the organization's next provisioning action that
enables Access Transparency: enabling Access Transparency also enables
the Compliance API, which serves its activity events, so such
provisioning (including re-runs) re-enables the Compliance API even
after a `disabled` request. Automated provisioning never disables
compliance settings.

##### Body



state: [BetaComplianceSettingsStateEnabledParam](api/http/beta/organization/compliance_settings.md) { type } or [BetaComplianceSettingsStateDisabledParam](api/http/beta/organization/compliance_settings.md) { type }

Desired state. Accepts the string shorthand "enabled" or "disabled" in place of the object form; the response always returns the canonical object form.

One of the following:



BetaComplianceSettingsStateEnabledParam object{ type }

type: "enabled"



BetaComplianceSettingsStateDisabledParam object{ type }

type: "disabled"

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

Update Compliance Settings

cURL

```shiki
curl https://api.anthropic.com/v1/organizations/compliance_settings \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "state": {
            "type": "enabled"
          }
        }'
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
