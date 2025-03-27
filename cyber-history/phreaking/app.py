from http.server import BaseHTTPRequestHandler, HTTPServer
import shutil
import json
import os

def get_flag():
    with open("/flag", "r") as fp:
        return fp.read()

class handler(BaseHTTPRequestHandler):
    def send_error(self, code, message=None):
        if code == 404:
            self.error_message_format = "Page not found!"
        BaseHTTPRequestHandler.send_error(self, code, message)

    def do_GET(self):
        basename = self.path.strip().split('/')[-1]
        if basename == '':
            basename = "index.html"

        # Check if file exists and its in the folder
        if not os.path.exists(basename):
            self.send_error(404)
            return

        self.send_response(200)
        MIMES = {
            "js": "text/javascript",
            "css": "text/css",
            "ttf": "font/ttf",
            "png": "image/png",
            "html": "text/html"
        }
        self.send_header('Content-type', \
           MIMES.get(basename.split('.')[-1], "text/html"))
        self.end_headers()

        with open(basename, 'rb') as content:
            shutil.copyfileobj(content, self.wfile)

    def do_POST(self):
        length = int(self.headers.get('content-length'))
        field_data = self.rfile.read(length)

        try:
          fields = json.loads(field_data.decode('UTF-8'))
        except:
          self.send_error(404)
          return

        verify = fields.get("verify", None)
        if verify and "7552099" in verify and " hacked" in verify:
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()

            self.wfile.write(bytes(get_flag(), "utf8"))
        else:
            self.send_error(404)

if __name__ == "__main__":
    ip = '127.0.0.1'
    port = 5000
    with HTTPServer((ip, port), handler) as server:
        print(f"Server started at http://{ip}:{port}")
        server.serve_forever()
