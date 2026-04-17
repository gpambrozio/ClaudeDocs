# Get started with Claude

Copy page

## Prerequisites

- An Anthropic [Console account](/)
- An [API key](/settings/keys)

## Call the API

cURL

cURL

CLI

CLI

Python

Python

TypeScript

TypeScript

Java

Java

1. 1

   Set your API key

   Get your API key from the [Claude Console](/settings/keys) and set it as an environment variable:

   ```shiki
   export ANTHROPIC_API_KEY='your-api-key-here'
   ```

   To persist the key across shell sessions, add the line to your shell profile (such as `~/.zshrc` or `~/.bashrc`).
2. 2

   Install the SDK

   Install the Anthropic Python SDK:

   ```shiki
   pip install anthropic
   ```
3. 3

   Create your code

   Save this as `quickstart.py`:

   ```shiki
   import anthropic

   client = anthropic.Anthropic()

   message = client.messages.create(
       model="claude-opus-4-7",
       max_tokens=1000,
       messages=[
           {
               "role": "user",
               "content": "What should I search for to find the latest developments in renewable energy?",
           }
       ],
   )
   print(message.content)
   ```
4. 4

   Run your code

   ```shiki
   python quickstart.py
   ```

   **Example output:**

   Output

   ```inline-block
   [
       TextBlock(
           text='Here are some effective search strategies for finding the latest renewable energy developments:\n\n**Search Terms to Use:**\n- "renewable energy news 2024"\n- "clean energy breakthroughs"\n- "solar/wind/battery technology advances"\n- "energy storage innovations"\n- "green hydrogen developments"\n- "renewable energy policy updates"\n\n**Reliable Sources to Check:**\n- **News & Analysis:** Reuters Energy, Bloomberg New Energy Finance, Greentech Media, Energy Storage News\n- **Industry Publications:** Renewable Energy World, PV Magazine, Wind Power Engineering\n- **Research Organizations:** International Energy Agency (IEA), National Renewable Energy Laboratory (NREL)\n- **Government Sources:** Department of Energy websites, EPA clean energy updates\n\n**Specific Topics to Explore:**\n- Perovskite and next-gen solar cells\n- Offshore wind expansion\n- Grid-scale battery storage\n- Green hydrogen production\n- Carbon capture technologies\n- Smart grid innovations\n- Energy policy changes and incentives...',
           type="text",
       )
   ]
   ```

## Next steps

You made your first API call. Next, learn the Messages API patterns you'll use in every Claude integration.

[Working with the Messages API

Learn multi-turn conversations, system prompts, stop reasons, and other core patterns.](build-with-claude/working-with-messages.md)

Once you're comfortable with the basics, explore further:

[Models overview

Compare Claude models by capability and cost.](about-claude/models/overview.md)[Features overview

Browse all Claude capabilities: tools, context management, structured outputs, and more.](build-with-claude/overview.md)[Client SDKs

Reference documentation for Python, TypeScript, Java, and other client libraries.](api/client-sdks.md)

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
