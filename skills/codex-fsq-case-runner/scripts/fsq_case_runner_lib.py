#!/usr/bin/env python3
"""Shared helpers for FSQ Codex case runner scripts."""

from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
import re
from typing import Any

import yaml

BACKENDS = {
    "windows": "pywinauto-mcp",
    "macos": "appium-mcp",
    "ios": "appium-mcp",
    "android": "appium-mcp",
}


def repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(Path.cwd().resolve()))
    except ValueError:
        return str(path)


def load_case_metadata(path: Path) -> dict[str, Any]:
    docs = list(yaml.safe_load_all(path.read_text(encoding="utf-8")))
    if len(docs) != 2 or not isinstance(docs[0], dict):
        raise ValueError(f"{path} is not a two-document FSQ testcase")
    config = docs[0]
    platform = config.get("platform")
    parts = path.parts
    area = None
    if "fsq-testcases" in parts:
        idx = parts.index("fsq-testcases")
        if len(parts) > idx + 2:
            area = parts[idx + 2]
    return {
        "path": repo_relative(path),
        "name": config.get("name", path.stem),
        "platform": platform,
        "backend": infer_backend(platform),
        "area": area,
        "tags": config.get("tags", []) or [],
    }


def infer_backend(platform: str | None) -> str:
    if platform not in BACKENDS:
        raise ValueError(f"unsupported or missing platform: {platform}")
    return BACKENDS[platform]


def discover_cases(
    cases_root: str | Path,
    platform: str | None = None,
    area: str | None = None,
    tags: list[str] | None = None,
    exclude_tags: list[str] | None = None,
    limit: int | None = None,
) -> list[dict[str, Any]]:
    root = Path(cases_root)
    if root.is_file():
        paths = [root]
    else:
        paths = sorted(root.glob("**/*.codex.yaml"))
    selected: list[dict[str, Any]] = []
    required_tags = set(tags or [])
    blocked_tags = set(exclude_tags or [])
    for path in paths:
        meta = load_case_metadata(path)
        case_tags = set(meta.get("tags", []))
        if platform and meta.get("platform") != platform:
            continue
        if area and meta.get("area") != area:
            continue
        if required_tags and not required_tags.issubset(case_tags):
            continue
        if blocked_tags and blocked_tags.intersection(case_tags):
            continue
        selected.append(meta)
        if limit is not None and len(selected) >= limit:
            break
    return selected


def make_run_id(now: datetime | None = None) -> str:
    current = now or datetime.now(timezone.utc)
    return "codex-" + current.astimezone().strftime("%Y%m%d-%H%M%S")


def slug_path(path: str | Path) -> str:
    raw = str(path).replace(".codex.yaml", "")
    slug = re.sub(r"[^A-Za-z0-9]+", "-", raw).strip("-").lower()
    return slug or "case"


def write_json(path: str | Path, data: Any) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def append_jsonl(path: str | Path, item: Any) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(item, sort_keys=True) + "\n")


def build_manifest(
    cases: list[dict[str, Any]],
    schema: str | Path,
    output_root: str | Path,
    run_id: str,
) -> dict[str, Any]:
    return {
        "runId": run_id,
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "schema": repo_relative(Path(schema)),
        "outputRoot": repo_relative(Path(output_root) / run_id),
        "backendDefaults": BACKENDS,
        "cases": cases,
    }
