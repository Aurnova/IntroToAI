"""Single-pass orchestration: call LLM, return response and usage."""
from llm.openrouter_client import call_openrouter

def run_once(prompt: str, config: dict) -> tuple[str, dict]:
    content, usage = call_openrouter(
        prompt,
        model=config.get("openrouter_model"),
        api_key=config.get("openrouter_api_key"),
    )
    return content, usage
