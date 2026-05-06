# Use WIF with SPIFFE

Copy page

SPIFFE assigns every workload a stable identity URI of the form `spiffe://<trust-domain>/<path>`, and SPIRE (the reference SPIFFE runtime) issues that identity as a JWT-SVID on demand through the Workload API. A JWT-SVID is an ordinary signed JWT whose `sub` claim is the workload's SPIFFE ID and whose `aud` claim is supplied by the workload at fetch time.

The bridge from a SPIRE trust domain to standard OIDC is the [SPIRE OIDC Discovery Provider](https://github.com/spiffe/spire/blob/main/support/oidc-discovery-provider/README.md), a standalone helper that publishes `/.well-known/openid-configuration` and a JWKS endpoint for the trust domain's JWT signing keys. With the discovery provider running, a JWT-SVID validates like any other OIDC token: register the discovery URL as a federation issuer, write a federation rule that matches the workload's SPIFFE ID, and have the workload present its JWT-SVID to Anthropic's token-exchange endpoint.

This page applies anywhere SPIRE Agent runs: Kubernetes pods, virtual machines, and bare-metal hosts.

If your Kubernetes cluster does not run SPIRE and you want to authenticate with the cluster's native projected service-account tokens instead, see [Use WIF with Kubernetes](manage-claude/wif-providers/kubernetes.md).

## Prerequisites

- Familiarity with [WIF concepts](manage-claude/workload-identity-federation.md): service accounts, federation issuers, and federation rules.
- A SPIRE deployment with SPIRE Server and SPIRE Agent running, and registration entries for the workloads that need to call the Claude API.
- The [SPIRE OIDC Discovery Provider](https://github.com/spiffe/spire/blob/main/support/oidc-discovery-provider/README.md) running with a publicly reachable HTTPS endpoint, or the JWKS exported for `inline` registration.
- SPIRE Server configured to set the `iss` claim on JWT-SVIDs (the `jwt_issuer` setting in the server config) to the same URL the OIDC Discovery Provider serves.
- JWT-SVIDs available to your workloads. WIF accepts JWT-SVIDs only; X.509-SVIDs are not used.
- Permission to create service accounts, federation issuers, and federation rules in the Claude Console for your Anthropic organization.

## Configure SPIRE

If you already run SPIRE with the OIDC Discovery Provider, federating with Anthropic requires three things on the SPIRE side: a `jwt_issuer` that matches the discovery URL, a registration entry for the workload that will call the Claude API, and a way for that workload to fetch a JWT-SVID with the Anthropic audience. The subsections below walk through each. The configuration snippets show only the settings relevant to Anthropic federation; they are not complete SPIRE deployment configs.

Setting up SPIRE for the first time? Deploy SPIRE Server and Agent following the [SPIRE quickstart](https://spiffe.io/docs/latest/try/), then add the [OIDC Discovery Provider](https://github.com/spiffe/spire/blob/main/support/oidc-discovery-provider/README.md) as a separate service alongside SPIRE Server. Discovery-mode federation depends on the provider being deployed and publicly reachable; it is not part of a default SPIRE install.

### Verify the JWT issuer

Anthropic validates a JWT-SVID by matching its `iss` claim against a registered federation issuer and fetching the JWKS from that issuer's discovery document. Two SPIRE settings must agree on the same URL: SPIRE Server's `jwt_issuer` (which becomes the `iss` claim in every minted JWT-SVID) and the OIDC Discovery Provider's `domains` list (which determines the host the discovery document and JWKS are served from). That shared URL is what you register with Anthropic.

The trust domain and the issuer URL are independent. The trust domain (`spiffe://prod.example.com`) scopes the `sub` claim; the issuer URL (`https://oidc-discovery.prod.example.com`) is where Anthropic fetches signing keys. They do not need to share a hostname.

Confirm `jwt_issuer` is set in SPIRE Server's configuration and points at the discovery provider's public URL. The example below also shows a default JWT-SVID lifetime; SPIRE's built-in default is five minutes, which is short enough that continuous rotation is required (see [Run spiffe-helper](#run-spiffe-helper)). Anthropic's token-exchange endpoint rejects identity tokens whose lifetime exceeds one hour. Keep `default_jwt_svid_ttl` (or any per-entry override) at one hour or less.

server.conf

```inline-block
server {
    trust_domain         = "prod.example.com"
    jwt_issuer           = "https://oidc-discovery.prod.example.com"
    default_jwt_svid_ttl = "5m"
    # ...
}
```

In the OIDC Discovery Provider's configuration, the same hostname must appear under `domains`, and the provider must be able to reach SPIRE Server's API socket. The provider serves the discovery document and JWKS over HTTPS; terminate TLS with its built-in ACME support or front it with a load balancer that does.

oidc-discovery-provider.conf

```inline-block
domains = ["oidc-discovery.prod.example.com"]

server_api {
    address = "unix:///run/spire/sockets/private/api.sock"
}

acme {
    email        = "platform@example.com"
    tos_accepted = true
}
```

### Register the workload

Each workload that calls the Claude API needs a SPIRE registration entry that maps its runtime selectors to a SPIFFE ID. If the workload is already registered, note its SPIFFE ID; you use it in the federation rule's `subject_prefix`. If not, register it. For a Kubernetes pod, the selectors are typically the namespace and Kubernetes service account:

CLI

```shiki
spire-server entry create \
    -spiffeID spiffe://prod.example.com/ns/inference/sa/worker \
    -parentID spiffe://prod.example.com/spire/agent/k8s_psat/prod-cluster/NODE_UID \
    -selector k8s:ns:inference \
    -selector k8s:sa:worker
```

The `parentID` shown is a single node's auto-generated agent ID. For cluster-wide registration, parent the entry to a [node alias](https://spiffe.io/docs/latest/deploying/registering/#node-aliasing) so it matches workloads on every node, as the [SPIRE Kubernetes quickstart](https://spiffe.io/docs/latest/try/getting-started-k8s/) does.

Workloads outside Kubernetes use host-level selectors such as `unix:uid:1000` (`unix:path` is also available but requires `discover_workload_path = true` in the agent's unix workload attestor configuration). Clusters running [spire-controller-manager](https://github.com/spiffe/spire-controller-manager) can declare entries with the `ClusterSPIFFEID` custom resource instead of calling `spire-server entry create` directly.

### Run spiffe-helper

[spiffe-helper](https://github.com/spiffe/spiffe-helper) is a sidecar utility that connects to the SPIRE Agent socket, fetches a JWT-SVID for a given audience, writes it to a file, and re-fetches it before expiry. The helper runs in daemon mode by default; the example below sets `daemon_mode = true` explicitly.

helper.conf

```inline-block
agent_address = "/run/spire/sockets/agent.sock"
cert_dir      = "/var/run/secrets/anthropic.com"
daemon_mode   = true

jwt_svids = [{
    jwt_audience       = "https://api.anthropic.com"
    jwt_svid_file_name = "token"
}]
```

In Kubernetes, run spiffe-helper as a sidecar container that shares a memory-backed `emptyDir` volume (`medium: Memory`) with your application container so the bearer SVID never lands on the node's disk. Mount the SPIRE Agent socket from the host into the sidecar, mount the shared volume at `/var/run/secrets/anthropic.com` in both containers, and set `ANTHROPIC_IDENTITY_TOKEN_FILE=/var/run/secrets/anthropic.com/token` on the application container. On VMs and bare metal, run spiffe-helper as a system service alongside the workload and point both at a shared directory.

## Configure Anthropic

Follow the [setup walkthrough](manage-claude/workload-identity-federation.md) to register a federation issuer, create an Anthropic service account, and create a federation rule in the Claude Console. Use these SPIFFE-specific values.

**Federation issuer:** Register the OIDC Discovery Provider's public URL in `discovery` mode. Anthropic fetches `/.well-known/openid-configuration` from this URL and follows the returned `jwks_uri` to retrieve the trust domain's signing keys.

```shiki
{
  "name": "spire-prod",
  "issuer_url": "https://oidc-discovery.prod.example.com",
  "jwks_source": "discovery"
}
```

If the discovery provider is not reachable from the public internet, fetch the JWKS yourself (`curl https://oidc-discovery.prod.example.com/keys`) and register the issuer with `"jwks_source": "inline"` and the contents of the returned `keys` array. In `inline` mode the `issuer_url` is only compared against the JWT-SVID's `iss` claim; Anthropic never attempts to reach it.

SPIRE rotates JWT signing keys frequently. If you register the issuer with an inline JWKS instead of a discovery URL, you must update the JWKS every time SPIRE rotates: add the new key before workloads start presenting it, and **remove superseded keys** once tokens signed with them have expired. Stale keys left in an inline JWKS remain trusted indefinitely.

**Federation rule:** Match the JWT-SVID's `sub` (the SPIFFE ID) and the `aud` you configured spiffe-helper to request. SPIFFE IDs are URI strings and `subject_prefix` matches them as opaque text, so an exact value or a trailing-`*` prefix match both work against them. For more complex patterns, use a CEL `condition`.

```shiki
{
  "name": "spire-inference-worker",
  "issuer_id": "fdis_...",
  "match": {
    "subject_prefix": "spiffe://prod.example.com/ns/inference/sa/worker",
    "audience": "https://api.anthropic.com"
  },
  "target": {
    "type": "service_account",
    "service_account_id": "svac_..."
  },
  "workspace_id": "wrkspc_...",
  "oauth_scope": "workspace:developer",
  "token_lifetime_seconds": 600
}
```

Be as specific as the workload allows. Loosen `subject_prefix` to `spiffe://prod.example.com/ns/inference/*` only if every workload registered under that path should map to the same Anthropic service account. Add the rule's `fdrl_...` ID to the workload's `ANTHROPIC_FEDERATION_RULE_ID` environment variable.

## Acquire and use the token

The Anthropic SDKs can either read the JWT-SVID from the file that spiffe-helper maintains or call the SPIFFE Workload API directly through a token-provider callable. The file path is the simplest integration and works in every SDK language; the callable path removes the sidecar but requires a SPIFFE Workload API client in your application's language.

File-based with spiffe-helper

File-based with spiffe-helper

Callable via the SPIFFE Workload API

Callable via the SPIFFE Workload API

With spiffe-helper writing a fresh JWT-SVID to `/var/run/secrets/anthropic.com/token`, set `ANTHROPIC_IDENTITY_TOKEN_FILE` to that path along with `ANTHROPIC_FEDERATION_RULE_ID`, `ANTHROPIC_ORGANIZATION_ID`, `ANTHROPIC_SERVICE_ACCOUNT_ID`, and `ANTHROPIC_WORKSPACE_ID`. The SDK reads the file on every token exchange, so it always picks up the most recently rotated SVID, and refreshes the Anthropic access token automatically before it expires.

cURLPythonTypeScriptGoJavaC#CLIPHPRuby

```shiki
import anthropic

# Reads the JWT-SVID that spiffe-helper writes to
# ANTHROPIC_IDENTITY_TOKEN_FILE, plus ANTHROPIC_FEDERATION_RULE_ID,
# ANTHROPIC_ORGANIZATION_ID, ANTHROPIC_SERVICE_ACCOUNT_ID, and ANTHROPIC_WORKSPACE_ID.
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(message.content[0].text)
```

## Verify the setup

Before wiring the SDK in, fetch a JWT-SVID directly from SPIRE Agent and confirm the claims match what your federation rule expects:

CLI

```shiki
spire-agent api fetch jwt \
    -audience https://api.anthropic.com \
    -socketPath /run/spire/sockets/agent.sock
```

`spire-agent api fetch jwt` prints a labeled block, not a bare JWT, so extract the token line before decoding it: pipe the output through `awk '/^[[:space:]]*eyJ/{print $1; exit}' | jq -rR 'split(".")[1] | gsub("-";"+") | gsub("_";"/") | @base64d | fromjson'`. Check that `iss` is the OIDC Discovery Provider URL you registered, `sub` is the workload's SPIFFE ID, and `aud` contains `https://api.anthropic.com`. Then run the cURL example from [Acquire and use the token](#acquire-and-use-the-token); a successful exchange returns an `access_token` beginning with `sk-ant-oat01-`. On `400 invalid_grant`, see [Troubleshoot a failed exchange](manage-claude/wif-reference.md); the most common SPIRE-side cause is a mismatch between SPIRE Server's `jwt_issuer` and the URL registered as the federation issuer.

## Scope your rule

SPIFFE ID path conventions are operator-defined, so the federation rule's `subject_prefix` matcher should reflect the path scheme your registration entries use. Common schemes include `spiffe://<trust-domain>/ns/<namespace>/sa/<service-account>` (the default emitted by the Kubernetes workload registrar and `ClusterSPIFFEID`) and `spiffe://<trust-domain>/host/<hostname>/<service>` for VM and bare-metal workloads.

A `subject_prefix` of `spiffe://prod.example.com/*` matches every workload in the trust domain. Without an `audience` matcher, the rule also accepts JWT-SVIDs minted for any audience, including ones the workload requested for unrelated relying parties.

Lock the rule's `match` block to the narrowest scope that fits your use case:

- **Pin to one workload:** Set `subject_prefix` to the full SPIFFE ID with no trailing `*`.
- **Always set an audience:** Require `audience` on the rule and configure spiffe-helper (or the Workload API call) with the same value so SVIDs minted for other relying parties are rejected.
- **Scope by path segment:** Use `spiffe://prod.example.com/ns/inference/*` to grant every workload registered under a namespace, and create a separate rule and Anthropic service account per namespace rather than widening one rule.
- **One issuer per trust domain:** Each SPIRE trust domain has its own signing keys and OIDC Discovery Provider. Register each as a separate federation issuer and bind rules to the issuer that owns the SPIFFE IDs they match.

## Next steps

- [Workload Identity Federation](manage-claude/workload-identity-federation.md): concepts, the token-exchange flow, and SDK configuration options.
- [WIF reference](manage-claude/wif-reference.md): environment variables, JWKS source modes, and rule match modes.
- [Use WIF with Kubernetes](manage-claude/wif-providers/kubernetes.md): for clusters that use native projected service-account tokens instead of SPIRE.

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
