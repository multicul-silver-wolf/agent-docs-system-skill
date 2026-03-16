# Memory Layout

## Canonical File Set

Use this layout when bootstrapping or repairing a project memory system:

- `AGENTS.md`
  - Mention the project memory system.
  - Link to `MEMORY.md` and `.memory/index.md`.
  - State that memory must be updated after user corrections and after new modules or domains are introduced.
- `MEMORY.md`
  - Store cross-domain, durable memory.
- `.memory/index.md`
  - Act as the map for domain memory files.
- `.memory/template.md`
  - Provide the standard template for new domain memory files.
- `.memory/<domain>.md`
  - Store durable knowledge that only applies to one domain.

## Frontmatter

Every memory document should start with frontmatter. When creating a new system, use at least:

```yaml
---
title: Example Title
description: One-line description of what this memory file covers.
updateAt: 2026-03-14
---
```

## File Roles

### `MEMORY.md`

Store:

- durable project-wide terminology
- cross-domain conventions
- recurring user preferences that affect many tasks
- architectural expectations that show up repeatedly

Avoid:

- module-specific implementation notes
- temporary debugging observations
- one-off task status

### `.memory/<domain>.md`

Store:

- domain-specific conventions
- ownership boundaries
- stable file or route relationships
- user corrections that only matter in that domain

Prefer one clear domain per file, such as:

- `homepage.md`
- `blog.md`
- `docs.md`
- `api-search.md`

### `.memory/index.md`

Include:

- a short usage note
- one entry per domain memory file
- when to consult each domain file
- a link to `.memory/template.md`

### `.memory/template.md`

Keep a reusable structure with these sections:

- `How To Use`
- `Scope`
- `Current Domain Memory`
- `Update Triggers`

Use [domain-memory-template.md](./domain-memory-template.md) as the reference content when creating or refreshing this file.

## Placement Rules

Use this decision rule before writing:

- If the memory should apply across the repository, put it in `MEMORY.md`.
- If it only matters for one domain, put it in `.memory/<domain>.md`.
- If it is too temporary to help future work, do not store it.

## Update Triggers

Update the relevant memory file when:

- the user corrects the agent
- the user clarifies a stable project convention
- a new module, route, feature, or workflow becomes important enough to remember
- an existing domain changes ownership, structure, or boundaries

Also update `.memory/index.md` whenever the set of domain memory files changes.
