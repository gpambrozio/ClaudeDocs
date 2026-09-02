# Messages

Copy page



cURL

# Messages

##### [Create a Message](api/http/beta/messages/create.md)

POST/v1/messages

##### [Count tokens in a Message](api/http/beta/messages/count_tokens.md)

POST/v1/messages/count\_tokens

##### Models



BetaAdvisorMessageIterationUsage object{ cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }

Token usage for an advisor sub-inference iteration.



BetaAdvisorRedactedResultBlock object{ encrypted\_content, stop\_reason, type }

encrypted\_content: string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: string or null

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).



type: "advisor\_redacted\_result"

defaultadvisor\_redacted\_result



BetaAdvisorRedactedResultBlockParam object{ encrypted\_content, type, stop\_reason }

encrypted\_content: string

Opaque blob produced by a prior response; must be round-tripped verbatim.

type: "advisor\_redacted\_result"

stop\_reason: optional string or null



BetaAdvisorResultBlock object{ stop\_reason, text, type }

stop\_reason: string or null

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: string



type: "advisor\_result"

defaultadvisor\_result



BetaAdvisorResultBlockParam object{ text, type, stop\_reason }

text: string

type: "advisor\_result"

stop\_reason: optional string or null



BetaAdvisorTool20260301 object{ model, name, type, 7 more }



BetaAdvisorToolResultBlock object{ content, tool\_use\_id, type }



BetaAdvisorToolResultBlockParam object{ content, tool\_use\_id, type, cache\_control }



BetaAdvisorToolResultError object{ error\_code, type }



error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 4 more

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"



type: "advisor\_tool\_result\_error"

defaultadvisor\_tool\_result\_error



BetaAdvisorToolResultErrorParam object{ error\_code, type }



error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 4 more

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: "advisor\_tool\_result\_error"



BetaAllThinkingTurns object{ type }

type: "all"



BetaBase64ImageSource object{ data, media\_type, type }



data: string

formatbyte



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



BetaBase64PDFSource object{ data, media\_type, type }



data: string

formatbyte

media\_type: "application/pdf"

type: "base64"



BetaBashCodeExecutionOutputBlock object{ file\_id, type }

file\_id: string



type: "bash\_code\_execution\_output"

defaultbash\_code\_execution\_output



BetaBashCodeExecutionOutputBlockParam object{ file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"



BetaBashCodeExecutionResultBlock object{ content, return\_code, stderr, 2 more }



content: array of [BetaBashCodeExecutionOutputBlock](api/http/beta/messages.md) { file\_id, type }

file\_id: string



type: "bash\_code\_execution\_output"

defaultbash\_code\_execution\_output

return\_code: number

stderr: string

stdout: string



type: "bash\_code\_execution\_result"

defaultbash\_code\_execution\_result



BetaBashCodeExecutionResultBlockParam object{ content, return\_code, stderr, 2 more }



content: array of [BetaBashCodeExecutionOutputBlockParam](api/http/beta/messages.md) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"



BetaBashCodeExecutionToolResultBlock object{ content, tool\_use\_id, type }



BetaBashCodeExecutionToolResultBlockParam object{ content, tool\_use\_id, type, cache\_control }



BetaBashCodeExecutionToolResultError object{ error\_code, type }



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"



type: "bash\_code\_execution\_tool\_result\_error"

defaultbash\_code\_execution\_tool\_result\_error



BetaBashCodeExecutionToolResultErrorParam object{ error\_code, type }



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BetaBrowserCloseTabConfig object{ defer\_loading, enabled }

`close_tab`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserDoubleClickConfig object{ defer\_loading, enabled }

`double_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserFileUploadConfig object{ defer\_loading, enabled }

`file_upload`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserFindConfig object{ defer\_loading, enabled }

`find`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserFormInputConfig object{ defer\_loading, enabled }

`form_input`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserGetPageTextConfig object{ defer\_loading, enabled }

`get_page_text`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserHoldKeyConfig object{ defer\_loading, enabled }

`hold_key`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserHoverConfig object{ defer\_loading, enabled }

`hover`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserJavascriptExecConfig object{ defer\_loading, enabled }

`javascript_exec`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserKeyConfig object{ defer\_loading, enabled }

`key`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserLeftClickConfig object{ defer\_loading, enabled }

`left_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserLeftClickDragConfig object{ defer\_loading, enabled }

`left_click_drag`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserLeftMouseDownConfig object{ defer\_loading, enabled }

`left_mouse_down`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserLeftMouseUpConfig object{ defer\_loading, enabled }

`left_mouse_up`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserListTabsConfig object{ defer\_loading, enabled }

`list_tabs`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserMiddleClickConfig object{ defer\_loading, enabled }

`middle_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserMouseMoveConfig object{ defer\_loading, enabled }

`mouse_move`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserNavigateConfig object{ defer\_loading, enabled }

`navigate`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserNewTabConfig object{ defer\_loading, enabled }

`new_tab`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserReadConsoleConfig object{ defer\_loading, enabled }

`read_console`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserReadNetworkConfig object{ defer\_loading, enabled }

`read_network`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserReadPageConfig object{ defer\_loading, enabled }

`read_page`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserRightClickConfig object{ defer\_loading, enabled }

`right_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserScreenshotConfig object{ defer\_loading, enabled }

`screenshot`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserScrollConfig object{ defer\_loading, enabled }

`scroll`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserScrollToConfig object{ defer\_loading, enabled }

`scroll_to`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserStateBlockParam object{ tabs, type, cache\_control, state\_changes }

The caller's browser state after a browser toolset member call —
the full inventory of open tabs, which tab is active, and any side
effects (tabs opened, download state changes) the call produced.

At most one per `tool_result`, only on a non-error result answering a
browser toolset member `tool_use`. The server renders the
model-visible text from it; the model never sees the raw fields.



BetaBrowserStateChange = [BetaBrowserStateChangeTabOpened](api/http/beta/messages.md) { tab\_id, type } or [BetaBrowserStateChangeDownloadStarted](api/http/beta/messages.md) { download\_id, type, url } or [BetaBrowserStateChangeDownloadCompleted](api/http/beta/messages.md) { download\_id, type, url, 2 more } or [BetaBrowserStateChangeDownloadFailed](api/http/beta/messages.md) { download\_id, type, url, error }

A tab this call's execution opened that remains open at its end —
the creation delta of the `tabs` inventory, not an event log.

Carries only the `tab_id`; the tab's `title` and `url` live on its
`tabs` entry, which must include the same `tab_id`. A tab opened
during a failed call gets no deferred `tab_opened`; it simply appears
in the next result's `tabs` inventory.

One of the following:



BetaBrowserStateChangeDownloadCompleted object{ download\_id, type, url, 2 more }

A file download that finished during this call, reported with the
same `download_id` as its `download_started` — or without a prior
`download_started`, when the download finished during the call that
started it (at most one state change per `download_id` per result).



download\_id: string

The caller-assigned identifier for this download, stable across the state changes reporting it.

maxLength4096

minLength1

pattern^[^\x00-\x1f\x7f-\x9f\u2028\u2029]\*$

type: "download\_completed"



url: string

The final post-redirect URL the download was served from.

maxLength4096

pattern^[^\x00-\x1f\x7f-\x9f\u2028\u2029]\*$



path: optional string or null

Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

pattern^[^\x00-\x1f\x7f-\x9f\u2028\u2029]\*$

maxLength4096



size\_bytes: optional number or null

The completed download's size.

minimum0



BetaBrowserStateChangeDownloadFailed object{ download\_id, type, url, error }

A file download that failed — or was cancelled — during this call.



download\_id: string

The caller-assigned identifier for this download, stable across the state changes reporting it.

maxLength4096

minLength1

pattern^[^\x00-\x1f\x7f-\x9f\u2028\u2029]\*$

type: "download\_failed"



url: string

The final post-redirect URL the download was served from.

maxLength4096

pattern^[^\x00-\x1f\x7f-\x9f\u2028\u2029]\*$



error: optional string or null

The failure or cancellation detail, when known.

pattern^[^\x00-\x1f\x7f-\x9f\u2028\u2029]\*$

maxLength4096



BetaBrowserStateChangeDownloadStarted object{ download\_id, type, url }

A file download that started during this call.



download\_id: string

The caller-assigned identifier for this download, stable across the state changes reporting it.

maxLength4096

minLength1

pattern^[^\x00-\x1f\x7f-\x9f\u2028\u2029]\*$

type: "download\_started"



url: string

The final post-redirect URL the download was served from.

maxLength4096

pattern^[^\x00-\x1f\x7f-\x9f\u2028\u2029]\*$



BetaBrowserStateChangeTabOpened object{ tab\_id, type }

A tab this call's execution opened that remains open at its end —
the creation delta of the `tabs` inventory, not an event log.

Carries only the `tab_id`; the tab's `title` and `url` live on its
`tabs` entry, which must include the same `tab_id`. A tab opened
during a failed call gets no deferred `tab_opened`; it simply appears
in the next result's `tabs` inventory.



tab\_id: string

The `tab_id` of the opened tab, present in `tabs`.

maxLength4096

minLength1

pattern^[^\x00-\x1f\x7f-\x9f\u2028\u2029]\*$

type: "tab\_opened"



BetaBrowserStateTabEntry object{ tab\_id, title, url, active }

One open browser tab reported in a `browser_state` block's `tabs`
inventory.

`tab_id` is the caller-assigned identifier for the tab; `title` and
`url` describe the page the tab is currently showing and may be empty
strings (a blank tab legitimately has both empty). `active` marks the
tab that is active after this call; whenever `tabs` is non-empty,
exactly one entry is marked.



tab\_id: string

The caller-assigned identifier for this tab, unique within the inventory.

maxLength4096

minLength1

pattern^[^\x00-\x1f\x7f-\x9f\u2028\u2029]\*$



title: string

The title of the page the tab is showing. May be empty.

maxLength4096

pattern^[^\x00-\x1f\x7f-\x9f\u2028\u2029]\*$



url: string

The URL of the page the tab is showing. May be empty.

maxLength4096

pattern^[^\x00-\x1f\x7f-\x9f\u2028\u2029]\*$

active: optional boolean

Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.



BetaBrowserSwitchTabConfig object{ defer\_loading, enabled }

`switch_tab`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserToolset20260801 object{ type, cache\_control, configs }

The browser toolset: a single `tools[]` entry (carrying no
`name`) that declares the browser tool family. The model is served
the family's tool with any members disabled via `configs` removed
from its schema.



BetaBrowserToolsetConfigs object{ close\_tab, double\_click, file\_upload, 28 more }

Per-member configuration for `browser_toolset_20260801`: one
optional field per member tool, keyed by the member name — the same
name the member's `tool_use` blocks carry. Every member is an
accepted key, and a member's defaults apply wherever its key is
absent. Unknown keys are rejected: the field set is this toolset
version's complete member set.



BetaBrowserTripleClickConfig object{ defer\_loading, enabled }

`triple_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserTypeConfig object{ defer\_loading, enabled }

`type`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserWaitConfig object{ defer\_loading, enabled }

`wait`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserZoomConfig object{ defer\_loading, enabled }

`zoom`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaCacheControlEphemeral object{ type, ttl }

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



BetaCacheCreation object{ ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }



ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

default0

minimum0



ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

default0

minimum0



BetaCacheMissMessagesChanged object{ cache\_missed\_input\_tokens, type }

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.



type: "messages\_changed"

defaultmessages\_changed



BetaCacheMissModelChanged object{ cache\_missed\_input\_tokens, type }

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.



type: "model\_changed"

defaultmodel\_changed



BetaCacheMissPreviousMessageNotFound object{ type }



type: "previous\_message\_not\_found"

defaultprevious\_message\_not\_found



BetaCacheMissSystemChanged object{ cache\_missed\_input\_tokens, type }

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.



type: "system\_changed"

defaultsystem\_changed



BetaCacheMissToolsChanged object{ cache\_missed\_input\_tokens, type }

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.



type: "tools\_changed"

defaulttools\_changed



BetaCacheMissUnavailable object{ type }



type: "unavailable"

defaultunavailable



BetaCitationCharLocation object{ cited\_text, document\_index, document\_title, 4 more }

cited\_text: string



document\_index: number

minimum0

document\_title: string or null

end\_char\_index: number

file\_id: string or null



start\_char\_index: number

minimum0



type: "char\_location"

defaultchar\_location



BetaCitationCharLocationParam object{ cited\_text, document\_index, document\_title, 3 more }

cited\_text: string



document\_index: number

minimum0



document\_title: string or null

maxLength500

minLength1

end\_char\_index: number



start\_char\_index: number

minimum0

type: "char\_location"



BetaCitationConfig object{ enabled }



enabled: boolean

defaultfalse



BetaCitationContentBlockLocation object{ cited\_text, document\_index, document\_title, 4 more }



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



document\_index: number

minimum0

document\_title: string or null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string or null



start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

minimum0



type: "content\_block\_location"

defaultcontent\_block\_location



BetaCitationContentBlockLocationParam object{ cited\_text, document\_index, document\_title, 3 more }



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



document\_index: number

minimum0



document\_title: string or null

maxLength500

minLength1



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

minimum0

type: "content\_block\_location"



BetaCitationPageLocation object{ cited\_text, document\_index, document\_title, 4 more }

cited\_text: string



document\_index: number

minimum0

document\_title: string or null

end\_page\_number: number

file\_id: string or null



start\_page\_number: number

minimum1



type: "page\_location"

defaultpage\_location



BetaCitationPageLocationParam object{ cited\_text, document\_index, document\_title, 3 more }

cited\_text: string



document\_index: number

minimum0



document\_title: string or null

maxLength500

minLength1

end\_page\_number: number



start\_page\_number: number

minimum1

type: "page\_location"



BetaCitationSearchResultLocation object{ cited\_text, end\_block\_index, search\_result\_index, 4 more }



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string



start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

minimum0

title: string or null



type: "search\_result\_location"

defaultsearch\_result\_location



BetaCitationSearchResultLocationParam object{ cited\_text, end\_block\_index, search\_result\_index, 4 more }



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string



start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

minimum0

title: string or null

type: "search\_result\_location"



BetaCitationWebSearchResultLocationParam object{ cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string



title: string or null

maxLength512

minLength1

type: "web\_search\_result\_location"



url: string

minLength1



BetaCitationsConfigParam object{ enabled }

enabled: optional boolean



BetaCitationsDelta object{ citation, type }



BetaCitationsWebSearchResultLocation object{ cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string



title: string or null

maxLength512



type: "web\_search\_result\_location"

defaultweb\_search\_result\_location

url: string



BetaClearThinking20251015Edit object{ type, keep }



BetaClearThinking20251015EditResponse object{ cleared\_input\_tokens, cleared\_thinking\_turns, type }



cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

minimum0



cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

minimum0



type: "clear\_thinking\_20251015"

The type of context management edit applied.

defaultclear\_thinking\_20251015



BetaClearToolUses20250919Edit object{ type, clear\_at\_least, clear\_tool\_inputs, 3 more }



BetaClearToolUses20250919EditResponse object{ cleared\_input\_tokens, cleared\_tool\_uses, type }



cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

minimum0



cleared\_tool\_uses: number

Number of tool uses that were cleared.

minimum0



type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

defaultclear\_tool\_uses\_20250919



BetaCodeExecutionOutputBlock object{ file\_id, type }

file\_id: string



type: "code\_execution\_output"

defaultcode\_execution\_output



BetaCodeExecutionOutputBlockParam object{ file\_id, type }

file\_id: string

type: "code\_execution\_output"



BetaCodeExecutionResultBlock object{ content, return\_code, stderr, 2 more }



content: array of [BetaCodeExecutionOutputBlock](api/http/beta/messages.md) { file\_id, type }

file\_id: string



type: "code\_execution\_output"

defaultcode\_execution\_output

return\_code: number

stderr: string

stdout: string



type: "code\_execution\_result"

defaultcode\_execution\_result



BetaCodeExecutionResultBlockParam object{ content, return\_code, stderr, 2 more }



content: array of [BetaCodeExecutionOutputBlockParam](api/http/beta/messages.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



BetaCodeExecutionTool20250522 object{ name, type, allowed\_callers, 3 more }



BetaCodeExecutionTool20250825 object{ name, type, allowed\_callers, 3 more }



BetaCodeExecutionTool20260120 object{ name, type, allowed\_callers, 3 more }

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



BetaCodeExecutionTool20260521 object{ name, type, allowed\_callers, 3 more }

Code execution tool with REPL state persistence.



BetaCodeExecutionToolResultBlock object{ content, tool\_use\_id, type }



content: [BetaCodeExecutionToolResultBlockContent](api/http/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



tool\_use\_id: string

pattern^srvtoolu\_[a-zA-Z0-9\_]+$



type: "code\_execution\_tool\_result"

defaultcode\_execution\_tool\_result



BetaCodeExecutionToolResultBlockContent = [BetaCodeExecutionToolResultError](api/http/beta/messages.md) { error\_code, type } or [BetaCodeExecutionResultBlock](api/http/beta/messages.md) { content, return\_code, stderr, 2 more } or [BetaEncryptedCodeExecutionResultBlock](api/http/beta/messages.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



BetaCodeExecutionToolResultBlockParam object{ content, tool\_use\_id, type, cache\_control }



content: [BetaCodeExecutionToolResultBlockParamContent](api/http/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



tool\_use\_id: string

pattern^srvtoolu\_[a-zA-Z0-9\_]+$

type: "code\_execution\_tool\_result"



cache\_control: optional [BetaCacheControlEphemeral](api/http/beta/messages.md) { type, ttl } or null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



BetaCodeExecutionToolResultBlockParamContent = [BetaCodeExecutionToolResultErrorParam](api/http/beta/messages.md) { error\_code, type } or [BetaCodeExecutionResultBlockParam](api/http/beta/messages.md) { content, return\_code, stderr, 2 more } or [BetaEncryptedCodeExecutionResultBlockParam](api/http/beta/messages.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



BetaCodeExecutionToolResultError object{ error\_code, type }



error\_code: [BetaCodeExecutionToolResultErrorCode](api/http/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"



type: "code\_execution\_tool\_result\_error"

defaultcode\_execution\_tool\_result\_error



BetaCodeExecutionToolResultErrorCode = "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"



BetaCodeExecutionToolResultErrorParam object{ error\_code, type }



error\_code: [BetaCodeExecutionToolResultErrorCode](api/http/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



BetaCompact20260112Edit object{ type, instructions, pause\_after\_compaction, trigger }

Automatically compact older context when reaching the configured trigger threshold.

type: "compact\_20260112"

instructions: optional string or null

Additional instructions for summarization.

pause\_after\_compaction: optional boolean

Whether to pause after compaction and return the compaction block to the user.



trigger: optional [BetaInputTokensTrigger](api/http/beta/messages.md) { type, value } or null

When to trigger compaction. Defaults to 150000 input tokens.

type: "input\_tokens"



value: number

minimum1



BetaCompactionBlock object{ content, encrypted\_content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string or null

Summary of compacted content, or null if compaction failed

encrypted\_content: string or null

Opaque metadata from prior compaction, to be round-tripped verbatim



type: "compaction"

defaultcompaction



BetaCompactionBlockParam object{ type, cache\_control, content, encrypted\_content }

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

type: "compaction"



cache\_control: optional [BetaCacheControlEphemeral](api/http/beta/messages.md) { type, ttl } or null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

content: optional string or null

Summary of previously compacted content, or null if compaction failed

encrypted\_content: optional string or null

Opaque metadata from prior compaction, to be round-tripped verbatim



BetaCompactionContentBlockDelta object{ content, encrypted\_content, type }

content: string or null

encrypted\_content: string or null

Opaque metadata from prior compaction, to be round-tripped verbatim



type: "compaction\_delta"

defaultcompaction\_delta



BetaCompactionIterationUsage object{ cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.



cache\_creation: [BetaCacheCreation](api/http/beta/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } or null

Breakdown of cached tokens by TTL



ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

default0

minimum0



ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

default0

minimum0



cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

default0

minimum0



cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

default0

minimum0



input\_tokens: number

The number of input tokens which were used.

minimum0



output\_tokens: number

The number of output tokens which were used.

minimum0



type: "compaction"

Usage for a compaction iteration

defaultcompaction



BetaComputerCursorPositionConfig object{ defer\_loading, enabled }

`cursor_position`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerDoubleClickConfig object{ defer\_loading, enabled }

`double_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerHoldKeyConfig object{ defer\_loading, enabled }

`hold_key`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerKeyConfig object{ defer\_loading, enabled }

`key`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerLeftClickConfig object{ defer\_loading, enabled }

`left_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerLeftClickDragConfig object{ defer\_loading, enabled }

`left_click_drag`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerLeftMouseDownConfig object{ defer\_loading, enabled }

`left_mouse_down`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerLeftMouseUpConfig object{ defer\_loading, enabled }

`left_mouse_up`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerMiddleClickConfig object{ defer\_loading, enabled }

`middle_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerMouseMoveConfig object{ defer\_loading, enabled }

`mouse_move`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerRightClickConfig object{ defer\_loading, enabled }

`right_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerScreenshotConfig object{ defer\_loading, enabled }

`screenshot`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerScrollConfig object{ defer\_loading, enabled }

`scroll`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerToolset20260801 object{ type, cache\_control, configs }

The computer toolset: a single `tools[]` entry (carrying no
`name`) that declares the computer tool family. The model is
served the family's tool with any members disabled via `configs`
removed from its schema. Every member is enabled by default, zoom
included. The single-tool options `display_number` and
`enable_zoom` are not fields of a toolset entry — it carries only
`type`, `configs`, and `cache_control`; zoom is controlled
via `configs.zoom.enabled`.



BetaComputerToolsetConfigs object{ cursor\_position, double\_click, hold\_key, 14 more }

Per-member configuration for `computer_toolset_20260801`: one
optional field per member tool, keyed by the member name — the same
name the member's `tool_use` blocks carry. Every member is an
accepted key, and a member's defaults apply wherever its key is
absent. Unknown keys are rejected: the field set is this toolset
version's complete member set.



BetaComputerTripleClickConfig object{ defer\_loading, enabled }

`triple_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerTypeConfig object{ defer\_loading, enabled }

`type`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerWaitConfig object{ defer\_loading, enabled }

`wait`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerZoomConfig object{ defer\_loading, enabled }

`zoom`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaContainer object{ id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request



expires\_at: string

The time at which the container will expire.

formatdate-time



skills: array of [BetaContainerSkill](api/http/beta/messages.md) { skill\_id, type, version } or null

Skills loaded in the container



skill\_id: string

Skill ID

maxLength64

minLength1



type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"



version: string

The resolved version: a skill version ID for custom skills.

maxLength64

minLength1



BetaContainerParams object{ id, skills }

Container parameters with skills to be loaded.

id: optional string or null

Container id



skills: optional array of [BetaSkillParams](api/http/beta/messages.md) { skill\_id, type, version } or null

List of skills to load in the container

maxItems20



skill\_id: string

Skill ID

maxLength64

minLength1



type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"



version: optional string

Skill version or 'latest' for most recent version

maxLength64

minLength1



BetaContainerSkill object{ skill\_id, type, version }

A skill that was loaded in a container (response model).



skill\_id: string

Skill ID

maxLength64

minLength1



type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"



version: string

The resolved version: a skill version ID for custom skills.

maxLength64

minLength1



BetaContainerUploadBlock object{ file\_id, type }

Response model for a file uploaded to the container.

file\_id: string



type: "container\_upload"

defaultcontainer\_upload



BetaContainerUploadBlockParam object{ file\_id, type, cache\_control }

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: string

type: "container\_upload"



cache\_control: optional [BetaCacheControlEphemeral](api/http/beta/messages.md) { type, ttl } or null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



BetaContentBlock = [BetaTextBlock](api/http/beta/messages.md) { citations, text, type } or [BetaThinkingBlock](api/http/beta/messages.md) { signature, thinking, type } or [BetaRedactedThinkingBlock](api/http/beta/messages.md) { data, type } or 14 more

Response model for a file uploaded to the container.

One of the following:



BetaContentBlockParam = [BetaTextBlockParam](api/http/beta/messages.md) { text, type, cache\_control, citations } or [BetaImageBlockParam](api/http/beta/messages.md) { source, type, cache\_control, transformations } or [BetaRequestDocumentBlock](api/http/beta/messages.md) { source, type, cache\_control, 3 more } or 20 more

Regular text content.

One of the following:



BetaContentBlockSource object{ content, type }



content: string or array of [BetaContentBlockSourceContent](api/http/beta/messages.md)

One of the following:

string



BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](api/http/beta/messages.md)

One of the following:



BetaTextBlockParam object{ text, type, cache\_control, citations }



BetaImageBlockParam object{ source, type, cache\_control, transformations }

type: "content"



BetaContentBlockSourceContent = [BetaTextBlockParam](api/http/beta/messages.md) { text, type, cache\_control, citations } or [BetaImageBlockParam](api/http/beta/messages.md) { source, type, cache\_control, transformations }

One of the following:



BetaTextBlockParam object{ text, type, cache\_control, citations }



BetaImageBlockParam object{ source, type, cache\_control, transformations }



BetaContextManagementConfig object{ edits }



BetaContextManagementResponse object{ applied\_edits }



BetaCountTokensContextManagementResponse object{ original\_input\_tokens }

original\_input\_tokens: number

The original token count before context management was applied



BetaDiagnostics object{ cache\_miss\_reason }

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



BetaDiagnosticsParam object{ previous\_message\_id }

Request-level diagnostics. Currently carries the previous response
id for prompt-cache divergence reporting.



previous\_message\_id: optional string or null

The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.

maxLength256



BetaDirectCaller object{ type }

Tool invocation directly from the model.

type: "direct"



BetaDocumentBlock object{ citations, source, title, type }



BetaEncryptedCodeExecutionResultBlock object{ content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [BetaCodeExecutionOutputBlock](api/http/beta/messages.md) { file\_id, type }

file\_id: string



type: "code\_execution\_output"

defaultcode\_execution\_output

encrypted\_stdout: string

return\_code: number

stderr: string



type: "encrypted\_code\_execution\_result"

defaultencrypted\_code\_execution\_result



BetaEncryptedCodeExecutionResultBlockParam object{ content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [BetaCodeExecutionOutputBlockParam](api/http/beta/messages.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"



BetaFallbackBlock object{ from, to, trigger, type }

Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and
declined. A turn where no preceding model ran and declined has no such
boundary and carries no block — the signal for whether a fallback model
served the response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



BetaFallbackBlockParam object{ from, to, type, trigger }

A `fallback` block echoed back from a prior response.

Accepted in `messages[].content` and not rendered into the prompt; not
validated against the request's `fallbacks` chain or top-level `model`.

Echo the assistant turn back verbatim, including this block in its
original position. The block marks the boundary between content produced
before and after a fallback hop, and the server relies on that boundary
to validate the turn: when thinking runs flank the boundary, omitting
the block merges them into one span the server cannot validate (the
request is rejected), and moving it into the middle of a single run is
likewise rejected; between non-thinking blocks the block's placement has
no validation effect.



from: [BetaFallbackInfoParam](api/http/beta/messages.md) { model }

Identifies one hop of a fallback transition.



model: [Model](api/http/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



to: [BetaFallbackInfoParam](api/http/beta/messages.md) { model }

Identifies one hop of a fallback transition.



model: [Model](api/http/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

type: "fallback"

trigger: optional unknown

The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



BetaFallbackCreditNotApplied object{ reason, type, remove\_to\_redeem }

No reprice was applied; `reason` says why.



BetaFallbackCreditRedeemed object{ type }

The reprice was applied: the retry is billed as if the conversation
had been on the retry model all along.



type: "redeemed"

defaultredeemed



BetaFallbackCreditTokenParam object{ token, mode }

Object form of `fallback_credit_token`: the token plus a redemption
mode.

Requires `anthropic-beta: fallback-credit-2026-07-01`; without that
header the field accepts the bare string only. The bare string and the
mode-less object are equivalent (both select `strict`), so wrapping
an existing token changes nothing by itself.



token: string

The opaque `fallback_credit_token` from a prior refusal's `stop_details` — the same string the bare-string form carries.

maxLength2048

minLength1



mode: optional "strict" or "best\_effort"

How a failing token affects the retry. `strict` (the default, and the bare-string behavior): a failing redemption is a 400 and the retry is not served. `best_effort`: the retry is served either way — a token-layer failure no longer rejects the request; the retry proceeds at normal price and the outcome is reported on the response's `usage.fallback_credit`. Two failures stay hard in both modes: a malformed token, and combining `fallback_credit_token` with `fallbacks`.

One of the following:

"strict"

"best\_effort"



BetaFallbackCreditUsage object{ status }

Outcome of the `fallback_credit_token` presented on this request.



status: [BetaFallbackCreditRedeemed](api/http/beta/messages.md) { type } or [BetaFallbackCreditNotApplied](api/http/beta/messages.md) { reason, type, remove\_to\_redeem }

Whether the fallback-credit reprice was applied to this response's billing.

A union discriminated on `type`. `redeemed`: the retry is billed as if
the conversation had been on the retry model all along — including when the
resulting shift is zero because there was nothing to move. `not_applied`:
no reprice was applied; the arm's `reason` says why.

One of the following:



BetaFallbackCreditRedeemed object{ type }

The reprice was applied: the retry is billed as if the conversation
had been on the retry model all along.



type: "redeemed"

defaultredeemed



BetaFallbackCreditNotApplied object{ reason, type, remove\_to\_redeem }

No reprice was applied; `reason` says why.



BetaFallbackInfo object{ model }

Identifies one hop of a fallback transition.



model: [Model](api/http/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



BetaFallbackInfoParam object{ model }

Identifies one hop of a fallback transition.



model: [Model](api/http/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



BetaFallbackMessageIterationUsage object{ cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



BetaFallbackParam object{ model, max\_tokens, output\_config, 2 more }

One entry in the `fallbacks` chain on a `/v1/messages` request.

`model` is required. The override fields (`max_tokens`, `thinking`,
`output_config`, and `speed`) set the corresponding parameter for this
attempt only and are validated as if the request were made to `model`.
Any other key is rejected at parse time.



BetaFallbackRefusalTrigger object{ category, type }

The `from` model declined for policy reasons.



category: "cyber" or "bio" or "frontier\_llm" or 2 more or null

The policy category that triggered a refusal.

One of the following:

"cyber"

The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

"bio"

The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

"frontier\_llm"

The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

"reasoning\_extraction"

The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](build-with-claude/adaptive-thinking.md).

"general\_harms"

The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.



type: "refusal"

defaultrefusal



BetaFallbacksParam = array of [BetaFallbackParam](api/http/beta/messages.md) { model, max\_tokens, output\_config, 2 more } or "default"

Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on. The string "default" requests the requested model's server-defined default fallback configuration.

One of the following:



BetaFileDocumentSource object{ file\_id, type }

file\_id: string

type: "file"



BetaFileImageSource object{ file\_id, type }

file\_id: string

type: "file"



BetaImageBlockParam object{ source, type, cache\_control, transformations }



BetaImageTransformationsParam object{ oversized\_image }

Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.



oversized\_image: optional "downsize" or "error"

What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

One of the following:

"downsize"

"error"



BetaInputJSONDelta object{ partial\_json, type }

partial\_json: string



type: "input\_json\_delta"

defaultinput\_json\_delta



BetaInputTokensClearAtLeast object{ type, value }

type: "input\_tokens"



value: number

minimum0



BetaInputTokensTrigger object{ type, value }

type: "input\_tokens"



value: number

minimum1



BetaIterationsUsage = array of [BetaMessageIterationUsage](api/http/beta/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } or [BetaCompactionIterationUsage](api/http/beta/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } or [BetaAdvisorMessageIterationUsage](api/http/beta/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } or [BetaFallbackMessageIterationUsage](api/http/beta/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the context window size from the last `message` entry
- Understand token accumulation across server-side tool use loops

A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.

One of the following:



BetaJSONOutputFormat object{ schema, type }

schema: map[unknown]

The JSON schema of the format

type: "json\_schema"



BetaMCPToolConfig object{ defer\_loading, enabled }

Configuration for a specific tool in an MCP toolset.

defer\_loading: optional boolean

enabled: optional boolean



BetaMCPToolDefaultConfig object{ defer\_loading, enabled }

Default configuration for tools in an MCP toolset.

defer\_loading: optional boolean

enabled: optional boolean



BetaMCPToolResultBlock object{ content, is\_error, tool\_use\_id, type }



BetaMCPToolUseBlock object{ id, input, name, 2 more }



id: string

pattern^[a-zA-Z0-9\_-]+$

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server



type: "mcp\_tool\_use"

defaultmcp\_tool\_use



BetaMCPToolUseBlockParam object{ id, input, name, 3 more }



BetaMCPToolset object{ mcp\_server\_name, type, cache\_control, 2 more }

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.



BetaMemoryTool20250818 object{ name, type, allowed\_callers, 4 more }



BetaMemoryTool20250818Command = [BetaMemoryTool20250818ViewCommand](api/http/beta/messages.md) { command, path, view\_range } or [BetaMemoryTool20250818CreateCommand](api/http/beta/messages.md) { command, file\_text, path } or [BetaMemoryTool20250818StrReplaceCommand](api/http/beta/messages.md) { command, new\_str, old\_str, path } or 3 more

One of the following:



BetaMemoryTool20250818CreateCommand object{ command, file\_text, path }



command: "create"

Command type identifier

defaultcreate

file\_text: string

Content to write to the file

path: string

Path where the file should be created



BetaMemoryTool20250818DeleteCommand object{ command, path }



command: "delete"

Command type identifier

defaultdelete

path: string

Path to the file or directory to delete



BetaMemoryTool20250818InsertCommand object{ command, insert\_line, insert\_text, path }



command: "insert"

Command type identifier

defaultinsert



insert\_line: number

Line number where text should be inserted

minimum1

insert\_text: string

Text to insert at the specified line

path: string

Path to the file where text should be inserted



BetaMemoryTool20250818RenameCommand object{ command, new\_path, old\_path }



command: "rename"

Command type identifier

defaultrename

new\_path: string

New path for the file or directory

old\_path: string

Current path of the file or directory



BetaMemoryTool20250818StrReplaceCommand object{ command, new\_str, old\_str, path }



command: "str\_replace"

Command type identifier

defaultstr\_replace

new\_str: string

Text to replace with

old\_str: string

Text to search for and replace

path: string

Path to the file where text should be replaced



BetaMemoryTool20250818ViewCommand object{ command, path, view\_range }



command: "view"

Command type identifier

defaultview

path: string

Path to directory or file to view



view\_range: optional array of number

Optional line range for viewing specific lines

minItems2

maxItems2



BetaMessage object{ id, container, content, 10 more }



BetaMessageDeltaUsage object{ cache\_creation\_input\_tokens, cache\_read\_input\_tokens, fallback\_credit, 5 more }



BetaMessageIterationUsage object{ cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }

Token usage for a sampling iteration.



BetaMessageParam object{ content, role, clear\_at, output\_config }



BetaMessageTokensCount object{ context\_management, input\_tokens }



context\_management: [BetaCountTokensContextManagementResponse](api/http/beta/messages.md) { original\_input\_tokens } or null

Information about context management applied to the message.

original\_input\_tokens: number

The original token count before context management was applied

input\_tokens: number

The total number of tokens across the provided list of messages, system prompt, and tools.



BetaMetadata object{ user\_id }



user\_id: optional string or null

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512



BetaOutputConfig object{ effort, format, task\_budget }



BetaOutputTokensDetails object{ thinking\_tokens }



thinking\_tokens: number

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

default0

minimum0



BetaPlainTextSource object{ data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"



BetaRawContentBlockDelta = [BetaTextDelta](api/http/beta/messages.md) { text, type } or [BetaInputJSONDelta](api/http/beta/messages.md) { partial\_json, type } or [BetaCitationsDelta](api/http/beta/messages.md) { citation, type } or 3 more

One of the following:



BetaRawContentBlockDeltaEvent object{ delta, index, type }



delta: [BetaRawContentBlockDelta](api/http/beta/messages.md)

One of the following:

index: number



type: "content\_block\_delta"

defaultcontent\_block\_delta



BetaRawContentBlockStartEvent object{ content\_block, index, type }



BetaRawContentBlockStopEvent object{ index, type }

index: number



type: "content\_block\_stop"

defaultcontent\_block\_stop



BetaRawMessageDeltaEvent object{ context\_management, delta, type, 2 more }



BetaRawMessageStartEvent object{ message, type }



message: [BetaMessage](api/http/beta/messages.md) { id, container, content, 10 more }



type: "message\_start"

defaultmessage\_start



BetaRawMessageStopEvent object{ type }



type: "message\_stop"

defaultmessage\_stop



BetaRawMessageStreamEvent = [BetaRawMessageStartEvent](api/http/beta/messages.md) { message, type } or [BetaRawMessageDeltaEvent](api/http/beta/messages.md) { context\_management, delta, type, 2 more } or [BetaRawMessageStopEvent](api/http/beta/messages.md) { type } or 3 more

One of the following:



BetaRedactedThinkingBlock object{ data, type }



data: string

The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

See [extended thinking](build-with-claude/extended-thinking.md) for details.



type: "redacted\_thinking"

defaultredacted\_thinking



BetaRedactedThinkingBlockParam object{ data, type }

data: string

The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

type: "redacted\_thinking"



BetaRefusalStopDetails object{ category, explanation, fallback\_credit\_token, 3 more }

Structured information about a refusal.



BetaRequestDocumentBlock object{ source, type, cache\_control, 3 more }



BetaRequestMCPServerToolConfiguration object{ allowed\_tools, enabled }

allowed\_tools: optional array of string or null

enabled: optional boolean or null



BetaRequestMCPServerURLDefinition object{ name, type, url, 2 more }

name: string

type: "url"

url: string

authorization\_token: optional string or null



tool\_configuration: optional [BetaRequestMCPServerToolConfiguration](api/http/beta/messages.md) { allowed\_tools, enabled } or null

allowed\_tools: optional array of string or null

enabled: optional boolean or null



BetaRequestMCPToolResultBlockParam object{ tool\_use\_id, type, cache\_control, 2 more }



BetaRequestToolAdditionBlock object{ tool, type, cache\_control }

Mid-conversation directive to surface a declared tool.

`tool` references a tool (or MCP toolset) by name from the request's
`tools`; it is offered to the model from this point in the
conversation onward.



BetaRequestToolRemovalBlock object{ tool, type, cache\_control }

Mid-conversation directive to withdraw a tool.

`tool` references a tool (or MCP toolset) by name from the request's
`tools`; it is no longer offered to the model from this point in the
conversation onward.



BetaSearchResultBlockParam object{ content, source, title, 3 more }



BetaServerToolCaller object{ tool\_id, type }

Tool invocation generated by a server-side tool.



tool\_id: string

pattern^srvtoolu\_[a-zA-Z0-9\_]+$

type: "code\_execution\_20250825"



BetaServerToolCaller20260120 object{ tool\_id, type }



tool\_id: string

pattern^srvtoolu\_[a-zA-Z0-9\_]+$

type: "code\_execution\_20260120"



BetaServerToolUsage object{ web\_fetch\_requests, web\_search\_requests }



web\_fetch\_requests: number

The number of web fetch tool requests.

default0

minimum0



web\_search\_requests: number

The number of web search tool requests.

default0

minimum0



BetaServerToolUseBlock object{ id, input, name, 2 more }



BetaServerToolUseBlockParam object{ id, input, name, 3 more }



BetaSignatureDelta object{ signature, type }

signature: string

The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.



type: "signature\_delta"

defaultsignature\_delta



BetaSkillParams object{ skill\_id, type, version }

Specification for a skill to be loaded in a container (request model).



skill\_id: string

Skill ID

maxLength64

minLength1



type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"



version: optional string

Skill version or 'latest' for most recent version

maxLength64

minLength1



BetaStopReason = "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

One of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"



BetaSystemMessageOutputConfig object{ effort }

Per-message output configuration on a role:"system" input message.

Fields here apply per-turn; `format` remains top-level only. An
empty `{}` is accepted on a message that carries content; a message
with neither content nor output\_config fields is rejected.



effort: optional "low" or "medium" or "high" or 2 more or null

All possible effort levels.

One of the following:

"low"

"medium"

"high"

"xhigh"

"max"



BetaTextBlock object{ citations, text, type }



BetaTextBlockParam object{ text, type, cache\_control, citations }



BetaTextCitation = [BetaCitationCharLocation](api/http/beta/messages.md) { cited\_text, document\_index, document\_title, 4 more } or [BetaCitationPageLocation](api/http/beta/messages.md) { cited\_text, document\_index, document\_title, 4 more } or [BetaCitationContentBlockLocation](api/http/beta/messages.md) { cited\_text, document\_index, document\_title, 4 more } or 2 more

One of the following:



BetaTextCitationParam = [BetaCitationCharLocationParam](api/http/beta/messages.md) { cited\_text, document\_index, document\_title, 3 more } or [BetaCitationPageLocationParam](api/http/beta/messages.md) { cited\_text, document\_index, document\_title, 3 more } or [BetaCitationContentBlockLocationParam](api/http/beta/messages.md) { cited\_text, document\_index, document\_title, 3 more } or 2 more

One of the following:



BetaTextDelta object{ text, type }

text: string



type: "text\_delta"

defaulttext\_delta



BetaTextEditorCodeExecutionCreateResultBlock object{ is\_file\_update, type }

is\_file\_update: boolean



type: "text\_editor\_code\_execution\_create\_result"

defaulttext\_editor\_code\_execution\_create\_result



BetaTextEditorCodeExecutionCreateResultBlockParam object{ is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



BetaTextEditorCodeExecutionStrReplaceResultBlock object{ lines, new\_lines, new\_start, 3 more }

lines: array of string or null

new\_lines: number or null

new\_start: number or null

old\_lines: number or null

old\_start: number or null



type: "text\_editor\_code\_execution\_str\_replace\_result"

defaulttext\_editor\_code\_execution\_str\_replace\_result



BetaTextEditorCodeExecutionStrReplaceResultBlockParam object{ type, lines, new\_lines, 3 more }

type: "text\_editor\_code\_execution\_str\_replace\_result"

lines: optional array of string or null

new\_lines: optional number or null

new\_start: optional number or null

old\_lines: optional number or null

old\_start: optional number or null



BetaTextEditorCodeExecutionToolResultBlock object{ content, tool\_use\_id, type }



BetaTextEditorCodeExecutionToolResultBlockParam object{ content, tool\_use\_id, type, cache\_control }



BetaTextEditorCodeExecutionToolResultError object{ error\_code, error\_message, type }



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string or null



type: "text\_editor\_code\_execution\_tool\_result\_error"

defaulttext\_editor\_code\_execution\_tool\_result\_error



BetaTextEditorCodeExecutionToolResultErrorParam object{ error\_code, type, error\_message }



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: "text\_editor\_code\_execution\_tool\_result\_error"

error\_message: optional string or null



BetaTextEditorCodeExecutionViewResultBlock object{ content, file\_type, num\_lines, 3 more }

content: string



file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number or null

start\_line: number or null

total\_lines: number or null



type: "text\_editor\_code\_execution\_view\_result"

defaulttext\_editor\_code\_execution\_view\_result



BetaTextEditorCodeExecutionViewResultBlockParam object{ content, file\_type, type, 3 more }

content: string



file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

type: "text\_editor\_code\_execution\_view\_result"

num\_lines: optional number or null

start\_line: optional number or null

total\_lines: optional number or null



BetaThinkingBlock object{ signature, thinking, type }



signature: string

A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

thinking: string

The text of Claude's thinking process for this block.



type: "thinking"

defaultthinking



BetaThinkingBlockBinding object{ prefix\_mismatch\_behavior }

Controls for block binding: what happens when a thinking block this
request sends back fails the conversation check. Every field is optional;
an empty object means every default.



prefix\_mismatch\_behavior: optional [BetaThinkingPrefixMismatchBehavior](api/http/beta/messages.md) or null

What happens when a thinking block in `messages` fails the conversation
check: it was created in a different conversation, or the messages before
it have changed since. `"error"` (the default) fails the request with a
400 error. `"drop_block"` removes the failing blocks and the request
proceeds; the model no longer sees the dropped reasoning.

One of the following:

"error"

"drop\_block"



BetaThinkingBlockParam object{ signature, thinking, type }



signature: string

The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

thinking: string

The `thinking` text of this block as returned by the API.

type: "thinking"



BetaThinkingConfigAdaptive object{ type, block\_binding, display }

type: "adaptive"



block\_binding: optional [BetaThinkingBlockBinding](api/http/beta/messages.md) { prefix\_mismatch\_behavior } or null

Controls for block binding: what happens when a thinking block this
request sends back fails the conversation check. Every field is optional;
an empty object means every default.



prefix\_mismatch\_behavior: optional [BetaThinkingPrefixMismatchBehavior](api/http/beta/messages.md) or null

What happens when a thinking block in `messages` fails the conversation
check: it was created in a different conversation, or the messages before
it have changed since. `"error"` (the default) fails the request with a
400 error. `"drop_block"` removes the failing blocks and the request
proceeds; the model no longer sees the dropped reasoning.

One of the following:

"error"

"drop\_block"



display: optional "summarized" or "omitted" or "updates" or null

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"

"updates"



BetaThinkingConfigDisabled object{ type }

type: "disabled"



BetaThinkingConfigEnabled object{ budget\_tokens, type, block\_binding, display }



BetaThinkingConfigParam = [BetaThinkingConfigEnabled](api/http/beta/messages.md) { budget\_tokens, type, block\_binding, display } or [BetaThinkingConfigDisabled](api/http/beta/messages.md) { type } or [BetaThinkingConfigAdaptive](api/http/beta/messages.md) { type, block\_binding, display }

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

One of the following:



BetaThinkingDelta object{ estimated\_tokens, thinking, type }

estimated\_tokens: number or null

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

thinking: string

The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.



type: "thinking\_delta"

defaultthinking\_delta



BetaThinkingDroppedInputTransformation object{ path, reason, type }

path: string

Where the removed block was in your request, as `messages.{i}.content.{j}`:
`i` indexes the `messages` array you sent and `j` that message's `content`
array — the same form error messages use.



reason: "model\_binding\_mismatch" or "prefix\_binding\_mismatch" or "organization\_binding\_mismatch" or "end\_user\_binding\_mismatch"

Which binding check removed the block: `model_binding_mismatch` — it was
created by a model whose reasoning the requested model may not read;
`prefix_binding_mismatch` — the conversation before it differs from the
conversation it was created in (the rest of that turn's consecutive thinking
blocks are removed with it, each with this reason);
`organization_binding_mismatch` — it was created under a different
organization (an Anthropic organization, AWS account or Google Cloud project)
and this organization is not one of its additional organizations;
`end_user_binding_mismatch` — it was created for a different end user, or
was removed by the consumer-organization binding. A block that would fail
several checks reports one reason, in this order of precedence:
`organization_binding_mismatch`, `end_user_binding_mismatch`,
`model_binding_mismatch`, `prefix_binding_mismatch`.

One of the following:

"model\_binding\_mismatch"

"prefix\_binding\_mismatch"

"organization\_binding\_mismatch"

"end\_user\_binding\_mismatch"



type: "thinking\_dropped"

Always `thinking_dropped` for this entry type.

defaultthinking\_dropped



BetaThinkingPrefixMismatchBehavior = "error" or "drop\_block"

What happens when a thinking block in `messages` fails the conversation
check: it was created in a different conversation, or the messages before
it have changed since. `"error"` (the default) fails the request with a
400 error. `"drop_block"` removes the failing blocks and the request
proceeds; the model no longer sees the dropped reasoning.

One of the following:

"error"

"drop\_block"



BetaThinkingTurns object{ type, value }

type: "thinking\_turns"



value: number

minimum1



BetaTokenTaskBudget object{ total, type, remaining }

User-configurable total token budget across contexts.



total: number

Total token budget across all contexts in the session.

minimum1024

type: "tokens"

The budget type. Currently only 'tokens' is supported.



remaining: optional number or null

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

minimum0



BetaTool object{ input\_schema, name, allowed\_callers, 7 more }



BetaToolBash20241022 object{ name, type, allowed\_callers, 4 more }



BetaToolBash20250124 object{ name, type, allowed\_callers, 4 more }



BetaToolChangeMCPToolReference object{ name, server\_name, type }

Reference to a single MCP tool by its server and remote name — the
same `server_name`/`name` pair `mcp_tool_use` carries.

name: string

server\_name: string

type: "mcp\_tool\_reference"



BetaToolChangeMCPToolsetReference object{ server\_name, type }

Reference to every tool in the named MCP server's toolset.

server\_name: string

type: "mcp\_toolset\_reference"



BetaToolChangeToolReference object{ name, type }

Reference to a single tool the caller declared directly in
`tools[]`. Does not accept the composed `{server}_{name}` form the
server assigns to MCP-resolved tools — use `mcp_tool_reference` or
`mcp_toolset_reference` for those.



name: string

pattern^[a-zA-Z0-9\_-]{1,128}$

type: "tool\_reference"



BetaToolChoice = [BetaToolChoiceAuto](api/http/beta/messages.md) { type, disable\_parallel\_tool\_use } or [BetaToolChoiceAny](api/http/beta/messages.md) { type, disable\_parallel\_tool\_use } or [BetaToolChoiceTool](api/http/beta/messages.md) { name, type, disable\_parallel\_tool\_use } or [BetaToolChoiceNone](api/http/beta/messages.md) { type }

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



BetaToolChoiceAny object{ type, disable\_parallel\_tool\_use }

The model will use any available tools.

type: "any"



disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



BetaToolChoiceAuto object{ type, disable\_parallel\_tool\_use }

The model will automatically decide whether to use tools.

type: "auto"



disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



BetaToolChoiceNone object{ type }

The model will not be allowed to use tools.

type: "none"



BetaToolChoiceTool object{ name, type, disable\_parallel\_tool\_use }

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"



disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



BetaToolComputerUse20241022 object{ display\_height\_px, display\_width\_px, name, 7 more }



BetaToolComputerUse20250124 object{ display\_height\_px, display\_width\_px, name, 7 more }



BetaToolComputerUse20251124 object{ display\_height\_px, display\_width\_px, name, 8 more }



BetaToolReferenceBlock object{ tool\_name, type }



tool\_name: string

maxLength256

minLength1

pattern^[a-zA-Z0-9\_-]{1,256}$



type: "tool\_reference"

defaulttool\_reference



BetaToolReferenceBlockParam object{ tool\_name, type, cache\_control }

Tool reference block that can be included in tool\_result content.



tool\_name: string

maxLength256

minLength1

pattern^[a-zA-Z0-9\_-]{1,256}$

type: "tool\_reference"



cache\_control: optional [BetaCacheControlEphemeral](api/http/beta/messages.md) { type, ttl } or null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



BetaToolResultBlockParam object{ tool\_use\_id, type, cache\_control, 3 more }



BetaToolSearchToolBm25\_20251119 object{ name, type, allowed\_callers, 3 more }



BetaToolSearchToolRegex20251119 object{ name, type, allowed\_callers, 3 more }



BetaToolSearchToolResultBlock object{ content, tool\_use\_id, type }



BetaToolSearchToolResultBlockParam object{ content, tool\_use\_id, type, cache\_control }



BetaToolSearchToolResultError object{ error\_code, error\_message, type }



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string or null



type: "tool\_search\_tool\_result\_error"

defaulttool\_search\_tool\_result\_error



BetaToolSearchToolResultErrorParam object{ error\_code, type, error\_message }



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "tool\_search\_tool\_result\_error"

error\_message: optional string or null



BetaToolSearchToolSearchResultBlock object{ tool\_references, type }



tool\_references: array of [BetaToolReferenceBlock](api/http/beta/messages.md) { tool\_name, type }



tool\_name: string

maxLength256

minLength1

pattern^[a-zA-Z0-9\_-]{1,256}$



type: "tool\_reference"

defaulttool\_reference



type: "tool\_search\_tool\_search\_result"

defaulttool\_search\_tool\_search\_result



BetaToolSearchToolSearchResultBlockParam object{ tool\_references, type }



BetaToolTextEditor20241022 object{ name, type, allowed\_callers, 4 more }



BetaToolTextEditor20250124 object{ name, type, allowed\_callers, 4 more }



BetaToolTextEditor20250429 object{ name, type, allowed\_callers, 4 more }



BetaToolTextEditor20250728 object{ name, type, allowed\_callers, 5 more }



BetaToolUnion = [BetaTool](api/http/beta/messages.md) { input\_schema, name, allowed\_callers, 7 more } or [BetaToolBash20241022](api/http/beta/messages.md) { name, type, allowed\_callers, 4 more } or [BetaToolBash20250124](api/http/beta/messages.md) { name, type, allowed\_callers, 4 more } or 25 more

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

One of the following:



BetaToolUseBlock object{ id, input, name, 3 more }



BetaToolUseBlockParam object{ id, input, name, 4 more }



BetaToolUsesKeep object{ type, value }

type: "tool\_uses"



value: number

minimum0



BetaToolUsesTrigger object{ type, value }

type: "tool\_uses"



value: number

minimum1



BetaURLImageSource object{ type, url }

type: "url"

url: string



BetaURLPDFSource object{ type, url }

type: "url"

url: string



BetaUsage object{ cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 9 more }



BetaUserLocation object{ type, city, country, 2 more }

type: "approximate"



city: optional string or null

The city of the user.

maxLength255

minLength1



country: optional string or null

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2



region: optional string or null

The region of the user.

maxLength255

minLength1



timezone: optional string or null

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1



BetaWebFetchBlock object{ content, retrieved\_at, type, url }



content: [BetaDocumentBlock](api/http/beta/messages.md) { citations, source, title, type }

retrieved\_at: string or null

ISO 8601 timestamp when the content was retrieved



type: "web\_fetch\_result"

defaultweb\_fetch\_result

url: string

Fetched content URL



BetaWebFetchBlockParam object{ content, type, url, retrieved\_at }



content: [BetaRequestDocumentBlock](api/http/beta/messages.md) { source, type, cache\_control, 3 more }

type: "web\_fetch\_result"

url: string

Fetched content URL

retrieved\_at: optional string or null

ISO 8601 timestamp when the content was retrieved



BetaWebFetchTool20250910 object{ name, type, allowed\_callers, 8 more }



BetaWebFetchTool20260209 object{ name, type, allowed\_callers, 8 more }



BetaWebFetchTool20260309 object{ name, type, allowed\_callers, 9 more }

Web fetch tool with use\_cache parameter for bypassing cached content.



BetaWebFetchTool20260318 object{ name, type, allowed\_callers, 10 more }



BetaWebFetchToolResultBlock object{ content, tool\_use\_id, type, caller }



BetaWebFetchToolResultBlockParam object{ content, tool\_use\_id, type, 2 more }



BetaWebFetchToolResultErrorBlock object{ error\_code, type }



error\_code: [BetaWebFetchToolResultErrorCode](api/http/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"



type: "web\_fetch\_tool\_result\_error"

defaultweb\_fetch\_tool\_result\_error



BetaWebFetchToolResultErrorBlockParam object{ error\_code, type }



error\_code: [BetaWebFetchToolResultErrorCode](api/http/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



BetaWebFetchToolResultErrorCode = "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 6 more

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"



BetaWebSearchResultBlock object{ encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string or null

title: string



type: "web\_search\_result"

defaultweb\_search\_result

url: string



BetaWebSearchResultBlockParam object{ encrypted\_content, title, type, 2 more }

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string or null



BetaWebSearchTool20250305 object{ name, type, allowed\_callers, 7 more }



BetaWebSearchTool20260209 object{ name, type, allowed\_callers, 7 more }



BetaWebSearchTool20260318 object{ name, type, allowed\_callers, 8 more }



BetaWebSearchToolRequestError object{ error\_code, type }



error\_code: [BetaWebSearchToolResultErrorCode](api/http/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



BetaWebSearchToolResultBlock object{ content, tool\_use\_id, type, caller }



BetaWebSearchToolResultBlockContent = [BetaWebSearchToolResultError](api/http/beta/messages.md) { error\_code, type } or array of [BetaWebSearchResultBlock](api/http/beta/messages.md) { encrypted\_content, page\_age, title, 2 more }

One of the following:



BetaWebSearchToolResultBlockParam object{ content, tool\_use\_id, type, 2 more }



BetaWebSearchToolResultBlockParamContent = array of [BetaWebSearchResultBlockParam](api/http/beta/messages.md) { encrypted\_content, title, type, 2 more } or [BetaWebSearchToolRequestError](api/http/beta/messages.md) { error\_code, type }

One of the following:



BetaWebSearchToolResultError object{ error\_code, type }



error\_code: [BetaWebSearchToolResultErrorCode](api/http/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"



type: "web\_search\_tool\_result\_error"

defaultweb\_search\_tool\_result\_error



BetaWebSearchToolResultErrorCode = "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

#### Messages[Batches](api/http/beta/messages/batches.md)

##### [Create a Message Batch](api/http/beta/messages/batches/create.md)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/http/beta/messages/batches/retrieve.md)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/http/beta/messages/batches/list.md)

GET/v1/messages/batches

##### [Cancel a Message Batch](api/http/beta/messages/batches/cancel.md)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/http/beta/messages/batches/delete.md)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/http/beta/messages/batches/results.md)

GET/v1/messages/batches/{message\_batch\_id}/results

---

*Copyright © Anthropic. All rights reserved.*
