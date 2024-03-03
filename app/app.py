from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from . import config, routes
from .db import db

app = Flask(__name__, static_url_path=None)

# Подключаем SQLAlchemy к Flask
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLA_DB_URL
db.init_app(app)

migrate = Migrate(app, db)

# Регистрируем эндпоинты
routes.register(app)


@app.route("/")
def hello_world() -> str:
    return "<h1>Welcome to blog-api</h1><span>made with <3 by untitled.arts</span>"


def run() -> None:
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
