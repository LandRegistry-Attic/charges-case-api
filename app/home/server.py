

def register_routes(blueprint):
    @blueprint.route('/', methods=['GET'])
    def get_title():

        result = {
            "Case": "gi/case",
            "Borrowers": "/case/<_id>/borrowers",
        }

        return result
