#using http.server to create a basic HTTP service for testing

import http.server
import socketserver

port=8888

with socketserver.TCPServer(('', port), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f"Serving at port {port}")
    httpd.serve_forever()


