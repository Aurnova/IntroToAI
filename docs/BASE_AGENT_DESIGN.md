# Base agent course template design

Design for the **Aurnova Agent Core (AAC)** that works with GitHub Classroom + Codespaces, supports autograding, and runs the full year on one core architecture. **v0.1 is CLI-only;** add FastAPI later if needed.

---

## 1. What you create (org level)

| Repo | Purpose |
|------|---------|
| **aurnova-agent-template** | GitHub Template Repo. Base agent every student forks into their persistent repo. |
| **msai-course-&lt;CODE&gt;** | Instructor repo per course: syllabus, lectures, assignment specs, rubrics, grading keys. |
| **msai-assignment-&lt;CODE&gt;-aN** | (Optional) Per-assignment template repos. Alternatively, all assignments as PRs against the persistent repo. |
| **msai-infra** | Ops: roster mapping (Populi↔GitHub), grade export scripts, SOPs. |

**GitHub Classroom**

- One Classroom per program year/cohort.
- **Assignment 0** creates the persistent repo from `aurnova-agent-template`.

---

## 2. Student workflow (persistent repo + PRs)

- Classroom creates: `msai-2026-agent-<github_user>`.
- Each assignment: student branches (e.g. `a1/...`), opens PR → CI runs tests + eval → instructor grades via rubric + CI evidence → merge → agent evolves.

---

## 3. Base agent template (aurnova-agent-template)

**Location in this repo:** [../aurnova-agent-template](../aurnova-agent-template/)

**Top-level structure:** `.devcontainer/`, `.github/workflows/ci.yml`, `agent/`, `llm/`, `tools/`, `memory/`, `orchestrator/`, `eval/`, `tests/`, `scripts/`, `README.md`, `ARCHITECTURE.md`, `.env.example`, `pyproject.toml`, `Makefile`.

**Core guarantees (unchanged by student):** `make run` loads config from env, calls OpenRouter, routes through orchestrator once, produces structured response, logs token usage & latency, exits cleanly.

**Commands:** `make setup` | `make run` | `make test` | `make eval` | `make format`.

---

## 4. Codespaces devcontainer

- Base image Python 3.11+.
- `postCreateCommand`: install deps, `python scripts/check_env.py` (no fail if key absent—print guidance), `pytest -q tests/test_smoke.py` (may skip if key absent).
- Repo boots even without API key; student is told how to set it.

---

## 5. CI / autograding

- **On PR:** pytest, `make eval`, optional lint/format.
- **Autograder:** required files exist; tool registry returns expected tools; memory module meets interface; eval harness produces JSON report; cost/latency fields present. Rubric handles subjective quality.

---

## 6. Course template (per course)

**Instructor repo (e.g. msai-course-INTRO):** syllabus, `lectures/`, `assignments/` (a0, a1, …), `rubrics/`, `eval_scenarios/`, `gradebook_export/schema.md`. Assignments reference the student’s persistent repo.

**Location in this repo:** [../msai-course-INTRO](../msai-course-INTRO/)

---

## 7. INTRO assignment cadence (example)

- **A0:** Onboarding (pass/fail) — join org, Codespaces, set key, `make run`, evidence in PR.
- **A1:** Git workflow — branch, PR, “How to run” in README.
- A2: Simple tool (e.g. CalculatorTool), register, unit test.
- A3: Logging + telemetry (request_id, model, tokens, latency).
- A4: Prompt/output contract (JSON schema, validator).
- A5: Mini app (CLI `agent ask "..."`, --model, --budget).

---

## 8. Deliverable list (hand to Aurnova)

1. **aurnova-agent-template** — template repo with devcontainer + CI + eval harness (implemented in this repo under `aurnova-agent-template/`).
2. **GitHub Classroom** — Assignment 0: “Create your Agent Repo”; subsequent PR-based assignments.
3. **Instructor repos** — INTRO (started in `msai-course-INTRO/`); Agentic Systems I (certificate) when ready.
4. **Standard rubrics + grading checklist** — A0/A1 rubrics in `msai-course-INTRO/rubrics/`.
5. **Populi↔GitHub roster mapping + grade export schema** — CSV schema in `msai-course-INTRO/gradebook_export/schema.md`; scripts in msai-infra.

---

## 9. Naming

- **Aurnova Agent Core (AAC)** or **Aurnova Core Agent (ACA)** — signature of the program.

---

## 10. Decisions (locked)

- **Language:** Python.
- **Repo model:** Persistent repo + PRs (not per-assignment repos).
- **OpenRouter key:** Per student or small pool (recommended: start per student).
- **v0.1:** CLI + minimal FastAPI server (`make run` and `make serve`; GET / health, POST /chat).
