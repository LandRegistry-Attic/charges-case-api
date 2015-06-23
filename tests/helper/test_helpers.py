from datetime import datetime
from tests.helpers import setUpApp, with_context
from app.helper.serialize import serialize_datetime

import unittest


class TestHelloWorld (unittest.TestCase):

    def setUp(self):
        setUpApp(self)

    @with_context
    def test_serialize_date(self):
        date_to_test = datetime(2007, 12, 6, 16, 29, 43, 79043)
        assert serialize_datetime(date_to_test) == '2007-12-06T16:29:43.079043'
