# Sandboxing & Data Protection for AI Coding Agents

## A Practitioner's Guide for Economists

**Emily Beam, University of Vermont**
**May 22, 2026**

> This brief provides sourced, actionable guidance on protecting sensitive research data when using AI coding agents. It covers Claude Code, Codex CLI, Cursor, and GitHub Copilot. Every factual claim is cited to official documentation or verifiable independent analysis. Tools change fast — treat this as accurate to its date stamp and verify current documentation before relying on specific configuration details.

---

## Table of Contents

0. [Quick Answers to the Questions You Came Here With](#0-quick-answers-to-the-questions-you-came-here-with)
1. [Introduction & Threat Model](#1-introduction--threat-model)
2. [Taxonomy of Protections](#2-taxonomy-of-protections)
3. [Tool Profiles](#3-tool-profiles)
   - [3.1 Claude Code (Anthropic)](#31-claude-code-anthropic)
   - [3.2 Codex CLI (OpenAI)](#32-codex-cli-openai)
   - [3.3 Cursor (Anysphere)](#33-cursor-anysphere)
   - [3.4 GitHub Copilot (GitHub/Microsoft)](#34-github-copilot-githubmicrosoft)
4. [Economist Use Cases](#4-economist-use-cases)
5. [Practical Checklists](#5-practical-checklists)
6. [Sources & Further Reading](#6-sources--further-reading)

---

## 0. Quick Answers to the Questions You Came Here With

Before diving into the full taxonomy, here are direct answers to the questions economists most commonly ask.

### "Is my code being used to train the AI?"

It depends on your provider and plan tier. Here is the complete picture as of May 2026:

| Tool | Personal/Free plans | Business/Enterprise plans |
|------|-------------------|--------------------------|
| **Claude Code** (Anthropic) | **No** by default. Opt-in only. | **No.** Not used for training. |
| **Codex CLI** (OpenAI) | **It depends on how you log in.** API key = no. ChatGPT personal login = **yes by default**. The default login flow is ChatGPT, so most individual users are opted in without realizing it. | **No.** Contractually excluded. |
| **Cursor** (Anysphere) | **Yes**, unless Privacy Mode is enabled. With Privacy Mode off, Cursor "may use and store codebase data, prompts, editor actions, code snippets, and other code data to improve AI features and train models." | **No**, if Privacy Mode is enforced (default for team/enterprise). |
| **GitHub Copilot** (Microsoft) | **Yes, by default** since April 24, 2026. Must actively opt out at Settings > Copilot > Features. | **No.** Contractually excluded. |

**The bottom line:** If you are on a paid commercial/enterprise plan from any provider, your data is not used for training. If you are on a personal or free plan, the defaults vary — and two of the four tools (Copilot and Codex via ChatGPT login) opt you *in* by default.

### "But if it's not used for training, my data stays private — right?"

**No.** This is the most common misconception, and it matters enormously for researchers with sensitive data.

"Not used for training" means the provider commits not to incorporate your inputs into future model weights. It does **not** mean your data never leaves your machine. Here is what actually happens during a normal session with *any* of these tools:

1. **You open a file.** The AI tool reads it into its context window.
2. **The file contents are transmitted** over TLS to the provider's servers for model inference. Every file the tool reads — code, data dictionaries, config files, even datasets if you let it — becomes part of an API request.
3. **The provider processes your data** on their servers, generates a response, and sends it back.
4. **The provider retains your data** for some period — typically 30 days for abuse monitoring, even on commercial plans. With Zero Data Retention (ZDR, available on enterprise tiers), data is not stored after inference, but ZDR is not available on standard plans and has its own caveats (see [Section 2, Layer 3](#layer-3-data-transmission-and-cloud-protections)).
5. **A copy is saved locally** on your machine as an unencrypted session transcript. All four tools do this by default.

**"Not used for training" ≠ "never leaves your machine."** If your IRB protocol or data use agreement requires that data not be transmitted to third-party servers, a no-training guarantee is insufficient. You need to ensure the data is never *read into the tool's context* in the first place.

### "What's the simplest way to keep sensitive data completely safe?"

**Put it on a separate drive and unmount it during AI sessions.**

This sounds low-tech, but it is the strongest practical protection available — stronger than any sandbox configuration, privacy mode, or enterprise plan. A USB drive or external SSD that is physically unmounted (ejected) from your machine cannot be read by any software, regardless of bugs, misconfigurations, or exploits. It is the only protection in this brief that is truly **architecturally guaranteed** with zero configuration required.

The tradeoff is workflow friction: you mount the drive when doing data work, unmount it when using AI tools, and never do both simultaneously. For researchers with serious IRB obligations, that 10-second step buys more assurance than any amount of software configuration.

Other options in decreasing order of strength:
- **Encrypted disk image** (macOS Disk Utility or VeraCrypt): mount only when needed, unmount before AI sessions. Same principle as a physical drive, without the dongle.
- **Separate machine**: keep data on a machine that never runs AI tools. Work on code on your AI-enabled machine; copy results (not data) between them.
- **Virtual machine**: run the AI inside a VM that can only see the code directory. Data stays on the host, invisible to the VM.
- **Docker container**: mount only the code directory. Less isolation than a VM (shared kernel), but effective against application-level access.
- **Tool-native sandbox** (Claude Code `denyRead`, Codex `workspace-write`): blocks tool access to specific paths. Kernel-enforced when the sandbox is enabled, but requires correct configuration and doesn't protect against all attack vectors.

The rest of this brief covers these options in detail, with specific configuration guidance for each tool.

---

## 1. Introduction & Threat Model

Economists increasingly use AI coding agents — tools like Claude Code, Codex CLI, Cursor, and GitHub Copilot — to write Stata code, clean data, build replication packages, and analyze results. These tools are genuinely useful. They are also, by design, pieces of software that read your files, execute commands on your machine, and transmit information to cloud servers.

This matters because economists routinely work with sensitive data on the same machines where they run these tools. IRB-protected survey microdata. Administrative records obtained under data use agreements. Student records governed by FERPA. Pre-publication results that represent years of fieldwork. The obligations attached to this data are real: IRB protocols, data use agreements, and institutional policies all require researchers to articulate what protections are in place and to demonstrate that access is appropriately controlled.

The problem is not that AI coding agents are uniquely dangerous. The problem is that they are new, their security models are poorly understood by most users, and the gap between "what a tool typically does" and "what a tool is guaranteed to do" is wider than most researchers realize.

### Four threat categories

This brief organizes data protection concerns around four threats:

1. **Unauthorized local reads.** The AI accesses files on your machine that you did not intend to share — credential files, datasets in adjacent directories, `.env` files with API keys. Every tool profiled here can, by default, read files beyond the immediate project directory. This is not a bug; it is how they build context for useful suggestions.

2. **Cloud exfiltration.** File contents, prompts, or code are transmitted to the provider's servers as part of normal operation. All four tools require cloud inference — none runs a model locally. Any file the tool reads into its context window is sent over the network. The question is not *whether* data leaves your machine, but *how much* and *under what retention policies*.

3. **Integrity risk.** The AI modifies or deletes files unexpectedly. Agent-mode tools can edit files and execute shell commands. A hallucinated `rm` command or a malformed file write can destroy work. Permission systems mitigate this, but their enforcement varies.

4. **Provider-side exposure.** Data transmitted to provider servers could be accessed by third parties, retained beyond the session, or used for model training. Privacy policies differ by provider, plan tier, and authentication method — sometimes in ways that are easy to miss.

These four threats map to three layers of protection, which form the taxonomy in the next section.

---

## 2. Taxonomy of Protections

Protections against the threats above operate at three layers, from closest to the AI tool outward to the operating system and network.

### Layer 1: Tool-native controls

Every AI coding agent ships with some form of permission system. These are application-level controls: the tool's own code decides whether to ask before reading a file, executing a command, or sending data to the server.

**Permission prompts and approval modes.** All four tools offer some version of "ask before acting." Claude Code and Codex CLI have the most granular models, with distinct modes ranging from read-only to fully autonomous. Cursor offers an allowlist model for terminal commands plus several protection toggles. Copilot's agent mode applies file edits automatically by default, requiring confirmation only for terminal commands.

**Configuration files.** Claude Code uses `settings.json` with allow/deny/ask rule arrays. Codex CLI uses `config.toml` with sandbox modes and environment filtering. Cursor uses `.cursorignore` (best-effort file exclusion) and `sandbox.json` (network restrictions). Copilot uses content exclusions (organization-level) and `.copilotignore`.

**Audit and logging.** All tools store session transcripts locally. Claude Code stores plaintext JSONL at `~/.claude/projects/`. Codex CLI stores JSONL at `~/.codex/sessions/`. These logs contain full conversation history including any file contents read into context. None encrypts these logs by default.

**Limitation.** Tool-native controls are enforced by the tool's own code, not by the operating system. If the tool has a bug, if a malicious project file overrides configuration, or if a spawned subprocess accesses files directly, application-level controls can be bypassed. Multiple CVEs across all four tools in 2025–2026 demonstrate this is not hypothetical.

### Layer 2: Operating system and environment sandboxing

OS-level protections are enforced by the kernel. A process cannot bypass them without a kernel exploit — a fundamentally harder attack than exploiting an application bug.

**Unix file permissions.** The most basic protection: files with `chmod 600` are readable only by their owner. But an AI agent running as *your* user inherits all your file permissions. Permissions only help if the agent runs as a different user, or if you proactively restrict permissions on sensitive files. Many credential files (`~/.aws/credentials`, `~/.ssh/config`) default to overly permissive modes.[^acl]

**macOS TCC (Transparency, Consent, and Control).** TCC protects Desktop, Documents, and Downloads folders behind permission prompts. However, TCC attributes all Terminal commands to the Terminal application itself. If your Terminal has Full Disk Access, every CLI tool — including AI agents — inherits that access. There is no per-command granularity.[^tcc]

**Seatbelt (sandbox-exec).** macOS's command-line sandboxing framework, using the kernel's TrustedBSD MAC layer. This is what Claude Code and Codex CLI use on macOS for filesystem and network restrictions. Kernel-enforced — child processes cannot escape the profile. Officially deprecated since ~2016 but still used by Apple internally, Anthropic, OpenAI, and Google Chrome. No replacement exists for CLI sandboxing.[^seatbelt]

**Docker containers.** Linux namespace and cgroup isolation provides a separate filesystem, process tree, and (optionally) network stack. The container sees only what you explicitly mount into it. Strong isolation *if configured correctly* — but bind-mounting your home directory defeats the purpose. The shared kernel is the fundamental weakness compared to VMs. Docker Sandboxes (2025–2026) address this by running each agent in a microVM with its own kernel and Docker daemon.[^docker]

**Virtual machines.** The strongest readily available isolation. Each VM runs its own kernel behind a hypervisor boundary. A compromise inside the VM cannot reach the host without a hypervisor exploit — rare and high-value. Practical options on macOS include UTM (free, open source), Parallels ($100/year, best toolchain integration), and Lima (free, Linux guests only).[^vm]

### Layer 3: Data transmission and cloud protections

Once data leaves your machine, protections depend on provider policies, contractual commitments, and encryption.

**What leaves the machine.** For all four tools, every file read into the AI's context window is transmitted to the provider's servers for inference. There is no local inference option for any of the tools profiled here. Prompts, file contents, command outputs, and file paths are all sent. Telemetry (usage metrics) is sent by default for all tools, though it can be disabled.

**Provider retention policies.** Retention periods range from "discarded after inference" (with Zero Data Retention agreements) to 30 days (standard API retention) to 2 years (telemetry/engagement data). The specifics vary by provider and plan tier — see the tool profiles below.

**Training data usage.** This is the question researchers most often ask. The answer depends on the provider *and* the plan:

| Provider | Personal/Free plans | Business/Enterprise plans |
|----------|-------------------|--------------------------|
| **Anthropic** (Claude Code) | Opt-in; off by default | Not used for training by default |
| **OpenAI** (Codex CLI) | Depends on auth method — ChatGPT login opts in by default; API key opts out | Not used for training |
| **Anysphere** (Cursor) | May be used unless Privacy Mode is on | Privacy Mode enforced; ZDR agreements with providers |
| **GitHub** (Copilot) | Used by default since April 2026; opt-out available | Contractually excluded |

**Zero Data Retention (ZDR).** Available on enterprise tiers from Anthropic, OpenAI, and via Cursor's provider agreements. ZDR means prompts and responses are not stored after inference. Important caveats: ZDR typically does not cover local transcript caches, telemetry metadata, or data flagged for safety review. Anthropic's ZDR permits retention for up to 2 years for policy violation investigations.[^zdr-anthropic]

### The guarantee spectrum

Not all protections are created equal. Throughout this brief, protections are classified at three levels:

| Level | Definition | Enforcement | Example |
|-------|-----------|-------------|---------|
| **Architecturally guaranteed** | Cannot be overridden by user action, misconfiguration, or application bugs. Enforced by the OS kernel, hypervisor, or network architecture. | Kernel syscall checks, hypervisor memory isolation, hardware separation | VM filesystem isolation; Docker namespace separation; Unix permission enforcement across UIDs |
| **Configurable protection** | User can enable a protection via settings. Enforced by the tool or OS as long as configuration is correct. Can be weakened by misconfiguration, software bugs, or social engineering. | Configuration files, permission settings, sandbox profiles | Claude Code `denyRead` rules; Codex sandbox mode; Docker bind mount scope; `chmod 600` on credential files |
| **Conventional behavior** | Default behavior under normal use. Relies on software functioning as documented. Could be overridden by bugs, prompt injection, malicious project files, or edge cases. | Software defaults, behavioral norms, application-layer checks | Tool-native permission prompts; `.cursorignore` exclusions; Copilot content exclusions in non-agent modes |

The most common mistake researchers make is treating conventional behavior as a guarantee. "The tool doesn't read files outside my project" is a description of typical behavior, not a security property. The sections below are explicit about which level applies to each protection.

---

## 3. Tool Profiles

### 3.1 Claude Code (Anthropic)

**Architecture.** Claude Code is a local CLI tool. All file I/O and shell execution happen on your machine as a user-level process with your filesystem permissions. There is no local model — every prompt and every file read into context is sent over TLS to Anthropic's API (or to AWS Bedrock / Google Vertex if configured) for inference. Responses stream back and the tool acts on them locally. Session transcripts are cached in plaintext at `~/.claude/projects/` for 30 days by default.[^cc-arch]

**Default permission model.** Read access is unrestricted by default — Claude Code can read any file on your filesystem without prompting, including `~/.aws/credentials`, `~/.ssh/`, and `.env` files.[^cc-sandbox] Write access is confined to the working directory. Bash commands require per-use approval, with a built-in set of read-only commands (ls, cat, grep, git status, etc.) pre-approved. Network requests require approval. Six permission modes range from `plan` (read-only) to `bypassPermissions` (no prompts).[^cc-perms]

**Configuration options.** Four settings layers (managed > user > project shared > project local) control permissions via allow/deny/ask rule arrays in `settings.json`. Rules use glob patterns; deny always wins. The sandbox provides OS-level enforcement beyond permission rules:

- macOS: Seatbelt (kernel-enforced filesystem and network restrictions)
- Linux: bubblewrap + socat (namespace isolation + network proxy)

Sandbox configuration supports `denyRead`, `denyWrite`, `allowRead`, `allowWrite` for filesystem paths, plus domain-level network allowlisting via a localhost proxy. CLAUDE.md shapes model behavior but is *not* a security boundary — only permission rules and sandbox settings enforce access control.[^cc-perms]

**Data transmission.** Every file Claude Code reads becomes part of the API request sent to Anthropic's servers. Telemetry (latency/reliability metrics, no code or file paths) and Sentry error reporting are on by default for Anthropic API users but can be disabled via environment variables (`DISABLE_TELEMETRY=1`, `DISABLE_ERROR_REPORTING=1`). When using Bedrock or Vertex, telemetry defaults to off.[^cc-data]

**Privacy commitments.** Commercial plans (Team, Enterprise, API): not trained on by default; 30-day retention. Consumer plans (Free, Pro, Max): training is opt-in; 30 days retention if opted out. Zero Data Retention available on Enterprise — prompts and responses not stored after inference, though local transcripts remain and Anthropic may retain data up to 2 years for policy violation investigations. Certifications: SOC 2 Type II, ISO 27001, ISO 42001.[^cc-privacy]

**Known gaps.**

- **File contents always leave your machine.** There is no local inference option. If Claude reads a dataset, its contents are transmitted to Anthropic's servers.[^cc-data]
- **Default read access is unrestricted.** Credential files, SSH keys, and data files in any directory are readable unless you add explicit `denyRead` sandbox rules.[^cc-sandbox]
- **Permission deny rules don't cover subprocess file access.** A Python script Claude spawns can read any file; only the OS-level sandbox blocks indirect access.[^cc-perms]
- **Local transcripts are unencrypted plaintext.** Full conversation history (including file contents) stored at `~/.claude/projects/` — discoverable even with server-side ZDR.[^cc-transcript]
- **Network sandbox doesn't inspect TLS.** Domain fronting could bypass allowlists; Anthropic acknowledges this limitation.[^cc-network]
- **Four patched CVEs in 2025–2026.** Including RCE via malicious project config files (CVE-2025-59536), API key exfiltration via base URL override (CVE-2026-21852), deny-rule bypass at >50 subcommands, and a SOCKS5 null-byte sandbox escape active for ~5.5 months.[^cc-cves]
- **Prompt injection from cloned repos** remains an active, unresolved threat class.[^cc-injection]

**Guarantee classification for Claude Code:**

| Protection | Level |
|-----------|-------|
| Seatbelt sandbox filesystem/network enforcement | Architecturally guaranteed (kernel MAC) |
| `denyRead`/`denyWrite` sandbox rules | Configurable (depends on correct configuration) |
| Permission prompt system (allow/deny/ask) | Conventional (application-layer; bypassable by subprocess) |
| CLAUDE.md behavioral instructions | Conventional (model compliance; not enforced) |

### 3.2 Codex CLI (OpenAI)

**Architecture.** Codex CLI runs locally — all file operations and code execution happen on your machine. Model inference happens on OpenAI's servers via API. The CLI was rewritten from TypeScript to Rust (the `codex-rs` crate) and is open source at github.com/openai/codex. A critical architectural detail: the Codex CLI *main process* runs without sandboxing. Only the AI-executed shell commands are confined by the sandbox. The main process has full user-level access to credentials and the filesystem.[^codex-arch]

**Default permission model.** Codex CLI is the only major agent with **sandbox on by default**. Three sandbox modes control what spawned commands can do:

| Sandbox mode | Filesystem | Network |
|---|---|---|
| `read-only` | Read only; edits need approval | Blocked |
| `workspace-write` (default) | Read/write within project directory | Blocked by default |
| `danger-full-access` | Unrestricted | Unrestricted |

Three approval modes (Auto, Read-only, Full Access) control when user confirmation is required. Auto mode (default for git-tracked directories) allows reads and edits within the working directory, asking before touching anything outside scope or using the network. `.git/` and `.codex/` directories are automatically read-only, preventing the AI from modifying git hooks or sandbox configuration.[^codex-perms]

**Configuration options.** Configuration files follow a precedence chain: CLI flags > named profiles > project config (`.codex/config.toml`, trusted projects only) > user config (`~/.codex/config.toml`) > system config > built-in defaults. Key capabilities:

- **Shell environment filtering**: automatically strips variables containing KEY, SECRET, or TOKEN from spawned processes. Configurable via `[shell_environment_policy]` with `inherit = "none"` option.[^codex-config]
- **Network allowlisting**: domain-level control with deny overriding allow. Blocks loopback, link-local, and private destinations by default. DNS rebinding checks reject suspicious lookups.[^codex-network]
- **History control**: `[history] persistence = "none"` disables local transcript storage entirely.[^codex-config]
- **Writable roots**: grant write access to specific additional directories without removing sandbox protections.[^codex-config]

**Data transmission.** Files read by the agent during a session are sent to OpenAI's servers as model context. The full codebase is not uploaded — only portions the agent reads. Session transcripts are stored locally as unencrypted JSONL at `~/.codex/sessions/`. Telemetry (feature usage, model names, app version — no code or PII) is enabled by default; disable via `[analytics] enabled = false`. Files listed in `.gitignore` are not included when referenced via `@`, but workspace commands (grep, cat) can still read ignored files and their contents may enter model context.[^codex-data]

**Privacy commitments.** The central policy: "data sent to the OpenAI API is not used to train or improve OpenAI models" unless you opt in (since March 2023).[^openai-data] However, this depends on authentication method:

| Auth method | Training default |
|---|---|
| **API key** | Opted OUT by default |
| **ChatGPT personal login** | Opted IN by default (can opt out in Settings > Data Controls) |
| **ChatGPT Enterprise/Team** | Opted OUT by default |

This is a critical distinction. The default authentication flow for Codex CLI is ChatGPT sign-in, which opts personal users into training data contribution. Researchers must use API key authentication or explicitly opt out.[^codex-auth]

Default retention: 30 days for abuse monitoring. ZDR available by prior approval for qualifying customers — not all endpoints are eligible. Safety retention exception: OpenAI may retain content from certain models if classifiers detect policy violations. Certifications: SOC 2 Type 2, ISO 27001, ISO 27701. Data residency available (US, EU, AU, CA, JP, and others) with 10% pricing uplift.[^openai-data]

**Known gaps.**

- **The main process is unconfined.** Only spawned tool commands run in the sandbox. The Codex process itself has full user-level filesystem and credential access. An independent analysis concludes it is "unsuitable for handling secrets, proprietary code, or PII without explicit infrastructure isolation."[^codex-safehouse]
- **`.gitignore` does not prevent file content transmission.** Workspace commands can read ignored files and their contents may end up in model context.[^codex-gitignore]
- **CVE-2025-59532** (CVSS 8.6): model-generated working directory paths could override sandbox boundaries, enabling arbitrary file writes outside the user's folder. Fixed in v0.39.0.[^codex-cve1]
- **CVE-2025-61260** (CVSS 9.8): malicious `.env` + `.codex/config.toml` in a cloned repository could execute arbitrary commands without approval. Fixed in v0.23.0.[^codex-cve2]
- **GitHub token exfiltration** via unsanitized branch names in the cloud container. Patched February 2026.[^codex-cve3]
- **ChatGPT sign-in default enables training.** Easy to miss — the default auth flow opts users in.[^codex-auth]
- **Telemetry is opt-out, not opt-in.** OpenAI declined community requests to change this.[^codex-telemetry]
- **Session transcripts stored unencrypted** at `~/.codex/` — full conversation history including file contents.[^codex-transcripts]

**Guarantee classification for Codex CLI:**

| Protection | Level |
|-----------|-------|
| Seatbelt/Landlock/seccomp sandbox for spawned commands | Architecturally guaranteed (kernel enforcement) |
| Network disabled by default | Configurable (can be overridden to `danger-full-access`) |
| Shell environment variable filtering | Configurable (must be explicitly set to `inherit = "none"` for maximum protection) |
| Approval prompts in Auto mode | Conventional (application-layer checks) |
| `.gitignore` excluding files from `@` references | Conventional (bypassed by workspace commands) |

### 3.3 Cursor (Anysphere)

**Architecture.** Cursor is a fork of VS Code's open-source codebase — not an extension. As a fork, Anysphere has deep access to the editor's rendering, filesystem, and extension host. All AI requests route through Cursor's AWS infrastructure, even when the user supplies their own API key. There is no direct-to-provider routing. Background Agents run in isolated Docker containers on AWS VMs (cloud, not local). No on-premise or VPC deployment exists.[^cursor-arch]

**Default permission model.** File reading requires no permission — the agent can read any file the OS user can access, including outside the workspace. File writes are workspace-scoped. Terminal commands operate under one of three modes: Allowlist (default; pre-approved command prefixes run automatically, everything else requires approval), Allowlist with Sandbox (unapproved commands auto-run inside an OS-level sandbox), or Run Everything ("YOLO mode"; no approvals). Protection toggles exist for file deletion, dotfiles, external files, and MCP tools.[^cursor-perms]

Cursor disables VS Code Workspace Trust by default and does not verify extension signatures — VS Code does both.[^cursor-trust]

**Configuration options.** `.cursorignore` uses `.gitignore` syntax to block files from AI indexing and reading. However, Cursor's own documentation states this is "best-effort" — "there may be bugs that allow ignored files to be sent up in certain cases." Critically, **terminal commands and MCP server tools bypass `.cursorignore`**. If the agent runs a shell command that reads a file, `.cursorignore` does not prevent it.[^cursor-ignore]

Privacy Mode enables Zero Data Retention with model providers. Enabled by default for team/enterprise accounts; not for individual accounts. Enterprise admins can enforce it. Sandbox network configuration (`sandbox.json`) restricts which domains the agent's shell commands can reach. Enterprise deployment via MDM (Jamf, Intune) is supported.[^cursor-privacy]

**Data transmission.** AI prompts and code context are always sent to Cursor's servers. Codebase indexing uploads code chunks temporarily — plaintext is deleted after embedding computation, but **embeddings and metadata (hashes, obfuscated file paths) are stored permanently** in Cursor's vector database. Cursor acknowledges that embedding reversal attacks are "definitely possible for an adversary who breaks into our vector database." With Privacy Mode off, Cursor may use code data for training. With Privacy Mode on, ZDR is enforced with model providers, but embeddings are still stored server-side.[^cursor-data]

Telemetry (device type, OS, IP, error logs, interaction patterns, usage dates, browsing history, geographic location) is collected by default; disable via `"telemetry.telemetryLevel": "off"` in settings.[^cursor-telemetry]

**Privacy commitments.** SOC 2 Type II certified. Contractual ZDR agreements with OpenAI, Anthropic, Google Vertex, xAI, and Fireworks. Annual penetration testing. TLS 1.2+ / AES-256 encryption. DPA available for organizations. Customer Managed Encryption Keys (CMEK) available for Enterprise. **Not available:** HIPAA/BAA, FedRAMP, data residency guarantees, on-premise deployment, or independently audited Privacy Mode implementation.[^cursor-security]

**Known gaps.**

- **`.cursorignore` is not a security boundary.** Terminal commands bypass it. For sensitive data, physical separation (data not in the workspace tree) is more reliable.[^cursor-ignore]
- **Codebase embeddings stored permanently.** Even with Privacy Mode, vector representations and obfuscated file paths persist server-side. Acknowledged as reversible by a motivated attacker.[^cursor-data]
- **No direct-to-provider routing.** All AI requests transit Cursor's infrastructure; users cannot bypass this intermediary.[^cursor-arch]
- **Unrestricted filesystem reads by default.** Flagged by Agent Safehouse: "full filesystem read access combined with aggressive auto-approval could leak credentials."[^cursor-safehouse]
- **Multiple CVEs in 2025–2026.** CurXecute (CVE-2025-54135, arbitrary command execution via Slack messages), MCPoison (CVE-2025-54136, persistent team compromise via shared configs), sensitive file overwrite via case-insensitive filesystem exploitation (CVE-2025-59944), and terminal allowlist bypass via shell built-ins (CVE-2026-22708).[^cursor-cves]
- **Extension security weaker than VS Code.** Workspace Trust disabled by default, extension signatures not verified. A malicious Open VSX extension led to a confirmed $500K cryptocurrency theft.[^cursor-trust]
- **Malicious `.cursorrules` files** in cloned repositories can contain hidden prompt injections.[^cursor-injection]

**Guarantee classification for Cursor:**

| Protection | Level |
|-----------|-------|
| OS-level sandbox for terminal commands (when enabled) | Architecturally guaranteed (kernel enforcement) |
| Privacy Mode + ZDR with providers | Configurable (depends on mode being enabled and enforced) |
| `.cursorignore` file exclusions | Conventional (best-effort; bypassed by terminal/MCP) |
| Protection toggles (file deletion, dotfiles, etc.) | Conventional (application-layer) |

### 3.4 GitHub Copilot (GitHub/Microsoft)

**Architecture.** GitHub Copilot is a family of products with fundamentally different security models. The **IDE extension** (inline completions + chat) runs locally in your editor, sending context (active file, open tabs, cursor position) to GitHub's servers for inference. **Agent mode** (VS Code) runs locally with expanded capabilities: file read/write, terminal execution, MCP server invocation. **Copilot CLI** runs in the terminal with similar capabilities. The **coding agent** runs entirely on GitHub's cloud infrastructure in ephemeral Actions runners, cloning the repo, working on a branch, and creating a draft PR.[^copilot-arch]

**Default permission model.** Inline completions require no approval — code context is silently sent to servers. In agent mode, file edits are **applied automatically without blocking on consent** (shown in a diff view after the fact); only terminal commands require confirmation in Default Approvals mode. The `Bypass Approvals` and `Autopilot` modes remove all prompts. Copilot CLI requires per-directory trust and per-tool approval unless overridden. The coding agent runs autonomously with no interactive approval — human review happens at the PR stage.[^copilot-perms]

Terminal auto-approval accepts regex patterns but GitHub warns this "provides best effort protections and assumes the agent is not acting maliciously" and that "quote concatenation or shell aliases might bypass the rules."[^copilot-terminal]

**Configuration options.** Content exclusions (Business/Enterprise only) let admins specify files Copilot should ignore. **However, content exclusions do not work in agent mode, Copilot CLI, or the coding agent.** GitHub documents this explicitly: "GitHub Copilot CLI, Copilot cloud agent, and Agent mode in Copilot Chat in IDEs, do not support content exclusion."[^copilot-exclusions] This is the single most important limitation for researchers — the primary mechanism for protecting sensitive files does not apply to the most capable (and risky) features.

Agent sandboxing (OS-level, preview) is available on macOS/Linux for VS Code agent mode, providing filesystem write restrictions and network isolation when enabled. The coding agent has a firewall with a default allowlist, but it "only applies to processes started by the agent's Bash tool — not Model Context Protocol servers or processes in setup steps."[^copilot-firewall]

Organization/enterprise policies control feature availability, model selection, MCP servers, and third-party agent access. IT admins can disable agent mode entirely via VS Code policy.[^copilot-policies]

**Data transmission.** Code context, file metadata, prompts, and terminal output are sent to GitHub/model provider servers during all Copilot interactions. Telemetry (engagement data) is always collected and retained for 2 years across all plans. For the coding agent, session logs are retained "for the life of the account."[^copilot-data]

**Privacy commitments.** The April 24, 2026 policy change is significant: interaction data from Free, Pro, and Pro+ users — "inputs, outputs, code snippets, and associated context" — is now used for model training **by default**. Users must actively opt out. Previous opt-outs carry over. Business and Enterprise customers are contractually excluded. Crucially, GitHub distinguishes between "code at rest" (stored in repos; not used for training) and "interaction data" (code processed during active sessions; subject to training). Private repo code *during active use* can be collected even though private repos "at rest" are excluded.[^copilot-training]

GitHub maintains ZDR agreements with OpenAI and Anthropic for generally available features. Certifications: SOC 2 Type 2, ISO 27001. GitHub follows Microsoft's Responsible AI Standard.[^copilot-privacy]

**Known gaps.**

- **Content exclusions don't work in agent features.** The most capable Copilot modes — agent mode, CLI, and the coding agent — bypass content exclusion rules entirely.[^copilot-exclusions]
- **No OS-level sandboxing by default.** Agent mode and CLI rely on application-level permission checks. The VS Code agent sandbox is preview-only and must be explicitly enabled.[^copilot-sandbox]
- **Agent mode applies file edits before showing them.** In Default Approvals mode, edits are written first, then displayed for review — not blocked pending consent.[^copilot-edits]
- **`.env` files are not automatically excluded.** The IDE setting to disable completions in `.env` files does not prevent agent mode from reading them as context.[^copilot-env]
- **Higher secrets leakage rate.** GitGuardian's 2026 report found repos using Copilot leaked secrets at 6.4% vs. 4.6% baseline — a 40% higher rate.[^copilot-secrets]
- **Training policy is opt-out, not opt-in.** Individual users are opted in by default since April 2026. "Interaction data" from private repos during active sessions is subject to training unless the user opts out.[^copilot-training]
- **Coding agent session logs retained indefinitely** ("life of the account"), unlike other features where prompts are discarded or retained for 28 days.[^copilot-logs]
- **Coding agent firewall has limited scope.** Does not cover MCP servers or setup-step processes.[^copilot-firewall]

**Guarantee classification for Copilot:**

| Protection | Level |
|-----------|-------|
| VS Code agent sandbox (when enabled, preview) | Architecturally guaranteed (kernel enforcement) |
| Coding agent ephemeral environment | Architecturally guaranteed (isolated Actions runner) |
| Content exclusions (Business/Enterprise, non-agent features) | Configurable (admin-managed; not enforced in agent modes) |
| Terminal command approval prompts | Conventional (application-layer; bypassable by concatenation) |
| `.copilotignore` file patterns | Conventional (not enforced in agent modes) |

---

## 4. Economist Use Cases

### Use Case 1: "Restrict AI to ONLY work within `/project-x/`"

*The scenario: You are starting to use AI coding agents and want to ensure the tool can only see and modify files within a specific project directory. Your machine has IRB-protected data in other directories, and you need to be able to tell your IRB that the AI cannot access it.*

**The honest answer:** No tool can architecturally guarantee this at the application layer alone. All four tools run as your user and inherit your filesystem permissions. True restriction requires OS-level enforcement.

#### Tool-native scoping

| Tool | Native project scoping | Limitation |
|------|----------------------|------------|
| **Claude Code** | Working directory scoping for writes; `denyRead` sandbox rules for reads. Sandbox uses Seatbelt (macOS) or bubblewrap (Linux) for kernel enforcement. | Must explicitly configure `denyRead` — default allows reading everything. Subprocess file access only blocked by sandbox, not permission rules. |
| **Codex CLI** | `workspace-write` mode (default) restricts writes to project directory. `--cd` flag sets working directory. Network blocked by default. | Main process is unconfined — only spawned commands are sandboxed. `.gitignore` doesn't prevent content from reaching model context via workspace commands. |
| **Cursor** | Writes are workspace-scoped by default. `.cursorignore` excludes files from AI. | `.cursorignore` is best-effort and bypassed by terminal commands. Reads are unrestricted across the filesystem. |
| **Copilot** | Agent mode file operations are workspace-scoped. Content exclusions block specific paths (Business/Enterprise). | Content exclusions don't work in agent mode, CLI, or coding agent. VS Code agent sandbox (preview) is the only kernel-enforced option. |

#### Recommended approach: defense in depth

**Level 1 (tool-native, conventional):** Configure the tool to scope to `/project-x/`. For Claude Code, enable the sandbox with explicit `denyRead` rules for sensitive paths. For Codex, use default `workspace-write` mode. For Cursor, create a comprehensive `.cursorignore`. For Copilot, configure content exclusions (Business/Enterprise) and enable agent sandbox if available.

**Level 2 (OS-enforced, configurable):** Tighten file permissions on sensitive directories:

```bash
# Restrict IRB data directory
chmod 700 ~/irb-data/
chmod -R go-rwx ~/irb-data/

# Restrict credential files
chmod 600 ~/.ssh/* ~/.aws/credentials ~/.aws/config
```

This is kernel-enforced but requires the AI agent to run as a different user to be effective (since it runs as *your* user by default).

**Level 3 (OS-enforced, architectural):** Run the AI agent in a Docker container or dev container that only mounts `/project-x/`:

```bash
# Docker: mount only the project directory
docker run -it -v /path/to/project-x:/workspace:rw ubuntu:latest

# Dev container (VS Code): mount project only, no credential pass-through
# .devcontainer/devcontainer.json mounts the project directory; host ~ is invisible
```

Or use a dedicated user account (kernel-enforced UID separation):

```bash
# Create sandbox user
sudo dscl . -create /Users/ai-sandbox
# ... configure minimal access ...
# Run agent as sandbox user
su ai-sandbox -c "cd /project-x && claude"
```

**Level 4 (hypervisor-enforced, architectural):** Run the AI agent inside a VM. Share only `/project-x/` as a folder mount. The VM has its own kernel — nothing on the host is accessible without an explicit share.

**What to tell your IRB:** "The AI coding agent runs inside a [container/VM] that has access only to the project code directory. Research data files are stored in a separate location that is not mounted into the agent's environment. The agent cannot read, access, or transmit any files outside the mounted project directory. This restriction is enforced by [the Linux kernel's namespace isolation / the hypervisor boundary], not by the AI tool's own software — meaning it cannot be bypassed by a software bug or misconfiguration in the AI tool itself."

### Use Case 2: "Allow full access EXCEPT `/irb-data/`"

*The scenario: You are an experienced user who wants the AI to work freely across your codebase but needs to ensure it never reads the contents of a specific directory containing restricted data.*

**The honest answer:** Deny-by-exception is inherently riskier than allow-by-inclusion (Use Case 1). You are relying on every access path being blocked, rather than allowing only what is needed. Defense in depth is even more important here.

#### Tool-native deny capabilities

| Tool | Deny mechanism | Reliability |
|------|---------------|-------------|
| **Claude Code** | `denyRead` in sandbox config: `"denyRead": ["/path/to/irb-data"]`. Kernel-enforced via Seatbelt/bubblewrap. | **Strong** when sandbox is enabled. Blocks all child process access. Does not block the main process from *sending* already-read content. |
| **Codex CLI** | No explicit deny-path mechanism in config. Must rely on not being in the writable roots, plus OS-level permissions. | **Weak** for deny-by-exception. The tool is designed for allow-by-inclusion (workspace-write), not per-path exclusion. |
| **Cursor** | `.cursorignore` for the path. | **Weak.** Best-effort, bypassed by terminal commands. |
| **Copilot** | Content exclusions for the path (Business/Enterprise only). | **Weak.** Not enforced in agent mode, CLI, or coding agent. |

#### Recommended approach

1. **Claude Code with sandbox** is the strongest tool-native option for this use case. Enable the sandbox and add `/irb-data/` to `denyRead`. This is kernel-enforced for all child processes.

2. **Regardless of tool**, apply OS-level restrictions:

```bash
# Make the data directory unreadable by removing your own read permission
# (Only works if YOU don't need to read it during the same session)
chmod 000 ~/irb-data/

# Or use POSIX ACLs to deny a specific user/group
# (Useful if running the agent as a separate user)
setfacl -m u:ai-sandbox:--- ~/irb-data/
```

3. **The most reliable approach is physical separation.** Store IRB data on an encrypted volume that is not mounted during AI sessions. Or keep it on a separate machine / cloud storage that the agent's machine cannot reach. If the data is not on the filesystem, no tool bug or misconfiguration can expose it.

4. **For maximum assurance**, combine approaches: sandbox `denyRead` (blocks tool access) + `chmod 000` or unmounted volume (blocks OS-level access) + network restrictions (blocks exfiltration even if data is somehow read).

**What to tell your IRB:** "Research data is stored in a directory with filesystem permissions set to block all access during AI-assisted coding sessions [or: on an encrypted volume that is unmounted during AI sessions]. Additionally, the AI tool's sandbox configuration explicitly denies read access to the data directory, enforced at the operating system kernel level. These are independent protections — both would need to fail simultaneously for the AI to access the data."

---

## 5. Practical Checklists

### Before your first AI coding session

- [ ] **Know your plan tier.** Business/Enterprise plans offer stronger privacy protections across all tools. Personal/free plans may use your data for training by default.
- [ ] **Identify sensitive files.** List directories containing IRB data, credentials, student records, and pre-publication results. These need explicit protection.
- [ ] **Tighten file permissions.** Run `chmod 600 ~/.ssh/* ~/.aws/credentials ~/.aws/config` at minimum. Audit with `find ~ -maxdepth 3 -perm -o+r -type f` for world-readable files.
- [ ] **Enable full-disk encryption.** FileVault (macOS) or LUKS (Linux). All tools store unencrypted session transcripts locally.
- [ ] **Review your authentication method.** For Codex CLI: use API key auth, not ChatGPT personal login (which opts into training by default). For Copilot: opt out of training data at Settings > Copilot > Features if on a personal plan.
- [ ] **Separate data from code.** The single most effective protection: keep sensitive data files in a different directory (or different machine) from your code. An AI tool scoped to your code directory cannot read data that isn't there.

### Per-tool quick setup

#### Claude Code

```json
// .claude/settings.json (project-level)
{
  "permissions": {
    "deny": ["Read(//**/.env)", "Read(//~/.ssh/**)", "Read(//~/.aws/**)"]
  },
  "sandbox": {
    "enabled": true,
    "filesystem": {
      "denyRead": ["~/.ssh", "~/.aws", "~/.config/gh", "/path/to/sensitive-data"]
    },
    "network": {
      "allowedDomains": []
    }
  }
}
```

Set environment variables:
```bash
export DISABLE_TELEMETRY=1
export DISABLE_ERROR_REPORTING=1
export CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1
```

#### Codex CLI

```toml
# ~/.codex/config.toml
[sandbox_workspace_write]
network_access = false

[shell_environment_policy]
inherit = "none"
set = { PATH = "/usr/bin:/usr/local/bin" }
ignore_default_excludes = false

[history]
persistence = "none"  # or "per_session" with a short retention

[analytics]
enabled = false
```

Authenticate with an API key, not ChatGPT login.

#### Cursor

1. Enable Privacy Mode: Cmd+Shift+J > General > Privacy Mode
2. Create `.cursorignore` in project root:
   ```
   .env*
   *.dta
   *.csv
   *.sav
   .ssh/
   .aws/
   **/data/
   **/secrets/
   ```
3. Set terminal to Allowlist mode (not Run Everything)
4. Enable all protection toggles (file deletion, dotfiles, external files, MCP)
5. Disable telemetry: `"telemetry.telemetryLevel": "off"` in settings
6. **Most important:** Keep sensitive data files outside the Cursor workspace entirely

#### GitHub Copilot

1. Opt out of training: Settings > Copilot > Features > disable "Allow GitHub to use my data for AI model training"
2. Configure content exclusions (Business/Enterprise) for sensitive paths
3. **Accept the limitation:** content exclusions do not work in agent mode, CLI, or coding agent
4. Enable VS Code agent sandbox (if on macOS/Linux): Settings > search "agent sandbox"
5. Do not open workspaces containing sensitive data files when using agent mode
6. For the coding agent: review the firewall allowlist; consider keeping sensitive data out of repositories entirely

### Decision tree: which protection approach fits your situation

```
Do you work with IRB-protected data, FERPA records, or data under
a data use agreement on the same machine where you use AI tools?
│
├── NO → Tool-native defaults are likely sufficient.
│        Enable sandbox/privacy mode. Opt out of training. Done.
│
└── YES
    │
    ├── Is the data so sensitive that any cloud transmission
    │   is unacceptable (e.g., DUA prohibits third-party servers)?
    │   │
    │   ├── YES → Keep data on a separate drive or encrypted disk
    │   │         image. Unmount/eject before AI sessions.
    │   │         This is the strongest protection: architecturally
    │   │         guaranteed, zero configuration, no software trust
    │   │         required. Use AI tools on code only.
    │   │         (See Section 0 for options.)
    │   │
    │   └── NO (cloud processing acceptable with protections)
    │       │
    │       ├── Can you keep data on a separate machine, drive,
    │       │   or unmounted encrypted volume?
    │       │   │
    │       │   ├── YES → Do that. Use AI tools normally on your
    │       │   │         code-only machine/session. Simplest and
    │       │   │         strongest — nothing to configure.
    │       │   │
    │       │   └── NO (data must stay on same machine, mounted)
    │       │       │
    │       │       ├── Can you keep data in a completely separate
    │       │       │   directory tree from your code?
    │       │       │   │
    │       │       │   ├── YES → Use Case 1: Run AI in a container
    │       │       │   │         or VM that mounts ONLY the code
    │       │       │   │         directory. Kernel/hypervisor-enforced.
    │       │       │   │
    │       │       │   └── NO (data and code are interleaved)
    │       │       │       │
    │       │       │       └── Use Case 2: Defense in depth.
    │       │       │           Claude Code sandbox with denyRead
    │       │       │           (strongest tool-native option) +
    │       │       │           chmod 000 on data dirs during AI
    │       │       │           sessions + full-disk encryption.
    │       │       │           Consider reorganizing to separate
    │       │       │           data from code.
    │       │       │
    │       │       └── Enterprise plan + ZDR + sandbox + file
    │       │           permission hardening. Document for IRB.
```

---

## 6. Sources & Further Reading

### Official documentation

**Anthropic / Claude Code**
- [Claude Code Security](https://code.claude.com/docs/en/security)
- [Claude Code Permissions](https://code.claude.com/docs/en/permissions)
- [Claude Code Sandboxing](https://code.claude.com/docs/en/sandboxing)
- [Claude Code Data Usage](https://code.claude.com/docs/en/data-usage)
- [Claude Code Zero Data Retention](https://code.claude.com/docs/en/zero-data-retention)
- [Claude Code Dev Containers](https://code.claude.com/docs/en/devcontainer)
- [Anthropic Engineering: Claude Code Sandboxing](https://www.anthropic.com/engineering/claude-code-sandboxing)

**OpenAI / Codex CLI**
- [Codex Agent Approvals & Security](https://developers.openai.com/codex/agent-approvals-security)
- [Codex Sandboxing Concepts](https://developers.openai.com/codex/concepts/sandboxing)
- [Codex CLI Features](https://developers.openai.com/codex/cli/features)
- [Codex CLI Reference](https://developers.openai.com/codex/cli/reference)
- [Codex Configuration (Basic)](https://developers.openai.com/codex/config-basic)
- [Codex Configuration (Advanced)](https://developers.openai.com/codex/config-advanced)
- [Codex Authentication](https://developers.openai.com/codex/auth)
- [OpenAI Data Controls](https://developers.openai.com/api/docs/guides/your-data)
- [OpenAI Enterprise Privacy](https://openai.com/enterprise-privacy/)
- [OpenAI Business Data](https://openai.com/business-data/)

**Anysphere / Cursor**
- [Cursor Data Use & Privacy Overview](https://cursor.com/data-use)
- [Cursor Privacy Policy](https://cursor.com/privacy)
- [Cursor Security Page](https://cursor.com/security)
- [Cursor Enterprise Privacy & Data Governance](https://cursor.com/docs/enterprise/privacy-and-data-governance)
- [Cursor Agent Security](https://cursor.com/docs/agent/security)
- [Cursor Terminal Docs](https://cursor.com/docs/agent/tools/terminal)
- [Cursor Ignore File Reference](https://cursor.com/docs/reference/ignore-file)
- [Cursor Blog: Agent Sandboxing](https://cursor.com/blog/agent-sandboxing)
- [Cursor Trust Center](https://trust.cursor.com/)

**GitHub / Copilot**
- [VS Code Copilot Security](https://code.visualstudio.com/docs/copilot/security)
- [VS Code Agent Tools](https://code.visualstudio.com/docs/copilot/agents/agent-tools)
- [GitHub Content Exclusion](https://docs.github.com/en/copilot/concepts/context/content-exclusion)
- [GitHub Copilot Policies](https://docs.github.com/en/copilot/concepts/policies)
- [Coding Agent Firewall](https://docs.github.com/copilot/customizing-copilot/customizing-or-disabling-the-firewall-for-copilot-coding-agent)
- [Coding Agent Overview](https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent)
- [GitHub Copilot Data Policy Update (April 2026)](https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/)
- [GitHub Copilot Trust Center](https://copilot.github.trust.page/)

**OS-level sandboxing**
- [Docker Engine Security](https://docs.docker.com/engine/security/)
- [Docker Sandboxes](https://docs.docker.com/ai/sandboxes/)
- [Docker User Namespace Isolation](https://docs.docker.com/engine/security/userns-remap/)
- [Apple Developer: App Sandbox](https://developer.apple.com/documentation/xcode/configuring-the-macos-app-sandbox)

### Privacy policies and terms of service

- [Anthropic Privacy Center](https://privacy.claude.com/)
- [Anthropic Trust Center](https://trust.anthropic.com)
- [OpenAI How Your Data Is Used](https://openai.com/policies/how-your-data-is-used-to-improve-model-performance/)
- [Cursor Privacy Policy](https://cursor.com/privacy)
- [Cursor DPA](https://cursor.com/terms/dpa)
- [GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement)
- [GitHub FAQ on Data Policy Changes](https://github.com/orgs/community/discussions/188488)

### Independent security analyses

- [Agent Safehouse: Claude Code Analysis](https://agent-safehouse.dev/docs/agent-investigations/codex) — independent sandbox audit
- [Agent Safehouse: Cursor Agent Analysis](https://agent-safehouse.dev/docs/agent-investigations/cursor-agent)
- [Agent Safehouse: Copilot CLI Analysis](https://agent-safehouse.dev/docs/agent-investigations/copilot-cli)
- [Cymulate: Sandbox Escape Research (2026)](https://cymulate.com/blog/the-race-to-ship-ai-tools-left-security-behind-part-1-sandbox-escape/)
- [Check Point: Claude Code Project File Vulnerabilities](https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/)
- [Check Point: Codex CLI Command Injection](https://research.checkpoint.com/2025/openai-codex-cli-command-injection-vulnerability/)
- [BeyondTrust: Codex GitHub Token Exfiltration](https://www.beyondtrust.com/blog/entry/openai-codex-command-injection-vulnerability-github-token)
- [Backslash Security: Cursor Denylist Bypass](https://www.backslash.security/blog/cursor-ai-security-flaw-autorun-denylist)
- [MintMCP: Cursor Security Guide](https://www.mintmcp.com/blog/cursor-security)
- [GitGuardian: Copilot Security & Privacy](https://blog.gitguardian.com/github-copilot-security-and-privacy/)
- [Adversa AI: Claude Code Deny Rule Bypass](https://adversa.ai/blog/claude-code-security-bypass-deny-rules-disabled/)
- [SecurityWeek: Claude Code Sandbox Bypass](https://www.securityweek.com/anthropic-silently-patches-claude-code-sandbox-bypass/)
- [Serendb: Claude Code Local Memory Security Risk](https://serendb.com/blog/claude-code-local-memory-security-risk)

### Practitioner guides

- [Daniel Demmel: Secured VS Code Dev Containers for AI Agents](https://www.danieldemmel.me/blog/coding-agents-in-secured-vscode-dev-containers)
- [Dev.to: Sandboxing AI Agents with Dev Containers](https://dev.to/klaus82/sandboxing-ai-coding-agents-with-devcontainers-4ja3)
- [Dev.to: VNC Restricted User on macOS](https://dev.to/jlarky/running-a-local-sandboxed-macos-desktop-using-vnc-and-a-restricted-user-38dk)
- [HowToHarden: Cursor Hardening Guide](https://howtoharden.com/guides/cursor/)
- [devActivity: Content Exclusion Blind Spot](https://devactivity.com/posts/apps-tools/github-copilot-s-content-exclusion-a-critical-blind-spot-for-agentic-workflows/)
- [devActivity: Keeping .env Files Out of Copilot](https://devactivity.com/posts/productivity-tips/securing-your-secrets-keeping-env-files-out-of-copilot-agent-mode-s-reach/)
- [Docker Blog: Docker Sandboxes for AI Agents](https://www.docker.com/blog/docker-sandboxes-run-claude-code-and-other-coding-agents-unsupervised-but-safely/)
- [Igor's Techno Club: sandbox-exec Guide](https://igorstechnoclub.com/sandbox-exec/)
- [GhostVM: Sandboxed macOS Environment](https://ghostvm.org/sandboxed-macos-environment)
- [Alcoholless: Lightweight macOS Sandbox](https://medium.com/nttlabs/alcoholless-a-lightweight-security-sandbox-for-macos-programs-homebrew-ai-agents-etc-ccf0d1927301)

### Community discussions

- [GitHub Discussion #5523: Codex .gitignore and file content transmission](https://github.com/openai/codex/discussions/5523)
- [GitHub Discussion #8291: Codex telemetry opt-out request](https://github.com/openai/codex/discussions/8291)
- [Cursor Forum: Privacy Mode and Codebase Indexing](https://forum.cursor.com/t/privacy-mode-and-codebase-indexing/15445)
- [Cursor Forum: Agent access outside project](https://forum.cursor.com/t/cursor-agents-should-be-restricted-from-access-of-files-outside-the-project-without-permission/149418)
- [GitHub Community Discussion #183099: Copilot data handling](https://github.com/orgs/community/discussions/183099)
- [GitHub Community Discussion #188488: Copilot training policy FAQ](https://github.com/orgs/community/discussions/188488)
- [Hacker News: sandbox-exec discussion](https://news.ycombinator.com/item?id=47101200)
- [GitHub: apple/containerization#737 (sandbox-exec deprecation)](https://github.com/apple/containerization/issues/737)

### Security advisories (CVEs)

- **Claude Code:** CVE-2025-59536 (RCE via project config hooks), CVE-2026-21852 (API key exfiltration via base URL override), deny-rule bypass at >50 subcommands (patched v2.1.90), SOCKS5 null-byte sandbox escape (patched v2.1.90)
- **Codex CLI:** CVE-2025-59532 (sandbox boundary bypass, CVSS 8.6), CVE-2025-61260 (command injection via project config, CVSS 9.8), GitHub token exfiltration via branch names (patched Feb 2026)
- **Cursor:** CVE-2025-54135 (CurXecute), CVE-2025-54136 (MCPoison), CVE-2025-59944 (case-insensitive file overwrite), CVE-2026-22708 (terminal allowlist bypass)
- **macOS:** TCC Spotlight bypass (patched macOS 26.4), CVE-2026-28910 (App Sandbox + TCC escape via Archive Utility)

---

## Footnotes

[^acl]: Linux man page: acl(5). https://man7.org/linux/man-pages/man5/acl.5.html
[^tcc]: Eclectic Light: TCC Explainer. https://eclecticlight.co/2025/11/08/explainer-permissions-privacy-and-tcc/
[^seatbelt]: Igor's Techno Club: sandbox-exec guide. https://igorstechnoclub.com/sandbox-exec/ ; GitHub: apple/containerization#737. https://github.com/apple/containerization/issues/737
[^docker]: Docker Engine Security. https://docs.docker.com/engine/security/ ; Docker Sandboxes. https://docs.docker.com/ai/sandboxes/
[^vm]: Northflank: Containers vs VMs. https://northflank.com/blog/containers-vs-virtual-machines ; GhostVM. https://ghostvm.org/sandboxed-macos-environment
[^zdr-anthropic]: Claude Code Zero Data Retention. https://code.claude.com/docs/en/zero-data-retention
[^cc-arch]: Claude Code Security. https://code.claude.com/docs/en/security ; Data Usage. https://code.claude.com/docs/en/data-usage
[^cc-sandbox]: Claude Code Sandboxing. https://code.claude.com/docs/en/sandboxing
[^cc-perms]: Claude Code Permissions. https://code.claude.com/docs/en/permissions
[^cc-data]: Claude Code Data Usage. https://code.claude.com/docs/en/data-usage
[^cc-privacy]: Anthropic Privacy Center. https://privacy.claude.com/ ; Trust Center. https://trust.anthropic.com
[^cc-transcript]: Serendb: Claude Code Local Memory Security Risk. https://serendb.com/blog/claude-code-local-memory-security-risk
[^cc-network]: Claude Code Sandboxing: Security Limitations. https://code.claude.com/docs/en/sandboxing#security-limitations
[^cc-cves]: Check Point Research. https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/ ; Adversa AI. https://adversa.ai/blog/claude-code-security-bypass-deny-rules-disabled/ ; SecurityWeek. https://www.securityweek.com/anthropic-silently-patches-claude-code-sandbox-bypass/
[^cc-injection]: TruFoundry. https://www.truefoundry.com/blog/claude-code-prompt-injection
[^codex-arch]: Agent Safehouse: Codex Analysis. https://agent-safehouse.dev/docs/agent-investigations/codex ; DeepWiki. https://deepwiki.com/openai/codex/5.6-sandboxing-implementation
[^codex-perms]: Codex Agent Approvals & Security. https://developers.openai.com/codex/agent-approvals-security
[^codex-config]: Codex Advanced Configuration. https://developers.openai.com/codex/config-advanced
[^codex-network]: Codex Agent Approvals & Security. https://developers.openai.com/codex/agent-approvals-security
[^codex-data]: Codex CLI Features. https://developers.openai.com/codex/cli/features ; Advanced Configuration. https://developers.openai.com/codex/config-advanced
[^openai-data]: OpenAI Data Controls. https://developers.openai.com/api/docs/guides/your-data
[^codex-auth]: Codex Auth. https://developers.openai.com/codex/auth ; OpenAI Data Policy. https://openai.com/policies/how-your-data-is-used-to-improve-model-performance/
[^codex-safehouse]: Agent Safehouse: Codex Analysis. https://agent-safehouse.dev/docs/agent-investigations/codex
[^codex-gitignore]: GitHub Discussion #5523. https://github.com/openai/codex/discussions/5523
[^codex-cve1]: GitHub Advisory GHSA-w5fx-fh39-j5rw. https://github.com/openai/codex/security/advisories/GHSA-w5fx-fh39-j5rw
[^codex-cve2]: Check Point Research. https://research.checkpoint.com/2025/openai-codex-cli-command-injection-vulnerability/
[^codex-cve3]: BeyondTrust. https://www.beyondtrust.com/blog/entry/openai-codex-command-injection-vulnerability-github-token
[^codex-telemetry]: GitHub Discussion #8291. https://github.com/openai/codex/discussions/8291
[^codex-transcripts]: Agent Safehouse: Codex Analysis. https://agent-safehouse.dev/docs/agent-investigations/codex
[^cursor-arch]: Cursor Data Use. https://cursor.com/data-use ; Enterprise Security Report. https://harini.blog/2025/05/07/detailed-security-and-enterprise-readiness-report-cursor-ai-ide/
[^cursor-perms]: Cursor Agent Security. https://cursor.com/docs/agent/security ; Terminal Docs. https://cursor.com/docs/agent/tools/terminal
[^cursor-trust]: MintMCP: Cursor Security. https://www.mintmcp.com/blog/cursor-security
[^cursor-ignore]: Cursor Ignore File Reference. https://cursor.com/docs/reference/ignore-file
[^cursor-privacy]: Cursor Security. https://cursor.com/security ; Enterprise Privacy. https://cursor.com/docs/enterprise/privacy-and-data-governance
[^cursor-data]: Cursor Data Use. https://cursor.com/data-use ; Enterprise Security Report. https://harini.blog/2025/05/07/detailed-security-and-enterprise-readiness-report-cursor-ai-ide/
[^cursor-telemetry]: Cursor Privacy Policy. https://cursor.com/privacy
[^cursor-security]: Cursor Security. https://cursor.com/security ; DPA. https://cursor.com/terms/dpa
[^cursor-safehouse]: Agent Safehouse: Cursor Analysis. https://agent-safehouse.dev/docs/agent-investigations/cursor-agent
[^cursor-cves]: Backslash Security. https://www.backslash.security/blog/cursor-ai-security-flaw-autorun-denylist ; Agent Safehouse. https://agent-safehouse.dev/docs/agent-investigations/cursor-agent ; MintMCP. https://www.mintmcp.com/blog/cursor-security
[^cursor-injection]: MintMCP: Cursor Security. https://www.mintmcp.com/blog/cursor-security ; HowToHarden. https://howtoharden.com/guides/cursor/
[^copilot-arch]: VS Code Copilot Overview. https://code.visualstudio.com/docs/copilot/overview ; Agent Safehouse. https://agent-safehouse.dev/docs/agent-investigations/copilot-cli ; GitHub Coding Agent. https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent
[^copilot-perms]: VS Code Agent Tools. https://code.visualstudio.com/docs/copilot/agents/agent-tools ; Agent Safehouse. https://agent-safehouse.dev/docs/agent-investigations/copilot-cli
[^copilot-terminal]: VS Code Agent Tools. https://code.visualstudio.com/docs/copilot/agents/agent-tools
[^copilot-exclusions]: GitHub Content Exclusion. https://docs.github.com/en/copilot/concepts/context/content-exclusion ; devActivity. https://devactivity.com/posts/apps-tools/github-copilot-s-content-exclusion-a-critical-blind-spot-for-agentic-workflows/
[^copilot-firewall]: GitHub Coding Agent Firewall. https://docs.github.com/copilot/customizing-copilot/customizing-or-disabling-the-firewall-for-copilot-coding-agent
[^copilot-policies]: GitHub Copilot Policies. https://docs.github.com/en/copilot/concepts/policies ; VS Code Copilot Security. https://code.visualstudio.com/docs/copilot/security
[^copilot-data]: GitHub Data Handling. https://resources.github.com/learn/pathways/copilot/essentials/how-github-copilot-handles-data/ ; VS Code Copilot Security. https://code.visualstudio.com/docs/copilot/security
[^copilot-training]: GitHub Blog: Data Policy Update. https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/ ; FAQ. https://github.com/orgs/community/discussions/188488
[^copilot-privacy]: GitHub Community Discussion #183099. https://github.com/orgs/community/discussions/183099 ; Copilot Trust Center. https://copilot.github.trust.page/
[^copilot-sandbox]: Agent Safehouse: Copilot CLI. https://agent-safehouse.dev/docs/agent-investigations/copilot-cli ; VS Code Copilot Security. https://code.visualstudio.com/docs/copilot/security
[^copilot-edits]: VS Code Blog: Agent Mode. https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode
[^copilot-env]: devActivity: .env Files. https://devactivity.com/posts/productivity-tips/securing-your-secrets-keeping-env-files-out-of-copilot-agent-mode-s-reach/
[^copilot-secrets]: GitGuardian: Copilot Security & Privacy. https://blog.gitguardian.com/github-copilot-security-and-privacy/
[^copilot-logs]: GitHub Community Discussion #183099. https://github.com/orgs/community/discussions/183099
