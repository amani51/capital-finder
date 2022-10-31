from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        capital="The capital of lebanon is Beirut"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
     
        self.wfile.write(capital.encode())
        return