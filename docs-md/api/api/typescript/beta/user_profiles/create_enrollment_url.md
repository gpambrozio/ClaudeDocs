# Create Enrollment URL

Copy page

TypeScript

# Create Enrollment URL

client.beta.userProfiles.createEnrollmentURL(stringuserProfileID, UserProfileCreateEnrollmentURLParams { betas } params?, RequestOptionsoptions?): [BetaUserProfileEnrollmentURL](api/beta.md) { expires\_at, type, url }

POST/v1/user\_profiles/{user\_profile\_id}/enrollment\_url

Create Enrollment URL

##### ParametersExpand Collapse

userProfileID: string

params: UserProfileCreateEnrollmentURLParams { betas }

betas?: Array<[AnthropicBeta](api/beta.md)>

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

(string & {})

"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 20 more

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

##### ReturnsExpand Collapse

BetaUserProfileEnrollmentURL { expires\_at, type, url }

expires\_at: string

A timestamp in RFC 3339 format

type: "enrollment\_url"

Object type. Always `enrollment_url`.

url: string

Enrollment URL to send to the end user. Valid until `expires_at`.

Create Enrollment URL

TypeScript

```shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaUserProfileEnrollmentURL = await client.beta.userProfiles.createEnrollmentURL(
  'uprof_011CZkZCu8hGbp5mYRQgUmz9',
);

console.log(betaUserProfileEnrollmentURL.expires_at);
```

Response 200

```shiki
{
  "expires_at": "2026-03-15T10:15:00Z",
  "type": "enrollment_url",
  "url": "https://platform.claude.com/user-profiles/enrollment/M3J0bGJxZ2ppMnptbnB1"
}
```

##### Returns Examples

Response 200

```shiki
{
  "expires_at": "2026-03-15T10:15:00Z",
  "type": "enrollment_url",
  "url": "https://platform.claude.com/user-profiles/enrollment/M3J0bGJxZ2ppMnptbnB1"
}
```

---

*Copyright © Anthropic. All rights reserved.*
