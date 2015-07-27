from app.case.model import Case
from flask.ext.api import exceptions, status
from flask import request, abort, jsonify


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

        case = Case(
            request.data['conveyancer_id'],
            request.data['deed_id']
        )

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

    @blueprint.route('/case/<deed_id>/status', methods=['POST'])
    def update_status(deed_id):
        case = Case.get_by_deed_id(deed_id)

        if case is None:
            abort(status.HTTP_404_NOT_FOUND)

        case_status = request.data['status']
        case.status = case_status

        if Case.is_case_status_valid(case_status):
            case.save()
            return jsonify(case_status=case_status), status.HTTP_200_OK
        else:
            abort(status.HTTP_400_BAD_REQUEST)
