# Download artifact content

Copy page



# Download artifact content

GET/v1/compliance/apps/artifacts/{artifact\_version\_id}/content

Download the content of an artifact version for compliance purposes.

Returns the full text content of the artifact version.

##### Path parameters

artifact\_version\_id: string

The artifact version ID (tagged ID, e.g., claude\_artifact\_version\_abc123)

##### Headers

"x-api-key": optional string

### Download artifact content

cURL



```shiki
curl https://api.anthropic.com/v1/compliance/apps/artifacts/$ARTIFACT_VERSION_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

---

*Copyright © Anthropic. All rights reserved.*
