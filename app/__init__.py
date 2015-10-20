from flask.ext.script import Manager
from app import helloworld, case, db, borrower, property, home, land_registry
from flask.ext.api import FlaskAPI


def create_manager():
    app = FlaskAPI(__name__)

    app.config.from_pyfile('config.py')

    app.register_blueprint(helloworld.blueprint)
    app.register_blueprint(home.blueprint)
    app.register_blueprint(case.blueprint)
    app.register_blueprint(borrower.blueprint)
    app.register_blueprint(property.blueprint)
    app.register_blueprint(land_registry.blueprint)

    manager = Manager(app)
    db.init(app, manager)

    return manager
