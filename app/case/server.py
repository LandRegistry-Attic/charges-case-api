from flask import jsonify
from app.case.model import Case
from datetime import datetime
from random import randint

def register_routes(blueprint):
    @blueprint.route('/case', methods=['GET'])
    def get_title():

        case = Case(randint(1, 99999999), 1, 1, "Stuff", datetime.today(), datetime.today())
        case

        case.save()

        result = {
            "Hello": "cases",
        }

        return jsonify(result)
