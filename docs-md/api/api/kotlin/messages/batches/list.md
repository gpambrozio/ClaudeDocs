# List Message Batches

Copy page

Kotlin

# List Message Batches

messages().batches().list(BatchListParamsparams = BatchListParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : BatchListPage

get/v1/messages/batches

List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

##### ParametersExpand Collapse

params: BatchListParams

afterId: Optional<String>

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

beforeId: Optional<String>

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

limit: Optional<Long>

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

maximum1000

minimum1

##### ReturnsExpand Collapse

class MessageBatch:

id: String

Unique object identifier.

The format and length of IDs may change over time.

archivedAt: Optional<LocalDateTime>

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

formatdate-time

cancelInitiatedAt: Optional<LocalDateTime>

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

formatdate-time

createdAt: LocalDateTime

RFC 3339 datetime string representing the time at which the Message Batch was created.

formatdate-time

endedAt: Optional<LocalDateTime>

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expiresAt: LocalDateTime

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

formatdate-time

processingStatus: ProcessingStatus

Processing status of the Message Batch.

Accepts one of the following:

IN\_PROGRESS("in\_progress")

CANCELING("canceling")

ENDED("ended")

requestCounts: [MessageBatchRequestCounts](api/messages.md)

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

canceled: Long

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: Long

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: Long

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: Long

Number of requests in the Message Batch that are processing.

succeeded: Long

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

resultsUrl: Optional<String>

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

type: JsonValue; "message\_batch"constant"message\_batch"constant

Object type.

For Message Batches, this is always `"message_batch"`.

Accepts one of the following:

MESSAGE\_BATCH("message\_batch")

List Message Batches

Kotlin

```shiki
package com.anthropic.example

import com.anthropic.client.AnthropicClient
import com.anthropic.client.okhttp.AnthropicOkHttpClient
import com.anthropic.models.messages.batches.BatchListPage
import com.anthropic.models.messages.batches.BatchListParams

fun main() {
    val client: AnthropicClient = AnthropicOkHttpClient.fromEnv()

    val page: BatchListPage = client.messages().batches().list()
}
```

Response 200

```shiki
{
  "data": [
    {
      "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
      "archived_at": "2024-08-20T18:37:24.100435Z",
      "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
      "created_at": "2024-08-20T18:37:24.100435Z",
      "ended_at": "2024-08-20T18:37:24.100435Z",
      "expires_at": "2024-08-20T18:37:24.100435Z",
      "processing_status": "in_progress",
      "request_counts": {
        "canceled": 10,
        "errored": 30,
        "expired": 10,
        "processing": 100,
        "succeeded": 50
      },
      "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
      "type": "message_batch"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

##### Returns Examples

Response 200

```shiki
{
  "data": [
    {
      "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
      "archived_at": "2024-08-20T18:37:24.100435Z",
      "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
      "created_at": "2024-08-20T18:37:24.100435Z",
      "ended_at": "2024-08-20T18:37:24.100435Z",
      "expires_at": "2024-08-20T18:37:24.100435Z",
      "processing_status": "in_progress",
      "request_counts": {
        "canceled": 10,
        "errored": 30,
        "expired": 10,
        "processing": 100,
        "succeeded": 50
      },
      "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
      "type": "message_batch"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```