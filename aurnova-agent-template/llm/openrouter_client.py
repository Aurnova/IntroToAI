"""Call OpenRouter API; return (content, usage)."""
import os
import httpx

def call_openrouter(prompt: str, model: str | None = None, api_key: str | None = None) -> tuple[str, dict]:
    key = api_key or os.environ.get("OPENROUTER_API_KEY", "")
    if not key:
        return '{"error": "OPENROUTER_API_KEY not set"}', {}
    model = model or os.environ.get("OPENROUTER_MODEL", "openai/gpt-4o-mini")
    url = "https://openrouter.ai/api/v1/chat/completions"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
    }
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    try:
        r = httpx.post(url, json=payload, headers=headers, timeout=30.0)
        r.raise_for_status()
        data = r.json()
        content = (data.get("choices") or [{}])[0].get("message", {}).get("content", "")
        usage = data.get("usage", {})
        return content, usage
    except Exception as e:
        return f'{{"error": "{str(e)[:200]}"}}', {}
