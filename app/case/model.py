from app.db import db
from app.helper.serialize import serialize_datetime
from app.helper.dict_from_model import sqlalchemy_to_dict

class Case(db.Model):

    __tablename__ = 'case'

    id = db.Column(db.Integer, primary_key=True)
    deed_id = db.Column(db.Integer)
    conveyancer_id = db.Column(db.Integer)
    status = db.Column(db.String())
    last_updated = db.Column(db.DateTime())
    created_on = db.Column(db.DateTime())

    def __init__(
            self,
            id,
            deed_id,
            conveyancer_id,
            status,
            last_updated,
            created_on):
        self.id = id
        self.deed_id = deed_id
        self.conveyancer_id = conveyancer_id
        self.status = status
        self.last_updated = last_updated
        self.created_on = created_on

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def all():
        return [sqlalchemy_to_dict(case) for case in Case.query.all()]

    @staticmethod
    def get(id_):
        case = Case.query.filter_by(id=id_).first()
        return sqlalchemy_to_dict(case)

    @staticmethod
    def delete(id_):
        case = Case.query.filter_by(id=id_).first()
        db.session.delete(case)
        db.session.commit()

    def as_json(self):
        return dict(
            id=self.id,
            deed_id=self.deed_id,
            conveyancer_id=self.conveyancer_id,
            status=self.status,
            last_updated=serialize_datetime(self.last_updated),
            created_on=serialize_datetime(self.created_on)
        )
