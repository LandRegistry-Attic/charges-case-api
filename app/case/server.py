from app.case.model import Case
from flask.ext.api import exceptions, status
from flask import request, abort, jsonify
from datetime import datetime


def register_routes(blueprint):
    @blueprint.route('/case', methods=['GET'])
    def get_cases():
        stuff = [case.to_json() for case in Case.all()]

        print(Case.all_with_borrowers())

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
            case_ref=request.data.get('case_ref')
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
            case.last_updated = datetime.now()
            case.save()
            return jsonify(case_status=case_status), status.HTTP_200_OK
        else:
            abort(status.HTTP_400_BAD_REQUEST)

    @blueprint.route('/case/<case_id>/deed', methods=['POST'])
    def update_case_deed(case_id):
        case = Case.get(case_id)

        if case is None:
            abort(status.HTTP_404_NOT_FOUND)

        if case.deed_id is not None:
            abort(status.HTTP_403_FORBIDDEN)

        deed_id = request.data['deed_id']
        case.deed_id = deed_id
        case.last_updated = datetime.now()
        case.status = 'Deed created'

        try:
            case.save()
        except Exception as inst:
            print(str(type(inst)) + ":" + str(inst))
            raise abort(status.HTTP_500_INTERNAL_SERVER_ERROR)

        return case.to_json(), status.HTTP_200_OK
