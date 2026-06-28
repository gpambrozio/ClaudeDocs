# [Claude docs changes for June 28th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/10a3b79bfd010553678e006520d54a783b35c089) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/10a3b79bfd010553678e006520d54a783b35c089)]

## Executive Summary
- The advisor tool gained an expanded model compatibility matrix (Haiku and Sonnet executors can now use Opus, Fable 5, or Mythos 5 as advisors), plus new behaviors for truncation signaling and `pause_turn` resumption.
- Server tools documentation now fully documents what happens when a server tool and a client tool are called in the same parallel group — a common agentic pattern that previously lacked clear guidance.
- The web fetch tool received major clarifications: it is now confirmed available on Claude Platform on AWS and Microsoft Foundry (not Bedrock/Google Cloud), PDFs are now returned as base64, `blocked_domains` cannot be combined with `allowed_domains`, and several error codes were corrected.
- Programmatic tool calling documentation was updated with corrected timeouts (4 min), required container IDs, and a stricter tool-result content rule (strings/text only).
- The memory tool doc confirmed GA status (no beta header needed) and documented many previously undocumented behaviors: `view` on image files, `view_range` with `-1`, `create` overwriting, `str_replace` deletion, and root-path protection for `delete`/`rename`.

-----

## API changes

### Changed documents

#### [Advisor Tool](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/advisor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

* The model compatibility table was significantly expanded: Haiku 4.5 and Sonnet 4.6 executors can now use Opus 4.6, Opus 4.7, Opus 4.8, Fable 5, or Mythos 5 as advisors; Sonnet 4.6 can also advise itself; same-capability Opus pairs can advise each other; Fable 5 and Mythos 5 executors can only use the same model as advisor. [[line ~32](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L32)]
* Clarified that Fable 5 and Mythos 5 advisors return `advisor_redacted_result` while all other supported advisors return `advisor_result`. [[line ~102](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L102)]
* New section documenting how to resume a `pause_turn` response that contains a pending advisor call: re-send the same assistant content with the same tools and beta header — no new user message or `tool_result` block needed. [[line ~146](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L146)]
* Added note that `tool_choice: {"type": "tool", "name": "advisor"}` can force an advisor call, but cannot be combined with extended thinking (returns 400). [[line ~215](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L215)]
* Clarified that top-level `max_tokens` does not cap advisor tokens, advisor tokens don't draw from task budgets, and Priority Tier applies per model independently. [[line ~232](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L232)]
* When `max_tokens` is hit, the API now appends `[Advisor output truncated at max_tokens=2048.]` to the advice text so the executor can detect the truncation in its own context. [[line ~354](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L354)]

#### [CMEK](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/manage-claude/cmek.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

* Added a reference to the new [CMEK content preservation](manage-claude/access-transparency.md) page for details on preservation behavior. [[line ~126](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/manage-claude/cmek.md?plain=1#L126)]

#### [Memory Tool](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/memory-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)]

* Memory tool is now generally available — no beta header is required. [[line ~128](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/memory-tool.md?plain=1#L128)]
* New section documenting ready-made handler implementations: `BetaLocalFilesystemMemoryTool` for Python and TypeScript; Go and Ruby require a manual tool-use loop; PHP uses `BetaRunnableTool`. [[line ~147](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/memory-tool.md?plain=1#L147)]
* `view` command now also displays image files (`.jpg`, `.jpeg`, `.png`) and truncates text files longer than 16,000 characters. [[line ~255](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/memory-tool.md?plain=1#L255)]
* `view_range: [start_line, -1]` reads from `start_line` to end of file. [[line ~200](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/memory-tool.md?plain=1#L200)]
* `create` can overwrite existing files; `str_replace` with `new_str` omitted deletes `old_str`; `insert` with `insert_line: 0` inserts at the beginning. [[line ~290](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/memory-tool.md?plain=1#L290)]
* `delete` and `rename` operations on the memory root (`/memories`) are now explicitly rejected. [[line ~361](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/memory-tool.md?plain=1#L361)]
* Error return format documented: errors are returned by setting `is_error: true` on the `tool_result` block. [[line ~460](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/memory-tool.md?plain=1#L460)]

#### [Parallel Tool Use](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/parallel-tool-use.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use)]

* Added explicit rule that every `tool_result` block must appear before any text content in a user message. [[line ~13](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/parallel-tool-use.md?plain=1#L13)]
* `disable_parallel_tool_use` now has a dedicated section with full runnable code examples clarifying it is set inside the `tool_choice` object and that its effect differs by mode: `auto` allows at most one tool call, `any`/`tool` allows exactly one. [[line ~170](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/parallel-tool-use.md?plain=1#L170)]

#### [Programmatic Tool Calling](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)]

* Both code execution version strings (`code_execution_20260120` and `code_execution_20260521`) are now accepted interchangeably in `allowed_callers`; response blocks always tag the caller as `code_execution_20260120`. [[line ~127](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md?plain=1#L127)]
* Container ID is now required (not optional) when responding to pending programmatic tool calls. Idle containers are reclaimed after ~5 minutes (up from 4.5). Pending tool calls time out after ~4 minutes, raising `TimeoutError` with message `(no response after 270s)`. [[line ~177](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md?plain=1#L177)]
* Tool results answering programmatic calls must be strings or text blocks — image, document, and other content block types are rejected. [[line ~591](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md?plain=1#L591)]
* All code examples updated: tools now take a single dict of arguments and return a string; Claude's generated code uses `json.loads(await tool_name({"key": "val"}))`. [[line ~97](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md?plain=1#L97)]

#### [Server Tools](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/server-tools.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools)]

* New major section documenting mixed server + client tool calls in the same parallel group: the API returns `stop_reason: "tool_use"` immediately with both the `server_tool_use` block and the client `tool_use` block (no server result yet); the client sends only its `tool_result` blocks in the follow-up, and the API then runs the deferred server tool. Full Python code example included. [[line ~81](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/server-tools.md?plain=1#L81)]
* Documented distinction from `pause_turn`: `pause_turn` never leaves a client `tool_use` block waiting; `tool_use` stop_reason does. MCP connector `mcp_tool_use` blocks follow the same deferred pattern. [[line ~180](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/server-tools.md?plain=1#L180)]

#### [Tool Runner](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/tool-runner.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner)]

* `max_iterations` is now supported across all seven SDKs; the tool runner loop exits when this limit is reached. [[line ~110](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/tool-runner.md?plain=1#L110)]
* Client-side automatic compaction (Python, TypeScript, Ruby) is now deprecated in favor of server-side context editing. Go, Java, C#, and PHP tool runners do not include client-side compaction. [[line ~249](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/tool-runner.md?plain=1#L249)]
* Debugging behavior is now documented per-SDK: only Python logs full exceptions (stack traces) via the `logging` module; Go, Ruby, C#, and PHP do not read `ANTHROPIC_LOG` and require exceptions to be caught inside the tool function. [[line ~253](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/tool-runner.md?plain=1#L253)]

#### [Web Fetch Tool](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]

* Web fetch (with and without dynamic filtering) is now documented as available on the Claude API, Claude Platform on AWS, and Microsoft Foundry — not on Amazon Bedrock or Google Cloud. [[line ~10](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L10)]
* Web fetch is now described as a server tool: the API fetches content during the request, so no `tool_result` is needed from the caller. [[line ~38](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L38)]
* PDF handling updated: the API now returns PDF content as base64-encoded data and processes it like a directly attached PDF document. [[line ~45](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L45)]
* Dynamic filtering no longer requires the caller to add the code execution tool to the `tools` array — the API enables it automatically. [[line ~71](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L71)]
* `blocked_domains` cannot be combined with `allowed_domains` (now documented in the parameter comment). [[line ~140](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L140)]
* Failed fetches now count against the `max_uses` limit. The `max_content_tokens` limit applies only to text content, not binary content such as PDFs. [[line ~153](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L153)]
* Added a `use_cache` code example and clarified that later tool versions add `use_cache` and `response_inclusion` parameters. [[line ~177](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L177)]
* Citations for web fetch are now explicitly documented as disabled by default. [[line ~217](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L217)]
* Several error codes corrected: `invalid_input` → `invalid_tool_input`; `web_fetch_tool_error` type → `web_fetch_tool_result_error`; new error code `url_not_in_prior_context`; `unsupported_content_type` now includes HTML. [[line ~361](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L361)]

-----

## Claude Code changes

### Changed documents

#### [Claude Code on Claude Platform on AWS](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/claude-code/claude-platform-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

* Removed the sales/pricing callout banner that appeared at the top of the page. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/10a3b79bfd010553678e006520d54a783b35c089/docs-md/claude-code/claude-platform-on-aws.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]
