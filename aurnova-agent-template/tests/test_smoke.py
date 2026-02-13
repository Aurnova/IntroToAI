"""Smoke tests: run without API key when possible."""
import os
import pytest

# Ensure builtin tools are registered
import tools.builtin  # noqa: F401
from tools.registry import get_tool_names
from memory.store import add, list_entries, clear


def test_tool_registry_has_tools():
    names = get_tool_names()
    assert "time" in names
    assert "web" in names


def test_memory_store_interface():
    clear()
    add({"k": "v"})
    entries = list_entries()
    assert len(entries) == 1
    assert entries[0]["k"] == "v"
    clear()
    assert list_entries() == []


def test_eval_harness_produces_json():
    from eval.harness import run_harness
    report = run_harness()
    assert "scenarios_run" in report
    assert "results" in report
    assert isinstance(report["results"], list)


def test_server_app_loads():
    from agent.server import app
    assert app is not None
    routes = [r.path for r in app.routes if hasattr(r, "path")]
    assert "/" in routes
    assert "/chat" in [getattr(r, "path", "") for r in app.routes]
