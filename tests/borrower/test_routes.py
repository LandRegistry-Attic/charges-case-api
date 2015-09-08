import json
from unittest import TestCase

from tests.helpers import with_client, setUpApp, \
    with_context, setUpDB, tearDownDB
from tests.case.helpers import CaseHelper
from tests.borrower.helpers import BorrowerHelper
from flask.ext.api import status


class TestBorrowerRoutes(TestCase):
    def setUp(self):
        setUpApp(self)
        setUpDB(self)

    def tearDown(self):
        tearDownDB(self)

    @with_context
    @with_client
    def test_add_borrowers(self, client):
        case = CaseHelper._create_case_and_save()
        borrower1 = BorrowerHelper._create_borrower()
        borrower2 = BorrowerHelper._create_borrower()

        payload = {
            "borrowers": [borrower1.to_json(), borrower2.to_json()]
        }

        add_response = client.post('/case/{}/borrowers'.format(case.id),
                                   data=json.dumps(payload),
                                   content_type='application/json')

        self.assertEqual(add_response.status_code, status.HTTP_200_OK)

        get_cases_response = client.get('/case')

        cases = json.loads(get_cases_response.data.decode())
        case_returned = cases[str(case.id)]
        self.assertIn('borrowers', case_returned)

        borrowers_returned = case_returned['borrowers']
        self.assertEqual(len(borrowers_returned), 2)
        self.assertEqual(borrowers_returned[0]['case_id'], case.id)

        CaseHelper._delete_case(case.id)

    @with_context
    @with_client
    def test_add_borrowers_bad_request(self, client):
        case = CaseHelper._create_case_and_save()
        borrower = BorrowerHelper._create_borrower()
        borrower.first_name = ''

        payload = {
            "borrowers": [borrower.to_json()]
        }

        add_response = client.post('/case/{}/borrowers'.format(case.id),
                                   data=json.dumps(payload),
                                   content_type='application/json')

        self.assertEqual(add_response.status_code, status.HTTP_400_BAD_REQUEST)

        CaseHelper._delete_case(case.id)

    @with_context
    @with_client
    def test_get_borrowers(self, client):
        borrower = BorrowerHelper._create_borrower_and_save()

        response = client.get('/case/{}/borrowers'.format(borrower.case_id))

        borrowers_returned = json.loads(response.data.decode())

        self.assertEqual(len(borrowers_returned), 1)
        self.assertEqual(borrower.id, borrowers_returned[0]['id'])
