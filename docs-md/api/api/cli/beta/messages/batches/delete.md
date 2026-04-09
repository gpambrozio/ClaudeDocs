# Delete a Message Batch

Copy page

CLI

# Delete a Message Batch

$ ant beta:messages:batches delete

DELETE/v1/messages/batches/{message\_batch\_id}

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

##### ParametersExpand Collapse

--message-batch-id: string

ID of the Message Batch.

--beta: optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

beta\_deleted\_message\_batch: object { id, type }

id: string

ID of the Message Batch.

type: "message\_batch\_deleted"

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Delete a Message Batch

CLI

```shiki
ant beta:messages:batches delete \
  --api-key my-anthropic-api-key \
  --message-batch-id message_batch_id
```

Response 200

```shiki
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
