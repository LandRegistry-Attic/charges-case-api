from flask import Flask
from flask.ext.script import Manager
from app import helloworld, db


def create_manager():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    app.register_blueprint(helloworld.blueprint)

    manager = Manager(app)
    db.init(app, manager)

    return manager
