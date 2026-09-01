# Migrating to Claude Haiku 4.5

Copy page



Claude Haiku 4.5 is the fastest and most intelligent Haiku model with near-frontier performance, delivering premium model quality for interactive applications and high-volume processing.

For a complete overview of capabilities, see the [models overview](models/overview.md).

## Migrating to Claude Haiku 4.5 from Claude Haiku 3.5 and earlier Haiku models

**Update your model name:**

```shiki
# From Haiku 3.5
model = "claude-3-5-haiku-20241022"  # Before
model = "claude-haiku-4-5-20251001"  # After
```



**Review new rate limits:** Haiku 4.5 has separate rate limits from Haiku 3.5. See [Rate limits](api/rate-limits.md) documentation for details.

**Explore new capabilities:** See the [models overview](models/overview.md) for details on context awareness, increased output capacity (64k tokens), higher intelligence, and improved speed.

### Breaking changes

These breaking changes apply when migrating from Claude 3.x Haiku models.

1. **Update sampling parameters**

   Use only `temperature` OR `top_p`, not both. Setting both returns a 400 error on Claude Haiku 4.5.
2. **Update tool versions**

   Update to the latest tool versions (`text_editor_20250728`, `code_execution_20250825`). Remove any code using the `undo_edit` command.
3. **Handle the `refusal` stop reason**

   Update your application to [handle `refusal` stop reasons](test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md).
4. **Update your prompts for behavioral changes**

   Claude 4 models have a more concise, direct communication style. Review [prompting best practices](build-with-claude/prompt-engineering/claude-prompting-best-practices.md) for optimization guidance.

### Haiku 4.5 migration checklist

- Update model ID to `claude-haiku-4-5-20251001`
- **BREAKING:** Update tool versions to latest (`text_editor_20250728`, `code_execution_20250825`); legacy versions are not supported
- **BREAKING:** Remove any code using the `undo_edit` command (if applicable)
- **BREAKING:** Update sampling parameters to use only `temperature` OR `top_p`, not both (setting both returns a 400 error)
- Handle new `refusal` stop reason in your application
- Review and adjust for new rate limits (separate from Haiku 3.5)
- Review and update prompts following [prompting best practices](build-with-claude/prompt-engineering/claude-prompting-best-practices.md)
- Consider enabling extended thinking for complex reasoning tasks
- Test in development environment before production deployment

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
