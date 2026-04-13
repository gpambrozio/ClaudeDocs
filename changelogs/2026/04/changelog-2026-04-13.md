# [Claude docs changes for April 13th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/a368cf252d9301481acfd474abacdeb117bbf6b9) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/a368cf252d9301481acfd474abacdeb117bbf6b9)]

## Executive Summary
- Files API requests within managed agent sessions now require the `managed-agents-2026-04-01` beta header in addition to `files-api-2025-04-14`
- Session ID prefix in the managed agents Files API examples corrected from `sess_` to `sesn_`

-----

## API changes

### Changed documents

#### [managed-agents/files](https://github.com/gpambrozio/ClaudeDocs/blob/a368cf252d9301481acfd474abacdeb117bbf6b9/docs-md/api/managed-agents/files.md) [[Source](https://platform.claude.com/docs/en/managed-agents/files)]

* Files API calls within managed agent sessions now require both `managed-agents-2026-04-01` and `files-api-2025-04-14` beta headers (previously only `files-api-2025-04-14` was shown). [[lines 110-116](https://github.com/gpambrozio/ClaudeDocs/blob/a368cf252d9301481acfd474abacdeb117bbf6b9/docs-md/api/managed-agents/files.md?plain=1#L110-L116)] [[Source](https://platform.claude.com/docs/en/managed-agents/files)]
* Session ID example value corrected from `sess_abc123` to `sesn_abc123`. [[line 107](https://github.com/gpambrozio/ClaudeDocs/blob/a368cf252d9301481acfd474abacdeb117bbf6b9/docs-md/api/managed-agents/files.md?plain=1#L107)] [[Source](https://platform.claude.com/docs/en/managed-agents/files)]
