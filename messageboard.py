from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

memory = []

form = '''<!DOCTYPE html>
  <title>Message Board</title>
  <form method="POST">
    <textarea name="message"></textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
{}
  </pre>
'''

class MessageHandler(BaseHTTPRequestHandler):
     def do_POST(self):

        length = int(self.headers.get('Content-length', 0))


        data = self.rfile.read(length).decode()
        message = parse_qs(data)["message"][0]


        message = message.replace("<", "&lt;")


        memory.append(message)


        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()



if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
