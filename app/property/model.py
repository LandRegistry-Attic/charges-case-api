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
                 title_number,
                 street,
                 tenure,
                 locality,
                 postcode,
                 extended=None):
        self.title_number = title_number
        self.street = street
        self.extended = extended
        self.locality = locality
        self.postcode = postcode
        self.tenure = tenure

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get(id_):
        return Property.query.filter_by(id=id_).first()

    @staticmethod
    def get_by_case_id(case_id):
        return Property.query.filter_by(case_id=case_id).first()

    def json_format(self):
        jsondata = {}

        def append(name, parameter):
            value = parameter(self)
            if value is not None:
                jsondata[name] = value

        append('title_number', lambda obj: obj.title_number)
        append('street', lambda obj: obj.street)
        append('extended', lambda obj: obj.extended)
        append('locality', lambda obj: obj.locality)
        append('postcode', lambda obj: obj.postcode)
        append('tenure', lambda obj: obj.tenure)

        return jsondata

    def object_hook(dct):
        _title_number = dct.get('title_number')
        _street = dct.get('street')
        _extended = dct.get('extended', None)
        _locality = dct.get('locality')
        _postcode = dct.get('postcode')
        _tenure = dct.get('tenure')

        property_ = Property(
            _title_number,
            _street,
            _tenure,
            _locality,
            _postcode,
            _extended
        )

        return property_
