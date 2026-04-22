import random
from http.server import BaseHTTPRequestHandler, HTTPServer

LINES_FILE = "lines.txt"


def random_line():
    with open(LINES_FILE) as f:
        lines = [line.strip() for line in f if line.strip()]
    return random.choice(lines)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        line = random_line()
        body = line.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print(fmt % args)


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Listening on port 8080")
    server.serve_forever()
