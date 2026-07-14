import os
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent / "yashaswini_project"
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from app import app


if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "5000"))

    print(f"Starting server on {host}:{port}...", flush=True)

    try:
        from waitress import serve

        print("Using waitress server", flush=True)
        serve(app, host=host, port=port)
    except Exception as e:
        print(f"Waitress error: {e}, falling back to Flask", flush=True)
        app.run(host=host, port=port, debug=False)
