

def register_routes(blueprint):
    @blueprint.route('/case/<case_id>/borrowers', methods=['GET'])
    def get_borrowers(case_id):
        stuff = [borrwers.to_json() for case in Case.all()]

        return stuff
