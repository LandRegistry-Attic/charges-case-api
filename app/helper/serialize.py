import types
from datetime import datetime


def serialize_datetime(value):
    if value is None:
        return None
    return value.isoformat()

def sqlalchemy_to_dict(model):
    model_dict = {}

    for i in model.__table__._columns:
        column_value = model.__getattribute__(i.name)
        if type(column_value) is datetime:
            column_value = serialize_datetime(column_value)

        model_dict[i.name] = column_value

    return model_dict

def dict_to_sqlalchemy(json, base_model):
    for key in json.keys():
        base_model.__setattr__(key, json[key])

    return base_model
