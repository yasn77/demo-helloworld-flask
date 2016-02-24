from flask import Flask, Response, request
app = Flask(__name__)
import os


@app.route("/")
def hello():
    return Response("\n".join(
        ["Hello World!",
         "You appear to hail from %s" % request.remote_addr,
         "\nEnvironment:" ] +\
         map("=".join, os.environ.items()) + \
         ['\nHeaders:'] +\
         map("=".join, request.headers.items()) + \
         ['\n']
    ), mimetype='text/plain')

if __name__ == "__main__":
    try:
        port = int(os.getenv("PORT"))
    except TypeError:
        port = None
    app.run(debug=True, port=port)
