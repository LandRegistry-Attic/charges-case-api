from app.case.model import Case
from random import randint
from datetime import datetime


class CaseHelper:
    _id = randint(1, 999999)
    _deed_id = 1
    _conveyancer_id = 1
    _status = "the status"
    _last_updated = datetime.today()
    _created_on = datetime.today()


    @staticmethod
    def _create_case_db():
        CaseHelper._id = randint(1, 999999)

        _case_dict = {"type": "Case",
                      "id": CaseHelper._id,
                      "deed_id": CaseHelper._deed_id,
                      "conveyancer_id": CaseHelper._conveyancer_id,
                      "status": CaseHelper._status,
                      "last_updated": CaseHelper._last_updated.isoformat(),
                      "created_on": CaseHelper._created_on.isoformat()}

        case = Case.from_json(_case_dict)

        case.save()

        return case.id

    @staticmethod
    def _create_case():
        CaseHelper._id = randint(1, 999999)

        _case_dict = {"type": "Case",
                      "id": CaseHelper._id,
                      "deed_id": CaseHelper._deed_id,
                      "conveyancer_id": CaseHelper._conveyancer_id,
                      "status": CaseHelper._status,
                      "last_updated": CaseHelper._last_updated.isoformat(),
                      "created_on": CaseHelper._created_on.isoformat()}

        case = Case.from_json(_case_dict)

        return case

    @staticmethod
    def _delete_case(_id):
        Case.delete(_id)
