# Cloud sandbox reference

Copy page



Cloud sandboxes run as isolated Linux containers on Anthropic-managed infrastructure. They come pre-installed with a comprehensive set of programming languages, databases, and utilities. The agent can use these immediately without any installation steps.

These specifications apply to `cloud` environments. Self-hosted sandboxes run on your infrastructure with whatever your worker provides.

##  Programming languages

| Language | Version | Package manager |
| --- | --- | --- |
| Python | 3.12+ | pip, uv |
| Node.js | 20+ | npm, yarn, pnpm |
| Go | 1.22+ | go modules |
| Rust | 1.77+ | cargo |
| Java | 21+ | maven, gradle |
| Ruby | 3.3+ | bundler, gem |
| PHP | 8.3+ | composer |
| C/C++ | GCC 13+ | make, cmake |

##  Databases

| Database | Description |
| --- | --- |
| SQLite | Pre-installed, available immediately |
| PostgreSQL client | `psql` client for connecting to external databases |
| Redis client | `redis-cli` for connecting to external instances |

##  Utilities

###  System tools

- `git` - Version control
- `curl`, `wget` - HTTP clients
- `jq` - JSON processing
- `tar`, `zip`, `unzip` - Archive tools
- `ssh`, `scp` - Remote access (requires a networking mode that allows the destination host)
- `tmux`, `screen` - Terminal multiplexers

###  Development tools

- `make`, `cmake` - Build systems
- `docker` - Container management (limited availability)
- `ripgrep` (`rg`) - Fast file search
- `tree` - Directory visualization
- `htop` - Process monitoring

###  Text processing

- `sed`, `awk`, `grep` - Stream editors
- `vim`, `nano` - Text editors
- `diff`, `patch` - File comparison

##  Sandbox specifications

| Property | Value |
| --- | --- |
| Operating system | Ubuntu 22.04 LTS |
| Architecture | x86\_64 (amd64) |
| Memory | Up to 8 GB |
| Disk space | Up to 10 GB |
| Network | API-created environments default to [`unrestricted` networking](managed-agents/environments.md); sandboxes provisioned through Claude Studio default to `limited` |

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
