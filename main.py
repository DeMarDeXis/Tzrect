import argparse
import signal
import sys

from flask import Flask

from internal.config.config import load_config
from internal.handler.handler import init_router

app = Flask(__name__)

def graceful_shutdown(sig, frame):
    print("\n 🛑 Server stopped gracefully.")
    sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description="Run a TZ-Flask web-server.")
    parser.add_argument("-c", "--config", default="config/local.yaml", help="Path to config file.")
    args = parser.parse_args()

    cfg = load_config(args.config)
    print(f"✅ Config loaded: {cfg}")

    init_router(app)

    signal.signal(signal.SIGINT, graceful_shutdown)
    signal.signal(signal.SIGTERM, graceful_shutdown)

    app.run(host=cfg["server"]["host"], port=cfg["server"]["port"])

if __name__ == "__main__":
    main()