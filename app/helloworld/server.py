from flask import jsonify


def register_routes(blueprint):
    @blueprint.route('/', methods=['GET'])
    @blueprint.route('/helloworld', methods=['GET'])
    def get_title():

        result = {
            "Hello": "World",
        }

        return jsonify(result)
