from __future__ import annotations

import argparse
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from stock_strategy.dashboard.server import create_server  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Serve the local 10B strategy dashboard.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--base-dir", default=str(BASE_DIR))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    server = create_server(args.host, args.port, Path(args.base_dir))
    url = f"http://{args.host}:{server.server_port}"
    print(f"本地投资策略控制台已启动：{url}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n正在关闭本地投资策略控制台。", flush=True)
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
