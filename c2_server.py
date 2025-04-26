import http.server
import socketserver
import os

PORT = 8000
UPLOAD_DIR = './uploads'  # Directory where uploaded files will be saved

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/upload':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            # Write the uploaded file to the server's storage
            with open(os.path.join(UPLOAD_DIR, 'exfiltrated_file.log'), 'wb') as f:
                f.write(post_data)
                
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"File uploaded successfully.")
        else:
            self.send_response(404)
            self.end_headers()

# Start the HTTP server
Handler = SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"Serving on port {PORT}...")
httpd.serve_forever()
