# This code sets up the web server for use in CPSC 231 only
# By Richard Zhao
# This file should not be edited in any way
# Your code should be created in a new, separate file called support_functions.py

from http.server import HTTPServer, BaseHTTPRequestHandler
import argparse
import json
import os
import support_functions



# Server class
class S(BaseHTTPRequestHandler):

    username = ""
    memory = ""
    # DO NOT copy this database into your own code. If you do that, your code will fail all test cases
    database = \
        {
            "name": "I am Chat231. My nickname is Riley.",
            "textbook": "The textbook we use is called The Python Workbook 2nd Edition.",
            "break": "Fall break is November 10-16. Can't wait!",
            "final exam": "The final exam will be on December 19th. Check D2L for details."
        }

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Private-Network", "true")
        self.end_headers()

    # handle GET
    def do_GET(self):
        rootdir = os.getcwd()

        try:
            path = self.path.split("?", 1)[0]
            # handle default file
            if path == '/':
                self.path += 'index.html'

            # handle endpoints
            elif path == '/greetings':

                self.username = self.path.split("?", 1)[1].split("=", 1)[1]

                self.send_response(200)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Access-Control-Allow-Methods", "*")
                self.send_header("Access-Control-Allow-Headers", "*")
                self.send_header("Access-Control-Allow-Private-Network", "true")
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                try:
                    result_string = support_functions.get_greetings(self.username)
                except AttributeError:
                    result_string = "Connected! But I can't reply because you didn't create get_greetings()."

                self.wfile.write(result_string.encode('utf-8'))


            # handle files
            elif self.path.endswith('.html'):
                f = open(rootdir + self.path)
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f.read().encode('utf-8'))
                f.close()
            elif self.path.endswith('.js'):
                f = open(rootdir + self.path)
                self.send_response(200)
                self.send_header("Content-type", "application/javascript")
                self.end_headers()
                self.wfile.write(f.read().encode('utf-8'))
                f.close()
            else:
                self.send_error(404, 'file not supported')

        except IOError:
            self.send_error(404, 'file not found')

    # handle POST
    def do_POST(self):
        rootdir = os.getcwd()

        try:
            path = self.path.split("?", 1)[0]

            # handle endpoints
            if path == '/chat':

                # JSON string
                payload_string = self.rfile.read(int(self.headers['Content-Length']))

                # Converts to Python dictionary
                payload = json.loads(payload_string)

                message = str(payload['message'])
                self.username = str(payload['username'])

                self.send_response(200)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Access-Control-Allow-Methods", "*")
                self.send_header("Access-Control-Allow-Headers", "*")
                self.send_header("Content-Type", "application/json")
                self.end_headers()


                try:
                    result_string = support_functions.get_answer(self.database, message)
                    print("Return value from get_answer(): " + str(result_string))
                except AttributeError as err:
                    result_string = "Function does not exist. Have you created all the functions?"
                    print("Error:", err)


                # make a Python dictionary from the result
                result_obj = {"response": result_string}

                # convert Python dictionary to JSON string
                result_string = json.dumps(result_obj)

                self.wfile.write(result_string.encode('utf-8'))

            else:
                self.send_error(404, 'endpoint not supported')

        except IOError:
            self.send_error(404, 'endpoint not found')


def run(server_class=HTTPServer, handler_class=S, addr="127.0.0.1", port=8080):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting server on {addr}:{port}.")
    httpd.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a simple server")
    parser.add_argument(
        "-l",
        "--listen",
        default="127.0.0.1",
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8080,
        help="Specify the port on which the server listens",
    )
    args = parser.parse_args()

    # start the server
    run(addr=args.listen, port=args.port)

