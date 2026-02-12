# Delete a Message Batch

Copy page

Ruby

# Delete a Message Batch

messages.batches.delete(message\_batch\_id) -> [DeletedMessageBatch](api/messages.md) { id, type }

DELETE/v1/messages/batches/{message\_batch\_id}

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

##### ParametersExpand Collapse

message\_batch\_id: String

ID of the Message Batch.

##### ReturnsExpand Collapse

class DeletedMessageBatch { id, type }

id: String

ID of the Message Batch.

type: :message\_batch\_deleted

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Delete a Message Batch

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

deleted_message_batch = anthropic.messages.batches.delete("message_batch_id")

puts(deleted_message_batch)
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
