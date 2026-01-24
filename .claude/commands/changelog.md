---
name:  changelog
description: "Looks at all git changes and create a markdown with notable changes."
allowed-tools:
  - Bash(git:*)
  - Read
  - Write
---

Look at the current git changes.

The `versions` folder contains release notes for new versions of claude code. Ignore file changes. If there are new files in this folder:

* Look at all the changes
* Ignore small bugfixes that would not affect overall claude code usage.
* Create a summary of the changes in this order:
** New features
** Existing feature improvements
** Major bug fixes

For files in the `docs-md` folder:

* Ignore removed file
* For new files:
- check if there's a removed file with a similar name
- If there is do a diff. If they're similar enough treat this as a file modification
- If there is not, summarize the file
* For modified files, look at the diff and for every significant change create a quick bullet point about it. Ignore very small changes that do not add any new relevant information in the context of technical documents. Examples of changes that should be ignores include, but are not limited to, spelling fixes, capitalization changes, company name changes, small url changes, etc.

After determining all changes commit changes to the `docs-md` and `versions` folders. Note the new commit hash.

Then create a markdown in this format. Files in `docs-md/claude-code` go in the `Claude Code changes` section and files in `docs-md/api` go in the `API changes` section:

```
# [Claude docs changes for <today's date, ie Sept, 10th 2025>](https://github.com/gpambrozio/ClaudeDocs/tree/{commit-hash}) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/{commit-hash})]

## New Claude Code versions

### [2.1.10](https://github.com/gpambrozio/ClaudeDocs/blob/{commit-hash}/versions/2.1.10.md)

#### New features

* Added a new cli option to help with debugging
* Added a new hook called Whatever

#### Existing feature improvements

* Improved caching

#### Major bug fixes

* Fixed bug where hook was not called

### [2.1.11](https://github.com/gpambrozio/ClaudeDocs/blob/{commit-hash}/versions/2.1.11.md)

#### Major bug fixes

* Fixed excessive MCP connection requests

-----

## Claude Code changes

### New Documents

#### [File name](https://github.com/gpambrozio/ClaudeDocs/blob/{commit-hash}/path/to/file.md)

New file that describes the new X feature. It shows how to use it and how to configure it...

### Changed documents

#### [File name](https://github.com/gpambrozio/ClaudeDocs/blob/{commit-hash}/path/to/file.md)

* A new configuration option was added to Stop hooks that determines their timeout. [[line 75](https://github.com/gpambrozio/ClaudeDocs/blob/{commit-hash}/path/to/file.md?plain=1#L75)]
* Clarification about how to use return values. [[lines 100-110](https://github.com/gpambrozio/ClaudeDocs/blob/{commit-hash}/path/to/file.md?plain=1#L100-L110)]

-----

## API changes

### New Documents

#### [File name](https://github.com/gpambrozio/ClaudeDocs/blob/{commit-hash}/path/to/file.md)

New file that describes the new X feature. It shows how to use it and how to configure it...

### Changed documents

#### [File name](https://github.com/gpambrozio/ClaudeDocs/blob/{commit-hash}/path/to/file.md)

* A new configuration option was added to Stop hooks that determines their timeout. [[line 75](https://github.com/gpambrozio/ClaudeDocs/blob/{commit-hash}/path/to/file.md?plain=1#L75)]
* Clarification about how to use return values. [[lines 100-110](https://github.com/gpambrozio/ClaudeDocs/blob/{commit-hash}/path/to/file.md?plain=1#L100-L110)]

```

File names on link descriptions should not include the .md extension. Order files by name in the doc.

Save this summary to a markdown named `changelog-YYYY-mm-dd.md` with today's date in the `changelogs/YYYY/mm` folder.

Commit this file (do not push).
