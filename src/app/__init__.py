import os

from flask import Flask

from app.config import config, init_config
from app.routes import route


def create_flask_app():
    app = Flask(__name__)

    route(app)

    path = (
        os.environ.get('CONFIG_PATH')
        if os.environ.get('CONFIG_PATH')
        else "./settings.ini"
    )
    init_config(path)
    try:
        app.config.update(
            dict(SECRET_KEY=str(config['FLASK_APP']['FLASK_APP_SECRET_KEY']))
        )
        print(
            f"\n\033[32m Сервер запустился с конфигом:\n\033[32m {path}\n\033[0m"
        )
    except KeyError:
        print(f"\033[31m Файл {path} не найден или неверный\n\033[0m")

    return app
