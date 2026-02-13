"""Simple in-memory store. Meets interface for autograder."""
_store: list[dict] = []

def add(entry: dict) -> None:
    _store.append(entry)

def list_entries() -> list[dict]:
    return list(_store)

def clear() -> None:
    _store.clear()
