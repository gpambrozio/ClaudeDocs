# Home

---
title: Documentation
url: https://platform.claude.com/docs/en/home
description: Claude API Documentation
---

  
    Quickstart

    Get API key

    API reference

    ```python Python
    import anthropic

    client = anthropic.Anthropic()

    message = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Hello, Claude",
            }
        ],
    )
    for block in message.content:
        if block.type == "text":
            print(block.text)
    ```

    ```typescript TypeScript
    import Anthropic from "@anthropic-ai/sdk";

    const client = new Anthropic();

    const msg = await client.messages.create({
      model: "claude-opus-5-5",
      max_tokens: 1024,
      messages: [
        {
          role: "user",
          content: "Hello, Claude"
        }
      ]
    });
    for (const block of msg.content) {
      if (block.type === "text") {
        console.log(block.text);
      }
    }
    ```

    ```go Go
    import "github.com/anthropics/anthropic-sdk-go"

    client := anthropic.NewClient()
    msg, _ := client.Messages.New(
      context.TODO(),
      anthropic.MessageNewParams{
        Model:     anthropic.ModelClaudeOpus5_5,
        MaxTokens: 1024,
        Messages: []anthropic.MessageParam{
          anthropic.NewUserMessage(
            anthropic.NewTextBlock("Hello, Claude"),
          ),
        },
      },
    )
    for _, block := range msg.Content {
      if textBlock, ok := block.AsAny().(anthropic.TextBlock); ok {
        fmt.Println(textBlock.Text)
      }
    }
    ```

    ```java Java
    import com.anthropic.client.okhttp.AnthropicOkHttpClient;

    var client = AnthropicOkHttpClient
      .fromEnv();

    var msg = client.messages().create(
      MessageCreateParams.builder()
        .model("claude-opus-5-5")
        .maxTokens(1024)
        .addUserMessage("Hello, Claude")
        .build()
    );
    for (var block : msg.content()) {
      block.text().ifPresent(
        textBlock -> System.out.println(textBlock.text()));
    }
    ```

    ```ruby Ruby
    require "anthropic"

    client = Anthropic::Client.new

    msg = client.messages.create(
      model: "claude-opus-5-5",
      max_tokens: 1024,
      messages: [{
        role: "user",
        content: "Hello, Claude"
      }]
    )
    msg.content.each do |block|
      puts block.text if block.type == :text
    end
    ```

    ```php PHP
    use Anthropic\Client;

    $client = new Client();

    $message = $client->messages->create(
      model: "claude-opus-5-5",
      maxTokens: 1024,
      messages: [['role' => 'user',
        'content' => 'Hello, Claude']],
    );
    foreach ($message->content as $block) {
      if ($block->type === 'text') {
        echo $block->text, PHP_EOL;
      }
    }
    ```

    ```csharp C#
    using Anthropic;

    var client = new AnthropicClient();

    var msg = await client.Messages
      .Create(new() {
        Model = "claude-opus-5-5",
        MaxTokens = 1024,
        Messages = [new() {
          Role = Role.User,
          Content = "Hello, Claude"
        }]
      });
    foreach (var block in msg.Content)
    {
      if (block.TryPickText(out var textBlock))
      {
        Console.WriteLine(textBlock.Text);
      }
    }
    ```

    ```bash cURL
    curl https://api.anthropic.com/v1/messages \
      -H "content-type: application/json" \
      -H "x-api-key: $ANTHROPIC_API_KEY" \
      -H "anthropic-version: 2023-06-01" \
      -d '{
        "model": "claude-opus-5-5",
        "max_tokens": 1024,
        "messages": [{
          "role": "user",
          "content": "Hello, Claude"
        }]
      }'
    ```

    ```bash CLI
    ant messages create \
      --model claude-opus-5-5 \
      --max-tokens 1024 \
      --message '{
        role: user,
        content: "Hello, Claude"
      }'
    ```
  

  Quickstart

  API reference

  Client SDKs

  Quickstart

  API reference

  Define your agent

  Amazon Bedrock

  Google Cloud

  Microsoft Foundry

  Quickstart

  Get API key

  Choose a model

  Install an SDK

  Try the API in playground

  Messages API

  Thinking

  Vision

  Tool use

  Web search

  Code execution

  Structured outputs

  Prompt caching

  Streaming

  Prompting best practices

  Run evals

  Batch testing

  Safety and guardrails

  Rate limits and errors

  Cost optimization

  Workspaces and admin

  API key management

  Usage monitoring

  Model migration

  Quickstart

  Get API key

  Build in Console

  Agent setup

  Tools

  Tool permissions

  Streaming and events

  Sessions API reference

  Workspaces and admin

  API key management

  Usage monitoring

  * [Claude Fable 5.1](models/fable-5-1/overview.md) (`claude-fable-5-1`) — New — *For demanding reasoning and long-horizon agentic work* — Most capable · Research · Multi-day tasks
  * [Claude Opus 5.5](models/opus-5-5/overview.md) (`claude-opus-5-5`) — New — *For long-running agentic coding and knowledge work* — Complex projects · Agents · Coding
  * [Claude Sonnet 5.5](models/sonnet-5-5/overview.md) (`claude-sonnet-5-5`) — New — *The best combination of speed and intelligence* — Everyday tasks · Writing · Cost-efficient
  * [Claude Haiku 5.5](models/haiku-5-5/overview.md) (`claude-haiku-5-5`) — New — *For high-volume, latency-sensitive tasks such as classification, extraction, and routing* — Fastest · Lowest cost · High volume

  **Courses**

  Interactive courses to master Claude.

  **Cookbook**

  Code samples and patterns.

  **Quickstarts**

  Deployable starter apps.

  **What's new**

  Latest features and updates.

  **Claude Code**

  An agentic coding assistant in your terminal.

---

*Copyright © Anthropic. All rights reserved.*
