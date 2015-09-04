from .model import Property


def get_property_by_case_id(case_id):
    return Property.query.filter_by(case_id=case_id).first()
