# Download Skill Version Content

Copy page

SDK language

CLI

# Download Skill Version Content

$ ant beta:skills:versions download

GET/v1/skills/{skill\_id}/versions/{version}/content

Download a skill version's content as a zip archive.

##### ParametersExpand Collapse



--skill-id: string

Path param: Unique identifier for the skill.

The format and length of IDs may change over time.



--version: string

Path param: Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

unnamed\_schema\_1: file path

Download Skill Version Content

CLI

```shiki
ant beta:skills:versions download \
  --api-key my-anthropic-api-key \
  --skill-id skill_id \
  --version version
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
