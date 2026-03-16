#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

PHASE_FILES = {
    "discover": ["00-mission.md", "01-decisions.md"],
    "define": ["02-mvp-spec.md", "01-decisions.md"],
    "design": ["03-design.md", "01-decisions.md"],
    "build": ["04-build-log.md", "01-decisions.md"],
    "validate": ["05-validate-report.md", "01-decisions.md"],
    "ship": ["06-ship-report.md", "01-decisions.md"],
    "iterate": ["07-iteration-log.md", "01-decisions.md"],
}

ORDER = ["discover", "define", "design", "build", "validate", "ship", "iterate"]


def file_ok(path: Path) -> bool:
    return path.exists() and path.stat().st_size > 0


def color_for_ratio(ratio: float) -> str:
    if ratio >= 1.0:
        return "green"
    if ratio >= 0.5:
        return "yellow"
    return "red"


def phase_report(project_dir: Path, phase: str):
    req = PHASE_FILES[phase]
    checks = []
    ok = 0
    for f in req:
        p = project_dir / f
        passed = file_ok(p)
        checks.append({"file": f, "present_nonempty": passed})
        ok += int(passed)
    ratio = ok / len(req)
    return {
        "phase": phase,
        "status": color_for_ratio(ratio),
        "passed": ok,
        "total": len(req),
        "checks": checks,
    }


def main():
    parser = argparse.ArgumentParser(description="Check Product Ship System phase artifact status")
    parser.add_argument("project_slug", help="Project slug under /home/ubuntu/clawd/projects")
    parser.add_argument("--phase", choices=ORDER, help="Single phase to check")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    project_dir = Path("/home/ubuntu/clawd/projects") / args.project_slug
    if not project_dir.exists():
        raise SystemExit(f"Project not found: {project_dir}")

    phases = [args.phase] if args.phase else ORDER
    reports = [phase_report(project_dir, p) for p in phases]

    if args.json:
        print(json.dumps({"project": args.project_slug, "reports": reports}, indent=2))
        return

    print(f"Project: {args.project_slug}")
    for r in reports:
        print(f"- {r['phase']:<8} [{r['status'].upper()}] {r['passed']}/{r['total']}")
        for c in r["checks"]:
            mark = "✅" if c["present_nonempty"] else "❌"
            print(f"    {mark} {c['file']}")


if __name__ == "__main__":
    main()
