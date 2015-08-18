from app.db import db, array_type


class Borrower(db.Model):
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
