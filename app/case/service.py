from flask_api import exceptions, status

from app.case.model import Case
from app.db import db
from app.service import deed_api as DeedApi

def save(case):
    try:
        db.session.add(case)
        db.session.commit()
    except Exception as inst:
        print(str(type(inst)) + ":" + str(inst))
        raise exceptions.NotAcceptable()


def all():
    return Case.query.all()


def get(id_):
    return Case.query.filter_by(id=id_).first()


def delete(id_):
    case = Case.query.filter_by(id=id_).first()

    if case is None:
        return case

    db.session.delete(case)
    db.session.commit()

    return case


def get_by_deed_id(deed_id):
    return Case.query.filter_by(deed_id=deed_id).first()


def is_case_status_valid(case_status):
    valid_statuses = ['Case created', 'Deed created', 'Deed signed',
                      'Completion confirmed', 'Submitted']
    return case_status in valid_statuses


def construct_as_payload(deed_id, key_number, reference, amount):

    payload = None

    deed_api = DeedApi()

    deed_json = deed_api.get(deed_id)

    if deed_json:
        payload = {
            "case":{
                "deed": deed_json,
                "key-number": key_number,
                "reference": reference,
                "mortgage-amount": amount
            }
        }

    return payload


def simulate_submit_to_land_registry(payload):

    response = {
        "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
    }

    # Check Payload has all required fields:
    if payload['case'] is not None:
        casedetails = payload['case']
        if casedetails['deed'] is not None and casedetails['key-number'] == '1958333' and casedetails['reference'] != "":

            response.status_code = status.HTTP_200_OK

    return response

