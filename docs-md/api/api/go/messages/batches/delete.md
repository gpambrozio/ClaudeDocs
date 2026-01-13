# Delete a Message Batch

Copy page

Go

# Delete a Message Batch

client.Messages.Batches.Delete(ctx, messageBatchID) (\*[DeletedMessageBatch](api/messages.md), error)

delete/v1/messages/batches/{message\_batch\_id}

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

##### ParametersExpand Collapse

messageBatchID string

ID of the Message Batch.

##### ReturnsExpand Collapse

type DeletedMessageBatch struct{…}

ID string

ID of the Message Batch.

Type MessageBatchDeleted

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Accepts one of the following:

const MessageBatchDeletedMessageBatchDeleted MessageBatchDeleted = "message\_batch\_deleted"

Delete a Message Batch

Go

```shiki
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  deletedMessageBatch, err := client.Messages.Batches.Delete(context.TODO(), "message_batch_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", deletedMessageBatch.ID)
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