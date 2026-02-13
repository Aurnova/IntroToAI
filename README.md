# Intro to AI

A GitHub Classroom–ready course repo for teaching AI. Use **GitHub Codespaces** for a consistent dev environment and a **Cursor-like AI assistant** (Qwen3 Coder Next via OpenRouter) inside the IDE.

---

## For students

### 1. Accept the assignment

- Use the **GitHub Classroom invitation link** from your instructor.
- This creates your own copy of this repo (e.g. `intro-to-ai-yourusername`).

### 2. Open in Codespaces

- In your assignment repo, click **Code** → **Codespaces** → **Create codespace on main** (or **Open in Codespaces**).
- Wait for the dev container to build. You’ll get VS Code in the browser with the course setup.

### 3. Enable the AI assistants (optional but recommended)

You get **two AI panels**, both using **Qwen3 Coder Next** (OpenRouter):

- **Cursor-like AI (Continue)** – Right sidebar. Chat, edit code, apply changes, and tab completion. Use for coding help and implementation.
- **Tutor AI** – Right sidebar, separate tab (book icon). Socratic tutor: explains concepts, asks questions, gives hints instead of full answers. Use for learning and understanding.

1. Get a free API key: [OpenRouter → Keys](https://openrouter.ai/settings/keys).
2. In your Codespace:
   - **Settings (gear)** → **Codespaces** → **Repository and organization secrets**
   - Add a secret: name `OPENROUTER_API_KEY`, value = your OpenRouter API key.
3. Rebuild or recreate the codespace so the secret is available.
4. **Continue:** Open the Continue panel (robot icon). Select **Qwen3 Coder Next (OpenRouter)** for coding.
5. **Tutor AI:** Open the right sidebar (secondary sidebar), then the **Tutor AI** tab (book icon). Chat there for conceptual help and guided learning.

### 4. Do the assignments

- Work is in the **`assignments/`** folder.
- Follow each assignment’s README; write code and answers in the places indicated.
- Commit and push when you’re done. Your instructor will see your repo (and any configured submission flow).

### 5. Submitting

- Push your latest work to the `main` (or default) branch.
- If your instructor uses **GitHub Classroom** with a deadline, make sure you push before the due date.
- If they use a specific branch or tag for submission, follow their instructions.

---

## For teachers

- **Repository:** [Aurnova/IntroToAI](https://github.com/Aurnova/IntroToAI)
- **Use this repo as a GitHub Classroom template.**  
  See [.github/CLASSROOM_SETUP.md](.github/CLASSROOM_SETUP.md) for:
  - Making this repo a template
  - Creating a Classroom and assignment
  - Optional: providing an OpenRouter key via Classroom/organization secrets

---

## Repo layout

| Path | Purpose |
|------|--------|
| `assignments/` | Assignment prompts and where students put work |
| `.devcontainer/` | Codespaces dev container (VS Code + Continue + Tutor AI) |
| `.continue/` | AI model config (Qwen3 Coder Next via OpenRouter) |
| `tutor-ai-panel/` | Tutor AI VS Code extension (right-tab Socratic tutor) |

---

## Tech stack

- **Environment:** GitHub Codespaces (VS Code in the cloud)
- **AI in the IDE:** Continue (cursor-like coding) + Tutor AI (right-tab Socratic tutor), both → OpenRouter → **qwen/qwen3-coder-next**
- **No local install required** for students beyond a browser and a GitHub account.
