# Aurnova Agent Core (AAC)

Base agent template for MSAI. Every student gets a persistent repo created from this template via GitHub Classroom. Assignments are submitted as PRs; the agent evolves across the program.

## Quick start

```bash
make setup   # install deps
make run     # run agent once (CLI; requires OPENROUTER_API_KEY)
make serve   # run FastAPI server on :8000 (GET / health, POST /chat)
make test    # unit tests
make eval    # scenario harness
```

- **CLI:** `make run` — one prompt, JSON to stdout.
- **Server:** `make serve` — then `curl http://localhost:8000` (health) or `curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{"prompt":"Hello"}'`.

## Environment

- Copy `.env.example` to `.env` and set `OPENROUTER_API_KEY`, or set it in Codespaces **Secrets**.
- In Codespaces: **Settings** → **Codespaces** → **Secrets** → `OPENROUTER_API_KEY`.

## Structure

See [ARCHITECTURE.md](ARCHITECTURE.md). Core: `agent/`, `llm/`, `tools/`, `memory/`, `orchestrator/`, `eval/`.

## Assignments

Your instructor repo (e.g. `msai-course-INTRO`) lists assignments. You work in this repo: branch per assignment, open PR, pass CI, get feedback.
