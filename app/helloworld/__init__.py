from flask import Blueprint
from . import server


blueprint = Blueprint('helloworld', __name__)
server.register_routes(blueprint)
