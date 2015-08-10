from app.case.model import Case
from tests.helpers import with_client, setUpApp, \
    with_context, setUpDB, tearDownDB
from tests.case.helpers import CaseHelper
from random import randint
from flask.ext.api import status
import json
import unittest


class TestCaseRoutes(unittest.TestCase):
    no_resource_text = '{"message":' \
                       ' "This resource does not exist."}'

    DEED_ID = 24

    def setUp(self):
        setUpApp(self)
        setUpDB(self)

    def tearDown(self):
        tearDownDB(self)

    @with_context
    @with_client
    def test_get_all_route(self, client):
        case = CaseHelper._create_case_and_save()

        response = client.get('/case')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('"id": {}'.format(case.id), response.data.decode())
        self.assertGreater(json.loads(response.data.decode()).__len__(), 0)

        CaseHelper._delete_case(case.id)

    @with_context
    @with_client
    def test_get_route(self, client):
        case = CaseHelper._create_case_and_save()
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
        case = CaseHelper._create_case_and_save()

        response = client.get('/case/{}'.format(case.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        Case.delete(case.id)

        response = client.get('/case/{}'.format(case.id))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data.decode(), self.no_resource_text)

    @with_context
    @with_client
    def test_update_case_status_route(self, client):
        case = CaseHelper._create_case_and_save()
        CaseHelper._update_case_deed_id(case.id, self.DEED_ID)

        case_status = 'Deed signed'
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
        case = CaseHelper._create_case_and_save()
        CaseHelper._update_case_deed_id(case.id, self.DEED_ID)

        case_status = 'Invalid'
        response = client.post('/case/' + str(case.deed_id) + '/status',
                               data={'status': case_status})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        CaseHelper._delete_case(case.id)

    @with_context
    @with_client
    def test_update_case_status_route_case_not_found(self, client):
        case = CaseHelper._create_case_and_save()
        CaseHelper._update_case_deed_id(case.id, self.DEED_ID)

        case_status = 'Deed signed'
        response = client.post('/case/20/status',
                               data={'status': case_status})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        CaseHelper._delete_case(case.id)

    @with_context
    @with_client
    def test_update_case_deed_route(self, client):
        case = CaseHelper._create_case_and_save()

        response = client.post('/case/' + str(case.id) + '/deed',
                               data={'deed_id': self.DEED_ID})

        updated_case = client.get('/case/{}'.format(case.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('"deed_id": {}'.format(self.DEED_ID),
                      updated_case.data.decode())
        self.assertIn('"status": "{}"'.format('Deed created'),
                      updated_case.data.decode())

        CaseHelper._delete_case(case.id)

    @with_context
    @with_client
    def test_update_case_deed_route_case_not_found(self, client):
        case = CaseHelper._create_case_and_save()

        deed_id = '1'
        response = client.post('/case/' + str(case.id + 1) + '/deed',
                               data={'deed_id': deed_id})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        CaseHelper._delete_case(case.id)

    @with_context
    @with_client
    def test_update_case_deed_route_missing_deed_id(self, client):
        case = CaseHelper._create_case_and_save()

        response = client.post('/case/' + str(case.id) + '/deed')

        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)

        CaseHelper._delete_case(case.id)

    @with_context
    @with_client
    def test_update_case_deed_route_deed_id_already_set(self, client):
        case = CaseHelper._create_case_and_save()
        CaseHelper._update_case_deed_id(case.id, self.DEED_ID)

        response = client.post('/case/' + str(case.id) + '/deed',
                               data={'deed_id': 10})

        self.assertEqual(response.status_code,
                         status.HTTP_403_FORBIDDEN)

        CaseHelper._delete_case(case.id)

    @with_context
    @with_client
    def test_create_case_with_ref_num(self, client):
        case = {
            'conveyancer_id': 1,
            'case_ref': 'abc1234'
        }
        response = client.post('/case', data=case)
        case_json = json.loads(response.data.decode())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(case_json['conveyancer_id'], case['conveyancer_id'])
        self.assertEqual(case_json['case_ref'], case['case_ref'])

        CaseHelper._delete_case(case_json['id'])

    @with_context
    @with_client
    def test_create_case_without_ref_num(self, client):
        case = {
            'conveyancer_id': 1
        }
        response = client.post('/case', data=case)
        case_json = json.loads(response.data.decode())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(case_json['conveyancer_id'], case['conveyancer_id'])
        self.assertNotIn('case_ref', case_json)

        CaseHelper._delete_case(case_json['id'])
