# Docs Layout

## Starter File Set

Use this layout when bootstrapping or repairing a project docs system:

- `AGENTS.md`
  - Keep this as the agent entry point.
  - If `docs/` is initialized, include the docs-system rules block.
  - If `docs/` is not initialized, defer adding the block.
- `docs/DOCS.md`
  - Act as the repository knowledge protocol.
  - Store cross-domain language, collaboration conventions, and boundary principles.
- `docs/DOCS.adr.md` (optional)
  - Preserve qualifying repository-wide decisions and rationale.
- `docs/index.md`
  - Act as the map for first-level domains.
- `docs/<domain>/DOCS.md`
  - Store domain-level language, conventions, and boundary principles shared by multiple subdomain docs.
- `docs/<domain>/DOCS.adr.md` (optional)
  - Preserve qualifying domain-wide decisions and rationale.
- `docs/<domain>/index.md`
  - Act as the map for second-level docs in one domain.
- `docs/<domain>/<subdomain>.md`
  - Store current durable knowledge that only applies to one subdomain.
- `docs/<domain>/<subdomain>.adr.md` (optional)
  - Preserve qualifying subdomain decisions and rationale.

This is the default starter shape for small and medium projects. Larger projects may add deeper docs scopes such as `docs/application/homepage/replication.md` when each docs directory has an `index.md` that maps direct Markdown files and child docs directories. Directories that only contain non-Markdown resources, such as images, are outside docs layout validation. Deeper scopes may add `DOCS.md` only when that scope has shared protocol or language worth preserving.

## AGENTS Rules Block

Treat `docs/` as initialized only when compatible `docs/DOCS.md` (Project Knowledge Protocol) and `docs/index.md` files exist. When initialized, ensure `AGENTS.md` includes this exact block:

```md
<!-- BEGIN:docs-system-rules -->
# This is NOT the docs system you know

This repository maintains project-specific knowledge and conventions in `docs/`; start with `docs/index.md` and `docs/DOCS.md`, then follow links into `docs/<domain>/DOCS.md`, `docs/<domain>/index.md`, and `docs/<domain>/<subdomain>.md` as needed, treat `docs/` as the source of durable non-obvious project practices, and use the installed `$project-docs-system` skill when initializing, maintaining, or updating this docs system.
<!-- END:docs-system-rules -->
```

## Frontmatter

Every docs document should start with frontmatter. When creating a new system, use at least:

```yaml
---
title: Example Title
description: One-line description of what this docs file covers.
updateAt: YYYY-MM-DD
---
```

## File Roles

### `docs/DOCS.md`

Store:

- durable cross-domain terminology and confirmed meanings
- collaboration conventions that affect multiple domains
- boundary principles for ownership, responsibility, or placement
- recurring user preferences that affect many tasks
- architectural expectations that show up repeatedly

Avoid:

- domain-specific implementation notes
- unconfirmed or speculative terminology
- temporary debugging observations
- one-off task status

Use this default structure when bootstrapping:

```md
# Project Knowledge Protocol

## Domain Language

- **Term**: One-sentence definition.
  _Avoid_: ambiguous or rejected names
  Related: **OtherTerm**

## Collaboration Conventions

- Durable project-wide conventions that affect multiple domains.

## Boundary Principles

- Cross-domain ownership, responsibility, or placement rules.
```

### `docs/index.md`

Include:

- a short usage note
- one entry per first-level domain
- when to consult each domain

Use this minimal map template:

```md
# Docs Index

## Domains

- [Domain Name](./domain/index.md): When to consult this domain.
```

### `docs/<domain>/DOCS.md`

Store current domain-level language, conventions, and boundary principles shared by multiple subdomain docs. Put qualifying domain-wide decision rationale in adjacent `DOCS.adr.md`.

### `docs/<domain>/index.md`

Include:

- a short usage note for that domain
- one entry per direct `docs/<domain>/<subdomain>.md` file or child docs scope
- when to consult each subdomain doc or child docs scope

Use this minimal map template:

```md
# Domain Name

## Subdomains

- [Subdomain Name](./subdomain.md): When to consult this doc.
```

### `docs/<domain>/<subdomain>.md`

Store:

- optional `## Domain Language` terms needed to understand this doc
- subdomain-specific conventions
- ownership boundaries
- stable file or route relationships
- user corrections that only matter in that subdomain
- an optional link to adjacent decision rationale in `<subdomain>.adr.md`

Prefer one clear subdomain per file, such as:

- `docs/frontend/routing.md`
- `docs/frontend/data-fetching.md`
- `docs/backend/api-contracts.md`
- `docs/backend/auth-flow.md`

## ADR Companions

Create an adjacent same-name `<stem>.adr.md` companion only when a decision meets all three conditions:

- It is hard to reverse.
- It would surprise a future reader without context.
- It came from a real trade-off between meaningful options.

The living doc is the authority for what is true now. The companion owns what was decided and why. Code owns implementation mechanics. Use the companion template in [adr-companion-template.md](./adr-companion-template.md).

Prefer one dated slug heading per new decision:

```md
## YYYY-MM-DD short-decision-slug

We chose X over Y because Z. The main consequence is C.
```

Use the date when the decision is first recorded. Keep the slug lowercase kebab-case and stable for future references. When a customized repository already uses consistent dated headings or dated list entries, preserve that format instead of mechanically rewriting its history. Add `Status`, alternatives, or consequences only when useful. Valid statuses are `Proposed`, `Accepted`, `Rejected`, `Deprecated`, or `Superseded by YYYY-MM-DD short-decision-slug`.

Keep the record at the same scope as the decision:

- Repo-wide decisions belong in `docs/DOCS.adr.md`, adjacent to `docs/DOCS.md`.
- Domain-wide decisions belong in `docs/<domain>/DOCS.adr.md`, adjacent to `docs/<domain>/DOCS.md`.
- Subdomain decisions belong in `<subdomain>.adr.md`, adjacent to the living subdomain doc.

New living docs and companions must link to each other with adjacent relative Markdown links. Missing links in an existing customized repository produce verifier warnings rather than a breaking error, so they can be migrated deliberately. Do not create empty or orphan companions, and do not attach companions to `index.md`. A proposed or accepted planning decision does not change the living doc until implementation changes current behavior.

Preserve final decision records as history. If a decision changes, update its status or add a superseding entry instead of rewriting the old rationale. Do not use ADR companions as generic incident logs unless the repository explicitly customizes the convention.

Generated catalogs omit `.adr.md` files, and parent indexes do not have to cover them. Manual index links are allowed when a repository deliberately treats decision history as first-class navigation.

## Placement Rules

Use this decision rule before writing:

- If knowledge should apply across the repository, put it in `docs/DOCS.md`.
- If knowledge is shared by multiple subdomain docs inside one domain, put it in `docs/<domain>/DOCS.md`.
- If a confirmed project-specific term is needed in one docs file, put it in that file's optional `## Domain Language` section.
- If a decision record is needed, put it in the adjacent same-name ADR companion matching the decision scope.
- If it maps first-level navigation, put it in `docs/index.md`.
- If it maps second-level navigation, put it in `docs/<domain>/index.md`.
- If it maps a deeper docs scope, put it in that scope's `index.md`.
- If it only matters for one subdomain, put it in `docs/<domain>/<subdomain>.md` or a deeper indexed docs file when the project needs that grouping.
- If it is too temporary to help future work, do not store it.

## Update Triggers

Update the relevant docs file when:

- the user corrects the agent
- the user clarifies a stable project convention
- a new module, route, feature, or workflow becomes important enough to remember
- an existing domain or subdomain changes ownership, structure, or boundaries

Also update map files whenever docs files or docs directories change:

- Update the nearest parent `index.md` when its direct non-ADR docs files or child docs directories change.
- Update `docs/index.md` when first-level domains change.
- Do not update generated catalog coverage merely because an `.adr.md` companion was added or removed.

## Cohesion Warning

The verifier emits a warning when any Markdown document has more than 500 author-maintained physical lines. Lines inside `<!-- BEGIN:docs-generated-catalog -->` and `<!-- END:docs-generated-catalog -->` are excluded. The warning includes the repository-relative path, actual count, threshold, and a prompt to consider splitting along cohesive DDD bounded-context or subdomain boundaries. It never changes an otherwise successful exit code.

## Verification Helper

When shell access is available and structure has changed, optionally run the bundled [scripts/verify-docs-system.sh](../scripts/verify-docs-system.sh) with the target repo root or `docs/` directory to verify the minimum docs-system contract.
