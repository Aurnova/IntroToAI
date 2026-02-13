# Aurnova Agent Core — Architecture

## Overview

- **agent/** — Entrypoint (`main.py` CLI, `server.py` FastAPI), config, runtime.
- **llm/** — OpenRouter client, model config.
- **tools/** — Tool base, registry, builtins (time, web stub).
- **memory/** — Store and optional RAG.
- **orchestrator/** — Planner, executor, guardrails; one pass by default.
- **eval/** — Harness and scenario JSON for autograding.

## Server (FastAPI)

- `make serve` runs `uvicorn agent.server:app --host 0.0.0.0 --port 8000`.
- **GET /** — Health check (`{"status":"ok"}`).
- **POST /chat** — Body `{"prompt": "..."}`; same orchestrator as CLI; returns `response`, `usage`, `latency_seconds`.

## Guarantees (out of the box)

With no student changes, `make run`:

1. Loads config from env.
2. Calls OpenRouter with a basic prompt.
3. Routes through orchestrator once.
4. Produces a structured response.
5. Logs token usage and latency.
6. Exits cleanly.

## Extending

- Add tools in `tools/builtin/` and register in `tools/registry.py`.
- Add eval scenarios in `eval/scenarios/`.
- CI runs `pytest` and `make eval` on every PR.
