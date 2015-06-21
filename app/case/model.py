from app.db import db


class Case(db.Model):

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

        db.session.delete(case)
        db.session.commit()
        return
