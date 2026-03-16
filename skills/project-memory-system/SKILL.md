---
name: project-memory-system
description: Bootstrap, audit, or maintain a repository-specific project memory system centered on `AGENTS.md`, `MEMORY.md`, and `.memory/*.md`. Use when Codex needs to set up memory files in a repo, add or update domain memory, record durable user corrections, create `.memory/index.md` or `.memory/template.md`, or decide whether knowledge belongs in long-term memory or a domain-specific memory file.
---

# Project Memory System

Build and maintain a layered memory system so future work can reuse durable project knowledge without collapsing everything into one file.

## Follow This Workflow

1. Inspect the current memory state.
   - Read `AGENTS.md`, `MEMORY.md`, and `.memory/index.md` if they exist.
   - Detect whether the repository already has a memory convention and preserve it when possible.

2. Use the canonical layout in [references/memory-layout.md](./references/memory-layout.md).
   - Create or maintain the core files.
   - Keep the file roles distinct.
   - Reuse the standard frontmatter keys and section layout.
   - When creating `.memory/template.md` or a new domain memory file, copy the structure in [references/domain-memory-template.md](./references/domain-memory-template.md).

3. Sort knowledge before writing.
   - Put cross-domain, durable knowledge in `MEMORY.md`.
   - Put stable knowledge that only applies to one module, route, feature, or workflow in `.memory/<domain>.md`.
   - Do not store short-lived debugging notes or one-off session details.

4. Keep `AGENTS.md` as the entry point.
   - Mention that the repository uses a project memory system.
   - Link to `MEMORY.md` and `.memory/index.md`.
   - State that memory must be updated after user corrections and when new modules or domains appear.

5. Keep the domain map complete.
   - When adding, renaming, merging, or removing `.memory/*.md` files, update `.memory/index.md` in the same change.
   - Add `.memory/template.md` when the repository does not already have a reusable template.

6. Update memory during normal work, not as an afterthought.
   - After a user correction, update the relevant memory file in the same task when possible.
   - After a new module or workflow appears, add or extend the relevant domain memory.
   - Prefer short, durable bullets over long narrative notes.

## Editing Rules

- Preserve the repository's chosen freshness key if one already exists.
- When bootstrapping a new system from scratch, use the frontmatter keys in [references/memory-layout.md](./references/memory-layout.md).
- Keep memory files scoped and stable; move repeated cross-domain knowledge up into `MEMORY.md`.
- Reference concrete files, routes, or modules when that makes the memory more reusable.

## Final Check

- Confirm the core files exist and are linked together.
- Confirm every memory document starts with frontmatter.
- Confirm `.memory/index.md` covers every domain memory file.
- Summarize what was created or updated and why.
