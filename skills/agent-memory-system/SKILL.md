---
name: agent-memory-system
description: Specialized skill for building and maintaining a structured, long-term project memory system for AI agents. Use this to initialize project directories, maintain decision logs, mission files, and MVP specs to ensure cross-session continuity and high-agency execution. Trigger when starting a new project, needing a "brain" for a project, or organizing unstructured work into a persistent system.
---

# Agent Memory System

This skill implements the **"Persistent Project Brain"** protocol for AI agents. It ensures that every decision, mission objective, and technical specification is captured in a structured filesystem that survives session restarts.

## 🧠 Core Principle

**"If it's not in the memory files, the agent didn't learn it."** 

This system moves project state from volatile LLM context to a permanent, human-readable, and agent-queryable filesystem structure.

## 📂 System Architecture

All memory artifacts are stored in `projects/<project-slug>/`:

- `00-mission.md`: The "Why" and "What". High-level objectives and kill criteria.
- `01-decisions.md`: The "How". An append-only log of every major technical and product decision.
- `02-mvp-spec.md`: The "Scope". Strict definition of the minimum viable product.
- `03-design.md`: The "Experience". User flows, wireframes, and UI/UX logic.
- `04-build-log.md`: The "Process". Record of implementation progress and technical blockers.
- `05-validate-report.md`: The "Quality". Verification results, test passes, and DoD checks.
- `06-ship-report.md`: The "Outcome". Release notes, deployment IDs, and rollback plans.
- `07-iteration-log.md`: The "Learning". Post-launch feedback and data-driven hypothesis tests.

## 🛠 Usage Patterns

### 1. Initialize Project Memory
When starting a new project:
1. Create `projects/<project-slug>/` directory.
2. Initialize `00-mission.md` with the core intent.
3. Record the first decision in `01-decisions.md` (e.g., "Choosing Next.js for the frontend").

### 2. The Decision Log (01-decisions.md)
Every time a choice is made (tech stack, UI component, API logic), append a block:
```markdown
### [YYYY-MM-DD HH:mm] Decision: <Title>
- **Context**: Why are we making this decision now?
- **Options Considered**: Option A, Option B, Option C.
- **Decision**: We chose Option B.
- **Rationale**: Best trade-off between speed and maintainability.
- **Impact**: Affects the `src/lib/auth.ts` implementation.
```

### 3. Mission Continuity (00-mission.md)
Update the mission file whenever the high-level goal shifts. Ensure "Kill Criteria" are clearly defined to prevent "zombie projects."

### 4. Definition of Done (DoD)
Before executing a task, record the DoD in `04-build-log.md`. Mark them off as they are completed.

## 🤖 Interaction Protocol

1. **Read First**: Always read the memory files at the start of a session.
2. **Write Last**: Always update the memory files before ending a session or after a milestone.
3. **Reference Often**: When asked "Why did we do X?", query `01-decisions.md`.

---
*Memory is the foundation of agency.* 👾
