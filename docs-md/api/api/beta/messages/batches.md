# Batches

Copy page



cURL

# Batches

##### [Create a Message Batch](api/http/beta/messages/batches/create.md)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/http/beta/messages/batches/retrieve.md)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/http/beta/messages/batches/list.md)

GET/v1/messages/batches

##### [Cancel a Message Batch](api/http/beta/messages/batches/cancel.md)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/http/beta/messages/batches/delete.md)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/http/beta/messages/batches/results.md)

GET/v1/messages/batches/{message\_batch\_id}/results

##### Models



BetaDeletedMessageBatch object{ id, type }

id: string

ID of the Message Batch.



type: "message\_batch\_deleted"

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

defaultmessage\_batch\_deleted



BetaMessageBatch object{ id, archived\_at, cancel\_initiated\_at, 7 more }



BetaMessageBatchCanceledResult object{ type }



type: "canceled"

defaultcanceled



BetaMessageBatchErroredResult object{ error, type }



error: [BetaErrorResponse](api/http/beta.md) { error, request\_id, type }



error: [BetaError](api/http/beta.md)

One of the following:

request\_id: string or null



type: "error"

defaulterror



type: "errored"

defaulterrored



BetaMessageBatchExpiredResult object{ type }



type: "expired"

defaultexpired



BetaMessageBatchIndividualResponse object{ custom\_id, result }

This is a single line in the response `.jsonl` file and does not represent the response as a whole.



custom\_id: string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.



result: [BetaMessageBatchResult](api/http/beta/messages/batches.md)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



BetaMessageBatchRequestCounts object{ canceled, errored, expired, 2 more }



canceled: number

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

default0



errored: number

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

default0



expired: number

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

default0



processing: number

Number of requests in the Message Batch that are processing.

default0



succeeded: number

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

default0



BetaMessageBatchResult = [BetaMessageBatchSucceededResult](api/http/beta/messages/batches.md) { message, type } or [BetaMessageBatchErroredResult](api/http/beta/messages/batches.md) { error, type } or [BetaMessageBatchCanceledResult](api/http/beta/messages/batches.md) { type } or [BetaMessageBatchExpiredResult](api/http/beta/messages/batches.md) { type }

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



BetaMessageBatchSucceededResult object{ message, type }



message: [BetaMessage](api/http/beta/messages.md) { id, container, content, 9 more }



type: "succeeded"

defaultsucceeded

---

*Copyright © Anthropic. All rights reserved.*
