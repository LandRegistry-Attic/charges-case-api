from flask import jsonify
from app.case.model import Case
from datetime import datetime
from random import randint
import json

def register_routes(blueprint):
    @blueprint.route('/case', methods=['GET'])
    def get_cases_json():
        return Case.all_as_json()
