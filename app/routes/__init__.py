from flask import Flask
from . import articles


def register(app: Flask) -> None:
    """ Регистрирует все эндпоинты """
    app.register_blueprint(articles.router)
