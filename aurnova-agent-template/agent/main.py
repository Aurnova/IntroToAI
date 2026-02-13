"""
Entrypoint: load config, call orchestrator, produce structured response, log usage.
"""
import json
import os
import time

# Load .env if present
_env = os.environ.get("OPENROUTER_API_KEY")
if not _env:
    try:
        from pathlib import Path
        from dotenv import load_dotenv
        load_dotenv(Path(__file__).resolve().parent.parent / ".env")
    except Exception:
        pass

from agent.config import get_config
from llm.openrouter_client import call_openrouter
from orchestrator.planner import run_once


def main():
    config = get_config()
    if not config["openrouter_api_key"]:
        print('{"error": "OPENROUTER_API_KEY not set. Set it in .env or Codespaces Secrets."}')
        return 1

    start = time.perf_counter()
    prompt = "Respond in one sentence: what is 2+2? Reply with valid JSON: {\"answer\": \"...\"}"
    response, usage = run_once(prompt, config)
    elapsed = time.perf_counter() - start

    out = {
        "response": response,
        "usage": usage or {},
        "latency_seconds": round(elapsed, 3),
    }
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
