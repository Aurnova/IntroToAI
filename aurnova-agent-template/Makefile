.PHONY: setup run serve test eval format

setup:
	pip install -e ".[dev]"
	cp -n .env.example .env 2>/dev/null || true

run:
	python -m agent.main

serve:
	uvicorn agent.server:app --host 0.0.0.0 --port 8000

test:
	pytest -q tests/

eval:
	python -m eval.harness

format:
	ruff format agent llm tools memory orchestrator eval tests scripts
	ruff check agent llm tools memory orchestrator eval tests scripts
