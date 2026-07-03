from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parents[2]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from stock_strategy.dashboard.data_loader import StrategyDashboardLoader  # noqa: E402


STATIC_DIR = BASE_DIR / "stock_strategy" / "dashboard" / "static"
DEFAULT_OUTPUT_DIR = BASE_DIR / "dist" / "strategy_site"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a publishable static strategy site.")
    parser.add_argument("--base-dir", default=str(BASE_DIR))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--clean", action="store_true", help="Remove the output directory before building.")
    return parser.parse_args()


def rewrite_index(html: str) -> str:
    return html.replace('data-api="/api/dashboard"', 'data-api="dashboard.json"').replace(
        'data-file-base="/files"',
        'data-file-base="files"',
    )


def artifact_paths(payload: dict[str, Any]) -> list[str]:
    paths: list[str] = []
    for strategy in payload.get("strategy_catalog", []):
        if not isinstance(strategy, dict):
            continue
        for group in ("reports", "docs", "scripts"):
            for item in strategy.get(group, []) or []:
                if isinstance(item, dict) and item.get("exists") and item.get("path"):
                    paths.append(str(item["path"]))
    return sorted(set(paths))


def copy_artifacts(paths: list[str], base_dir: Path, output_dir: Path) -> int:
    copied = 0
    files_dir = output_dir / "files"
    base_root = base_dir.resolve()
    for relative in paths:
        source = (base_dir / relative).resolve()
        if source != base_root and base_root not in source.parents:
            continue
        if not source.is_file():
            continue
        target = files_dir / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        copied += 1
    return copied


def build_static_site(base_dir: Path, output_dir: Path, clean: bool = False) -> dict[str, Any]:
    if clean and output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for filename in ("app.js", "strategy_order.js", "styles.css"):
        shutil.copy2(STATIC_DIR / filename, output_dir / filename)

    index_html = rewrite_index((STATIC_DIR / "index.html").read_text("utf-8"))
    (output_dir / "index.html").write_text(index_html, "utf-8")

    payload = StrategyDashboardLoader(base_dir).load_dashboard()
    (output_dir / "dashboard.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        "utf-8",
    )

    paths = artifact_paths(payload)
    copied = copy_artifacts(paths, base_dir, output_dir)
    return {
        "output_dir": str(output_dir),
        "strategy_count": len(payload.get("strategy_catalog", [])),
        "artifact_count": len(paths),
        "copied_artifacts": copied,
    }


def main() -> None:
    args = parse_args()
    result = build_static_site(Path(args.base_dir), Path(args.output_dir), clean=args.clean)
    print(json.dumps(result, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
