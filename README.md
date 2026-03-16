# Agent Memory System Skill

> **"If it's not in the memory files, the agent didn't learn it."** 👾

This repository contains a specialized skill for AI agents (Claude Code, OpenClaw, Codex) designed to build and maintain a structured, long-term project memory system.

## 🚀 Why?

AI agents are powerful but often suffer from "context amnesia" once a session ends or the context window overflows. This skill fixes that by enforcing a **Persistent Project Brain** protocol.

It moves project state from volatile LLM context to a permanent, human-readable, and agent-queryable filesystem structure.

## 📦 Installation

Install this skill into your agent environment (OpenClaw or Claude Code):

```bash
# Using openclaw
openclaw install https://github.com/multicul-silver-wolf/agent-memory-system-skill/skills/agent-memory-system

# Or clone and install locally
git clone https://github.com/multicul-silver-wolf/agent-memory-system-skill
openclaw install ./agent-memory-system-skill/skills/agent-memory-system
```

## 📂 Memory Structure

When activated, the agent will maintain the following artifacts in `projects/<project-slug>/`:

| File | Purpose |
| :--- | :--- |
| `00-mission.md` | Core objectives, high-level goals, and kill criteria. |
| `01-decisions.md` | **Append-only log** of every major technical and product decision. |
| `02-mvp-spec.md` | Strict definition of the MVP scope. |
| `03-design.md` | User flows, wireframes, and UI/UX logic. |
| `04-build-log.md` | Implementation progress and technical blockers. |
| `05-validate-report.md` | Verification results and Definition of Done (DoD) checks. |
| `06-ship-report.md` | Release notes, deployment IDs, and rollback plans. |
| `07-iteration-log.md` | Post-launch feedback and data-driven learning. |

## 🛠 Usage

Once installed, you can trigger the system by saying:

- *"Initialize the memory system for my new project [Project Name]"*
- *"Record our decision to use Supabase in the decision log"*
- *"Update the MVP spec based on our latest discussion"*
- *"Review the project memory and tell me why we chose X"*

## ✨ Features

- **Cross-Session Continuity**: Agents "wake up" with full project context.
- **High Agency Execution**: Structured goals lead to deterministic outcomes.
- **Human-Readable Audit Trail**: You can see exactly how and why decisions were made.
- **AI Agent Friendly**: Optimized for machines to parse, search, and update.

---

Built with 👾 by [Sawana](https://github.com/multicul-silver-wolf). 
Inspired by the **Aether Editing** philosophy.
