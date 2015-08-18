from app.borrower.model import Borrower
from tests.case.helpers import CaseHelper
from random import randint


class BorrowerHelper:
    _id = randint(1, 999999)
    _first_name = "Frank"
    _middle_names = "The Undesputable"
    _last_name = "Tank"
    _mobile_no = "666"
    _email_address = "tank@armour.com"
    _address = ["addr1", "addr2"]

    @staticmethod
    def _create_borrower_and_save():
        case = CaseHelper._create_case_and_save()

        borrower = BorrowerHelper._create_borrower()
        borrower.case_id = case.id
        borrower.save()

        return borrower

    @staticmethod
    def _create_borrower():

        borrower = Borrower(BorrowerHelper._first_name,
                            BorrowerHelper._middle_names,
                            BorrowerHelper._last_name,
                            BorrowerHelper._mobile_no,
                            BorrowerHelper._email_address,
                            BorrowerHelper._address)
        borrower.id = BorrowerHelper._id

        return borrower

    @staticmethod
    def _delete_borrower(_id):
        Borrower.delete(_id)
