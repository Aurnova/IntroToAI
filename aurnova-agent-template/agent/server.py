"""
Minimal FastAPI server: health + POST /chat using the same orchestrator as CLI.
"""
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Load env before config
try:
    from pathlib import Path
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
except Exception:
    pass

from agent.config import get_config
from orchestrator.planner import run_once


class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    response: str
    usage: dict
    latency_seconds: float


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: validate config (don't fail if key missing; 500 on first /chat is ok)
    yield
    # Shutdown
    pass


app = FastAPI(title="Aurnova Agent Core", lifespan=lifespan)


@app.get("/")
def health():
    """Health check for Codespaces / load balancers."""
    return {"status": "ok", "service": "aurnova-agent-core"}


@app.post("/chat", response_model=ChatResponse)
def chat(body: ChatRequest):
    """Single-turn chat: same behavior as `make run`."""
    config = get_config()
    if not config["openrouter_api_key"]:
        raise HTTPException(
            status_code=503,
            detail="OPENROUTER_API_KEY not set. Set it in .env or Codespaces Secrets.",
        )
    start = time.perf_counter()
    response, usage = run_once(body.prompt, config)
    elapsed = time.perf_counter() - start
    return ChatResponse(
        response=response,
        usage=usage or {},
        latency_seconds=round(elapsed, 3),
    )
