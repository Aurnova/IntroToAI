"""Web tool stub — placeholder for future HTTP fetch."""
from tools.base import BaseTool
from tools.registry import register

@register
class WebToolStub(BaseTool):
    name = "web"
    description = "Fetch URL (stub)"

    def run(self, url: str = "", **kwargs) -> str:
        return f"stub: would fetch {url or 'no url'}"
