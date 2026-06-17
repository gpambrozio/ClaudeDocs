# Download File

Copy page



CLI

# Download File

$ ant beta:files download

GET/v1/files/{file\_id}/content

Download File

##### ParametersExpand Collapse

--file-id: string

ID of the File.

--beta: optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

unnamed\_schema\_0: file path

Download File

CLI

```shiki
ant beta:files download \
  --api-key my-anthropic-api-key \
  --file-id file_id
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
