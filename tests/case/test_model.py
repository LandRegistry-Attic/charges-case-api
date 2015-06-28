from app.case.model import Case
import unittest
from app.helper.serialize import serialize_datetime
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
        case_id = CaseHelper._create_case_db()
        case = Case.get(case_id)

        assert case in Case.all()

        CaseHelper._delete_case(case_id)

        assert case not in Case.all()

    @with_context
    def test_get(self):
        case_id = CaseHelper._create_case_db()
        case = Case.get(case_id)

        assert case.id == case_id

        CaseHelper._delete_case(case_id)

    @with_context
    def test_delete(self):
        case_id = CaseHelper._create_case_db()
        case = Case.get(case_id)

        assert case.id == CaseHelper._id

        Case.delete(case.id)
        case = Case.get(case.id)

        assert case is None

    @with_context
    def test_to_json(self):
        case = CaseHelper._create_case()

        case_as_json = case.to_json()

        assert case_as_json["id"] == CaseHelper._id
        assert case_as_json["deed_id"] == CaseHelper._deed_id
        assert case_as_json["conveyancer_id"] == CaseHelper._conveyancer_id
        assert case_as_json["status"] == CaseHelper._status
        assert case_as_json["last_updated"] == serialize_datetime(
            CaseHelper._last_updated.isoformat())
        assert case_as_json["created_on"] == serialize_datetime(
            CaseHelper._created_on.isoformat())

    @with_context
    def test_from_json(self):

        case = CaseHelper._create_case()

        assert case.id == CaseHelper._id
        assert case.deed_id == CaseHelper._deed_id
        assert case.conveyancer_id == CaseHelper._conveyancer_id
        assert case.status == CaseHelper._status
        assert case.last_updated == CaseHelper._last_updated
        assert case.created_on == CaseHelper._created_on

    @with_context
    def test_model(self):
        case = CaseHelper._create_case()

        assert case.id == CaseHelper._id
        assert case.deed_id == CaseHelper._deed_id
        assert case.conveyancer_id == CaseHelper._conveyancer_id
        assert case.status == CaseHelper._status
        assert case.last_updated == CaseHelper._last_updated
        assert case.created_on == CaseHelper._created_on
