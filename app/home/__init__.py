from flask import Blueprint
from . import server


blueprint = Blueprint('home', __name__)
server.register_routes(blueprint)
