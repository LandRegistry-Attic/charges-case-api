from .model import Property
from app.db import db


def get_property_by_case_id(case_id):
    return Property.query.filter_by(case_id=case_id).first()


def save(property_):
    db.session.add(property_)
    db.session.commit()


def get(id_):
    return Property.query.filter_by(id=id_).first()
