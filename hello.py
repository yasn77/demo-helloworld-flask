from flask import Flask, Response, request
app = Flask(__name__)
import os
import socket


@app.route("/<name>")
@app.route("/")
def hello(name=None):
    u = name if name is not None else 'World!'
    return Response("\n".join(
        ["Hello {}".format(u),
         "I am running on %s" % socket.gethostname(),
         "\nHeaders:"] + map("=".join, request.headers.items())
        ), mimetype='text/plain')


if __name__ == "__main__":
    try:
        port = int(os.getenv("PORT"))
    except TypeError:
        port = None
    app.run(debug=True, port=port)
