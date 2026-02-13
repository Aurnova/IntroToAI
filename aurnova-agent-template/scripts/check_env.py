"""
Check that env is ready (OPENROUTER_API_KEY). Don't fail on first boot — print guidance.
"""
import os
import sys

def main():
    key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if key:
        print("OPENROUTER_API_KEY is set.")
        return 0
    print(
        "OPENROUTER_API_KEY is not set. To run the agent:\n"
        "  1. Get a key from https://openrouter.ai/settings/keys\n"
        "  2. In Codespaces: Settings → Codespaces → Secrets → New secret\n"
        "     Name: OPENROUTER_API_KEY, Value: <your key>\n"
        "  3. Rebuild or recreate the codespace."
    )
    return 0  # don't fail so devcontainer can finish

if __name__ == "__main__":
    sys.exit(main())
