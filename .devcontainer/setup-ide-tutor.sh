#!/bin/bash
set -e
IDE_REPO="${AI_IDE_REPO:-Aurnova/ai-ide}"
TUTOR_REPO="${AI_TUTOR_REPO:-Aurnova/ai-tutor}"
BRANCH="${AI_BRANCH:-main}"

echo "==> Cloning $IDE_REPO and $TUTOR_REPO (branch: $BRANCH)..."
git clone --depth 1 -b "$BRANCH" "https://github.com/${IDE_REPO}.git" /tmp/ai-ide && echo "  ai-ide OK" || echo "  ai-ide clone failed"
git clone --depth 1 -b "$BRANCH" "https://github.com/${TUTOR_REPO}.git" /tmp/ai-tutor && echo "  ai-tutor OK" || echo "  ai-tutor clone failed"

mkdir -p /home/vscode/.continue
if [ -f /tmp/ai-ide/.continue/config.yaml ]; then
  cp /tmp/ai-ide/.continue/config.yaml /home/vscode/.continue/config.yaml
  echo "==> Continue config installed"
fi

if [ -d /tmp/ai-tutor ]; then
  echo "==> Building Tutor AI extension..."
  (cd /tmp/ai-tutor && npm install && npm run compile)
  EXT=/home/vscode/.vscode-server/extensions
  mkdir -p "$EXT/aurnova.tutor-ai-panel-0.1.0"
  cp /tmp/ai-tutor/package.json "$EXT/aurnova.tutor-ai-panel-0.1.0/"
  cp -r /tmp/ai-tutor/out /tmp/ai-tutor/resources "$EXT/aurnova.tutor-ai-panel-0.1.0/"
  echo "==> Tutor AI extension installed"
fi

echo "==> Done. Reload the window (Ctrl/Cmd+Shift+P -> Developer: Reload Window) if Tutor AI does not appear."
