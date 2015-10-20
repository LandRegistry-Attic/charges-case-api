from flask import request, abort
from flask.ext.api import status


def register_routes(blueprint):
    @blueprint.route('/landregistry/submit', methods=['POST'])
    def submit():

        payload = request.form['payload']

        if payload:
            return {"submissionRef": "submission Ref",
                    "applicationReference": "ABR1234",
                    "TitleValidationCode": "title_validation_code"}
        else:
            abort(status.HTTP_500_INTERNAL_SERVER_ERROR)
