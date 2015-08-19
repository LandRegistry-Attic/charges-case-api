from flask import Blueprint
from . import server


blueprint = Blueprint('borrower', __name__)
server.register_routes(blueprint)
