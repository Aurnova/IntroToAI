# A1: Git Workflow

**Due:** End of Week 2.  
**Repo:** Your persistent agent repo (same as A0).

## Goals

- Create a branch, make a small change, open a PR.
- Add a short “How to run” section to the repo README.
- Use the code review checklist (if provided).

## Tasks

1. **Create a branch**  
   From `main`:
   ```bash
   git checkout -b a1/git-practice
   ```

2. **Update README**  
   In the repo root `README.md`, add a **“How to run”** section (or expand the existing one) so that a new reader can:
   - Install deps: `make setup`
   - Run the agent: `make run` (and note that `OPENROUTER_API_KEY` is required)
   - Run tests: `make test`
   - Run eval: `make eval`  
   Keep it to 4–6 lines; no need to repeat the full quick start.

3. **Commit and push**  
   ```bash
   git add README.md
   git commit -m "A1: add How to run section to README"
   git push -u origin a1/git-practice
   ```

4. **Open a PR**  
   - Open a PR from `a1/git-practice` into `main`.  
   - In the description, write one sentence on what you changed.  
   - Ensure CI passes (pytest + make eval).

5. **Code review**  
   - If your instructor uses a PR checklist, complete it.  
   - Address any requested changes; re-push so CI stays green.

## Submission

- PR from `a1/git-practice` → `main`, CI green, README contains a clear “How to run” section.
