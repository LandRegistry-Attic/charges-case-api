from random import randint
from app.borrower.model import Borrower
from app.borrower import service as BorrowerService
from tests.case.helpers import CaseHelper


class BorrowerHelper:
    _id = '1'
    _case_id = '0'
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
        BorrowerService.save(borrower)

        return borrower

    @staticmethod
    def _create_borrower():
        BorrowerHelper._id = randint(1, 999999)
        borrower = Borrower(BorrowerHelper._case_id,
                            BorrowerHelper._first_name,
                            BorrowerHelper._last_name,
                            BorrowerHelper._mobile_no,
                            BorrowerHelper._email_address,
                            BorrowerHelper._address,
                            BorrowerHelper._middle_names)
        borrower.id = BorrowerHelper._id

        return borrower

    @staticmethod
    def _delete_borrower(_id):
        BorrowerService.delete(_id)
