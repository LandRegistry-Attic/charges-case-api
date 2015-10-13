from datetime import datetime
from flask import request, abort
from app.case.model import Case
from app.case import service as CaseService
from flask.ext.api import exceptions, status


def register_routes(blueprint):
    @blueprint.route('/case', methods=['GET'])
    def get_cases():
        return [case.to_json() for case in CaseService.all()]

    @blueprint.route('/case/<id_>', methods=['GET'])
    def get_case(id_):
        case = CaseService.get(id_)

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

        CaseService.save(case)

        return case.to_json(), status.HTTP_201_CREATED

    @blueprint.route('/case/<id_>', methods=['DELETE'])
    def delete_case(id_):

        try:
            case = CaseService.delete(id_)
        except Exception as inst:
            print(str(type(inst)) + ":" + str(inst))

        if case is None:
            raise exceptions.NotFound
        else:
            return case.to_json(), status.HTTP_200_OK

    @blueprint.route('/case/<deed_id>/status', methods=['POST'])
    def update_status(deed_id):
        case = CaseService.get_by_deed_id(deed_id)

        if case is None:
            abort(status.HTTP_404_NOT_FOUND)

        case_status = request.data['status']
        case.status = case_status

        if CaseService.is_case_status_valid(case_status):
            case.last_updated = datetime.now()
            CaseService.save(case)
            return {'case_status': case_status}, status.HTTP_200_OK
        else:
            abort(status.HTTP_400_BAD_REQUEST)

    @blueprint.route('/case/<case_id>/deed', methods=['POST'])
    def update_case_deed(case_id):
        case = CaseService.get(case_id)

        if case is None:
            abort(status.HTTP_404_NOT_FOUND)

        if case.deed_id is not None:
            abort(status.HTTP_403_FORBIDDEN)

        deed_id = request.data['deed_id']
        case.deed_id = deed_id
        case.last_updated = datetime.now()
        case.status = 'Deed created'

        try:
            CaseService.save(case)
        except Exception as inst:
            print(str(type(inst)) + ":" + str(inst))
            abort(status.HTTP_500_INTERNAL_SERVER_ERROR)

        return case.to_json(), status.HTTP_200_OK

    @blueprint.route('/case/<case_id>/<payload>/application', methods=['POST'])
    def submit(case_id):
        case = CaseService.get(case_id)

        if case is None:
            abort(status.HTTP_404_NOT_FOUND)

        if case.deed_id is None:
            abort(status.HTTP_403_FORBIDDEN)

        if case.status != 'Completion confirmed':
            abort(status.HTTP_403_FORBIDDEN)

        case.status = 'Submitted'
        case.last_updated = datetime.now()

        try:
            # submit the new case to the land registry case workers
            payload = CaseService.construct_as_payload(case.deed_id,"1958333","GR514526")

            CaseService.save(case)


        except Exception as inst:
            print(str(type(inst)) + ":" + str(inst))
            abort(status.HTTP_500_INTERNAL_SERVER_ERROR)

        return case.to_json(), status.HTTP_200_OK
