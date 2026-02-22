## [​](#available-models) Available models

For the `model` setting in Claude Code, you can configure either:

- A **model alias**
- A **model name**
  - Anthropic API: A full **[model name](about-claude/models/overview.md)**
  - Bedrock: an inference profile ARN
  - Foundry: a deployment name
  - Vertex: a version name

### [​](#model-aliases) Model aliases

Model aliases provide a convenient way to select model settings without
remembering exact version numbers:

| Model alias | Behavior |
| --- | --- |
| **`default`** | Recommended model setting, depending on your account type |
| **`sonnet`** | Uses the latest Sonnet model (currently Sonnet 4.6) for daily coding tasks |
| **`opus`** | Uses the latest Opus model (currently Opus 4.6) for complex reasoning tasks |
| **`haiku`** | Uses the fast and efficient Haiku model for simple tasks |
| **`sonnet[1m]`** | Uses Sonnet with a [1 million token context window](build-with-claude/context-windows.md) for long sessions |
| **`opusplan`** | Special mode that uses `opus` during plan mode, then switches to `sonnet` for execution |

Aliases always point to the latest version. To pin to a specific version, use the full model name (for example, `claude-opus-4-6`) or set the corresponding environment variable like `ANTHROPIC_DEFAULT_OPUS_MODEL`.

### [​](#setting-your-model) Setting your model

You can configure your model in several ways, listed in order of priority:

1. **During session** - Use `/model <alias|name>` to switch models mid-session
2. **At startup** - Launch with `claude --model <alias|name>`
3. **Environment variable** - Set `ANTHROPIC_MODEL=<alias|name>`
4. **Settings** - Configure permanently in your settings file using the `model`
   field.

Example usage:

Report incorrect code

Copy

Ask AI

```shiki
# Start with Opus
claude --model opus

# Switch to Sonnet during session
/model sonnet
```

Example settings file:

Report incorrect code

Copy

Ask AI

```shiki
{
    "permissions": {
        ...
    },
    "model": "opus"
}
```

## [​](#restrict-model-selection) Restrict model selection

Enterprise administrators can use `availableModels` in [managed or policy settings](settings.md) to restrict which models users can select.
When `availableModels` is set, users cannot switch to models not in the list via `/model`, `--model` flag, Config tool, or `ANTHROPIC_MODEL` environment variable.

Report incorrect code

Copy

Ask AI

```shiki
{
  "availableModels": ["sonnet", "haiku"]
}
```

### [​](#default-model-behavior) Default model behavior

The Default option in the model picker is not affected by `availableModels`. It always remains available and represents the system’s runtime default [based on the user’s subscription tier](#default-model-setting).
Even with `availableModels: []`, users can still use Claude Code with the Default model for their tier.

### [​](#control-the-model-users-run-on) Control the model users run on

To fully control the model experience, use `availableModels` together with the `model` setting:

- **availableModels**: restricts what users can switch to
- **model**: sets the explicit model override, taking precedence over the Default

This example ensures all users run Sonnet 4.6 and can only choose between Sonnet and Haiku:

Report incorrect code

Copy

Ask AI

```shiki
{
  "model": "sonnet",
  "availableModels": ["sonnet", "haiku"]
}
```

### [​](#merge-behavior) Merge behavior

When `availableModels` is set at multiple levels, such as user settings and project settings, arrays are merged and deduplicated. To enforce a strict allowlist, set `availableModels` in managed or policy settings which take highest priority.

## [​](#special-model-behavior) Special model behavior

### [​](#default-model-setting) `default` model setting

The behavior of `default` depends on your account type:

- **Max and Team Premium**: defaults to Opus 4.6
- **Pro and Team Standard**: defaults to Sonnet 4.6
- **Enterprise**: Opus 4.6 is available but not the default

Claude Code may automatically fall back to Sonnet if you hit a usage threshold with Opus.

### [​](#opusplan-model-setting) `opusplan` model setting

The `opusplan` model alias provides an automated hybrid approach:

- **In plan mode** - Uses `opus` for complex reasoning and architecture
  decisions
- **In execution mode** - Automatically switches to `sonnet` for code generation
  and implementation

This gives you the best of both worlds: Opus’s superior reasoning for planning,
and Sonnet’s efficiency for execution.

### [​](#adjust-effort-level) Adjust effort level

[Effort levels](build-with-claude/effort.md) control Opus 4.6’s adaptive reasoning, which dynamically allocates thinking based on task complexity. Lower effort is faster and cheaper for straightforward tasks, while higher effort provides deeper reasoning for complex problems.
Three levels are available: **low**, **medium**, and **high** (default).
**Setting effort:**

- **In `/model`**: use left/right arrow keys to adjust the effort slider when selecting a model
- **Environment variable**: set `CLAUDE_CODE_EFFORT_LEVEL=low|medium|high`
- **Settings**: set `effortLevel` in your settings file

Effort is currently supported on Opus 4.6. The effort slider appears in `/model` when a supported model is selected.

### [​](#extended-context) Extended context

Opus 4.6 and Sonnet 4.6 support a [1 million token context window](build-with-claude/context-windows.md) for long sessions with large codebases.

The 1M context window is currently in beta. Features, pricing, and availability may change.

Extended context is available for:

- **API and pay-as-you-go users**: full access to 1M context
- **Pro, Max, Teams, and Enterprise subscribers**: available with [extra usage](https://support.claude.com/en/articles/12429409-extra-usage-for-paid-claude-plans) enabled

To disable 1M context entirely, set `CLAUDE_CODE_DISABLE_1M_CONTEXT=1`. This removes 1M model variants from the model picker. See [environment variables](settings.md).
Selecting a 1M model does not immediately change billing. Your session uses standard rates until it exceeds 200K tokens of context. Beyond 200K tokens, requests are charged at [long-context pricing](about-claude/pricing.md) with dedicated [rate limits](api/rate-limits.md). For subscribers, tokens beyond 200K are billed as extra usage rather than through the subscription.
If your account supports 1M context, the option appears in the model picker (`/model`) in the latest versions of Claude Code. If you don’t see it, try restarting your session.
You can also use the `[1m]` suffix with model aliases or full model names:

Report incorrect code

Copy

Ask AI

```shiki
# Use the sonnet[1m] alias
/model sonnet[1m]

# Or append [1m] to a full model name
/model claude-sonnet-4-6[1m]
```

## [​](#checking-your-current-model) Checking your current model

You can see which model you’re currently using in several ways:

1. In [status line](statusline.md) (if configured)
2. In `/status`, which also displays your account information.

## [​](#environment-variables) Environment variables

You can use the following environment variables, which must be full **model
names** (or equivalent for your API provider), to control the model names that the aliases map to.

| Environment variable | Description |
| --- | --- |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` | The model to use for `opus`, or for `opusplan` when Plan Mode is active. |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | The model to use for `sonnet`, or for `opusplan` when Plan Mode is not active. |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | The model to use for `haiku`, or [background functionality](costs.md) |
| `CLAUDE_CODE_SUBAGENT_MODEL` | The model to use for [subagents](sub-agents.md) |

Note: `ANTHROPIC_SMALL_FAST_MODEL` is deprecated in favor of
`ANTHROPIC_DEFAULT_HAIKU_MODEL`.

### [​](#pin-models-for-third-party-deployments) Pin models for third-party deployments

When deploying Claude Code through [Bedrock](amazon-bedrock.md), [Vertex AI](google-vertex-ai.md), or [Foundry](microsoft-foundry.md), pin model versions before rolling out to users.
Without pinning, Claude Code uses model aliases (`sonnet`, `opus`, `haiku`) that resolve to the latest version. When Anthropic releases a new model, users whose accounts don’t have the new version enabled will break silently.

Set all three model environment variables to specific version IDs as part of your initial setup. Skipping this step means a Claude Code update can break your users without any action on your part.

Use the following environment variables with version-specific model IDs for your provider:

| Provider | Example |
| --- | --- |
| Bedrock | `export ANTHROPIC_DEFAULT_OPUS_MODEL='us.anthropic.claude-opus-4-6-v1'` |
| Vertex AI | `export ANTHROPIC_DEFAULT_OPUS_MODEL='claude-opus-4-6'` |
| Foundry | `export ANTHROPIC_DEFAULT_OPUS_MODEL='claude-opus-4-6'` |

Apply the same pattern for `ANTHROPIC_DEFAULT_SONNET_MODEL` and `ANTHROPIC_DEFAULT_HAIKU_MODEL`. For current and legacy model IDs across all providers, see [Models overview](about-claude/models/overview.md). To upgrade users to a new model version, update these environment variables and redeploy.

The `settings.availableModels` allowlist still applies when using third-party providers. Filtering matches on the model alias (`opus`, `sonnet`, `haiku`), not the provider-specific model ID.

### [​](#prompt-caching-configuration) Prompt caching configuration

Claude Code automatically uses [prompt caching](build-with-claude/prompt-caching.md) to optimize performance and reduce costs. You can disable prompt caching globally or for specific model tiers:

| Environment variable | Description |
| --- | --- |
| `DISABLE_PROMPT_CACHING` | Set to `1` to disable prompt caching for all models (takes precedence over per-model settings) |
| `DISABLE_PROMPT_CACHING_HAIKU` | Set to `1` to disable prompt caching for Haiku models only |
| `DISABLE_PROMPT_CACHING_SONNET` | Set to `1` to disable prompt caching for Sonnet models only |
| `DISABLE_PROMPT_CACHING_OPUS` | Set to `1` to disable prompt caching for Opus models only |

These environment variables give you fine-grained control over prompt caching behavior. The global `DISABLE_PROMPT_CACHING` setting takes precedence over the model-specific settings, allowing you to quickly disable all caching when needed. The per-model settings are useful for selective control, such as when debugging specific models or working with cloud providers that may have different caching implementations.

---

*Copyright © Anthropic. All rights reserved.*
