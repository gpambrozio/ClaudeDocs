---
name:  changelog
description: "Looks at all git changes and create a markdown with notable changes."
allowed-tools:
  - Bash(git:*)
  - Read
  - Write
  - AskUserQuestion
---

Look at the current git changes.

* Ignore removed file
* For new files:
- check if there's a removed file with a similar name
- If there is do a diff. If they're similar enough treat this as a file modification
- If there is not, summarize the file
* For modified files, look at the diff and for every significant change create a quick bullet point about it. Ignore very small changes that do not add any new relevant information in the context of technical documents. Examples of changes that should be ignores include, but are not limited to, spelling fixes, capitalization changes, company name changes, small url changes, etc.

After determining all changes commit all doc changes. Note the new commit hash.

Then create a markdown in this format:

```
# [Claude docs changes for <today's date, ie Sept, 10th 2025>](https://github.com/gpambrozio/ClaudeDocs/tree/{commit-hash})

## New Documents

### [File name](https://github.com/gpambrozio/ClaudeDocs/blob/{commit-hash}/path/to/file.md) [[Original](link_to_source)]

New file that describes the new X feature. It shows how to use it and how to configure it...

## Changed documents

### [File name](https://github.com/gpambrozio/ClaudeDocs/blob/{commit-hash}/path/to/file.md) [[Original](link_to_source)]

* A new configuration option was added to Stop hooks that determines their timeout. [[line 75](https://github.com/gpambrozio/ClaudeDocs/blob/{commit-hash}/path/to/file.md?plain=1#L75)] [[Original](link_to_source#anchor)]
* Clarification about how to use return values. [[lines 100-110](https://github.com/gpambrozio/ClaudeDocs/blob/{commit-hash}/path/to/file.md?plain=1#L100-L110)] [[Original](link_to_source#anchor)]
```

To determine link_to_source you need to map the file name here using this mapping logic:

- docs-md/claude-code/<path>.md → https://code.claude.com/docs/en/<path>
- docs-md/api/<path>.md → https://platform.claude.com/docs/en/<path>

Examples:
docs-md/claude-code/common-workflows.md
  → https://code.claude.com/docs/en/common-workflows

docs-md/api/build-with-claude/vision.md
  → https://platform.claude.com/docs/en/build-with-claude/vision

The anchor to use on the original link is the closest anchor right above the given change. If necessary read the full file to determine that.

File names on link descriptions should not include the .md extension. Order files by name in the doc.

Save this summary to a file in the `changelogs` folder. Name it `changelog-YYYY-mm-dd.md`.

Commit this file and push.
