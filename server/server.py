"""
Whispers of the Wind — AI Voice Agent Server (Python)
Provides static asset serving and an API endpoint for simulated conversation turns.
"""

import http.server
import socketserver
import os
from pathlib import Path

PORT = 8080
PUBLIC_DIR = Path(__file__).parent.parent / "public"

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(PUBLIC_DIR), **kwargs)

    def end_headers(self):
        # Enable CORS and Cache-Control headers for development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

def main():
    os.chdir(PUBLIC_DIR)
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"===========================================================")
        print(f"Whispers of the Wind — AI Voice Agent Showcase Live Server")
        print(f"Serving at: http://localhost:{PORT}")
        print(f"===========================================================")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")

if __name__ == "__main__":
    main()
