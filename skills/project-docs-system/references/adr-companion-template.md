---
title: ADR Companion Template
description: Reference template for an adjacent same-name decision rationale companion.
updateAt: YYYY-MM-DD
---

# Living Doc Decision Records

[Current living document](./<stem>.md)

## YYYY-MM-DD short-decision-slug

We chose X over Y because Z. The main consequence is C.

<!-- Add only the fields that prevent future confusion:
Status: Proposed | Accepted | Rejected | Deprecated | Superseded by YYYY-MM-DD short-decision-slug
Context: Why this decision came up.
Alternatives: Meaningful options that were rejected and why.
Decision: The chosen path.
Consequences: The main cost, constraint, or follow-up.
-->

## How To Use

- Rename this file by inserting `.adr` before the living doc's `.md` suffix: `routing.md` becomes `routing.adr.md`.
- Replace `<stem>.md` with the adjacent living document's basename and add the reverse `./<stem>.adr.md` link to that living document.
- Keep one decision per dated lowercase kebab-case heading. One companion may hold multiple decisions.
- Create an entry only when the decision is hard to reverse, surprising without context, and based on a real trade-off.
- Keep what and why here, current truth in the living doc, and implementation mechanics in code.
- Do not create an empty or orphan companion. Do not create `index.adr.md`.
- Preserve superseded decisions as history instead of rewriting their original rationale.
