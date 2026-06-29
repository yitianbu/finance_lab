from __future__ import annotations

import json
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse

from stock_strategy.dashboard.data_loader import DEFAULT_BASE_DIR, StrategyDashboardLoader


STATIC_DIR = Path(__file__).with_name("static")


class StrategyDashboardHandler(SimpleHTTPRequestHandler):
    base_dir: Path = DEFAULT_BASE_DIR
    static_dir: Path = STATIC_DIR

    def log_message(self, format: str, *args: Any) -> None:
        return

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/api/dashboard":
            self._send_dashboard()
            return
        self._send_static(parsed.path)

    def _send_dashboard(self) -> None:
        payload = StrategyDashboardLoader(self.base_dir).load_dashboard()
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_static(self, request_path: str) -> None:
        if request_path in ("", "/"):
            relative = "index.html"
        else:
            relative = unquote(request_path).lstrip("/")
        parts = Path(relative).parts
        if ".." in parts:
            self.send_error(400, "Invalid path")
            return

        target = (self.static_dir / relative).resolve()
        static_root = self.static_dir.resolve()
        if target != static_root and static_root not in target.parents:
            self.send_error(400, "Invalid path")
            return
        if not target.is_file():
            self.send_error(404, "Not found")
            return

        body = target.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", self._content_type(target))
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _content_type(self, path: Path) -> str:
        suffix = path.suffix.lower()
        if suffix == ".html":
            return "text/html; charset=utf-8"
        if suffix == ".css":
            return "text/css; charset=utf-8"
        if suffix == ".js":
            return "application/javascript; charset=utf-8"
        if suffix == ".svg":
            return "image/svg+xml"
        return "application/octet-stream"


def create_server(host: str = "127.0.0.1", port: int = 8765, base_dir: Path | str = DEFAULT_BASE_DIR) -> ThreadingHTTPServer:
    handler = partial(type("ConfiguredStrategyDashboardHandler", (StrategyDashboardHandler,), {"base_dir": Path(base_dir)}))
    return ThreadingHTTPServer((host, port), handler)
