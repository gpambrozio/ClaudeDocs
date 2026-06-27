# Batches

Copy page



PHP

# Batches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

$client->beta->messages->batches->create(list<Request> requests, ?list<AnthropicBeta> betas): [MessageBatch](api/beta/messages/batches.md)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

$client->beta->messages->batches->retrieve(string messageBatchID, ?list<AnthropicBeta> betas): [MessageBatch](api/beta/messages/batches.md)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

$client->beta->messages->batches->list(?string afterID, ?string beforeID, ?int limit, ?list<AnthropicBeta> betas): Page<[MessageBatch](api/beta/messages/batches.md)>

GET/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

$client->beta->messages->batches->cancel(string messageBatchID, ?list<AnthropicBeta> betas): [MessageBatch](api/beta/messages/batches.md)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

$client->beta->messages->batches->delete(string messageBatchID, ?list<AnthropicBeta> betas): [DeletedMessageBatch](api/beta/messages/batches.md)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

$client->beta->messages->batches->results(string messageBatchID, ?list<AnthropicBeta> betas): [MessageBatchIndividualResponse](api/beta/messages/batches.md)

GET/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse



[DeletedMessageBatch](api/beta/messages/batches.md)

string id

ID of the Message Batch.



"message\_batch\_deleted" type

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.



[MessageBatch](api/beta/messages/batches.md)



string id

Unique object identifier.

The format and length of IDs may change over time.

?\Datetime archivedAt

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

?\Datetime cancelInitiatedAt

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

\Datetime createdAt

RFC 3339 datetime string representing the time at which the Message Batch was created.



?\Datetime endedAt

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

\Datetime expiresAt

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

ProcessingStatus processingStatus

Processing status of the Message Batch.



[MessageBatchRequestCounts](api/beta/messages/batches.md) requestCounts

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.



?string resultsURL

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.



"message\_batch" type

Object type.

For Message Batches, this is always `"message_batch"`.



[MessageBatchCanceledResult](api/beta/messages/batches.md)

"canceled" type



[MessageBatchErroredResult](api/beta/messages/batches.md)

[BetaErrorResponse](api/beta.md) error

"errored" type



[MessageBatchExpiredResult](api/beta/messages/batches.md)

"expired" type



[MessageBatchIndividualResponse](api/beta/messages/batches.md)



string customID

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.



[MessageBatchResult](api/beta/messages/batches.md) result

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.



[MessageBatchRequestCounts](api/beta/messages/batches.md)



int canceled

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.



int errored

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.



int expired

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

int processing

Number of requests in the Message Batch that are processing.



int succeeded

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.



[MessageBatchResult](api/beta/messages/batches.md)

One of the following:



[MessageBatchSucceededResult](api/beta/messages/batches.md)

[BetaMessage](api/beta/messages.md) message

"succeeded" type



[MessageBatchErroredResult](api/beta/messages/batches.md)

[BetaErrorResponse](api/beta.md) error

"errored" type



[MessageBatchCanceledResult](api/beta/messages/batches.md)

"canceled" type



[MessageBatchExpiredResult](api/beta/messages/batches.md)

"expired" type



[MessageBatchSucceededResult](api/beta/messages/batches.md)

[BetaMessage](api/beta/messages.md) message

"succeeded" type

---

*Copyright © Anthropic. All rights reserved.*
