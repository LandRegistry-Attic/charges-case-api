from flask import request, abort
from flask.ext.api import status
from app.borrower.model import Borrower


def register_routes(blueprint):
    @blueprint.route('/case/<case_id>/borrowers', methods=['POST'])
    def add_borrowers(case_id):
        request_data = request.data['borrowers']

        def add_case_id(borrower):
            borrower['case_id'] = case_id
            return borrower

        borrowers = [add_case_id(item) for item in request_data]

        try:
            Borrower.add(borrowers)
        except Exception as exc:
            print(str(type(exc)) + ":" + str(exc))
            abort(status.HTTP_500_INTERNAL_SERVER_ERROR)

        return {'status_code': status.HTTP_200_OK}
