from datetime import datetime


def app(environ, start_response):
    start_response("200 OK", [])
    return [str(datetime.now().replace(microsecond=0)).encode()]


def main():
    from wsgiref.simple_server import make_server

    with make_server("0.0.0.0", 8000, app) as httpd:
        print("Serving on port 8000...")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Bye")
