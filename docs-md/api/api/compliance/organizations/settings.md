# Settings

Copy page



# Settings

##### [Get effective organization settings](api/http/compliance/organizations/settings/retrieve.md)

GET/v1/compliance/organizations/{organization\_id}/settings

##### Models



SettingRetrieveResponse object{ api\_keys, organization\_id, settings, type }

The resolved settings in force for one organization at read time.

Settings appear at most once each, in a fixed relative order, and values
reflect the enforced state. A setting the organization's administrators
cannot change — for example, one controlled by Anthropic policy or not
available to the organization — is omitted from the list.

---

*Copyright © Anthropic. All rights reserved.*
