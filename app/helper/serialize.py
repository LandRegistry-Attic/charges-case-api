from datetime import datetime
from dateutil.parser import parse


def serialize_datetime(value):
    if value is None:
        return None
    if isinstance(value, str):
        return parse(value).isoformat()
    if isinstance(value, datetime):
        return value.isoformat()
