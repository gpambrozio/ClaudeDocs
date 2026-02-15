# Delete a Message Batch

Copy page

C#

# Delete a Message Batch

[DeletedMessageBatch](api/messages.md) Messages.Batches.Delete(BatchDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/messages/batches/{message\_batch\_id}

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

##### ParametersExpand Collapse

BatchDeleteParams parameters

required string messageBatchID

ID of the Message Batch.

##### ReturnsExpand Collapse

class DeletedMessageBatch:

required string ID

ID of the Message Batch.

JsonElement Type "message\_batch\_deleted"constant

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Delete a Message Batch

C#

```shiki
BatchDeleteParams parameters = new() { MessageBatchID = "message_batch_id" };

var deletedMessageBatch = await client.Messages.Batches.Delete(parameters);

Console.WriteLine(deletedMessageBatch);
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
