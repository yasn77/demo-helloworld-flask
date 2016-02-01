from flask import Flask, Response
app = Flask(__name__)
import os


@app.route("/")
def hello():
    return Response("\n".join(
        ["Hello World!\n"] + map("=".join, os.environ.items())), mimetype='text/plain')

if __name__ == "__main__":
    try:
        port = int(os.getenv("PORT"))
    except TypeError:
        port = None
    app.run(debug=True, port=port)
