from app.case.model import Case
from flask.ext.api import exceptions


def register_routes(blueprint):

    @blueprint.route('/case', methods=['GET'])
    def get_cases_json():
        return Case.all()

    @blueprint.route('/case/<id_>', methods=['GET'])
    def get_case_json(id_):
        case = Case.get(id_)

        if case is not None:
            return case
        else:
            raise exceptions.NotFound()
