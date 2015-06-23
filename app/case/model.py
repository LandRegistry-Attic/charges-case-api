from sqlalchemy.orm.exc import UnmappedInstanceError
from app.db import db
from app.helper.serialize import serialize_datetime
from app import json


class Case(db.Model, json.Serialisable):

    __tablename__ = 'case'

    id = db.Column(db.Integer, primary_key=True)
    deed_id = db.Column(db.Integer)
    conveyancer_id = db.Column(db.Integer)
    status = db.Column(db.String())
    last_updated = db.Column(db.DateTime())
    created_on = db.Column(db.DateTime())

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def all():
        return Case.query.all()

    @staticmethod
    def get(id_):
        return Case.query.filter_by(id=id_).first()

    @staticmethod
    def delete(id_):
        case = Case.query.filter_by(id=id_).first()

        if case is None:
            return case

        db.session.delete(case)
        db.session.commit()

        return case

    @staticmethod
    def _json_format(o):
        jsondata = {}

        def append(name, parameter):
            value = parameter(o)
            if value is not None:
                jsondata[name] = value

        append('id', lambda obj: obj.id)
        append('deed_id', lambda obj: obj.deed_id)
        append('conveyancer_id', lambda obj: obj.conveyancer_id)
        append('status', lambda obj: obj.status)
        append('last_updated',
               lambda obj: serialize_datetime(obj.last_updated))
        append('created_on',
               lambda obj: serialize_datetime(obj.created_on))

        return jsondata

    @staticmethod
    def _object_hook(dct):
        _id = dct.get('id')
        _deed_id = dct.get('deed_id')
        _conveyancer_id = dct.get('conveyancer_id')
        _status = dct.get('status')
        _last_updated = dct.get('last_updated')
        _created_on = dct.get('created_on')

        case = Case()
        case.id = _id
        case.deed_id = _deed_id
        case.conveyancer_id = _conveyancer_id
        case.status = _status
        case.last_updated = _last_updated
        case.created_on = _created_on

        return case
