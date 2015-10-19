from flask import Blueprint
from . import server


blueprint = Blueprint('land_registry', __name__)
server.register_routes(blueprint)
