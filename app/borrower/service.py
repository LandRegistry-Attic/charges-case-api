from app.borrower.model import Borrower
from app.db import db


def save(borrower):
    db.session.add(borrower)
    db.session.commit()


def bulk_add(borrowers):
    conn = db.session.connection()
    conn.execute(Borrower.__table__.insert(), borrowers)
    db.session.commit()


def all():
    return Borrower.query.all()


def get(id_):
    return Borrower.query.filter_by(id=id_).first()


def get_by_case_id(case_id):
    return Borrower.query.filter_by(case_id=case_id).all()


def delete(id_):
    borrower = Borrower.query.filter_by(id=id_).first()

    if borrower is None:
        return borrower

    db.session.delete(borrower)
    db.session.commit()

    return borrower
