from app.borrower.model import Borrower
from app.db import db


class Service:

    @staticmethod
    def save(borrower):
        db.session.add(borrower)
        db.session.commit()

    @staticmethod
    def bulk_add(borrowers):
        conn = db.session.connection()
        conn.execute(Borrower.__table__.insert(), borrowers)
        db.session.commit()

    @staticmethod
    def all():
        return Borrower.query.all()

    @staticmethod
    def get(id_):
        return Borrower.query.filter_by(id=id_).first()

    @staticmethod
    def get_by_case_id(case_id):
        return Borrower.query.filter_by(case_id=case_id).all()

    @staticmethod
    def delete(id_):
        borrower = Borrower.query.filter_by(id=id_).first()

        if borrower is None:
            return borrower

        db.session.delete(borrower)
        db.session.commit()

        return borrower
