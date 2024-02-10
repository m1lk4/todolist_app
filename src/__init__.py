from flask import Flask

from src.routes.list import list_blueprint
from src.config import ConfigDev
from src.database.todolist_db import db


def create_app():
    app = Flask(__name__)

    app.config.from_object(ConfigDev)

    db.init_app(app)

    app.register_blueprint(list_blueprint)

    return app
