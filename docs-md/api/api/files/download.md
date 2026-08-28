# Download File

Copy page



cURL

# Download File

GET/v1/files/{file\_id}/content

Download File

##### Path parameters

file\_id: string

ID of the File.



### Download File

cURL



```shiki
curl https://api.anthropic.com/v1/files/$FILE_ID/content \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

---

*Copyright © Anthropic. All rights reserved.*
