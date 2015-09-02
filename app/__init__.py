from flask.ext.script import Manager
from app import helloworld, case, db, borrower, property
from flask.ext.api import FlaskAPI


def create_manager():
    app = FlaskAPI(__name__)

    app.config.from_pyfile('config.py')

    app.register_blueprint(helloworld.blueprint)
    app.register_blueprint(case.blueprint)
    app.register_blueprint(borrower.blueprint)
    app.register_blueprint(property.blueprint)

    manager = Manager(app)
    db.init(app, manager)

    return manager
