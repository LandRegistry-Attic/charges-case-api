import unittest

from tests.borrower.helpers import BorrowerHelper
from tests.helpers import setUpApp, with_context, setUpDB, tearDownDB


class TestBorrowerModel(unittest.TestCase):
    def setUp(self):
        setUpApp(self)
        setUpDB(self)

    def tearDown(self):
        tearDownDB(self)

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
