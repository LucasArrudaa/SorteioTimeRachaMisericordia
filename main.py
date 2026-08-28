"""Servidor local do Racha da Misericórdia.

Execute ``python main.py`` e abra http://127.0.0.1:8000.
"""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent


class AppHandler(SimpleHTTPRequestHandler):
    """Serve os arquivos estáticos do frontend sem dependências externas."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PROJECT_ROOT, **kwargs)

    def do_GET(self):
        if self.path in {"", "/"}:
            self.path = "/static/index.html"
        return super().do_GET()


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8000), AppHandler)
    print("Racha da Misericórdia em http://127.0.0.1:8000")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")
    finally:
        server.server_close()
