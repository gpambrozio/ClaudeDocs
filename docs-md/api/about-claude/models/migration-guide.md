# Migration guide

Copy page





This guide covers migrating [Messages API](build-with-claude/working-with-messages.md) code. If you use [Claude Managed Agents](managed-agents/overview.md), no changes beyond updating the model name are required.



**Automate your migration with the Claude API skill.** In Claude Code, run `/claude-api migrate` to invoke the bundled [Claude API skill](agents-and-tools/agent-skills/claude-api-skill.md). It works for any target model on this page:

```shiki
/claude-api migrate this project to claude-opus-4-8
```



The skill applies the model ID swap and, as needed, breaking parameter changes, prefill replacement, and effort calibration for your target model across your code base, then produces a checklist of items to verify manually. It asks you to confirm the migration scope (entire working directory, a subdirectory, or a specific file list) before editing any files. The skill also detects Amazon Bedrock, Claude Platform on AWS, Google Cloud, and Microsoft Foundry clients and adjusts model ID formats and feature changes for each platform.

##  Migrating to Claude Mythos 5

[Claude Mythos 5](https://anthropic.com/glasswing) is the access-gated model offered in limited availability to approved customers in Project Glasswing. It shares the same specs and pricing as [Claude Fable 5](about-claude/models/introducing-claude-fable-5-and-claude-mythos-5.md): a [1M token context window](build-with-claude/context-windows.md) by default, and up to 128k output tokens per request.

The baseline settings for `claude-mythos-5`:

- **Thinking:** [Adaptive thinking](build-with-claude/thinking-steering-and-cost.md) is always on. The model determines when and how much to think on each request, and no `thinking` configuration is required. Both `thinking: {type: "disabled"}` and manual extended thinking (`thinking: {type: "enabled", budget_tokens: N}`) return a 400 error.
- **Prefill:** Prefilling the assistant message returns a 400 error. Use system prompt instructions instead.
- **Data retention:** Claude Mythos 5 requires 30-day data retention and is not available under zero data retention (ZDR) arrangements; it is designated a Covered Model. See [Model-specific data retention requirements](manage-claude/api-and-data-retention.md).

###  Migrating to Claude Mythos 5 from Claude Mythos Preview

[Claude Mythos 5](https://anthropic.com/glasswing) is the access-gated successor to [Claude Mythos Preview](https://anthropic.com/glasswing), the invitation-only research preview. For a generally available model with the same capabilities, see [Claude Fable 5](about-claude/models/introducing-claude-fable-5-and-claude-mythos-5.md).

Migration is mostly drop-in. Claude Mythos 5 uses the same [Messages API](build-with-claude/working-with-messages.md) and the same [tool use](agents-and-tools/tool-use/overview.md) patterns as Claude Mythos Preview, and token counts are roughly unchanged because both models use the same tokenizer. The key changes to check are the features that are no longer available (listed in the next section) and thinking output.

For the Claude Mythos Preview retirement timeline, see [Model deprecations](about-claude/model-deprecations.md).

####  Update your model name

```shiki
model = "claude-mythos-preview"  # Before
model = "claude-mythos-5"  # After
```



####  Features not available on Claude Mythos 5

1. **Extended thinking and thinking token budgets:** Manual extended thinking (`thinking: {type: "enabled", budget_tokens: N}`) is not supported on `claude-mythos-5` and returns a 400 error. [Adaptive thinking](build-with-claude/thinking-steering-and-cost.md) is always on: the model determines when and how much to think on each request, and no `thinking` configuration is required. `thinking: {type: "disabled"}` returns an error. `budget_tokens` has no direct replacement: thinking is adaptive, and the [effort parameter](build-with-claude/effort.md) is a separate output-level control, not a thinking budget.

   Before (Claude Mythos Preview):

   cURLCLIPythonTypeScriptC#GoJavaPHPRuby

   

   ```shiki
   client.messages.create(
       model="claude-mythos-preview",
       max_tokens=16000,
       thinking={"type": "enabled", "budget_tokens": 10000},
       messages=[{"role": "user", "content": "..."}],
   )
   ```

   After (Claude Mythos 5):

   cURLCLIPythonTypeScriptC#GoJavaPHPRuby

   

   ```shiki
   client.messages.create(
       model="claude-mythos-5",
       max_tokens=16000,
       messages=[{"role": "user", "content": "..."}],
   )
   ```
2. **Assistant prefill:** Prefilling the assistant message is not supported on `claude-mythos-5` and returns a 400 error, the same as on Claude Mythos Preview. Use system prompt instructions instead.
3. **Thinking output:** On `claude-mythos-5`, the raw chain of thought is never returned, but thinking blocks still carry readable summarized text when `thinking.display` is set to `summarized`. Pass thinking blocks back unchanged when continuing a conversation on the same model. See [Thinking output on Claude Fable 5 and Claude Mythos 5](build-with-claude/thinking.md).

####  Token counting and billing

`claude-mythos-5` uses the same tokenizer as `claude-mythos-preview` (the tokenizer introduced with Claude Opus 4.7). Token counts are roughly unchanged when migrating from `claude-mythos-preview`. Compared with models before Claude Opus 4.7, the same content can tokenize to roughly 30% more tokens, varying by content and workload shape.

[`/v1/messages/count_tokens`](build-with-claude/token-counting.md) returns roughly unchanged values for `claude-mythos-5` compared with `claude-mythos-preview`. Re-baseline cost and latency on your own workloads.

####  Migration checklist

- Update the model name from `claude-mythos-preview` to `claude-mythos-5`.
- Remove manual extended thinking configuration (`thinking: {type: "enabled", budget_tokens: N}`). Adaptive thinking is always on, and no `thinking` field is required.
- Remove any `thinking: {type: "disabled"}` configuration. Disabling thinking returns an error on `claude-mythos-5`.
- Remove `budget_tokens`. It has no direct replacement: thinking is adaptive, and the `effort` parameter is a separate output-level control, not a thinking budget.
- Verify any code that parses the `thinking` field treats it as display text only and passes thinking blocks back unchanged when continuing on the same model. `thinking.display` defaults to `"omitted"` on `claude-mythos-5`, the same as on Claude Mythos Preview; set `display: "summarized"` to receive readable summaries. See [Thinking output on Claude Fable 5 and Claude Mythos 5](build-with-claude/thinking.md).
- If you replay conversation history on another model, strip `thinking` and `redacted_thinking` blocks from prior assistant turns first. Thinking blocks from `claude-mythos-5` are tied to the model that produced them, and models other than Claude Fable 5 and Claude Mythos 5 silently ignore them. Stripping keeps cross-model requests minimal and uniform.
- Re-baseline token counts and costs on your own workloads. Token counts are roughly unchanged when migrating from `claude-mythos-preview`.

##  Migrating to Claude Fable 5

[Claude Fable 5](about-claude/models/introducing-claude-fable-5-and-claude-mythos-5.md) is Anthropic's most capable widely released model, generally available on the Claude API, [Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md), [Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md), [Google Cloud](build-with-claude/claude-on-vertex-ai.md), and [Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md).

Migration is mostly drop-in. Claude Fable 5 uses the same [Messages API](build-with-claude/working-with-messages.md) and the same [tool use](agents-and-tools/tool-use/overview.md) patterns as Claude Opus 4.8. It supports the same [1M token context window](build-with-claude/context-windows.md) by default and the same [128k max output tokens](about-claude/models/overview.md). Token counts are roughly unchanged because both models use the same tokenizer.

The key changes to check are always-on [adaptive thinking](build-with-claude/thinking-steering-and-cost.md), thinking output, safety classifier refusals, and pricing. [Before you migrate](#before-you-migrate) covers pricing and data retention; [What changed](#what-changed) covers the rest.

###  Before you migrate

Claude Fable 5 is priced at $10 USD per million input tokens and $50 USD per million output tokens, compared with $5 USD and $25 USD for Claude Opus 4.8. See [Claude pricing](about-claude/pricing.md) for details.

Claude Fable 5 requires 30-day data retention and is not available under zero data retention (ZDR) arrangements; it is designated a Covered Model. On the Claude API, a request from an organization whose data retention configuration does not meet this requirement returns a 400 `invalid_request_error`. Organizations with a ZDR arrangement should contact their Anthropic account team to discuss data retention configuration; Claude Opus 4.8 remains available under ZDR. Alternatively, you can configure data retention per workspace. The 30-day data retention requirement applies on every platform where Claude Fable 5 is offered; see [Model-specific data retention requirements](manage-claude/api-and-data-retention.md) for per-platform details.



If your code is on Claude Opus 4.7 or earlier, first apply the relevant [Migrating to Claude Opus 4.8](#migrating-to-claude-opus-4-8) sub-section for your current model. Those sections cover breaking changes (sampling parameters rejected, manual extended thinking rejected, prefill removed, new tokenizer) that this section does not repeat.

###  Migrating to Claude Fable 5 from Claude Opus 4.8

####  Update your model name

```shiki
model = "claude-opus-4-8"  # Before
model = "claude-fable-5"  # After
```



####  What changed

The items in this section describe the API and behavior differences worth checking after you swap the model ID.

1. **Adaptive thinking is always on:** [Adaptive thinking](build-with-claude/thinking-steering-and-cost.md) is the only thinking mode on `claude-fable-5`. The model determines when and how much to think on each request, and no `thinking` configuration is required. `thinking: {type: "disabled"}` returns an error. Use the [effort parameter](build-with-claude/effort.md) to control thinking depth.

   The behavior change to check: on Claude Opus 4.8, requests without a `thinking` field run without thinking; on `claude-fable-5`, those same requests run with adaptive thinking. `max_tokens` remains a hard limit on total output, thinking plus response text, so revisit it for workloads that ran without thinking on Claude Opus 4.8. See [Cost control](build-with-claude/thinking-steering-and-cost.md).

   Before (Claude Opus 4.8):

   cURLCLIPythonTypeScriptC#GoJavaPHPRuby

   

   ```shiki
   client.messages.create(
       model="claude-opus-4-8",
       max_tokens=16000,
       thinking={"type": "adaptive"},
       output_config={"effort": "high"},
       messages=[{"role": "user", "content": "..."}],
   )
   ```

   After (Claude Fable 5):

   cURLCLIPythonTypeScriptC#GoJavaPHPRuby

   

   ```shiki
   client.messages.create(
       model="claude-fable-5",
       max_tokens=16000,
       output_config={"effort": "high"},
       messages=[{"role": "user", "content": "..."}],
   )
   ```
2. **Extended thinking and thinking budgets (unchanged):** Manual extended thinking (`thinking: {type: "enabled", budget_tokens: N}`) is not supported on `claude-fable-5` and returns a 400 error, the same as on Claude Opus 4.8. `budget_tokens` has no direct replacement: thinking is adaptive, and the [effort parameter](build-with-claude/effort.md) is a separate output-level control, not a thinking budget.
3. **Assistant prefill (unchanged):** Prefilling the assistant message is not supported on `claude-fable-5` and returns a 400 error, the same as on Claude Opus 4.8. Use system prompt instructions instead.
4. **Thinking output:** On `claude-fable-5`, the raw chain of thought is never returned, but thinking blocks still carry readable summarized text when `thinking.display` is set to `summarized`. Pass thinking blocks back unchanged when continuing a conversation on the same model. See [Thinking output on Claude Fable 5 and Claude Mythos 5](build-with-claude/thinking.md).
5. **Safety classifiers and the `refusal` stop reason:** `claude-fable-5` runs safety classifiers on requests and during response generation. When a classifier declines a request, the Messages API returns `stop_reason: "refusal"` as a successful HTTP 200 response, not an error. The `stop_details.category` field reports which classifier fired, with categories such as `"cyber"`, `"bio"`, and `"reasoning_extraction"`, or `null` when the refusal maps to no named category. See the [refusal category table](build-with-claude/refusals-and-fallback.md) for the full set.

   You are not billed for the input tokens of a request refused before any output is generated. When a classifier fires mid-stream, the input and already-streamed output are billed; discard the partial output.

   To re-run refused requests on another model automatically, pass the opt-in `fallbacks` parameter, which is in beta on the Claude API and Claude Platform on AWS. The parameter is not available on the Message Batches API or on Amazon Bedrock, Google Cloud, and Microsoft Foundry; on those three platforms, run the retry client-side or use the SDK refusal-fallback middleware. See [Refusals and fallback](build-with-claude/refusals-and-fallback.md).
6. **Start at `high` effort:** The [effort parameter](build-with-claude/effort.md) default remains `high`. On Claude Opus 4.8, the recommendation for coding and high-autonomy work is to set `xhigh` explicitly. On `claude-fable-5`, use `high` as the default for most tasks and reserve `xhigh` for the most capability-sensitive workloads. Lower effort settings on `claude-fable-5` still perform well and often exceed `xhigh` performance on prior models. Reduce effort if a task completes but takes longer than necessary. See [Prompting Claude Fable 5](build-with-claude/prompt-engineering/prompting-claude-fable-5.md).
7. **Lower prompt caching minimum:** The minimum cacheable prompt length on `claude-fable-5` is 512 tokens, lower than the 1,024 tokens on Claude Opus 4.8. Prompts that were too short to cache on Claude Opus 4.8 can now create cache entries, with no code changes required. On Amazon Bedrock, the minimum for `claude-fable-5` is 1,024 tokens. See [Prompt caching](build-with-claude/prompt-caching.md) for per-model minimums.

####  Migration checklist

- If your organization has a zero data retention (ZDR) arrangement, confirm eligibility before migrating. `claude-fable-5` requires 30-day data retention and, on the Claude API, returns a 400 `invalid_request_error` otherwise. See [Model-specific data retention requirements](manage-claude/api-and-data-retention.md).
- Update the model name from `claude-opus-4-8` to `claude-fable-5`.
- Remove any `thinking: {type: "disabled"}` configuration. Disabling thinking returns an error on `claude-fable-5`, and requests without a `thinking` field run with adaptive thinking.
- If you removed manual extended thinking and assistant prefills during earlier migrations, no action is needed: both remain unsupported on `claude-fable-5`.
- Verify any code that parses the `thinking` field treats it as display text only and passes thinking blocks back unchanged when continuing on the same model. `thinking.display` defaults to `"omitted"` on `claude-fable-5`, the same as on Claude Opus 4.8; set `display: "summarized"` to receive readable summaries. See [Thinking output on Claude Fable 5 and Claude Mythos 5](build-with-claude/thinking.md).
- If you replay conversation history on another model, strip `thinking` and `redacted_thinking` blocks from prior assistant turns first. Thinking blocks from `claude-fable-5` are tied to the model that produced them, and models other than Claude Fable 5 and Claude Mythos 5 silently ignore them. Stripping keeps cross-model requests minimal and uniform. The exception is redeeming a [fallback credit](build-with-claude/fallback-credit.md), which requires the request body echoed under that feature's exact rules.
- Handle `stop_reason: "refusal"` and read the `stop_details.category` field. To re-run refused requests on another model automatically, consider the opt-in `fallbacks` parameter (beta). See [Refusals and fallback](build-with-claude/refusals-and-fallback.md).
- Re-evaluate your `effort` setting. Start at `high` for most tasks, including workloads that ran at `xhigh` on Claude Opus 4.8.
- Re-baseline cost and latency on your own workloads. Token counts are roughly unchanged when migrating from `claude-opus-4-8`; per-token pricing differs.

##  Migrating to Claude Opus 4.8

Claude Opus 4.8 is built for complex agentic coding and enterprise work. These are the baseline settings for `claude-opus-4-8`. The following sub-sections cover the specific changes to make from each earlier Opus model.

- **Pricing:** see [Claude pricing](about-claude/pricing.md).
- **Thinking:** [Adaptive thinking](build-with-claude/thinking-steering-and-cost.md) (`thinking: {type: "adaptive"}`) is the supported thinking mode and is off by default: requests with no `thinking` field run without thinking. Manual extended thinking (`thinking: {type: "enabled", budget_tokens: N}`) returns a 400 error.
- **Effort:** The [effort parameter](build-with-claude/effort.md) defaults to `high` across all surfaces. For coding and high-autonomy work, set `xhigh` explicitly.
- **Sampling parameters:** `temperature`, `top_p`, and `top_k` set to a non-default value return a 400 error. Omit them and use prompting to guide the model's behavior.
- **Prefill:** Prefilling the assistant message returns a 400 error. Use [structured outputs](build-with-claude/structured-outputs.md) or `output_config.format` instead.
- **Context window and output:** The full [1M token context window](build-with-claude/context-windows.md) is served by default with no beta header and no long-context premium, with [128k max output tokens](about-claude/models/overview.md).

Claude Opus 4.8 also supports [prompt caching](build-with-claude/prompt-caching.md), [batch processing](build-with-claude/batch-processing.md), the [Files API](build-with-claude/files.md), [PDF support](build-with-claude/pdf-support.md), [vision](build-with-claude/vision.md), the full set of server-side and client-side [tools](agents-and-tools/tool-use/overview.md), [mid-conversation system messages](about-claude/models/whats-new-claude-4-8.md), and [refusal stop details](about-claude/models/whats-new-claude-4-8.md).

###  Migrating to Claude Opus 4.8 from Claude Opus 4.7

Claude Opus 4.8 builds on Claude Opus 4.7.

Claude Opus 4.8 should have strong out-of-the-box performance on existing Claude Opus 4.7 prompts and evals. There are no breaking API changes for code already running on Claude Opus 4.7. It supports the same set of features as Claude Opus 4.7, including the [1M token context window](build-with-claude/context-windows.md), [128k max output tokens](about-claude/models/overview.md), [adaptive thinking](build-with-claude/thinking-steering-and-cost.md), [prompt caching](build-with-claude/prompt-caching.md), [batch processing](build-with-claude/batch-processing.md), the [Files API](build-with-claude/files.md), [PDF support](build-with-claude/pdf-support.md), [vision](build-with-claude/vision.md), and the full set of server-side and client-side [tools](agents-and-tools/tool-use/overview.md). It also adds [mid-conversation system messages](about-claude/models/whats-new-claude-4-8.md) and publicly documents [refusal stop details](about-claude/models/whats-new-claude-4-8.md).



If your code is on Claude Opus 4.6 or earlier, use [Migrating to Claude Opus 4.8 from Claude Opus 4.6](#migrating-from-claude-opus-46) or [Migrating to Claude Opus 4.8 from Claude Opus 4.5 or earlier](#migrating-from-claude-opus-45) instead. Those sections include breaking changes (sampling parameters rejected, manual extended thinking rejected, new tokenizer) that the upgrade from Claude Opus 4.7 alone does not cover.

####  Update your model name

```shiki
# Opus migration
model = "claude-opus-4-7"  # Before
model = "claude-opus-4-8"  # After
```



####  What changed

These are not breaking changes. Code that runs on Claude Opus 4.7 continues to work unchanged on Claude Opus 4.8. The following items describe behavior differences worth checking after you swap the model ID.

1. **Sampling parameters (unchanged):** Setting `temperature`, `top_p`, or `top_k` to a non-default value returns a 400 error on Claude Opus 4.8, the same as on Claude Opus 4.7. The SDK request types still define these fields for compatibility with earlier models, so code that sets them type-checks, but the API rejects the request server-side. If you removed these parameters when migrating to Opus 4.7, no further changes are needed.
2. **Effort default is `high`:** The [effort parameter](build-with-claude/effort.md) default on Claude Opus 4.8 is `high` across all surfaces, including Claude Code and the Messages API. If you already set effort explicitly, your setting is unchanged. For coding and high-autonomy work, set `xhigh` explicitly. Re-evaluate your effort setting against your latency and cost budget.
3. **1M context window is the default:** Claude Opus 4.8 serves the full 1M token [context window](build-with-claude/context-windows.md) by default with no beta header and no long-context premium. If your client passes a context-window beta header for compatibility with older models, you can remove it on Claude Opus 4.8.
4. **Mid-conversation system messages:** Claude Opus 4.8 accepts `role: "system"` messages immediately after a user turn in the `messages` array (subject to [placement rules](build-with-claude/mid-conversation-system-messages.md)). Use the top-level `system` field for instructions that apply from the start. Earlier models, including Claude Opus 4.7, reject `role: "system"` in `messages` with a 400 error. If you maintain code paths that rebuild the full message history to update instructions, you can simplify them and preserve [prompt cache](build-with-claude/prompt-caching.md) hits on earlier turns.
5. **Refusal stop details:** The `stop_details` object on refusal responses (available since Claude Opus 4.7) is now publicly documented. When the model declines a request, it identifies the category of refusal, in addition to the existing `refusal` stop reason. No beta header is required, and there is no opt-out. See [Handling stop reasons](build-with-claude/handling-stop-reasons.md).
6. **Lower prompt caching minimum:** The minimum cacheable prompt length on Claude Opus 4.8 is 1,024 tokens, lower than on Claude Opus 4.7. Prompts that were too short to cache on Claude Opus 4.7 can now create cache entries, with no code changes required. See [Prompt caching](build-with-claude/prompt-caching.md) for per-model minimums.
7. **Effort levels recalibrated:** The token allocation behind each effort level changes on Claude Opus 4.8 compared to Claude Opus 4.7: `medium` allows somewhat more thinking, `high` somewhat less, and `xhigh` substantially more. If you tuned an effort level against Claude Opus 4.7 cost or latency, re-baseline at the same level before adjusting it. See [Effort](build-with-claude/effort.md).

####  Migration checklist

- Update model name from `claude-opus-4-7` to `claude-opus-4-8` (or update aliases).
- If you removed sampling parameters during the Opus 4.7 migration, no action is needed. If you re-added them with a 400-retry path, remove that retry path.
- Re-evaluate your `effort` setting. The default is `high` across all surfaces; for coding and high-autonomy work, set `xhigh` explicitly.
- Remove any context-window beta header. The 1M context window is the default on the Claude API, Amazon Bedrock, Google Cloud, and Microsoft Foundry.
- If you rebuild conversation history to update instructions, consider switching to a mid-conversation system message to preserve prompt cache hits.
- Verify your stop-reason handling reads `stop_details` on refusals (available since Claude Opus 4.7; now publicly documented).
- Re-baseline cost and latency at your chosen effort level.

###  Migrating to Claude Opus 4.8 from Claude Opus 4.6

Claude Opus 4.8 should have strong out-of-the-box performance on existing Claude Opus 4.6 prompts and evals at the same pricing, but there are a handful of behavioral and API changes worth knowing about as you migrate. These changes took effect in Claude Opus 4.7, and there are no additional breaking API changes between Claude Opus 4.7 and Claude Opus 4.8. It supports the same set of features as Claude Opus 4.6, including:

- [1M token context window](build-with-claude/context-windows.md) at standard API pricing with no long-context premium
- [128k max output tokens](about-claude/models/overview.md)
- [Adaptive thinking](build-with-claude/thinking-steering-and-cost.md)
- [Prompt caching](build-with-claude/prompt-caching.md)
- [Batch processing](build-with-claude/batch-processing.md)
- [Files API](build-with-claude/files.md)
- [PDF support](build-with-claude/pdf-support.md)
- [Vision](build-with-claude/vision.md)
- The full set of server-side and client-side [tools](agents-and-tools/tool-use/overview.md) ([bash](agents-and-tools/tool-use/bash-tool.md), [code execution](agents-and-tools/tool-use/code-execution-tool.md), [computer use](agents-and-tools/tool-use/computer-use-tool.md), [text editor](agents-and-tools/tool-use/text-editor-tool.md), [web search](agents-and-tools/tool-use/web-search-tool.md), [web fetch](agents-and-tools/tool-use/web-fetch-tool.md), [MCP connector](agents-and-tools/mcp-connector.md), [memory](agents-and-tools/tool-use/memory-tool.md))

####  Update your model name

```shiki
# Opus migration
model = "claude-opus-4-6"  # Before
model = "claude-opus-4-8"  # After
```



####  Breaking changes

1. **Extended thinking removed:** `thinking: {type: "enabled", budget_tokens: N}` is no longer supported on Claude Opus 4.7 or later models and returns a 400 error. Switch to [adaptive thinking](build-with-claude/thinking-steering-and-cost.md) (`thinking: {type: "adaptive"}`) and use the [effort parameter](build-with-claude/effort.md) to control thinking depth. Adaptive thinking is **off by default** on Claude Opus 4.7: requests with no `thinking` field run without thinking, matching Opus 4.6 behavior. Set `thinking: {type: "adaptive"}` explicitly to enable it.

   Before (Claude Opus 4.6):

   cURLCLIPythonTypeScriptC#GoJavaPHPRuby

   

   ```shiki
   client.messages.create(
       model="claude-opus-4-6",
       max_tokens=16000,
       thinking={"type": "enabled", "budget_tokens": 10000},
       messages=[{"role": "user", "content": "..."}],
   )
   ```

   After (Claude Opus 4.8):

   cURLCLIPythonTypeScriptC#GoJavaPHPRuby

   

   ```shiki
   client.messages.create(
       model="claude-opus-4-8",
       max_tokens=16000,
       thinking={"type": "adaptive"},
       output_config={"effort": "high"},  # or "max", "xhigh", "medium", "low"
       messages=[{"role": "user", "content": "..."}],
   )
   ```

   Adaptive thinking is steerable through prompting. For guidance on tuning when the model over- or under-thinks, see [Calibrating effort and thinking depth](build-with-claude/prompt-engineering/prompting-claude-opus-4-8.md).
2. **Sampling parameters removed:** Setting `temperature`, `top_p`, or `top_k` to any non-default value on Claude Opus 4.7 returns a 400 error. The safest migration path is to omit these parameters entirely from request payloads. Prompting is the recommended way to guide model behavior on Claude Opus 4.7. If you were using `temperature = 0` for determinism, note that it never guaranteed identical outputs on prior models.
3. **Thinking content omitted by default:** Thinking blocks still appear in the response stream on Claude Opus 4.7, but their `thinking` field is empty unless you explicitly opt in. This is a silent change from Claude Opus 4.6, where the default was to return summarized thinking text. To restore summarized thinking content on Claude Opus 4.7, set `thinking.display` to `"summarized"`:

   PythonTypeScriptC#GoJavaPHPRuby

   

   ```shiki
   thinking = {
       "type": "adaptive",
       "display": "summarized",
   }
   ```

   The default is `"omitted"` on Claude Opus 4.7. If your product streams reasoning to users, the new default appears as a long pause before output begins; set `display: "summarized"` to restore visible progress during thinking. See [Controlling thinking display](build-with-claude/thinking.md) for details.
4. **Updated token counting:** Claude Opus 4.7 uses a new tokenizer, contributing to its improved performance on a wide range of tasks. The new tokenizer may use roughly 1x to 1.35x as many tokens when processing text compared to previous models (up to ~35% more, varying by content).

   [`/v1/messages/count_tokens`](build-with-claude/token-counting.md) returns a different number of tokens for Claude Opus 4.7 than it did for Claude Opus 4.6. Token efficiency can vary by workload shape.

   Prompting interventions, `task_budget`, and `effort` can help control costs and ensure appropriate token usage. These controls may trade off model intelligence. Update your `max_tokens` parameters to give additional headroom, including compaction triggers. Claude Opus 4.7 provides a 1M context window at standard API pricing with no long-context premium.
5. **Prefill removal (carried over from Opus 4.6):** Prefilling assistant messages returns a 400 error on Claude Opus 4.7. Use [structured outputs](build-with-claude/structured-outputs.md), system prompt instructions, or `output_config.format` instead.

####  Choosing an effort level

The [effort parameter](build-with-claude/effort.md) allows you to tune Claude's intelligence versus token spend, trading off capability for faster speed and lower costs. Start with the `xhigh` effort level for coding and agentic use cases, and use a minimum of `high` effort for most intelligence-sensitive use cases. Experiment with other effort levels to further tune token usage and intelligence:

- **`max`:** Max effort can deliver performance gains in some use cases, but may show diminishing returns from increased token usage. This setting can also sometimes be prone to overthinking. Test max effort for intelligence-demanding tasks.
- **`xhigh`:** Extra high effort is the best setting for most coding and agentic use cases.
- **`high`:** This setting balances token usage and intelligence. For most intelligence-sensitive use cases, use a minimum of `high` effort.
- **`medium`:** Good for cost-sensitive use cases that need to reduce token usage while trading off intelligence.
- **`low`:** Reserve for short, scoped tasks and latency-sensitive workloads that are not intelligence-sensitive.

Effort is more important for this model than for any prior Opus. Experiment with it actively when you upgrade.

####  Behavior changes

Claude Opus 4.7 has several behavioral differences from Claude Opus 4.6 that are not API breaking changes but may require prompt updates or scaffolding removal.

1. **Response length varies by use case:** Claude Opus 4.7 calibrates response length to how complex it judges the task to be, rather than defaulting to a fixed verbosity. This usually means shorter answers on simple lookups and much longer ones on open-ended analysis.

   If your product depends on a certain style or verbosity of output, you may need to tune your prompts. For example, to decrease verbosity, add: "Provide concise, focused responses. Skip non-essential context, and keep examples minimal." If you see specific kinds of over-explaining, add targeted instructions in your prompt to prevent them.

   Positive examples showing how Claude can communicate with the appropriate level of concision tend to be more effective than negative examples or instructions that tell the model what not to do.
2. **More literal instruction following:** Claude Opus 4.7 interprets prompts more literally and explicitly than Claude Opus 4.6, particularly at lower effort levels. It does not silently generalize an instruction from one item to another, and it does not infer requests you didn't make. The upside of this literalism is precision and less thrash. It generally performs better for API use cases with carefully tuned prompts, structured extraction, and pipelines where you want predictable behavior. A prompt and harness review may be especially helpful for migration to Claude Opus 4.8.
3. **More direct tone:** As with any new model, prose style on long-form writing may shift. Claude Opus 4.7 is more direct and opinionated, with less validation-forward phrasing and fewer emoji than Claude Opus 4.6's warmer style. If your product relies on a specific voice, re-evaluate style prompts against the new baseline.
4. **Built-in progress updates in agentic traces:** Claude Opus 4.7 provides more regular, higher-quality updates to the user throughout long agentic traces. If you've added scaffolding to force interim status messages ("After every 3 tool calls, summarize progress"), try removing it. If you find that the length or contents of Claude Opus 4.7's user-facing updates are not well-calibrated to your use case, explicitly describe what these updates should look like in the prompt and provide examples.
5. **Fewer subagents spawned by default:** Claude Opus 4.7 tends to spawn fewer subagents by default. However, this behavior is steerable through prompting; give Claude Opus 4.7 explicit guidance around when subagents are desirable.
6. **Stricter effort calibration:** Meaningfully changing from Claude Opus 4.6, Claude Opus 4.7 respects [effort levels](build-with-claude/effort.md) strictly, especially at the low end. At `low` and `medium`, the model scopes its work to what was asked rather than doing more than requested.

   This is good for latency and cost, but on moderately complex tasks running at `low` effort there is some risk of under-thinking. If you observe shallow reasoning on complex problems, raise effort to `high` or `xhigh` rather than prompting around it.

   If you need to keep effort at `low` for latency, add targeted guidance: "This task involves multistep reasoning. Think carefully through the problem before responding." See [Recommended effort levels for Claude Opus 4.7](build-with-claude/effort.md).
7. **Fewer tool calls by default:** Claude Opus 4.7 has a tendency to use tools less often than Claude Opus 4.6 and to use reasoning more. This produces better results in most cases.

   To increase tool usage, raise the effort setting. `high` or `xhigh` effort settings show substantially more tool usage in agentic search and coding. You can also adjust your prompt to explicitly instruct the model about when and how to properly use its tools.
8. **Real-time cybersecurity safeguards:** Newly added in Claude Opus 4.7, requests that involve prohibited or high-risk topics may lead to refusals. For legitimate security work such as penetration testing, vulnerability research, or red-teaming, apply to the [Cyber Verification Program](https://claude.com/form/cyber-use-case) to request reduced restrictions. See [Safeguards, warnings, and appeals](https://support.claude.com/en/articles/8241253-safeguards-warnings-and-appeals) for background.
9. **High-resolution image support:** Claude Opus 4.7 is the first Claude model with high-resolution image support. Maximum image resolution is 2,576 pixels on the long edge, up from 1,568 pixels on prior models. This unlocks gains on vision-heavy workloads and is particularly valuable for computer use, screenshot understanding, and document analysis.

   High-resolution support is automatic and requires no beta header or client-side opt-in. Two things to plan for:

   - Full-resolution images can use up to approximately 3x more image tokens than on prior models (up to 4,784 tokens per image, compared to the previous cap of roughly 1,600 tokens per image). Re-budget `max_tokens` and cost expectations for image-heavy workloads, or downsample before sending if you do not need the additional fidelity.
   - Pointing and bounding-box coordinates returned by the model are 1:1 with actual image pixels on Claude Opus 4.7, so no scale-factor conversion is required.

   See [High-resolution image support on Claude Opus 4.7](build-with-claude/vision.md) for details.

####  Recommended changes

These are not required but will improve your experience:

1. **Re-evaluate `max_tokens`:** Because the same text produces a higher token count on Claude Opus 4.7 and later models, update your `max_tokens` parameters to give additional headroom, including compaction triggers. Prompting interventions, [`task_budget`](build-with-claude/task-budgets.md), and [`effort`](build-with-claude/effort.md) can help control costs and ensure appropriate token usage.
2. **Audit token-count expectations:** Any code path that estimates tokens client-side or assumes a fixed token-to-character ratio should be re-tested against Claude Opus 4.8. Use the [Token counting endpoint](build-with-claude/token-counting.md) to verify.
3. **Adopt [task budgets](build-with-claude/task-budgets.md) (beta):** Claude Opus 4.7 introduces task budgets. These budgets let you inform Claude how many tokens it has for a full agentic loop, including thinking, tool calls, tool results, and final output. The model sees a running countdown and uses it to prioritize work and finish the task gracefully as the budget is consumed. To use, set the beta header `task-budgets-2026-03-13` and add the following to your output config:

   PythonTypeScriptC#GoJavaPHPRuby

   

   ```shiki
   output_config = {
       "effort": "high",
       "task_budget": {"type": "tokens", "total": 128000},
   }
   ```

   You may need to experiment with different task budgets for your use case. If the model is given a task budget that is too restrictive, it may complete the task less thoroughly, referencing its budget as the constraint.

   For open-ended agentic tasks where quality matters more than speed, do not set a task budget. Reserve task budgets for workloads where you need the model to scope its work to a token allowance. The minimum value for a task budget is 20k tokens.

   A task budget is not a hard cap; it's a suggestion that the model is aware of. It differs from `max_tokens`:

   - **`task_budget`:** an advisory cap across the full agentic loop. The model sees it and uses it to pace itself.
   - **`max_tokens`:** a hard per-request ceiling on generated tokens. It is not passed to the model, so the model is not aware of it.

   Use `task_budget` when you want the model to self-moderate, and `max_tokens` as a hard ceiling to cap usage.
4. **Set a large `max_tokens` at `max` or `xhigh` effort:** If you are running Claude Opus 4.7 or a later model at `max` or `xhigh` effort, set a large max output token budget so the model has room to think and act across its subagents and tool calls. Start at 64k tokens and tune from there.
5. **Downsample images if high resolution is unnecessary:** Claude Opus 4.7 supports images up to 2576px / 3.75MP. High-res images use more tokens. If the additional image fidelity is unnecessary, downsample images before sending to Claude to avoid token-usage increases. See [Images and vision](build-with-claude/vision.md).

####  Migration checklist

- Update model name from `claude-opus-4-6` to `claude-opus-4-8` (or update aliases).
- Remove `temperature`, `top_p`, and `top_k` from request payloads.
- Replace `thinking: {type: "enabled", budget_tokens: N}` with `thinking: {type: "adaptive"}` plus the [effort parameter](build-with-claude/effort.md).
- Remove any assistant-message prefills.
- If your UI displays thinking content, explicitly opt in to thinking summarization.
- Re-benchmark end-to-end cost and latency under the updated tokenization.
- Re-tune `max_tokens` to account for the updated tokenization.
- Re-test any client-side token-count estimations.
- If your application sends images, re-budget for [high-resolution image support](build-with-claude/vision.md) (up to approximately 3x more image tokens per full-resolution image). Downsample before sending if you do not need the additional fidelity.
- If you consume pointing or bounding-box coordinates from the model, remove any scale-factor conversion; coordinates are 1:1 with actual image pixels on Claude Opus 4.7.
- Review prompts for the behavior changes (response length, literalism, tone, progress updates, subagents, effort calibration, tool triggering, cyber safeguards, high-resolution image handling).
- Re-baseline response length with existing length-control prompts removed, then tune explicitly.
- If using `xhigh` or `max` effort, raise `max_tokens` to at least 64k as a starting point.
- Consider adopting task budgets (beta) for agentic workflows.
- If your product does legitimate security work, apply to the [Cyber Verification Program](https://claude.com/form/cyber-use-case) for access to lower restrictions on cyber content.

###  Migrating to Claude Opus 4.8 from Claude Opus 4.5 or earlier

If you are migrating from Claude Opus 4.5, Opus 4.1 (deprecated), or an earlier model directly to Claude Opus 4.8, apply **all of the changes in [Migrating to Claude Opus 4.8 from Claude Opus 4.6](#migrating-from-claude-opus-46)** plus the cumulative changes in this section that took effect between Opus 4.5 and Opus 4.7. If you are migrating from Opus 4.6, you only need the [from Claude Opus 4.6 section](#migrating-from-claude-opus-46).

####  Update your model name

```shiki
# Opus migration
model = "claude-opus-4-5"  # Before
model = "claude-opus-4-8"  # After
```



####  Breaking changes

1. **Prefill removal** is covered in the [breaking changes for migrating from Claude Opus 4.6](#breaking-changes).
2. **Tool parameter quoting:** Claude Opus 4.6 and later models may produce slightly different JSON string escaping in tool call arguments (for example, different handling of Unicode escapes or forward slash escaping). If you parse tool call `input` as a raw string rather than using a JSON parser, verify your parsing logic. Standard JSON parsers (such as `json.loads()` or `JSON.parse()`) handle these differences automatically.

####  Recommended changes

These changes improve your experience on Claude Opus 4.7 and later models. Items marked **(required on Opus 4.7)** were optional recommendations when Opus 4.6 launched but are now mandatory; the rest remain recommended.

1. **Migrate to adaptive thinking (required on Opus 4.7):** `thinking: {type: "enabled", budget_tokens: N}` returns a 400 error on Claude Opus 4.7. Switch to `thinking: {type: "adaptive"}` and use the [effort parameter](build-with-claude/effort.md) to control thinking depth. See [Adaptive thinking](build-with-claude/thinking-steering-and-cost.md).

   cURLBeforeAfterCLITypeScriptC#GoJavaPHPRuby

   

   ```shiki
   response = client.beta.messages.create(
       model="claude-opus-4-5",
       max_tokens=16000,
       thinking={"type": "enabled", "budget_tokens": 32000},
       betas=["interleaved-thinking-2025-05-14"],
       messages=[{"role": "user", "content": "Your prompt here"}],
   )
   ```

   Note that the migration also moves from `client.beta.messages.create` to `client.messages.create`. Adaptive thinking and effort are GA features and do not require the beta SDK namespace or any beta headers.
2. **Remove effort beta header:** The effort parameter is now GA. Remove `betas=["effort-2025-11-24"]` from your requests.
3. **Remove fine-grained tool streaming beta header:** Fine-grained tool streaming is now GA. Remove `betas=["fine-grained-tool-streaming-2025-05-14"]` from your requests.
4. **Remove interleaved thinking beta header:** Adaptive thinking automatically enables interleaved thinking on Claude Opus 4.7, Opus 4.6, and Sonnet 4.6. Remove `betas=["interleaved-thinking-2025-05-14"]` from your requests. The header is still functional on Sonnet 4.6 with manual extended thinking, but manual mode is deprecated.
5. **Migrate to output\_config.format:** If using structured outputs, update `output_format={...}` to `output_config={"format": {...}}`. The old parameter remains functional but is deprecated and will be removed in a future model release.

####  Migrating from Claude 4.1 or earlier

If you're migrating from Opus 4.1 (deprecated) or earlier models directly to Claude Opus 4.8, apply the [Migrating to Claude Opus 4.8 from Claude Opus 4.6](#migrating-from-claude-opus-46) changes and the cumulative changes earlier in this section, plus the additional changes in this sub-section.

```shiki
# From Opus 4.1
model = "claude-opus-4-1-20250805"  # Before
model = "claude-opus-4-8"  # After

# From Sonnet 3.7
model = "claude-3-7-sonnet-20250219"  # Before
model = "claude-opus-4-8"  # After
```



##### Additional breaking changes

1. **Remove sampling parameters**

   

   This is a breaking change when migrating from Claude 3.x models.

   Starting with Claude Opus 4.7, setting `temperature`, `top_p`, or `top_k` to any non-default value returns a 400 error. The safest migration path is to omit these parameters entirely from requests, and to use prompting to guide the model's behavior. If you were using `temperature = 0` for determinism, note that it never guaranteed identical outputs.

   PythonTypeScriptC#GoJavaPHPRuby

   

   ```shiki
   # Before - This will error in Claude 4+ models
   response = client.messages.create(
       model="claude-3-7-sonnet-20250219",
       temperature=0.7,
       top_p=0.9,  # Non-default sampling params return 400 on Opus 4.7
       # ...
   )

   # After
   response = client.messages.create(
       model="claude-opus-4-8",
       # ...
   )
   ```
2. **Update tool versions**

   

   This is a breaking change when migrating from Claude 3.x models.

   Update to the latest tool versions. Remove any code using the `undo_edit` command.

   PythonTypeScriptC#GoJavaPHPRuby

   

   ```shiki
   # Before
   tools = [{"type": "text_editor_20250124", "name": "str_replace_editor"}]

   # After
   tools = [{"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"}]
   ```

   - **Text editor:** Use `text_editor_20250728` and `str_replace_based_edit_tool`. See [Text editor tool](agents-and-tools/tool-use/text-editor-tool.md) documentation for details.
   - **Code execution:** Upgrade to `code_execution_20260521`. See [Code execution tool](agents-and-tools/tool-use/code-execution-tool.md) documentation for migration instructions.
3. **Handle the `refusal` stop reason**

   Update your application to [handle `refusal` stop reasons](test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md):

   PythonTypeScriptC#GoJavaPHPRuby

   

   ```shiki
   response = client.messages.create(...)

   if response.stop_reason == "refusal":
       # Handle refusal appropriately
       pass
   ```
4. **Handle the `model_context_window_exceeded` stop reason**

   Claude 4.5+ models return a `model_context_window_exceeded` stop reason when generation stops because of hitting the context window limit, rather than the requested `max_tokens` limit. Update your application to handle this new stop reason:

   PythonTypeScriptC#GoJavaPHPRuby

   

   ```shiki
   response = client.messages.create(...)

   if response.stop_reason == "model_context_window_exceeded":
       # Handle context window limit appropriately
       pass
   ```
5. **Verify tool parameter handling (trailing newlines)**

   Claude 4.5+ models preserve trailing newlines in tool call string parameters that were previously stripped. If your tools rely on exact string matching against tool call parameters, verify your logic handles trailing newlines correctly.
6. **Update your prompts for behavioral changes**

   Claude 4+ models have a more concise, direct communication style and require explicit direction. Review [prompting best practices](build-with-claude/prompt-engineering/claude-prompting-best-practices.md) for optimization guidance.

##### Additional recommended changes

- **Remove legacy beta headers:** Remove `token-efficient-tools-2025-02-19` and `output-128k-2025-02-19`. All Claude 4+ models have built-in token-efficient tool use and these headers have no effect.

####  Migration checklist (from Opus 4.5 or earlier)

- Update model ID to `claude-opus-4-8`
- Apply all breaking changes in [Migrating to Claude Opus 4.8 from Claude Opus 4.6](#migrating-from-claude-opus-46) (extended thinking removed, sampling parameters removed, thinking display omitted by default, updated tokenization)
- **BREAKING:** Remove assistant message prefills (returns 400 error); use structured outputs or `output_config.format` instead
- **BREAKING on Opus 4.7:** Replace `thinking: {type: "enabled", budget_tokens: N}` with `thinking: {type: "adaptive"}` plus the [effort parameter](build-with-claude/effort.md) (returns 400 on Opus 4.7)
- Verify tool call JSON parsing uses a standard JSON parser
- Remove `effort-2025-11-24` beta header (effort is now GA)
- Remove `fine-grained-tool-streaming-2025-05-14` beta header
- Remove `interleaved-thinking-2025-05-14` beta header (adaptive thinking enables interleaved thinking automatically)
- Migrate `output_format` to `output_config.format` (if applicable)
- If migrating from Claude 4.1 or earlier: remove `temperature`, `top_p`, and `top_k` (non-default values return 400 on Opus 4.7)
- If migrating from Claude 4.1 or earlier: update tool versions (`text_editor_20250728`, `code_execution_20260521`)
- If migrating from Claude 4.1 or earlier: handle `refusal` stop reason
- If migrating from Claude 4.1 or earlier: handle `model_context_window_exceeded` stop reason
- If migrating from Claude 4.1 or earlier: verify tool string parameter handling for trailing newlines
- If migrating from Claude 4.1 or earlier: remove legacy beta headers (`token-efficient-tools-2025-02-19`, `output-128k-2025-02-19`)
- Review and update prompts following [prompting best practices](build-with-claude/prompt-engineering/claude-prompting-best-practices.md)
- Test in development environment before production deployment

---

##  Migrating to Claude Sonnet 5

Claude Sonnet 5 offers the best combination of speed and intelligence in the Claude model family. It builds on Claude Sonnet 4.6.

Claude Sonnet 5 is a drop-in upgrade for Claude Sonnet 4.6. Introductory pricing of $2/$10 USD per million input/output tokens is in effect through August 31, 2026, after which the standard pricing of $3/$15 USD per million input/output tokens will take effect; see [Pricing](about-claude/pricing.md) for details. There are two breaking API changes for code already running on Claude Sonnet 4.6: manual extended thinking (`thinking: {type: "enabled", budget_tokens: N}`) and sampling parameters (`temperature`, `top_p`, `top_k`) set to non-default values are no longer accepted and return a 400 error. Use [adaptive thinking](build-with-claude/thinking-steering-and-cost.md) with the [effort parameter](build-with-claude/effort.md) instead. Claude Sonnet 5 supports the same set of features as Claude Sonnet 4.6, including the [1M token context window](build-with-claude/context-windows.md), [adaptive thinking](build-with-claude/thinking-steering-and-cost.md), [prompt caching](build-with-claude/prompt-caching.md), [batch processing](build-with-claude/batch-processing.md), the [Files API](build-with-claude/files.md), [PDF support](build-with-claude/pdf-support.md), [vision](build-with-claude/vision.md), and the full set of server-side and client-side [tools](agents-and-tools/tool-use/overview.md). [Priority Tier](api/service-tiers.md) is not available on Claude Sonnet 5. Claude Sonnet 5 also uses a new tokenizer.

###  Migrating to Claude Sonnet 5 from Claude Sonnet 4.6



If your code is on Claude Sonnet 4.5 or earlier, also apply [Migrating to Claude Sonnet 5 from Claude Sonnet 4.5 or earlier](#migrating-from-sonnet-45). Those steps include breaking changes (assistant message prefilling rejected, tool parameter JSON escaping differences) that this section alone does not cover.

####  Update your model name

```shiki
# Sonnet migration
model = "claude-sonnet-4-6"  # Before
model = "claude-sonnet-5"  # After
```



####  What changed

Items 4 and 5 in the following list are breaking changes. `max_tokens` remains a hard limit on total output (thinking plus response text), so revisit it for workloads that ran without thinking on Claude Sonnet 4.6.

1. **New tokenizer:** Claude Sonnet 5 uses a new tokenizer. The same input text produces approximately 30% more tokens than on Claude Sonnet 4.6. The exact increase depends on the content. Requests, responses, and streaming events keep the same shape, and no code changes are required, but anything you measure or budget in tokens shifts: `usage` fields and [token counting](build-with-claude/token-counting.md) results for the same text are higher, the 1M token context window holds less text, and a `max_tokens` limit tuned for Claude Sonnet 4.6 may truncate equivalent output. Per-token pricing is unchanged, so the cost of an equivalent request can differ. Re-run token counting against Claude Sonnet 5 rather than reusing counts measured against earlier models.
2. **128k max output tokens (unchanged):** Claude Sonnet 5 supports up to 128k output tokens, the same as Claude Sonnet 4.6. Existing `max_tokens` values remain valid. Account for the new tokenizer when sizing them.
3. **Assistant message prefilling (unchanged):** Prefilling the assistant message returns a `400` error on Claude Sonnet 5, the same as on Claude Sonnet 4.6. If you removed prefill when migrating to Claude Sonnet 4.6, no further changes are needed. Use [structured outputs](build-with-claude/structured-outputs.md), system prompt instructions, or `output_config.format` instead.
4. **Adaptive thinking on by default:** On Claude Sonnet 4.6, requests without a `thinking` field run without thinking; on Claude Sonnet 5, the same requests run with [adaptive thinking](build-with-claude/thinking-steering-and-cost.md). To turn thinking off, pass `thinking: {type: "disabled"}`. Manual extended thinking (`thinking: {type: "enabled", budget_tokens: N}`) is not supported and returns a 400 error. Use the [effort parameter](build-with-claude/effort.md) (default `high`) to control thinking depth.

   Claude Sonnet 5

   Claude Sonnet 5

   Claude Sonnet 4.6

   Claude Sonnet 4.6

   

   Adaptive thinking is on by default for Claude Sonnet 5. The `thinking` field is shown explicitly here to set `display: "summarized"`; if you omit `thinking`, Claude Sonnet 5 omits thinking content from the response by default. For per-model defaults, see [Adaptive thinking](build-with-claude/thinking-steering-and-cost.md).

   cURLCLIPythonTypeScriptC#GoJavaPHPRuby

   

   ```shiki
   client = anthropic.Anthropic()

   response = client.messages.create(
       model="claude-sonnet-5",
       max_tokens=16000,
       thinking={"type": "adaptive", "display": "summarized"},
       output_config={"effort": "high"},
       messages=[
           {
               "role": "user",
               "content": "Are there an infinite number of prime numbers such that n mod 4 == 3?",
           }
       ],
   )

   # The response contains summarized thinking blocks and text blocks
   for block in response.content:
       match block.type:
           case "thinking":
               print(f"\nThinking summary: {block.thinking}")
           case "text":
               print(f"\nResponse: {block.text}")
   ```
5. **Sampling parameters removed:** Sampling parameters (`temperature`, `top_p`, `top_k`) set to a non-default value are not accepted and return a 400 error.
6. **Cybersecurity safeguards:** Claude Sonnet 5 is the first Sonnet-tier model with real-time cybersecurity safeguards. Requests that involve prohibited or high-risk cybersecurity topics may be refused. Refusals return as a successful HTTP 200 response with `stop_reason: "refusal"`, not an error. See [Safeguards, warnings, and appeals](https://support.claude.com/en/articles/8241253-safeguards-warnings-and-appeals) for background.

####  Migration checklist

- Update model name from `claude-sonnet-4-6` to `claude-sonnet-5`.
- Re-run [token counting](build-with-claude/token-counting.md) against Claude Sonnet 5. The new tokenizer produces approximately 30% more tokens for the same text, which can change per-request cost even though per-token pricing is unchanged. The exact increase depends on the content and workload shape.
- Revisit `max_tokens` limits sized close to your expected output length, and raise them up to the 128k maximum (unchanged from Claude Sonnet 4.6) where useful.
- Remove `thinking: {type: "enabled", budget_tokens: N}` configuration (returns a 400 error). Adaptive thinking is on by default; pass `{type: "disabled"}` to turn it off, or use the [effort parameter](build-with-claude/effort.md) to control depth.
- Remove `temperature`, `top_p`, and `top_k` parameters set to non-default values (they return a 400 error on Claude Sonnet 5).
- Add handling for `stop_reason: "refusal"` if your workload may touch cybersecurity topics.
- Re-baseline cost on your typical workload before production deployment.
- Review `max_tokens` for workloads that previously ran without thinking.

###  Migrating to Claude Sonnet 5 from Claude Sonnet 4.5 or earlier

If you are migrating from Claude Sonnet 4.5 or an earlier Sonnet model directly to Claude Sonnet 5, apply the [Migrating to Claude Sonnet 5 from Claude Sonnet 4.6](#migrating-from-claude-sonnet-4-6-to-claude-sonnet-5) changes plus the changes in this section.



Claude Sonnet 5 defaults to an effort level of `high`, in contrast to Sonnet 4.5 which had no effort parameter. Consider adjusting the [effort parameter](build-with-claude/effort.md) as you migrate. If not explicitly set, you may experience higher latency with the default effort level.

####  Breaking changes

##### When migrating from Sonnet 4.5

1. **Prefilling assistant messages is no longer supported**

   

   This is a breaking change when migrating from Sonnet 4.5 or earlier.

   Prefilling assistant messages returns a `400` error on Claude Sonnet 4.6 and later models, including Claude Sonnet 5. Use [structured outputs](build-with-claude/structured-outputs.md), system prompt instructions, or `output_config.format` instead.

   **Common prefill use cases and migrations:**

   - **Controlling output formatting** (forcing JSON/YAML output): Use [structured outputs](build-with-claude/structured-outputs.md) or tools with enum fields for classification tasks.
   - **Eliminating preambles** (removing "Here is..." phrases): Add direct instructions in the system prompt: "Respond directly without preamble. Do not start with phrases like 'Here is...', 'Based on...', etc."
   - **Avoiding bad refusals:** Claude is much better at appropriate refusals now. Clear prompting in the user message without prefill should be sufficient.
   - **Continuations** (resuming interrupted responses): Move the continuation to the user message: "Your previous response was interrupted and ended with `[previous_response]`. Continue from where you left off."
   - **Context hydration / role consistency** (refreshing context in long conversations): Inject what were previously prefilled-assistant reminders into the user turn instead.
2. **Tool parameter JSON escaping may differ**

   

   This is a breaking change when migrating from Sonnet 4.5 or earlier.

   JSON string escaping in tool parameters may differ from previous models. Standard JSON parsers handle this automatically, but custom string-based parsing may need updates.

**Extended thinking changes:** `budget_tokens` configurations from Claude Sonnet 4.5 (`thinking: {type: "enabled", budget_tokens: N}`) are not supported on Claude Sonnet 5 and return a 400 error. Adaptive thinking is on by default, so most workloads need no `thinking` configuration at all; use the [effort parameter](build-with-claude/effort.md) to control thinking depth. If you ran Claude Sonnet 4.5 without extended thinking, pass `thinking: {type: "disabled"}` to preserve that behavior.

##### When migrating from Claude 3.x

1. **Remove sampling parameters**

   

   This is a breaking change when migrating from Claude 3.x models.

   Sampling parameters (`temperature`, `top_p`, `top_k`) set to a non-default value return a 400 error on Claude Sonnet 5. Remove them from requests, and use prompting to guide the model's behavior instead.
2. **Update tool versions**

   

   This is a breaking change when migrating from Claude 3.x models.

   Update to the latest tool versions (`text_editor_20250728`, `code_execution_20260521`). Remove any code using the `undo_edit` command.
3. **Handle the `refusal` stop reason**

   Update your application to [handle `refusal` stop reasons](test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md).
4. **Update your prompts for behavioral changes**

   Claude 4 models have a more concise, direct communication style. Review [prompting best practices](build-with-claude/prompt-engineering/claude-prompting-best-practices.md) for optimization guidance.

---

##  Migrating to Claude Haiku 4.5

Claude Haiku 4.5 is the fastest and most intelligent Haiku model with near-frontier performance, delivering premium model quality for interactive applications and high-volume processing.

For a complete overview of capabilities, see the [models overview](about-claude/models/overview.md).



For Claude Haiku 4.5 pricing, see [Claude pricing](about-claude/pricing.md).



For significant performance improvements on coding and reasoning tasks, consider enabling extended thinking with `thinking: {type: "enabled", budget_tokens: N}`.



Extended thinking impacts [prompt caching](build-with-claude/prompt-caching.md) efficiency.

Extended thinking is deprecated in Claude 4.6 models and removed in Claude Opus 4.7. If using newer models, use [adaptive thinking](build-with-claude/thinking-steering-and-cost.md) instead.

###  Migrating to Claude Haiku 4.5 from Claude Haiku 3.5 or earlier

**Update your model name:**

```shiki
# From Haiku 3.5
model = "claude-3-5-haiku-20241022"  # Before
model = "claude-haiku-4-5-20251001"  # After
```



**Review new rate limits:** Haiku 4.5 has separate rate limits from Haiku 3.5. See [Rate limits](api/rate-limits.md) documentation for details.

**Explore new capabilities:** See the [models overview](about-claude/models/overview.md) for details on context awareness, increased output capacity (64k tokens), higher intelligence, and improved speed.

####  Breaking changes

These breaking changes apply when migrating from Claude 3.x Haiku models.

1. **Update sampling parameters**

   

   This is a breaking change when migrating from Claude 3.x models.

   Use only `temperature` OR `top_p`, not both. Setting both returns a 400 error on Claude Haiku 4.5.
2. **Update tool versions**

   

   This is a breaking change when migrating from Claude 3.x models.

   Update to the latest tool versions (`text_editor_20250728`, `code_execution_20250825`). Remove any code using the `undo_edit` command.
3. **Handle the `refusal` stop reason**

   Update your application to [handle `refusal` stop reasons](test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md).
4. **Update your prompts for behavioral changes**

   Claude 4 models have a more concise, direct communication style. Review [prompting best practices](build-with-claude/prompt-engineering/claude-prompting-best-practices.md) for optimization guidance.

####  Haiku 4.5 migration checklist

- Update model ID to `claude-haiku-4-5-20251001`
- **BREAKING:** Update tool versions to latest (`text_editor_20250728`, `code_execution_20250825`); legacy versions are not supported
- **BREAKING:** Remove any code using the `undo_edit` command (if applicable)
- **BREAKING:** Update sampling parameters to use only `temperature` OR `top_p`, not both (setting both returns a 400 error)
- Handle new `refusal` stop reason in your application
- Review and adjust for new rate limits (separate from Haiku 3.5)
- Review and update prompts following [prompting best practices](build-with-claude/prompt-engineering/claude-prompting-best-practices.md)
- Consider enabling extended thinking for complex reasoning tasks
- Test in development environment before production deployment

---

##  Get help

- Check the [API documentation](api/overview.md) for detailed specifications
- Review [model capabilities](about-claude/models/overview.md) for performance comparisons
- Review [API release notes](release-notes/api.md) for API updates
- Contact support if you encounter any issues during migration

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
