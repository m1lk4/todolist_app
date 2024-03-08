from flask import Flask

from src.routes.list import list_blueprint
from src.routes.task import task_blueprint
from src.routes.auth import auth_blueprint
from src.config import ConfigDev
from src.database.todolist import db


def create_app(static_folder="static"):
    app = Flask(__name__, static_folder=static_folder)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/1'

    app.config.from_object(ConfigDev)

    db.init_app(app)

    app.register_blueprint(list_blueprint)
    app.register_blueprint(task_blueprint)
    app.register_blueprint(auth_blueprint)

    return app
