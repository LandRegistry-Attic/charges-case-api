def serialize_datetime(value):
    if value is None:
        return None
    return value.isoformat()

def serialize_list(json_list):
    return [i.as_json() for i in json_list]
