from app.case.model import Case
from tests.helpers import with_client, setUpApp, \
    with_context, setUpDB, tearDownDB
from tests.case.helpers import CaseHelper
from random import randint
from flask.ext.api import status
import json
import unittest


class TestCaseRoutes (unittest.TestCase):

    no_resource_text = '{"message":' \
        ' "This resource does not exist."}'

    def setUp(self):
        setUpApp(self)
        setUpDB(self)

    def tearDown(self):
        tearDownDB(self)

    @with_context
    @with_client
    def test_get_all_route(self, client):
        case_id = CaseHelper._create_case_db()

        response = client.get('/case')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('"id": {}'.format(case_id), response.data.decode())
        self.assertGreater(json.loads(response.data.decode()).__len__(), 0)

        CaseHelper._delete_case(case_id)

    @with_context
    @with_client
    def test_get_route(self, client):
        case_id = CaseHelper._create_case_db()
        case = Case.get(case_id)

        response = client.get('/case/{}'.format(case_id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.decode(), json.dumps(case.to_json()))

        CaseHelper._delete_case(case_id)

    @with_context
    @with_client
    def test_no_get_route(self, client):

        response = client.get('/case/{}'.format(randint(1, 9999999)))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data.decode(), self.no_resource_text)

    @with_context
    @with_client
    def test_delete_route(self, client):
        case_id = CaseHelper._create_case_db()

        response = client.get('/case/{}'.format(case_id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        Case.delete(case_id)

        response = client.get('/case/{}'.format(case_id))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data.decode(), self.no_resource_text)
