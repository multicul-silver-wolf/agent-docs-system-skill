---
name: project-docs-system
description: Bootstrap, audit, or maintain a repository-specific project docs system centered on `AGENTS.md` and `docs/`, including repository DOCS, domain DOCS, docs indexes, living subdomain docs, and adjacent ADR companions. Use for any agent (such as Codex, Claude Code, and OpenClaw) when it needs to initialize docs files, maintain indexed docs maps, add or update project conventions, capture durable non-obvious practices, preserve scoped decision rationale, or sync AGENTS.md docs-system rules.
---

# Project Docs System

Build and maintain a layered docs system so future work can reuse durable project knowledge without collapsing everything into one file.

## Design Philosophy

This docs system borrows from Domain-Driven Design: organize durable knowledge around project domains and bounded contexts, keep shared vocabulary explicit, and place each convention where its scope belongs. `docs/DOCS.md` is the repository knowledge protocol for cross-domain language, collaboration conventions, and boundary principles; `docs/<domain>/DOCS.md` carries the same kind of shared principles inside one domain; index files act as a context map, and leaf docs capture stable knowledge inside one focused subdomain. Living docs state the current truth. Optional adjacent same-name `.adr.md` companions preserve the decisions and rationale that explain that truth. Do not force tactical DDD patterns into the docs unless the project itself uses them.

## Follow This Workflow

1. Inspect the current docs state.
   - Read `AGENTS.md`, `docs/DOCS.md`, and `docs/index.md` if they exist.
   - If `docs/index.md` exists, read relevant `docs/<domain>/DOCS.md` and `docs/<domain>/index.md` files before editing leaf docs.
   - When a relevant living doc links an adjacent `.adr.md` companion, read it for decision context; do not treat it as the authority for current behavior.
   - Treat `docs/` as initialized only when compatible `docs/DOCS.md` (Project Knowledge Protocol) and `docs/index.md` files exist.
   - Detect whether the repository already has a docs convention and preserve it when possible.

2. Use the starter layout in [references/docs-layout.md](./references/docs-layout.md).
   - Create or maintain the core files.
   - Keep file roles distinct.
   - Reuse the standard frontmatter keys and section layout.
   - When creating a new leaf doc, copy the structure in [references/subdomain-doc-template.md](./references/subdomain-doc-template.md).
   - When a qualifying decision needs durable rationale, copy [references/adr-companion-template.md](./references/adr-companion-template.md) into an adjacent same-name `<stem>.adr.md` file.
   - Allow deeper docs scopes when they are useful and indexed.
   - Treat non-Markdown resource directories under `docs/` as outside docs layout validation.

3. Sort knowledge before writing.
   - Put cross-domain language, collaboration conventions, and boundary principles in `docs/DOCS.md`.
   - Put domain-level language, conventions, and boundary principles shared by multiple subdomain docs in `docs/<domain>/DOCS.md`.
   - Put domain navigation in `docs/<domain>/index.md`.
   - Put stable subdomain knowledge in `docs/<domain>/<subdomain>.md` by default, or in a deeper indexed scope when the project needs another grouping level.
   - Add a `## Domain Language` section only when a docs file depends on confirmed project-specific terms.
   - Put current behavior, boundaries, and conventions in the living doc.
   - Add an ADR entry only when a decision is hard to reverse, surprising without context, and the result of a real trade-off.
   - Put the decision and its rationale in the adjacent ADR companion; keep implementation mechanics in code and link concrete files when useful.
   - Do not add an inline `## Decision Records` section to a living doc.
   - Do not use ADR companions as a general incident log. A repository may preserve an explicit local customization, but incident history is not the default contract.
   - Do not store short-lived debugging notes or one-off session details.

4. Keep `AGENTS.md` as the entry point.
   - If `docs/` is initialized, ensure `AGENTS.md` includes this exact rules block:

```md
<!-- BEGIN:docs-system-rules -->
# This is NOT the docs system you know

This repository maintains project-specific knowledge and conventions in `docs/`; start with `docs/index.md` and `docs/DOCS.md`, then follow links into `docs/<domain>/DOCS.md`, `docs/<domain>/index.md`, and `docs/<domain>/<subdomain>.md` as needed, treat `docs/` as the source of durable non-obvious project practices, and use the installed `$project-docs-system` skill when initializing, maintaining, or updating this docs system.
<!-- END:docs-system-rules -->
```

   - If `docs/` is not initialized yet, do not add the rules block yet.

5. Keep maps complete.
   - When adding a first-level domain, create both `docs/<domain>/DOCS.md` and `docs/<domain>/index.md`.
   - When adding, renaming, merging, or removing non-ADR Markdown docs files, update the nearest parent `index.md` in the same change.
   - When adding, renaming, merging, or removing a child docs directory, update the nearest parent `index.md` with the child `index.md` link in the same change.
   - When adding, renaming, merging, or removing first-level domains, update `docs/index.md` in the same change.
   - Omit `.adr.md` companions from generated catalogs and index-coverage requirements. A repository may add a manual index link when decision history is intentionally first-class navigation.

6. Update docs during normal work, not as an afterthought.
   - After a user correction, update the relevant docs file in the same task when possible.
   - After a new module or workflow appears, add or extend the relevant domain and subdomain docs.
   - Prefer short, durable bullets over long narrative notes.

## Editing Rules

- Preserve the repository's chosen freshness key if one already exists.
- When bootstrapping a new system from scratch, use the frontmatter keys in [references/docs-layout.md](./references/docs-layout.md).
- Keep docs files scoped and stable; move repeated domain-level knowledge into `docs/<domain>/DOCS.md` and repeated cross-domain knowledge into `docs/DOCS.md`.
- Keep `## Domain Language` short: use one-sentence definitions, optional `_Avoid_: ...`, and optional `Related: ...`; skip the section when no confirmed terms are needed.
- Name a companion by inserting `.adr` before `.md`: `DOCS.md` → `DOCS.adr.md`, `routing.md` → `routing.adr.md`.
- Keep one companion per living doc and one decision per dated entry. Prefer `## YYYY-MM-DD short-decision-slug` for new entries; preserve an existing repository's dated heading or dated-list style when it is already consistent. A companion may contain multiple entries.
- Give newly created companions bidirectional adjacent Markdown links: the living doc links `./<stem>.adr.md`, and the companion links `./<stem>.md`. The verifier reports missing links as warnings so an existing customized repository can migrate without a breaking upgrade.
- Never create an empty or orphan ADR companion. Index files do not own ADR companions.
- Keep ADR entries concise by default. Add `Status`, alternatives, or consequences only when they prevent future confusion.
- When status adds value, use one of: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, or `Superseded by YYYY-MM-DD short-decision-slug`.
- Preserve final decision records as history. When a decision changes, add or link a superseding record instead of rewriting the old rationale.
- A proposed or accepted planning decision does not change the living doc until implementation changes current behavior.
- Reference concrete files, routes, or modules when that makes the docs more reusable.
- Treat the 500-line verifier result as a cohesion prompt, not a hard limit. It counts physical author-maintained Markdown lines, excludes generated catalog blocks, warns only above 500, and does not change a successful exit code.

## Final Verification

- Confirm the core docs files exist and are linked together.
- Confirm every docs document starts with frontmatter.
- Confirm every first-level Markdown docs domain has `docs/<domain>/DOCS.md` and `docs/<domain>/index.md`.
- Confirm `docs/index.md` covers every first-level Markdown docs domain.
- Confirm each docs scope `index.md` covers its direct Markdown docs files and child docs scope indexes.
- Confirm living docs contain no inline `## Decision Records` section.
- Confirm each ADR companion has an adjacent living doc and at least one recognizable dated history entry; review any missing-link warnings. New generic companions should still contain a qualifying decision, while explicitly customized repositories may preserve their durable incident convention.
- Confirm generated catalogs omit `.adr.md` companions.
- When shell access is available, run the bundled [scripts/verify-docs-system.sh](./scripts/verify-docs-system.sh) with the target repo root or `docs/` directory to verify the docs structure.
- Summarize what was created or updated and why.
