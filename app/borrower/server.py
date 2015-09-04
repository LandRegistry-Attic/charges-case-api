from flask import request, abort
from flask.ext.api import status
from app.borrower.model import Borrower


def register_routes(blueprint):
    @blueprint.route('/case/<case_id>/borrowers', methods=['POST'])
    def add_borrowers(case_id):
        def validate_request_data():
            def in_and_not_empty(val, borrower):
                return val in borrower and borrower[val]

            for borrower_ in request_data:
                if not (in_and_not_empty('first_name', borrower_) and
                        in_and_not_empty('last_name', borrower_) and
                        in_and_not_empty('mobile_no', borrower_) and
                        in_and_not_empty('email_address', borrower_) and
                        in_and_not_empty('address', borrower_)):
                    abort(status.HTTP_400_BAD_REQUEST)

        request_data = request.data['borrowers']
        validate_request_data()

        def add_case_id(borrower):
            borrower['case_id'] = case_id
            return borrower

        borrowers = [add_case_id(item) for item in request_data]

        try:
            Borrower.add(borrowers)
        except Exception as exc:
            print(str(type(exc)) + ":" + str(exc))
            abort(status.HTTP_500_INTERNAL_SERVER_ERROR)

        return borrowers

    @blueprint.route('/case/<case_id>/borrowers', methods=['GET'])
    def get_borrowers(case_id):
        borrowers = Borrower.get_by_case_id(case_id)

        if borrowers is None or borrowers == []:
            abort(status.HTTP_404_NOT_FOUND)

        return [borrower.to_json() for borrower in borrowers]
