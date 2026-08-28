# Retrieve Message Batch results

Copy page



cURL

# Retrieve Message Batch results

GET/v1/messages/batches/{message\_batch\_id}/results

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](build-with-claude/batch-processing.md)

##### Path parameters

message\_batch\_id: string

ID of the Message Batch.

##### Returns

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



### Retrieve Message Batch results

cURL



```shiki
curl https://api.anthropic.com/v1/messages/batches/$MESSAGE_BATCH_ID/results \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

---

*Copyright © Anthropic. All rights reserved.*
