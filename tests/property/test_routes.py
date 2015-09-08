from unittest import TestCase
from tests.helpers import with_client, setUpApp, \
    with_context, setUpDB, tearDownDB
from tests.case.helpers import CaseHelper
from tests.property.helpers import PropertyHelper
import json
from flask.ext.api import status


class TestPropertyRoutes(TestCase):
    def setUp(self):
        setUpApp(self)
        setUpDB(self)

    def tearDown(self):
        tearDownDB(self)

    @with_context
    @with_client
    def test_add_get_property(self, client):
        case = CaseHelper._create_case_and_save()
        property_ = PropertyHelper._create_property()

        payload = {
            "property": property_.to_json()
        }

        add_response = client.post('/case/{}/property'.format(case.id),
                                   data=json.dumps(payload),
                                   content_type='application/json')

        self.assertEqual(add_response.status_code, status.HTTP_200_OK)

        get_property_response = client.get('/case/{}/property'.format(case.id))

        property_returned = json.loads(get_property_response.data.decode())
        self.assertEqual(property_returned['case_id'], case.id)
        self.assertEqual(property_returned['street'], property_.street)
        self.assertEqual(property_returned['title_number'],
                         property_.title_number)
        self.assertEqual(property_returned['tenure'], property_.tenure)
        self.assertEqual(property_returned['postcode'], property_.postcode)
        self.assertEqual(property_returned['locality'], property_.locality)

        CaseHelper._delete_case(case.id)

    @with_context
    @with_client
    def test_add_two_properties(self, client):
        case = CaseHelper._create_case_and_save()
        property_ = PropertyHelper._create_property()

        payload = {
            "property": property_.to_json()
        }

        add_response = client.post('/case/{}/property'.format(case.id),
                                   data=json.dumps(payload),
                                   content_type='application/json')

        self.assertEqual(add_response.status_code, status.HTTP_200_OK)

        add_response = client.post('/case/{}/property'.format(case.id),
                                   data=json.dumps(payload),
                                   content_type='application/json')
        self.assertEqual(add_response.status_code,
                         status.HTTP_500_INTERNAL_SERVER_ERROR)
