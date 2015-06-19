def serialize_datetime(value):
    if value is None:
        return None
    return value.isoformat()

def serialize_list(list_):
    try:
        return [i.as_json() for i in list_]
    except NotImplementedError:
        print("You need to implement an as_json() function for your object")
        raise

def serialize_object(model):
    try:
        return model.as_json()
    except NotImplementedError:
        print("You need to implement an as_json() function for your object")
        raise
