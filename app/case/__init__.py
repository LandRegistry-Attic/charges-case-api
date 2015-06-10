from flask import Blueprint
from . import server

blueprint = Blueprint('case', __name__)
server.register_routes(blueprint)
