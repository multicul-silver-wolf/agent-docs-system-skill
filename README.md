# Project Docs System Skill

> **"Build and maintain a layered docs system for durable project knowledge."**

This repository contains a specialized skill for AI agents (Claude Code, OpenClaw, Codex) designed to bootstrap, audit, or maintain a repository-specific project docs system centered on `AGENTS.md` and `docs/`.

## Why

Durable project knowledge often gets lost in long chat threads. This skill enforces a structured approach to saving reusable knowledge directly in the repository so future sessions can continue with less re-discovery.

## Installation

Install this skill into your agent environment (Claude Code, OpenClaw, or Codex):

```bash
# Using npx skills (Recommended)
npx skills add multicul-silver-wolf/agent-docs-system-skill/skills/project-docs-system

# Using openclaw
openclaw install https://github.com/multicul-silver-wolf/agent-docs-system-skill/skills/project-docs-system

# Or clone and install locally
git clone https://github.com/multicul-silver-wolf/agent-docs-system-skill
openclaw install ./agent-docs-system-skill/skills/project-docs-system
```

## System Architecture

The docs system starts with a two-level domain structure and allows deeper indexed docs scopes when a project needs them:

- **`AGENTS.md`**: Agent entry point. Adds docs-system rules only after `docs/` is initialized.
- **`docs/DOCS.md`**: Repository knowledge protocol for cross-domain language, collaboration conventions, and boundary principles.
- **`docs/index.md`**: Top-level map of first-level domains.
- **`docs/<domain>/DOCS.md`**: Domain protocol for language, conventions, and boundaries shared by multiple subdomain docs.
- **`docs/<domain>/index.md`**: Map of second-level docs inside one domain.
- **`docs/<domain>/<subdomain>.md`**: Current durable truth for one subdomain, with an optional adjacent `<subdomain>.adr.md` companion for scoped decision rationale.

Directories under `docs/` that only contain resources, such as images, are outside docs layout validation. Deeper Markdown docs are valid when each docs scope has an `index.md` that links its direct docs files and child docs scopes.

Decision records stay lightweight and lazy: add an adjacent same-name `.adr.md` companion only for decisions that are hard to reverse, surprising without context, and based on a real trade-off. Living docs describe what is true now; ADR companions preserve what was decided and why. The verifier recognizes dated heading and dated-list history styles used by existing customizations, warns on missing bidirectional links without breaking customized repositories, omits ADR companions from generated catalogs, and emits a non-blocking cohesion warning above 500 author-maintained lines (generated catalog blocks are excluded).

## Usage

Trigger the skill in your chat:

- *"Bootstrap the project docs system in this repo"*
- *"Update `docs/DOCS.md` with our global API naming conventions"*
- *"Audit `docs/` and fix missing index links"*
- *"Add a new subdomain doc under `docs/frontend/` and update maps"*
- *"Record why this subdomain chose a non-obvious runtime boundary"*

---

Built by [Silver Wolf](https://github.com/multicul-silver-wolf) and [Sawana](https://github.com/waitlistSawana).  
Inspired by the **Aether Editing** philosophy.
