# SDK middleware

Copy page



The Anthropic SDKs provide a middleware (or interceptor) hook that lets you run code before a request is sent and after the response is received. Use middleware for cross-cutting concerns such as logging, custom retries, request annotation, and refusal fallback handling.

Claude APISDK coreMiddleware BMiddleware AYour codeClaude APISDK coreMiddleware BMiddleware AYour coderequest1next(request)2next(request)3HTTP request4HTTP response5response6response7response8

Each middleware can inspect or replace the request before calling `next()`, and the response after `next()` returns.

##  Registering middleware

Each middleware is a function that receives the outgoing request and a `next` callable. Call `next` to forward the request to the rest of the chain (or directly to the SDK core if this is the last middleware), and return its response. Anything before the `next` call runs on the way out; anything after runs on the way back.

PythonTypeScriptC#GoJavaPHPRuby



```shiki
def logging_middleware(request: APIRequest, call_next: CallNext) -> APIResponse[Any]:
    # Before the request
    print(f"-> {request.method} {request.url}")

    # Forward the request to the rest of the chain
    response = call_next(request)

    # After the request
    print(f"<- {response.status_code}")

    return response

client = Anthropic(middleware=[logging_middleware])
```

##  Middleware ordering

When you register multiple middleware, they apply in the order given: the first middleware's "before" code runs first, and its "after" code runs last. Middleware registered on the client runs before middleware passed as a per-request option.

In the Go SDK, repeated `option.WithMiddleware` calls concatenate (client first, then method). In the other SDKs, pass an array; later entries wrap inner.

##  Replacing the HTTP client

Each SDK also accepts a custom HTTP client (for proxy configuration, custom TLS, or connection pooling). Only one HTTP client is used per SDK client; setting it replaces the default. The custom HTTP client receives requests after all middleware has run.

##  Built-in middleware

The SDKs ship a refusal-fallback middleware that automatically retries requests Claude Fable 5 declines on a fallback model. See [Detect and retry on a fallback model](build-with-claude/refusals-and-fallback.md) for setup and per-language examples.

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
