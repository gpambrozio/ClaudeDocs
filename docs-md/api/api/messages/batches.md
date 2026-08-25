# Batches

Copy page



cURL

# Batches

##### [Create a Message Batch](api/http/messages/batches/create.md)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/http/messages/batches/retrieve.md)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/http/messages/batches/list.md)

GET/v1/messages/batches

##### [Cancel a Message Batch](api/http/messages/batches/cancel.md)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/http/messages/batches/delete.md)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/http/messages/batches/results.md)

GET/v1/messages/batches/{message\_batch\_id}/results

##### Models



DeletedMessageBatch object{ id, type }

id: string

ID of the Message Batch.



type: "message\_batch\_deleted"

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

defaultmessage\_batch\_deleted



MessageBatch object{ id, archived\_at, cancel\_initiated\_at, 7 more }



MessageBatchCanceledResult object{ type }



type: "canceled"

defaultcanceled



MessageBatchErroredResult object{ error, type }



error: [ErrorResponse](api/http/$shared.md) { error, request\_id, type }



error: [ErrorObject](api/http/$shared.md)

One of the following:

request\_id: string or null



type: "error"

defaulterror



type: "errored"

defaulterrored



MessageBatchExpiredResult object{ type }



type: "expired"

defaultexpired



MessageBatchIndividualResponse object{ custom\_id, result }

This is a single line in the response `.jsonl` file and does not represent the response as a whole.



custom\_id: string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.



result: [MessageBatchResult](api/http/messages/batches.md)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



MessageBatchRequestCounts object{ canceled, errored, expired, 2 more }



canceled: number

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

default0



errored: number

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

default0



expired: number

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

default0



processing: number

Number of requests in the Message Batch that are processing.

default0



succeeded: number

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

default0



MessageBatchResult = [MessageBatchSucceededResult](api/http/messages/batches.md) { message, type } or [MessageBatchErroredResult](api/http/messages/batches.md) { error, type } or [MessageBatchCanceledResult](api/http/messages/batches.md) { type } or [MessageBatchExpiredResult](api/http/messages/batches.md) { type }

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



MessageBatchSucceededResult object{ message, type }



message: [Message](api/http/messages.md) { id, container, content, 7 more }



type: "succeeded"

defaultsucceeded

---

*Copyright © Anthropic. All rights reserved.*
