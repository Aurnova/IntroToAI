# GitHub Classroom setup (for instructors)

Use this guide to run **Intro to AI** with GitHub Classroom so every student gets their own copy of this repo with Codespaces and the optional AI (Qwen3 Coder Next via OpenRouter).

---

## 1. Make this repository a template

1. Open this repo on GitHub: **Aurnova/IntroToAI** (or your fork).
2. Go to **Settings** → **General**.
3. Under **Repository type**, check **Template repository**.
4. Save.

Students will get their own repos created from this template when they accept the assignment.

---

## 2. Create or use a GitHub Classroom

1. Go to [classroom.github.com](https://classroom.github.com) and sign in with GitHub.
2. Create a **Classroom** (e.g. “Intro to AI – Spring 2026”).
3. Link it to the GitHub organization that will own the assignment repos (e.g. your school org or a personal org).

---

## 3. Create an assignment

1. In the Classroom, click **New assignment**.
2. **Choose template:** Pick **Aurnova/IntroToAI** (or your template repo).  
   - If you forked the repo, select your fork and ensure it’s marked as a template (step 1).
3. **Assignment basics:**
   - **Title:** e.g. “Intro to AI – Assignment repository”
   - **Deadline:** optional; set if you want automatic submission timing.
   - **Type:** Individual assignment (or Group assignment if you use teams).
4. **Repository name:** e.g. `intro-to-ai-{{ student_identifier }}` so each student gets a unique repo.
5. **Visibility:** Private (recommended) so only you and the student see the repo.
6. Create the assignment and copy the **invitation link** to share with students.

---

## 4. Give each student an OpenRouter API key ($10/month limit)

**Recommended:** Use one OpenRouter API key per student with a **$10/month** spending limit. The institute creates keys via OpenRouter’s Management API and assigns each key to the student’s repo so Codespaces gets it automatically.

- **Full guide:** [.github/INSTITUTE_OPENROUTER_KEYS.md](INSTITUTE_OPENROUTER_KEYS.md) — create a Management API key, run the provided script to create keys per student and (optionally) set `OPENROUTER_API_KEY` on each repo via GitHub CLI.
- **Summary:** Add credits to one OpenRouter account → create a Management key → run `scripts/create-student-keys.js` with a students CSV → script creates keys (limit $10, reset monthly) and can set the secret on each student repo. Students then get the key automatically in Codespaces.

---

## 5. How students use it

- Students use the **invitation link** → accept the assignment → get a new repo.
- They open that repo in **Codespaces** (Code → Codespaces → Create codespace on main).
- If the institute set repo secrets, the AI key is already available. Otherwise they add `OPENROUTER_API_KEY` (see [README](../README.md)) and use the AI assistants.
- They do work in **`assignments/`** and push to the default branch. You grade by looking at their repo (or using any automation you add).

---

## 6. Grading and submission

- **Submission = latest push** to the default branch (usually `main`) before the deadline, if you set one.
- You can:
  - Open each student repo and review `assignments/` and any linked work.
  - Use GitHub Classroom’s “Download submissions” (if enabled) to get a ZIP of all repos.
  - Add your own GitHub Actions or scripts to run tests and post feedback.

---

## 7. Customizing the template

- **Add assignments:** Edit or add markdown/code under **`assignments/`** in this repo, then update the template (or re-save). New assignments only apply to **new** student repos; existing ones keep their copy unless you give new instructions (e.g. pull from template).
- **Change AI model:** Edit **`.continue/config.yaml`** (e.g. change `model` or `apiBase`). The dev container copies this into the Codespace; students get the update on the next rebuild or new clone.
- **Dev container:** Change **`.devcontainer/devcontainer.json`** to add extensions, env vars, or different base image. Existing Codespaces may need a rebuild (Codespaces → “Rebuild container”) to pick up changes.

---

## Quick checklist

- [ ] Repo is set as **Template repository** (Settings → General).
- [ ] Classroom created and linked to your GitHub org.
- [ ] Assignment created from this template; **invitation link** copied and shared.
- [ ] OpenRouter keys: run [INSTITUTE_OPENROUTER_KEYS.md](INSTITUTE_OPENROUTER_KEYS.md) to create one key per student ($10/month) and set repo secrets (or distribute keys securely).
- [ ] Students know to open their repo in **Codespaces**; the AI key is pre-set if you used the script.
