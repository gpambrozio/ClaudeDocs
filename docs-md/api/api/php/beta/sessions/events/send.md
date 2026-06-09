# Send Events

Copy page

SDK language

PHP

# Send Events

$client->beta->sessions->events->send(string sessionID, list<[ManagedAgentsEventParams](api/beta.md)> events, ?list<AnthropicBeta> betas): [ManagedAgentsSendSessionEvents](api/beta.md)

POST/v1/sessions/{session\_id}/events

Send Events

##### ParametersExpand Collapse

sessionID: string

events: list<[ManagedAgentsEventParams](api/beta.md)>

Events to send to the `session`.

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

[ManagedAgentsSendSessionEvents](api/beta.md)

?list<Data> data

Sent events

Send Events

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsSendSessionEvents = $client->beta->sessions->events->send(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  events: [
    [
      'content' => [['text' => 'Where is my order #1234?', 'type' => 'text']],
      'type' => 'user.message',
    ],
  ],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsSendSessionEvents);
```

Response 200



```shiki
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ]
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ]
}
```

---

*Copyright © Anthropic. All rights reserved.*
