from app.db import db
from app import json


class Property(db.Model, json.Serialisable):
    __tablename__ = 'property'

    id = db.Column(db.Integer(), primary_key=True)
    case_id = db.Column(db.Integer(),
                        db.ForeignKey('case.id', ondelete="CASCADE"),
                        nullable=False,
                        unique=True)
    title_number = db.Column(db.String(), nullable=False)
    street = db.Column(db.String(), nullable=False)
    extended = db.Column(db.String(), nullable=True)
    locality = db.Column(db.String(), nullable=False)
    postcode = db.Column(db.String(), nullable=False)
    tenure = db.Column(db.String(), nullable=False)

    def __init__(self,
                 case_id,
                 title_number,
                 street,
                 tenure,
                 locality,
                 postcode,
                 extended=None):
        self.case_id = case_id
        self.title_number = title_number
        self.street = street
        self.extended = extended
        self.locality = locality
        self.postcode = postcode
        self.tenure = tenure

    def json_format(self):
        jsondata = {}

        def append(name, parameter):
            value = parameter(self)
            if value is not None:
                jsondata[name] = value

        append('id', lambda obj: obj.id)
        append('case_id', lambda obj: obj.case_id)
        append('title_number', lambda obj: obj.title_number)
        append('street', lambda obj: obj.street)
        append('extended', lambda obj: obj.extended)
        append('locality', lambda obj: obj.locality)
        append('postcode', lambda obj: obj.postcode)
        append('tenure', lambda obj: obj.tenure)

        return jsondata

    def object_hook(dct):
        _id = dct.get('id')
        _case_id = dct.get('case_id')
        _title_number = dct.get('title_number')
        _street = dct.get('street')
        _extended = dct.get('extended', None)
        _locality = dct.get('locality')
        _postcode = dct.get('postcode')
        _tenure = dct.get('tenure')

        property_ = Property(
            _case_id,
            _title_number,
            _street,
            _tenure,
            _locality,
            _postcode,
            _extended
        )

        property_.id = _id

        return property_
