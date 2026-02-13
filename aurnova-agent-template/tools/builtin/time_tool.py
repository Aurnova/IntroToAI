"""Time tool — returns current UTC time string."""
from tools.base import BaseTool
from tools.registry import register
from datetime import datetime, timezone

@register
class TimeTool(BaseTool):
    name = "time"
    description = "Get current UTC time"

    def run(self, **kwargs) -> str:
        return datetime.now(timezone.utc).isoformat()
