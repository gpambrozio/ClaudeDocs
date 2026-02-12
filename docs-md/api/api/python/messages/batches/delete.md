# Delete a Message Batch

Copy page

Python

# Delete a Message Batch

messages.batches.delete(strmessage\_batch\_id)  -> [DeletedMessageBatch](api/messages.md)

DELETE/v1/messages/batches/{message\_batch\_id}

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

##### ParametersExpand Collapse

message\_batch\_id: str

ID of the Message Batch.

##### ReturnsExpand Collapse

class DeletedMessageBatch: …

id: str

ID of the Message Batch.

type: Literal["message\_batch\_deleted"]

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Delete a Message Batch

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
deleted_message_batch = client.messages.batches.delete(
    "message_batch_id",
)
print(deleted_message_batch.id)
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
