import unittest

from tests.borrower.helpers import BorrowerHelper
from tests.case.helpers import CaseHelper
from app.borrower import service as BorrowerService
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
    def test_get_by_case_id(self):
        borrower = BorrowerHelper._create_borrower_and_save()

        borrowers = BorrowerService.get_by_case_id(borrower.case_id)

        self.assertEqual(borrower.id, borrowers[0].id)

        CaseHelper._delete_case(borrower.case_id)
