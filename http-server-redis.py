import socket
import redis
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer


# HTTPRequestHandler class
class RequestHandler(BaseHTTPRequestHandler):

    # Construct
    def __init__(self, request, client_address, server):
        # Connect to master with a pool
        pool = redis.ConnectionPool(host=sys.argv[1], port=6379, db=0)
        self.redis_master = redis.Redis(connection_pool=pool)
        super().__init__(request, client_address, server)

    # GET
    def do_GET(self):

        # Get data from Redis
        redis_slave = redis.StrictRedis(host=sys.argv[2], port=6379, db=0)
        foo = redis_slave.get('foo')
        if (foo is None):
            foo = b'None'

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = 'I\'m {}<BR>'.format(socket.gethostname())
        message += 'Foo is {}<BR>'.format(str(foo, 'utf-8'))

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

    # POST
    def do_POST(self):
        # Read POST data
        varLen = int(self.headers['Content-Length'])
        postVars = bytes(self.rfile.read(varLen))

        # Send data from Redis
        foo = self.redis_master.set('foo', postVars)

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        return

def main():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print('running server...')
    httpd.serve_forever()


if __name__ == "__main__":
    main()
