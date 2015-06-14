from app.case.model import Case


def register_routes(blueprint):
    @blueprint.route('/case', methods=['GET'])
    def get_cases_json():
        return Case.all_as_json()
