from app.case.model import Case
from random import randint
from datetime import datetime


class CaseHelper:
    _id = randint(1, 999999)
    _conveyancer_id = 1
    _status = "the status"
    _last_updated = datetime.today()
    _created_on = datetime.today()

    @staticmethod
    def _create_case_db(deed_id=None):
        CaseHelper._id = randint(1, 999999)

        _case_dict = {"type": "Case",
                      "id": CaseHelper._id,
                      "conveyancer_id": CaseHelper._conveyancer_id,
                      "status": CaseHelper._status,
                      "last_updated": CaseHelper._last_updated.isoformat(),
                      "created_on": CaseHelper._created_on.isoformat()}

        if deed_id is not None:
            _case_dict['deed_id'] = deed_id

        case = Case.from_json(_case_dict)

        case.save()

        return case

    @staticmethod
    def _create_case():
        CaseHelper._id = randint(1, 999999)

        _case_dict = {"type": "Case",
                      "id": CaseHelper._id,
                      "conveyancer_id": CaseHelper._conveyancer_id,
                      "status": CaseHelper._status,
                      "last_updated": CaseHelper._last_updated.isoformat(),
                      "created_on": CaseHelper._created_on.isoformat()}

        case = Case.from_json(_case_dict)

        return case

    @staticmethod
    def _delete_case(_id):
        Case.delete(_id)
