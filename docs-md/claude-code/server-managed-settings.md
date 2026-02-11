# Configure server-managed settings (public beta)

Server-managed settings allow administrators to centrally configure Claude Code through a web-based interface on Claude.ai. Claude Code clients automatically receive these settings when users authenticate with their organization credentials.
This approach is designed for organizations that do not have device management infrastructure in place, or need to manage settings for users on unmanaged devices.

Server-managed settings are in public beta and available for [Claude for Teams](https://claude.com/pricing#team-&-enterprise) and [Claude for Enterprise](https://anthropic.com/contact-sales) customers. Features may evolve before general availability.

## [​](#requirements) Requirements

To use server-managed settings, you need:

- Claude for Teams or Claude for Enterprise plan
- Claude Code version 2.1.30 or later
- Network access to `api.anthropic.com`

## [​](#choose-between-server-managed-and-endpoint-managed-settings) Choose between server-managed and endpoint-managed settings

Claude Code supports two approaches for centralized configuration. Server-managed settings deliver configuration from Anthropic’s servers. [Endpoint-managed settings](permissions.md) deploy a `managed-settings.json` file to system directories via MDM (mobile device management).

| Approach | Best for | Security model |
| --- | --- | --- |
| **Server-managed settings** | Organizations without MDM, or users on unmanaged devices | Settings delivered from Anthropic’s servers at authentication time |
| **[Endpoint-managed settings](permissions.md)** | Organizations with MDM or endpoint management | Settings deployed to protected system directories by IT |

If your devices are enrolled in an MDM or endpoint management solution, endpoint-managed settings provide stronger security guarantees because the settings file can be protected from user modification at the OS level.

## [​](#configure-server-managed-settings) Configure server-managed settings

1

Open the admin console

In [Claude.ai](https://claude.ai), navigate to **Admin Settings > Claude Code > Managed settings**.

2

Define your settings

Add your configuration as JSON. All [settings available in `settings.json`](settings.md) are supported, including [managed-only settings](permissions.md) like `disableBypassPermissionsMode`.This example enforces a permission deny list and prevents users from bypassing permissions:

Report incorrect code

Copy

Ask AI

```shiki
{
  "permissions": {
    "deny": [
      "Bash(curl *)",
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)"
    ]
  },
  "disableBypassPermissionsMode": "disable"
}
```

3

Save and deploy

Save your changes. Claude Code clients receive the updated settings on their next startup or hourly polling cycle.

### [​](#verify-settings-delivery) Verify settings delivery

To confirm that settings are being applied, ask a user to restart Claude Code. If the configuration includes settings that trigger the [security approval dialog](#security-approval-dialogs), the user sees a prompt describing the managed settings on startup. You can also verify that managed permission rules are active by having a user run `/permissions` to view their effective permission rules.

### [​](#access-control) Access control

The following roles can manage server-managed settings:

- **Primary Owner**
- **Owner**

Restrict access to trusted personnel, as settings changes apply to all users in the organization.

### [​](#current-limitations) Current limitations

Server-managed settings have the following limitations during the beta period:

- Settings apply uniformly to all users in the organization. Per-group configurations are not yet supported.
- [MCP server configurations](mcp.md) cannot be distributed through server-managed settings.

## [​](#settings-delivery) Settings delivery

### [​](#settings-precedence) Settings precedence

Server-managed settings and [endpoint-managed settings](permissions.md) both occupy the highest tier in the Claude Code [settings hierarchy](settings.md), and user or project settings cannot override them. When both are present, server-managed settings take precedence and the local `managed-settings.json` file is not used.

### [​](#fetch-and-caching-behavior) Fetch and caching behavior

Claude Code fetches settings from Anthropic’s servers at startup and polls for updates hourly during active sessions.
**First launch without cached settings:**

- Claude Code fetches settings asynchronously
- If the fetch fails, Claude Code continues without managed settings
- There is a brief window before settings load where restrictions are not yet enforced

**Subsequent launches with cached settings:**

- Cached settings apply immediately at startup
- Claude Code fetches fresh settings in the background
- Cached settings persist through network failures

Claude Code applies settings updates automatically without a restart, except for advanced settings like OpenTelemetry configuration, which require a full restart to take effect.

### [​](#security-approval-dialogs) Security approval dialogs

Certain settings that could pose security risks require explicit user approval before being applied:

- **Shell command settings**: settings that execute shell commands
- **Custom environment variables**: variables not in the known safe allowlist
- **Hook configurations**: any hook definition

When these settings are present, users see a security dialog explaining what is being configured. Users must approve to proceed. If a user rejects the settings, Claude Code exits.

In non-interactive mode with the `-p` flag, Claude Code skips security dialogs and applies settings without user approval.

## [​](#platform-availability) Platform availability

Server-managed settings require a direct connection to `api.anthropic.com` and are not available when using third-party model providers:

- Amazon Bedrock
- Google Vertex AI
- Microsoft Foundry
- Custom API endpoints via `ANTHROPIC_BASE_URL` or [LLM gateways](llm-gateway.md)

## [​](#audit-logging) Audit logging

Audit log events for settings changes are available through the compliance API or audit log export. Contact your Anthropic account team for access.
Audit events include the type of action performed, the account and device that performed the action, and references to the previous and new values.

## [​](#security-considerations) Security considerations

Server-managed settings provide centralized policy enforcement, but they operate as a client-side control. On unmanaged devices, users with admin or sudo access can modify the Claude Code binary, filesystem, or network configuration.

| Scenario | Behavior |
| --- | --- |
| User edits the cached settings file | Tampered file applies at startup, but correct settings restore on the next server fetch |
| User deletes the cached settings file | First-launch behavior occurs: settings fetch asynchronously with a brief unenforced window |
| API is unavailable | Cached settings apply if available, otherwise managed settings are not enforced until the next successful fetch |
| User authenticates with a different organization | Settings are not delivered for accounts outside the managed organization |
| User sets a non-default `ANTHROPIC_BASE_URL` | Server-managed settings are bypassed when using third-party API providers |

For stronger enforcement guarantees, use [endpoint-managed settings](permissions.md) on devices enrolled in an MDM solution.

## [​](#see-also) See also

Related pages for managing Claude Code configuration:

- [Settings](settings.md): complete configuration reference including all available settings
- [Endpoint-managed settings](permissions.md): file-based managed settings deployed by IT
- [Authentication](authentication.md): set up user access to Claude Code
- [Security](security.md): security safeguards and best practices

---

*Copyright © Anthropic. All rights reserved.*
