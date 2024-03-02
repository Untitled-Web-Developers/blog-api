from flask import Flask

from . import config

app = Flask(__name__)


@app.route("/")
def hello_world() -> str:
    return "<h1>Welcome to blog-api</h1><span>made with <3 by untitled.arts</span>"


def run() -> None:
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
