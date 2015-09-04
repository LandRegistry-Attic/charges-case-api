from random import randint
from app.property.model import Property
from tests.case.helpers import CaseHelper


class PropertyHelper:
    _id = '1'
    _case_id = '0'
    _title_number = 'LH1362'
    _street = "25B Friar Street"
    _extended = None
    _locality = "Reading"
    _postcode = "RG1 1DP"
    _tenure = "freehold"

    @staticmethod
    def _create_property_and_save():
        case = CaseHelper._create_case_and_save()

        property_ = PropertyHelper._create_property()
        property_.case_id = case.id
        property_.save()

        return property_

    @staticmethod
    def _create_property():
        PropertyHelper._id = randint(1, 999999)
        property_ = Property(PropertyHelper._case_id,
                             PropertyHelper._title_number,
                             PropertyHelper._street,
                             PropertyHelper._tenure,
                             PropertyHelper._locality,
                             PropertyHelper._postcode,
                             PropertyHelper._extended)
        property_.id = PropertyHelper._id

        return property_

    @staticmethod
    def _delete_property(_id):
        Property.delete(_id)
