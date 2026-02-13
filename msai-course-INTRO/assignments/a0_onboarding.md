# A0: Onboarding (pass/fail)

**Due:** End of Week 1.  
**Repo:** Your persistent agent repo (created by GitHub Classroom from `aurnova-agent-template`).

## Goals

- Join the GitHub org and Classroom.
- Open your agent repo in Codespaces.
- Set `OPENROUTER_API_KEY` in Codespaces secrets.
- Run the agent and confirm it responds.

## Tasks

1. **Accept the Classroom assignment** (Assignment 0: “Create your Agent Repo”).  
   This creates your repo: `msai-2026-agent-<your_github_username>` (or as configured).

2. **Open in Codespaces**  
   In your repo: **Code** → **Codespaces** → **Create codespace on main**.  
   Wait for the dev container to build (postCreateCommand runs `check_env.py` and smoke test).

3. **Set the API key**  
   - Get an OpenRouter key: https://openrouter.ai/settings/keys  
   - In the codespace: **Settings** (gear) → **Codespaces** → **Secrets** → **New secret**  
   - Name: `OPENROUTER_API_KEY`, Value: your key  
   - Rebuild or recreate the codespace so the secret is available.

4. **Run the agent**  
   In the terminal:
   ```bash
   make run
   ```
   You should see JSON output with `response`, `usage`, and `latency_seconds`.

5. **Submit**  
   - Create a branch (e.g. `a0/onboarding`).  
   - In the PR description, paste a **screenshot or log output** of `make run` (redact the key if visible).  
   - Optionally add a one-line note in `README.md`: “Checked: make run succeeds with OPENROUTER_API_KEY.”  
   - Open a PR into `main`.  
   - CI must pass (tests + eval).  
   - Instructor will mark A0 complete when the PR is approved.

## Pass criteria

- PR opened with evidence that `make run` was executed successfully.
- CI green (pytest + make eval).
