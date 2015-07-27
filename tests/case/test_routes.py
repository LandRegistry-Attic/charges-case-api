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
        case = CaseHelper._create_case_db()

        response = client.get('/case')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('"id": {}'.format(case.id), response.data.decode())
        self.assertGreater(json.loads(response.data.decode()).__len__(), 0)

        CaseHelper._delete_case(case.id)

    @with_context
    @with_client
    def test_get_route(self, client):
        case = CaseHelper._create_case_db()
        case = Case.get(case.id)

        response = client.get('/case/{}'.format(case.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.decode(), json.dumps(case.to_json()))

        CaseHelper._delete_case(case.id)

    @with_context
    @with_client
    def test_no_get_route(self, client):
        response = client.get('/case/{}'.format(randint(1, 9999999)))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data.decode(), self.no_resource_text)

    @with_context
    @with_client
    def test_delete_route(self, client):
        case = CaseHelper._create_case_db()

        response = client.get('/case/{}'.format(case.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        Case.delete(case.id)

        response = client.get('/case/{}'.format(case.id))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data.decode(), self.no_resource_text)

    @with_context
    @with_client
    def test_update_case_status_route(self, client):
        case = CaseHelper._create_case_db()

        case_status = 'Signed'
        response = client.post('/case/' + str(case.deed_id) + '/status',
                               data={"status": case_status})

        updated_case = client.get('/case/{}'.format(case.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('"status": "{}"'.format(case_status),
                      updated_case.data.decode())

        CaseHelper._delete_case(case.id)

    @with_context
    @with_client
    def test_update_case_status_route_invalid_status(self, client):
        case = CaseHelper._create_case_db()

        case_status = 'Invalid'
        response = client.post('/case/' + str(case.deed_id) + '/status',
                               data={'status': case_status})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        CaseHelper._delete_case(case.id)

    @with_context
    @with_client
    def test_update_case_status_route_case_not_found(self, client):
        case = CaseHelper._create_case_db()

        case_status = 'Signed'
        response = client.post('/case/' + str(case.deed_id + 1) + '/status',
                               data={'status': case_status})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        CaseHelper._delete_case(case.id)
