from app.db import db, array_type
from app import json


class Borrower(db.Model, json.Serialisable):
    __tablename__ = 'borrower'

    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'))
    first_name = db.Column(db.String())
    middle_names = db.Column(db.String())
    last_name = db.Column(db.String())
    mobile_no = db.Column(db.String())
    email_address = db.Column(db.String())
    address = db.Column(array_type(db.String()))

    def __init__(self,
                 case_id,
                 first_name,
                 last_name,
                 mobile_no,
                 email_address,
                 address,
                 middle_names=None):

        if middle_names is not None:
            self.middle_names = middle_names

        self.case_id = case_id
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_no = mobile_no
        self.email_address = email_address
        self.address = address

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def all():
        return Borrower.query.all()

    @staticmethod
    def get(id_):
        return Borrower.query.filter_by(id=id_).first()

    @staticmethod
    def delete(id_):
        borrower = Borrower.query.filter_by(id=id_).first()

        if borrower is None:
            return borrower

        db.session.delete(borrower)
        db.session.commit()

        return borrower

    def json_format(self):
        jsondata = {}

        def append(name, parameter):
            value = parameter(self)
            if value is not None:
                jsondata[name] = value

        append('id', lambda obj: obj.id)
        append('case_id', lambda obj: obj.case_id)
        append('first-name', lambda obj: obj.first_name)
        append('middle-names', lambda obj: obj.middle_names)
        append('last-name', lambda obj: obj.last_name)
        append('mobile-no', lambda obj: obj.mobile_no)
        append('email-address', lambda obj: obj.email_address)
        append('address', lambda obj: obj.address)

        return jsondata

    def object_hook(dct):
        _id = dct.get('id')
        _case_id = dct.get('case_id')
        _first_name = dct.get('first-name')
        _middle_names = dct.get('middle-names')
        _last_name = dct.get('last-name')
        _mobile_no = dct.get('mobile-no')
        _email_address = dct.get('email-address')
        _address = dct.get('address')

        borrower = Borrower(
            _case_id,
            _first_name,
            _middle_names,
            _last_name,
            _mobile_no,
            _email_address,
            _address
        )
        borrower.id = _id

        return borrower