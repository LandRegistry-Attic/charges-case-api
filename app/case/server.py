from app.case.model import Case
from flask.ext.api import exceptions, status
from flask import request


def register_routes(blueprint):

    @blueprint.route('/case', methods=['GET'])
    def get_cases():
        stuff = [case.to_json() for case in Case.all()]

        return stuff

    @blueprint.route('/case/<id_>', methods=['GET'])
    def get_case(id_):
        case = Case.get(id_)

        if case is None:
            raise exceptions.NotFound()
        else:
            return case.to_json(), status.HTTP_200_OK

    @blueprint.route('/case', methods=['POST'])
    def create_case():
        case_json = request.data
        case_json["type"] = "Case"

        case = Case.from_json(case_json)

        try:
            case.save()
        except Exception as inst:
            print(str(type(inst)) + ":" + str(inst))
            raise exceptions.NotAcceptable()

        return case.to_json(), status.HTTP_201_CREATED

    @blueprint.route('/case/<id_>', methods=['DELETE'])
    def delete_case(id_):

        try:
            case = Case.delete(id_)
        except Exception as inst:
            print(type(inst) + ":" + inst)

        if case is None:
            raise exceptions.NotFound
        else:
            return case.to_json(), status.HTTP_200_OK
