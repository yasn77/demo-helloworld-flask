from flask import Flask, Response
app = Flask(__name__)
import os


@app.route("/")
def hello():
    return Response("\n".join(
        ["Hello World!\n"] + map("=".join, os.environ.items())), mimetype='text/plain')

if __name__ == "__main__":
    app.run(debug=True)
