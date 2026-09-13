# [Claude docs changes for September 13th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/e892407e80da6759655a284d9b8f932b34407ff8) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/e892407e80da6759655a284d9b8f932b34407ff8)]

## Executive Summary
- Claude Code 2.1.270 fixes a regression where read-only git commands run through Bash would unexpectedly prompt for permission after a session had been running for a while.

## New Claude Code versions

### [2.1.270](https://github.com/gpambrozio/ClaudeDocs/blob/e892407e80da6759655a284d9b8f932b34407ff8/versions/2.1.270.md)

#### Major bug fixes

* Fixed read-only git commands in Bash unexpectedly asking for permission after a session had been running for a while (regression in 2.1.269)
