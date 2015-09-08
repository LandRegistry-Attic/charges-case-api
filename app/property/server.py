from flask import request, abort
from flask.ext.api import status
from app.property.model import Property
from app.property import service


def register_routes(blueprint):
    @blueprint.route('/case/<case_id>/property', methods=['POST'])
    def add_property(case_id):
        property_json = request.data['property']
        property_ = Property.from_json(property_json)
        property_.case_id = case_id

        try:
            service.save(property_)
        except Exception as exc:
            print(str(type(exc)) + ":" + str(exc))
            abort(status.HTTP_500_INTERNAL_SERVER_ERROR)

        return property_.to_json()

    @blueprint.route('/case/<case_id>/property', methods=['GET'])
    def get_property(case_id):
        property_ = service.get_property_by_case_id(case_id)

        if property_ is None:
            abort(status.HTTP_404_NOT_FOUND)

        return property_.to_json()
