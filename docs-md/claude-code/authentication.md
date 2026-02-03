## [​](#authentication-methods) Authentication methods

Setting up Claude Code requires access to Anthropic models. For teams, you can set up Claude Code access in one of these ways:

- [Claude for Teams or Enterprise](#claude-for-teams-or-enterprise) (recommended)
- [Claude Console](#claude-console-authentication)
- [Amazon Bedrock](amazon-bedrock.md)
- [Google Vertex AI](google-vertex-ai.md)
- [Microsoft Foundry](microsoft-foundry.md)

### [​](#claude-for-teams-or-enterprise) Claude for Teams or Enterprise

[Claude for Teams](https://claude.com/pricing#team-&-enterprise) and [Claude for Enterprise](https://anthropic.com/contact-sales) provide the best experience for organizations using Claude Code. Team members get access to both Claude Code and Claude on the web with centralized billing and team management.

- **Claude for Teams**: self-service plan with collaboration features, admin tools, and billing management. Best for smaller teams.
- **Claude for Enterprise**: adds SSO, domain capture, role-based permissions, compliance API, and managed policy settings for organization-wide Claude Code configurations. Best for larger organizations with security and compliance requirements.

1

Subscribe

Subscribe to [Claude for Teams](https://claude.com/pricing#team-&-enterprise) or contact sales for [Claude for Enterprise](https://anthropic.com/contact-sales).

2

Invite team members

Invite team members from the admin dashboard.

3

Install and log in

Team members install Claude Code and log in with their Claude.ai accounts.

### [​](#claude-console-authentication) Claude Console authentication

For organizations that prefer API-based billing, you can set up access through the Claude Console.

1

Create or use a Console account

Use your existing Claude Console account or create a new one.

2

Add users

You can add users through either method:

- Bulk invite users from within the Console (Console -> Settings -> Members -> Invite)
- [Set up SSO](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)

3

Assign roles

When inviting users, assign one of:

- **Claude Code** role: users can only create Claude Code API keys
- **Developer** role: users can create any kind of API key

4

Users complete setup

Each invited user needs to:

- Accept the Console invite
- [Check system requirements](setup.md)
- [Install Claude Code](setup.md)
- Log in with Console account credentials

### [​](#cloud-provider-authentication) Cloud provider authentication

For teams using Amazon Bedrock, Google Vertex AI, or Microsoft Azure:

1

Follow provider setup

Follow the [Bedrock docs](amazon-bedrock.md), [Vertex docs](google-vertex-ai.md), or [Microsoft Foundry docs](microsoft-foundry.md).

2

Distribute configuration

Distribute the environment variables and instructions for generating cloud credentials to your users. Read more about how to [manage configuration here](settings.md).

3

Install Claude Code

Users can [install Claude Code](setup.md).

## [​](#credential-management) Credential management

Claude Code securely manages your authentication credentials:

- **Storage location**: on macOS, API keys, OAuth tokens, and other credentials are stored in the encrypted macOS Keychain.
- **Supported authentication types**: Claude.ai credentials, Claude API credentials, Azure Auth, Bedrock Auth, and Vertex Auth.
- **Custom credential scripts**: the [`apiKeyHelper`](settings.md) setting can be configured to run a shell script that returns an API key.
- **Refresh intervals**: by default, `apiKeyHelper` is called after 5 minutes or on HTTP 401 response. Set `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` environment variable for custom refresh intervals.

## [​](#see-also) See also

- [Permissions](permissions.md): configure what Claude Code can access and do
- [Settings](settings.md): complete configuration reference
- [Security](security.md): security safeguards and best practices

---

*Copyright © Anthropic. All rights reserved.*
