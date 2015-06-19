from flask import Flask
from flask.ext.script import Manager
from app import helloworld, case, db
from flask.ext.api import FlaskAPI, renderers
from flask.ext.api.decorators import set_renderers



def create_manager():

    app = FlaskAPI(__name__)

    # app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # app.config['DEFAULT_RENDERERS'] = ['app.helper.custom_api_render.JSONRenderer']

    app.register_blueprint(helloworld.blueprint)
    app.register_blueprint(case.blueprint)

    manager = Manager(app)
    db.init(app, manager)

    return manager
