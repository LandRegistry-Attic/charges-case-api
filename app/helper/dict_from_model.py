import types
from app.helper.serialize import serialize_datetime
from datetime import datetime

def sqlalchemy_to_dict(model):
    model_dict = {}

    for i in model.__table__._columns._all_columns:
        column_value = model.__getattribute__(i.name)
        if type(column_value) is datetime:
            column_value = serialize_datetime(column_value)

        model_dict[i.name] = column_value

    return model_dict