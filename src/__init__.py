from flask import Flask

from src.routes.list import list_blueprint
from src.routes.task import task_blueprint
from src.routes.auth import auth_blueprint
from src.routes.tag import tag_blueprint
from src.routes import home_blueprint
from src.config import config
from src.database.todolist import db


def create_app(env="development", static_folder="static"):
    app = Flask(__name__, static_folder=static_folder)

    # Loading config
    app.config.from_object(config[env])

    # Init database
    db.init_app(app)

    # Controllers
    app.register_blueprint(list_blueprint)
    app.register_blueprint(task_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(home_blueprint)
    app.register_blueprint(tag_blueprint)

    return app
