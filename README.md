# Project Memory System Skill

> **"Build and maintain a layered memory system for durable project knowledge."** 👾

This repository contains a specialized skill for AI agents (Claude Code, OpenClaw, Codex) designed to bootstrap, audit, or maintain a repository-specific project memory system centered on `AGENTS.md`, `MEMORY.md`, and `.memory/*.md`.

## 🚀 Why?

Durable project knowledge often gets lost in long chat threads. This skill enforces a structured approach to saving "what we learned" directly into the repository, ensuring that future agent sessions can pick up exactly where we left off.

## 📦 Installation

Install this skill into your agent environment (OpenClaw or Claude Code):

```bash
# Using openclaw
openclaw install https://github.com/multicul-silver-wolf/agent-memory-system-skill/skills/project-memory-system

# Or clone and install locally
git clone https://github.com/multicul-silver-wolf/agent-memory-system-skill
openclaw install ./agent-memory-system-skill/skills/project-memory-system
```

## 📂 System Architecture

The system uses a canonical file set to separate cross-domain knowledge from module-specific details:

- **`AGENTS.md`**: The entry point for agents. Links to the memory system.
- **`MEMORY.md`**: Durable, cross-domain conventions and recurring user preferences.
- **`.memory/index.md`**: The map for domain-specific memory files.
- **`.memory/<domain>.md`**: Stable knowledge that only applies to one module, route, or feature.

## 🛠 Usage

Trigger the skill in your chat:

- *"Bootstrap the project memory system in this repo"*
- *"Update the memory for the 'api' domain with our new auth pattern"*
- *"Audit our current memory files and link them in AGENTS.md"*
- *"Check the project memory to see why we chose this architecture"*

---

Built with 👾 by [Sawana](https://github.com/multicul-silver-wolf). 
Inspired by the **Aether Editing** philosophy.
