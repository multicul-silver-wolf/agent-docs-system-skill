# Project Docs System Skill

> **"Build and maintain a layered docs system for durable project knowledge."**

This repository contains a specialized skill for AI agents (Claude Code, OpenClaw, Codex) designed to bootstrap, audit, or maintain a repository-specific project docs system centered on `AGENTS.md` and `.docs/`.

## Why

Durable project knowledge often gets lost in long chat threads. This skill enforces a structured approach to saving reusable knowledge directly in the repository so future sessions can continue with less re-discovery.

## Installation

Install this skill into your agent environment (Claude Code, OpenClaw, or Codex):

```bash
# Using npx skills (Recommended for Claude Code)
npx skills add multicul-silver-wolf/agent-docs-system-skill/skills/project-docs-system

# Using openclaw
openclaw install https://github.com/multicul-silver-wolf/agent-docs-system-skill/skills/project-docs-system

# Or clone and install locally
git clone https://github.com/multicul-silver-wolf/agent-docs-system-skill
openclaw install ./agent-docs-system-skill/skills/project-docs-system
```

## System Architecture

The docs system uses a two-level domain structure with index maps at each folder level:

- **`AGENTS.md`**: Agent entry point. Adds docs-system rules only after `.docs/` is initialized.
- **`.docs/DOCS.md`**: Cross-domain durable conventions and recurring preferences.
- **`.docs/index.md`**: Top-level map of first-level domains.
- **`.docs/<domain>/index.md`**: Map of second-level docs inside one domain.
- **`.docs/<domain>/<subdomain>.md`**: Durable docs for one subdomain.

## Usage

Trigger the skill in your chat:

- *"Bootstrap the project docs system in this repo"*
- *"Update `.docs/DOCS.md` with our global API naming conventions"*
- *"Audit `.docs/` and fix missing index links"*
- *"Add a new subdomain doc under `.docs/frontend/` and update maps"*

---

Built by [Silver Wolf](https://github.com/multicul-silver-wolf) and [Sawana](https://github.com/waitlistSawana).  
Inspired by the **Aether Editing** philosophy.
