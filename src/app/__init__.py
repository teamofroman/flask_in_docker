import os

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.config import config, init_config
from app.routes import route


def init_flask_app():
    app = Flask(__name__)

    route(app)

    path = (
        os.environ.get('CONFIG_PATH')
        if os.environ.get('CONFIG_PATH')
        else "./settings.ini"
    )
    run_in_docker = (
        os.environ.get('RUN_IN_DOCKER')
        if os.environ.get('RUN_IN_DOCKER')
        else False
    )

    init_config(path)

    try:
        app.config.update(
            dict(SECRET_KEY=str(config['FLASK_APP']['FLASK_APP_SECRET_KEY']))
        )
        db_host = (
            str(config['FLASK_APP']['POSTGRES_HOST'])
            if run_in_docker
            else 'localhost'
        )

        db_user = str(config['FLASK_APP']['POSTGRES_USER'])
        db_passwd = str(config['FLASK_APP']['POSTGRES_PASSWORD'])
        db_name = str(config['FLASK_APP']['POSTGRES_DB'])
        db_port = int(config['FLASK_APP']['POSTGRES_PORT'])

        app.config['SQLALCHEMY_DATABASE_URI'] = (
            f'postgresql+psycopg2://{db_user}:{db_passwd}@{db_host}:{db_port}/{db_name}'
        )
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db = SQLAlchemy(app)
        migrate = Migrate(app, db)

        admin = Admin(app, name='flast_in_docker')

        print(
            f"\n\033[32m Сервер запустился с конфигом:\n\033[32m {path}\n\033[0m"
        )
    except KeyError:
        print(f"\033[31m Файл {path} не найден или неверный\n\033[0m")

    return app, db, admin


app, db, admin = init_flask_app()

from models import User  # noqa

admin.add_view(ModelView(User, db.session))
