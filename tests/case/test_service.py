import unittest

from app.case import service as CaseService
from tests.helpers import setUpApp, with_context, setUpDB, tearDownDB
from tests.case.helpers import CaseHelper


class TestCaseModel (unittest.TestCase):

    def setUp(self):
        setUpApp(self)
        setUpDB(self)

    def tearDown(self):
        tearDownDB(self)

    @with_context
    def test_get_all(self):
        case = CaseHelper._create_case_and_save()
        case = CaseService.get(case.id)

        self.assertIn(case, CaseService.all())

        CaseHelper._delete_case(case.id)

        self.assertNotIn(case, CaseService.all())

    @with_context
    def test_get(self):
        case = CaseHelper._create_case_and_save()
        case = CaseService.get(case.id)

        self.assertEqual(case.id, case.id)

        CaseHelper._delete_case(case.id)

    @with_context
    def test_delete(self):
        case = CaseHelper._create_case_and_save()
        case = CaseService.get(case.id)

        self.assertEqual(case.id, CaseHelper._id)

        CaseService.delete(case.id)
        case = CaseService.get(case.id)

        self.assertIs(case, None)

    @with_context
    def test_is_case_status_valid_positive(self):
        self.assertTrue(CaseService.is_case_status_valid("Deed signed"))

    @with_context
    def test_is_case_status_valid_negative(self):
        self.assertFalse(CaseService.is_case_status_valid("Invalid status"))
