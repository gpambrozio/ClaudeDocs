# Compliance Settings

Copy page



cURL

# Compliance Settings

##### [Get Compliance Settings](api/http/beta/organization/compliance_settings/retrieve.md)

GET/v1/organizations/compliance\_settings

##### [Update Compliance Settings](api/http/beta/organization/compliance_settings/update.md)

POST/v1/organizations/compliance\_settings

##### Models

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



BetaComplianceSettingsStateDisabled object{ type }



type: "disabled"

defaultdisabled



BetaComplianceSettingsStateDisabledParam object{ type }

type: "disabled"



BetaComplianceSettingsStateEnabled object{ type }



type: "enabled"

defaultenabled



BetaComplianceSettingsStateEnabledParam object{ type }

type: "enabled"

---

*Copyright © Anthropic. All rights reserved.*
