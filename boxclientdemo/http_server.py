import http
import http.server

class MyHandlerClass(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.server.last_path = self.path
        print("Inside GET callback with path as ", self.path)
        self.send_response(http.HTTPStatus.OK)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello, world!')
        

def run():
    s = http.server.HTTPServer(
        ('localhost', 49152), MyHandlerClass
    )
    s.handle_request()
    return s.last_path
