"""Base class for tools."""
from abc import ABC, abstractmethod

class BaseTool(ABC):
    name: str = "base"
    description: str = ""

    @abstractmethod
    def run(self, **kwargs) -> str:
        pass
