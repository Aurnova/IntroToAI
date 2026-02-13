"""Load config from env."""
import os
from pathlib import Path

def get_config():
    return {
        "openrouter_api_key": os.environ.get("OPENROUTER_API_KEY", ""),
        "openrouter_model": os.environ.get("OPENROUTER_MODEL", "openai/gpt-4o-mini"),
        "env_file": Path(__file__).resolve().parent.parent / ".env",
    }
