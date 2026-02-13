# Repositories

The course uses **three repositories**:

| Repo | Purpose |
|------|--------|
| **Aurnova/IntroToAI** (this repo) | **Course only:** assignments, syllabus, readings (docs/), GitHub Classroom, institute OpenRouter keys script. Devcontainer clones the IDE and Tutor repos and wires them in. |
| **Aurnova/ai-ide** | IDE config: `.continue/config.yaml` for Continue + OpenRouter (Qwen3 Coder Next, Tutor AI model). Not course-specific. |
| **Aurnova/ai-tutor** | Tutor AI VS Code extension (right-sidebar Socratic tutor). Not course-specific. |

When students open this repo in Codespaces, the devcontainer fetches **ai-ide** and **ai-tutor** from GitHub and installs the Continue config and Tutor extension. To override repo or branch (e.g. forks), set in the Codespace:

- `AI_IDE_REPO` (default: `Aurnova/ai-ide`)
- `AI_TUTOR_REPO` (default: `Aurnova/ai-tutor`)
- `AI_BRANCH` (default: `main`)
