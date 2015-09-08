from app.borrower.model import Borrower
from app.case.model import Case
from app.db import db


class Service:

    @staticmethod
    def save(case):
        db.session.add(case)
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
    def all_with_borrowers():
        return db.session.query(Case, Borrower).outerjoin(Borrower).all()

    @staticmethod
    def get_by_deed_id(deed_id):
        return Case.query.filter_by(deed_id=deed_id).first()

    @staticmethod
    def is_case_status_valid(case_status):
        valid_statuses = ['Case created', 'Deed created', 'Deed signed',
                          'Completion confirmed', 'Submitted']
        return case_status in valid_statuses
