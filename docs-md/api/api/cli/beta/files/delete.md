# Delete File

Copy page



CLI

# Delete File

$ ant beta:files delete

DELETE/v1/files/{file\_id}

Delete File

##### ParametersExpand Collapse

--file-id: string

ID of the File.

--beta: optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



deleted\_file: object { id, type } 

id: string

ID of the deleted file.



type: optional "file\_deleted"

Deleted object type.

For file deletion, this is always `"file_deleted"`.

"file\_deleted"

Delete File

CLI

```shiki
ant beta:files delete \
  --api-key my-anthropic-api-key \
  --file-id file_id
```

Response 200



```shiki
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file_deleted"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
