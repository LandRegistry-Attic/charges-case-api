from flask import Blueprint
from . import routes

blueprint = Blueprint('helloworld', __name__)
routes.register_routes(blueprint)
