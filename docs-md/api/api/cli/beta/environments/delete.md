# Delete Environment

Copy page

CLI

# Delete Environment

$ ant beta:environments delete

DELETE/v1/environments/{environment\_id}

Delete an environment by ID. Returns a confirmation of the deletion.

##### ParametersExpand Collapse

--environment-id: string

--beta: optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

beta\_environment\_delete\_response: object { id, type }

Response after deleting an environment.

id: string

Environment identifier

type: "environment\_deleted"

The type of response

Delete Environment

CLI

```shiki
ant beta:environments delete \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW
```

Response 200

```shiki
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "type": "environment_deleted"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "type": "environment_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
