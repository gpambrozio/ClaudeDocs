# Delete a Message Batch

Copy page

Kotlin

# Delete a Message Batch

messages().batches().delete(BatchDeleteParamsparams = BatchDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : [DeletedMessageBatch](api/messages.md)

delete/v1/messages/batches/{message\_batch\_id}

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

##### ParametersExpand Collapse

params: BatchDeleteParams

messageBatchId: Optional<String>

ID of the Message Batch.

##### ReturnsExpand Collapse

class DeletedMessageBatch:

id: String

ID of the Message Batch.

type: JsonValue; "message\_batch\_deleted"constant"message\_batch\_deleted"constant

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Accepts one of the following:

MESSAGE\_BATCH\_DELETED("message\_batch\_deleted")

Delete a Message Batch

Kotlin

```shiki
package com.anthropic.example

import com.anthropic.client.AnthropicClient
import com.anthropic.client.okhttp.AnthropicOkHttpClient
import com.anthropic.models.messages.batches.BatchDeleteParams
import com.anthropic.models.messages.batches.DeletedMessageBatch

fun main() {
    val client: AnthropicClient = AnthropicOkHttpClient.fromEnv()

    val deletedMessageBatch: DeletedMessageBatch = client.messages().batches().delete("message_batch_id")
}
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
