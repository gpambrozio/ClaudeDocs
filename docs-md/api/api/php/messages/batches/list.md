# List Message Batches

Copy page



PHP

# List Message Batches

$client->messages->batches->list(?string afterID, ?string beforeID, ?int limit): Page<[MessageBatch](api/messages/batches.md)>

GET/v1/messages/batches

List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](build-with-claude/batch-processing.md)

##### ParametersExpand Collapse

afterID?:optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

beforeID?:optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.



limit?:optional int

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

##### ReturnsExpand Collapse



[MessageBatch](api/messages/batches.md)

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

[MessageBatchRequestCounts](api/messages/batches.md) requestCounts

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

List Message Batches

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->messages->batches->list(
  afterID: 'after_id', beforeID: 'before_id', limit: 1
);

var_dump($page);
```

Response 200



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



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

---

*Copyright © Anthropic. All rights reserved.*
