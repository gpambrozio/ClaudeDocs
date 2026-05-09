# Download artifact content

GET/v1/compliance/apps/artifacts/{artifact\_version\_id}/content

Download the content of an artifact version for compliance purposes.

Returns the full text content of the artifact version.

##### Path ParametersExpand Collapse

artifact\_version\_id: string

The artifact version ID (tagged ID, e.g., claude\_artifact\_version\_abc123)

##### Header ParametersExpand Collapse

"x-api-key": optional string

Download artifact content

```shiki
curl https://api.anthropic.com/v1/compliance/apps/artifacts/$ARTIFACT_VERSION_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200

```shiki
{}
```

##### Returns Examples

Response 200

```shiki
{}
```

---

*Copyright © Anthropic. All rights reserved.*
