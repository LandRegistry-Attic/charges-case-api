from app.case.model import Case
from app.case import service as CaseService
from random import randint
from datetime import datetime


class CaseHelper:
    _id = randint(1, 999999)
    _conveyancer_id = 1
    _status = "the status"
    _last_updated = datetime.today()
    _created_on = datetime.today()

    @staticmethod
    def _create_case_and_save():
        case = CaseHelper._create_case()
        CaseService.save(case)

        return case

    @staticmethod
    def _update_case_deed_id(case_id, deed_id):
        case = CaseService.get(case_id)
        case.deed_id = deed_id
        CaseService.save(case)

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
        CaseService.delete(_id)

    @staticmethod
    def _update_status(case_id, status):
        case = CaseService.get(case_id)
        case.status = status
        CaseService.save(case)
