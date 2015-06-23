from app.case.model import Case
from flask.ext.api import exceptions, status
from app.helper.serialize import sqlalchemy_to_dict, dict_to_sqlalchemy
from flask import request


def register_routes(blueprint):

    @blueprint.route('/case', methods=['GET'])
    def get_cases():
        stuff = [case.to_json() for case in Case.all()]

        return stuff

    @blueprint.route('/case/<id_>', methods=['GET'])
    def get_case(id_):
        case = Case.get(id_)

        if case is not None:
            return case.to_json(), status.HTTP_200_OK
        else:
            raise exceptions.NotFound()

    @blueprint.route('/case', methods=['POST'])
    def create_case():
        case_json = request.data
        case = Case()

        case = dict_to_sqlalchemy(case_json, case)
        case.save()

        return sqlalchemy_to_dict(case), status.HTTP_200_OK

    @blueprint.route('/case/<id_>', methods=['DELETE'])
    def delete_case(id_):
        case = Case.delete(id_)

        if case is None:
            raise exceptions.NotFound
        else:
            return case.to_json(), status.HTTP_200_OK
