from app.case.model import Case
from tests.helpers import with_client, setUpApp, with_context
import unittest
from tests.case.helpers import CaseHelper
import json


class TestCaseRoutes (unittest.TestCase):

    def setUp(self):
        setUpApp(self)

    @with_context
    @with_client
    def test_get_all_route(self, client):
        case_id = CaseHelper._create_case_db()

        response = client.get('/case')

        assert response.status_code == 200
        assert '"id": {}'.format(case_id) in response.data.decode()
        assert json.loads(response.data.decode()).__len__() > 0

        CaseHelper._delete_case(case_id)

    @with_context
    @with_client
    def test_get_route(self, client):
        case_id = CaseHelper._create_case_db()
        case = Case.get(case_id)

        response = client.get('/case/{}'.format(case_id))

        assert response.status_code == 200
        assert response.data.decode() == json.dumps(case.to_json())

        CaseHelper._delete_case(case_id)

    @with_context
    @with_client
    def test_delete_route(self, client):
        case_id = CaseHelper._create_case_db()

        response = client.get('/case/{}'.format(case_id))

        assert response.status_code == 200

        Case.delete(case_id)

        response = client.get('/case/{}'.format(case_id))

        assert response.status_code == 404
        assert response.data.decode() == '{"message":'\
                                         '"This resource does not exist."}'
