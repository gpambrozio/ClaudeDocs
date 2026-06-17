# Delete a Message Batch

Copy page



PHP

# Delete a Message Batch

$client->messages->batches->delete(string messageBatchID): [DeletedMessageBatch](api/messages.md)

DELETE/v1/messages/batches/{message\_batch\_id}

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

##### ParametersExpand Collapse

messageBatchID: string

ID of the Message Batch.

##### ReturnsExpand Collapse



[DeletedMessageBatch](api/messages.md)

string id

ID of the Message Batch.



"message\_batch\_deleted" type

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Delete a Message Batch

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$deletedMessageBatch = $client->messages->batches->delete('message_batch_id');

var_dump($deletedMessageBatch);
```

Response 200



```shiki
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
