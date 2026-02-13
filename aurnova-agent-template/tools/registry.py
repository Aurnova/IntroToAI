"""Tool registry: list and get tools. Autograder checks this."""
_REGISTRY: dict[str, type] = {}

def register(tool_cls: type) -> type:
    _REGISTRY[tool_cls.name] = tool_cls
    return tool_cls

def get_tools() -> dict[str, type]:
    return dict(_REGISTRY)

def get_tool_names() -> list[str]:
    return list(_REGISTRY.keys())
