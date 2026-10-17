import http.server
import socketserver

PORT = 3000
HANDLER = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), HANDLER) as httpd:
    httpd.serve_forever()