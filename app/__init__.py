from flask import Flask
from flask.ext.script import Manager
from app import helloworld, case


def create_manager():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    manager = Manager(app)
    app.register_blueprint(helloworld.blueprint)
    app.register_blueprint(case.blueprint)

    return manager
