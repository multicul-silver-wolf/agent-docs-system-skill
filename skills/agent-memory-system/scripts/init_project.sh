#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 <project-slug>"
  exit 1
fi

ROOT="/home/ubuntu/clawd/projects/$1"
mkdir -p "$ROOT"

touch "$ROOT/00-mission.md" \
      "$ROOT/01-decisions.md" \
      "$ROOT/02-mvp-spec.md" \
      "$ROOT/03-design.md" \
      "$ROOT/04-build-log.md" \
      "$ROOT/05-validate-report.md" \
      "$ROOT/06-ship-report.md" \
      "$ROOT/07-iteration-log.md"

echo "Initialized project artifacts at $ROOT"
