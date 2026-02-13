# Intro to AI

A GitHub Classroom–ready course repo for teaching AI. Use **GitHub Codespaces** for a consistent dev environment and a **Cursor-like AI assistant** (Qwen3 Coder Next via OpenRouter) inside the IDE.

---

## Test in Codespaces

1. **Add your OpenRouter key** so the container can use the AI:
   - On GitHub: open this repo → **Settings** → **Secrets and variables** → **Codespaces** → **New repository secret**
   - Name: `OPENROUTER_API_KEY`, Value: your key from [OpenRouter](https://openrouter.ai/settings/keys)
2. **Start a codespace:** **Code** → **Codespaces** → **Create codespace on main**
3. **Wait for the dev container** to finish building. In the terminal you should see: cloning ai-ide and ai-tutor, then “Continue config installed”, “Tutor AI extension installed”, and “Done.”
4. **Reload the window** once (Command Palette → **Developer: Reload Window**) so the Tutor AI extension is picked up.
5. **Test Continue:** Open the **Continue** panel (sidebar), choose **Qwen3 Coder Next (OpenRouter)**, send a message.
6. **Test Tutor AI:** Open the **right sidebar** (View → Appearance → Secondary Side Bar), click the **Tutor AI** (book) icon, send a message.

If the key is missing, Continue and Tutor AI will show an error; add the secret and rebuild the codespace.

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

**API key:** Your institution provides one OpenRouter API key per student (with a $10/month limit). It is usually already set as a secret on your assignment repo so Codespaces picks it up automatically. If not, your instructor will give you the key; add it as a **repository secret** named `OPENROUTER_API_KEY` (repo **Settings** → **Secrets and variables** → **Actions** → **New repository secret**), or in **Codespaces** → **Repository and organization secrets**. If your course does not provide keys, you can [create your own key](https://openrouter.ai/settings/keys) and add it the same way.
4. Rebuild or recreate the codespace if you added a secret so it’s available.
5. **Continue:** Open the Continue panel (robot icon). Select **Qwen3 Coder Next (OpenRouter)** for coding.
6. **Tutor AI:** Open the right sidebar (secondary sidebar), then the **Tutor AI** tab (book icon). Chat there for conceptual help and guided learning.

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
- **Course site (GitHub Pages):** The `docs/` folder is set up as a Jekyll site with course description, syllabus, and readings. To publish it: **Settings** → **Pages** → **Build and deployment** → **Source**: Deploy from a branch → **Branch**: `main`, **Folder**: `/docs` → Save. The site will be at `https://<org>.github.io/IntroToAI/` (or your custom domain).
- **Use this repo as a GitHub Classroom template.**  
  See [.github/CLASSROOM_SETUP.md](.github/CLASSROOM_SETUP.md) for template and assignment setup.
- **Using Google Classroom?**  
  See [.github/GOOGLE_CLASSROOM_SETUP.md](.github/GOOGLE_CLASSROOM_SETUP.md) to create the Google Classroom “Intro to AI,” link it with GitHub Classroom (roster import), and create assignments.
- **Provide one OpenRouter key per student ($10/month limit):**  
  See [.github/INSTITUTE_OPENROUTER_KEYS.md](.github/INSTITUTE_OPENROUTER_KEYS.md) for creating keys and assigning them to student repos.
- **IDE and Tutor** live in separate repos ([ai-ide](https://github.com/Aurnova/ai-ide), [ai-tutor](https://github.com/Aurnova/ai-tutor)); see [.github/REPOS.md](.github/REPOS.md).

---

## Repo layout

| Path | Purpose |
|------|--------|
| `docs/` | GitHub Pages site (course description, syllabus, readings) |
| `assignments/` | Assignment prompts and where students put work |
| `.devcontainer/` | Codespaces dev container; pulls [ai-ide](https://github.com/Aurnova/ai-ide) and [ai-tutor](https://github.com/Aurnova/ai-tutor) at build time |
| `scripts/` | Institute script: create per-student OpenRouter keys ($10/mo limit) |

---

## Tech stack

- **Environment:** GitHub Codespaces (VS Code in the cloud)
- **AI in the IDE:** Continue (cursor-like coding) + Tutor AI (right-tab Socratic tutor), both → OpenRouter → **qwen/qwen3-coder-next**
- **No local install required** for students beyond a browser and a GitHub account.
