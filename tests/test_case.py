import json
from app.case.model import Case, as_json
from tests.helpers import with_client, setUpApp, with_context
import unittest
from datetime import datetime
from app.helper.serialize import serialize_datetime
from random import randint


class TestCase (unittest.TestCase):

    def setUp(self):
        setUpApp(self)

    @with_context
    @with_client
    def test_get_api(self, client):
        response = client.get('/case')
        assert response.status_code == 200

    @with_context
    def test_as_json(self):
        id = 1001
        deed_id = 1
        conveyancer_id = 1
        status = "the status"
        last_updated = datetime.today()
        created_on = datetime.today()

        case = Case(id, deed_id, conveyancer_id, status, last_updated, created_on)
        case_as_json = as_json(case)

        assert case_as_json["id"] == id
        assert case_as_json["deed_id"] == deed_id
        assert case_as_json["conveyancer_id"] == conveyancer_id
        assert case_as_json["status"] == status
        assert case_as_json["last_updated"] == serialize_datetime(last_updated)
        assert case_as_json["created_on"] == serialize_datetime(created_on)

    @with_context
    def test_model(self):
        id = 1001
        deed_id = 1
        conveyancer_id = 1
        status = "the status"
        last_updated = datetime.today()
        created_on = datetime.today()

        case = Case(id, deed_id, conveyancer_id, status, last_updated, created_on)

        assert case.id == id
        assert case.deed_id == deed_id
        assert case.conveyancer_id == conveyancer_id
        assert case.status == status
        assert case.last_updated == last_updated
        assert case.created_on == created_on
