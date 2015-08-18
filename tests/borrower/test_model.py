from tests.borrower.helpers import BorrowerHelper
from app.borrower.model import Borrower
import unittest
from tests.helpers import setUpApp, with_context, setUpDB, tearDownDB


class TestBorrowerModel (unittest.TestCase):

    def setUp(self):
        setUpApp(self)
        setUpDB(self)

    def tearDown(self):
        tearDownDB(self)

    @with_context
    def test_get_all(self):
        borrower = BorrowerHelper._create_borrower_and_save()
        borrower = Borrower.get(borrower.id)

        self.assertIn(borrower, Borrower.all())

        BorrowerHelper._delete_borrower(borrower.id)

        self.assertNotIn(borrower, Borrower.all())
