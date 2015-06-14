def serialize_datetime(value):
    if value is None:
        return None
    return value.isoformat()
