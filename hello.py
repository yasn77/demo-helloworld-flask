from flask import Flask
app = Flask(__name__)
import os


@app.route("/")
def hello():
    return "\n".join(
        ["Hello World!\n"] + map("=".join, os.environ.items()))

if __name__ == "__main__":
    app.run(debug=True)
