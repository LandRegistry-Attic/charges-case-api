from app.db import db
from flask import Flask

class Case(db.Model):
    __tablename__ = 'case'

    id = db.Column(db.Integer, primary_key=True)
    deed_id = db.Column(db.Integer)
    converyancer_id = db.Column(db.Integer)
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
        self.converyancer_id = conveyancer_id
        self.status = status
        self.last_updated = last_updated
        self.created_on = created_on

    def __repr__(self):
        return '<Case(id {}, deed_id {}, conveyancer_id {}, status {}, last_updated {}, created {})>'.format(
            self.id,
            self.deed_id,
            self.converyancer_id,
            self.status,
            self.last_updated,
            self.created_on
        )

    def save(self):
        app = Flask(__name__)

        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.session.execute("select * from case")
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def delete(id_):
        case = Case.query.filter_by(id=id_).first()
        db.session.delete(case)
        db.session.commit()
