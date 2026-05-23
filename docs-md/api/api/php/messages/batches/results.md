# Retrieve Message Batch results

Copy page

PHP

# Retrieve Message Batch results

$client->messages->batches->results(string messageBatchID): [MessageBatchIndividualResponse](api/messages.md)

GET/v1/messages/batches/{message\_batch\_id}/results

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

##### ParametersExpand Collapse

messageBatchID: string

ID of the Message Batch.

##### ReturnsExpand Collapse

[MessageBatchIndividualResponse](api/messages.md)

string customID

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

[MessageBatchResult](api/messages.md) result

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Retrieve Message Batch results

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$messageBatchIndividualResponse = $client->messages->batches->resultsStream(
  'message_batch_id'
);

var_dump($messageBatchIndividualResponse);
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
