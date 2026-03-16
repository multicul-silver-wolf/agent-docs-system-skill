# Product Ship System (Next.js)

> **"Turn product intent into shipped outcomes with a persistent project brain."** 👾

This repository contains the **Product Ship System**, a production-grade skill for AI agents (Claude Code, OpenClaw, Codex) designed to manage the end-to-end lifecycle of building and shipping user-loved products.

## 🚀 Why?

Most AI agents can write code, but they struggle to **ship products**. This skill enforces a rigorous, multi-phase operating system that ensures every decision, mission objective, and technical specification is captured in a structured filesystem that survives session restarts.

## 📦 Installation

Install this skill into your agent environment (OpenClaw or Claude Code):

```bash
# Using openclaw
openclaw install https://github.com/multicul-silver-wolf/agent-memory-system-skill/skills/agent-memory-system

# Or clone and install locally
git clone https://github.com/multicul-silver-wolf/agent-memory-system-skill
openclaw install ./agent-memory-system-skill/skills/agent-memory-system
```

## 🧠 Core Methodology

The system operates in 7 distinct phases, each with its own Definition of Done (DoD) and artifacts:

1. **Discover**: Problem validation and ICP check.
2. **Define**: MVP scoping and success metrics.
3. **Design**: User flow mapping and conversion copy.
4. **Build**: Next.js full-stack implementation.
5. **Validate**: Pre-ship checklists and quality gates.
6. **Ship**: Production deployment and release report.
7. **Iterate**: Post-launch feedback and learning loops.

## 📂 Memory Artifacts

All project state is persisted in `projects/<project-slug>/`:

| File | Phase | Purpose |
| :--- | :--- | :--- |
| `00-mission.md` | Discover | High-level goals and kill criteria. |
| `01-decisions.md` | All | **Append-only log** of every major decision. |
| `02-mvp-spec.md` | Define | Strict MVP scope definition. |
| `03-design.md` | Design | Experience and UI/UX logic. |
| `04-build-log.md` | Build | Implementation progress and blockers. |
| `05-validate-report.md` | Validate | Verification and quality gate results. |
| `06-ship-report.md` | Ship | Release notes and rollback plans. |
| `07-iteration-log.md` | Iterate | Qualitative feedback and metrics. |

## 🛠 Usage

Once installed, you can trigger the system by saying:

- *"Build this and ship it: [Idea]"*
- *"I want to launch a product users love."*
- *"Initialize the Product Ship System for [Project Name]"*

## ✨ Features

- **Cross-Session Continuity**: The agent never forgets a decision or goal.
- **Phase Gates**: Prevents "blind building" without validation.
- **Next.js Optimized**: Built-in standards for the modern web stack.
- **AI Agent Friendly**: Optimized for machines to parse and update.

---

Built with 👾 by [Sawana](https://github.com/multicul-silver-wolf). 
Inspired by the **Aether Editing** philosophy.
