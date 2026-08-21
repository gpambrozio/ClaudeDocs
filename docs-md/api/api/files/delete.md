# Delete File

Copy page



cURL

# Delete File

DELETE/v1/files/{file\_id}

Delete File

##### Path ParametersExpand Collapse

file\_id: string

ID of the File.

##### ReturnsExpand Collapse



DeletedFile object { id, type } 

id: string

ID of the deleted file.



type: optional "file\_deleted"

Deleted object type.

For file deletion, this is always `"file_deleted"`.

Delete File

cURL

```shiki
curl https://api.anthropic.com/v1/files/$FILE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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
