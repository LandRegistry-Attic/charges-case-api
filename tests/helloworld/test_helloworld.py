import unittest
from tests.helpers import setUpApp, with_client, with_context


class TestHelloWorld (unittest.TestCase):

    def setUp(self):
        setUpApp(self)

    @with_context
    @with_client
    def test_get_api(self, client):
        response = client.get('/helloworld')
        self.assertEqual(response.status_code, 200)
        self.assertIn('"Hello": "World"', response.data.decode())
