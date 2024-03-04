from flask import Flask
from flask_migrate import Migrate

from . import config, routes
from .db import db

migrate = Migrate(db=db)


def create_app() -> Flask:
    """ Application factory """
    app = Flask(__name__)

    app.json.sort_keys = False  # Офаем сортировку ключей JSON

    # Настраиваем ORM и мигратор
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    db.init_app(app)
    migrate.init_app(app)

    # Подключаем эндпоинты
    app.register_blueprint(routes.router)

    return app
