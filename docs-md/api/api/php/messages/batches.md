# Batches

Copy page

PHP

# Batches

##### [Create a Message Batch](api/messages/batches/create.md)

$client->messages->batches->create(list<Request> requests): [MessageBatch](api/messages.md)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/messages/batches/retrieve.md)

$client->messages->batches->retrieve(string messageBatchID): [MessageBatch](api/messages.md)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/messages/batches/list.md)

$client->messages->batches->list(?string afterID, ?string beforeID, ?int limit): Page<[MessageBatch](api/messages.md)>

GET/v1/messages/batches

##### [Cancel a Message Batch](api/messages/batches/cancel.md)

$client->messages->batches->cancel(string messageBatchID): [MessageBatch](api/messages.md)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/messages/batches/delete.md)

$client->messages->batches->delete(string messageBatchID): [DeletedMessageBatch](api/messages.md)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/messages/batches/results.md)

$client->messages->batches->results(string messageBatchID): [MessageBatchIndividualResponse](api/messages.md)

GET/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse

[DeletedMessageBatch](api/messages.md)

string id

ID of the Message Batch.

"message\_batch\_deleted" type

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

[MessageBatch](api/messages.md)

string id

Unique object identifier.

The format and length of IDs may change over time.

?\Datetime archivedAt

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

?\Datetime cancelInitiatedAt

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

\Datetime createdAt

RFC 3339 datetime string representing the time at which the Message Batch was created.

?\Datetime endedAt

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

\Datetime expiresAt

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

ProcessingStatus processingStatus

Processing status of the Message Batch.

[MessageBatchRequestCounts](api/messages.md) requestCounts

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

?string resultsURL

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

"message\_batch" type

Object type.

For Message Batches, this is always `"message_batch"`.

[MessageBatchCanceledResult](api/messages.md)

"canceled" type

[MessageBatchErroredResult](api/messages.md)

[ErrorResponse](api/$shared.md) error

"errored" type

[MessageBatchExpiredResult](api/messages.md)

"expired" type

[MessageBatchIndividualResponse](api/messages.md)

string customID

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

[MessageBatchResult](api/messages.md) result

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

[MessageBatchRequestCounts](api/messages.md)

int canceled

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

int errored

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

int expired

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

int processing

Number of requests in the Message Batch that are processing.

int succeeded

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

[MessageBatchResult](api/messages.md)

One of the following:

[MessageBatchSucceededResult](api/messages.md)

[Message](api/messages.md) message

"succeeded" type

[MessageBatchErroredResult](api/messages.md)

[ErrorResponse](api/$shared.md) error

"errored" type

[MessageBatchCanceledResult](api/messages.md)

"canceled" type

[MessageBatchExpiredResult](api/messages.md)

"expired" type

[MessageBatchSucceededResult](api/messages.md)

[Message](api/messages.md) message

"succeeded" type

---

*Copyright © Anthropic. All rights reserved.*
