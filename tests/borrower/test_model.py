from tests.borrower.helpers import BorrowerHelper
from tests.case.helpers import CaseHelper
from app.borrower.model import Borrower
from app.borrower.service import Service as BorrowerService
import unittest
from tests.helpers import setUpApp, with_context, setUpDB, tearDownDB


class TestBorrowerModel(unittest.TestCase):
    def setUp(self):
        setUpApp(self)
        setUpDB(self)

    def tearDown(self):
        tearDownDB(self)

    @with_context
    def test_get_all(self):
        borrower = BorrowerHelper._create_borrower_and_save()
        borrower = BorrowerService.get(borrower.id)

        self.assertIn(borrower, BorrowerService.all())

        BorrowerHelper._delete_borrower(borrower.id)

        self.assertNotIn(borrower, BorrowerService.all())

    @with_context
    def test_to_json(self):
        borrower = BorrowerHelper._create_borrower()

        borrower_as_json = borrower.to_json()

        self.assertEqual(borrower_as_json["id"], BorrowerHelper._id)
        self.assertEqual(borrower_as_json["first_name"],
                         BorrowerHelper._first_name)
        self.assertEqual(borrower_as_json["last_name"],
                         BorrowerHelper._last_name)
        self.assertEqual(borrower_as_json["middle_names"],
                         BorrowerHelper._middle_names)
        self.assertEqual(borrower_as_json["mobile_no"],
                         BorrowerHelper._mobile_no)
        self.assertEqual(borrower_as_json["email_address"],
                         BorrowerHelper._email_address)
        self.assertEqual(borrower_as_json["address"],
                         BorrowerHelper._address)

    @with_context
    def test_get_by_case_id(self):
        borrower = BorrowerHelper._create_borrower_and_save()

        borrowers = BorrowerService.get_by_case_id(borrower.case_id)

        self.assertEqual(borrower.id, borrowers[0].id)

        CaseHelper._delete_case(borrower.case_id)
