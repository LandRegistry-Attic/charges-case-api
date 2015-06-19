import json
from flask.ext.api import status

def record_not_found():
    return json.dumps(
        {
            "title": "record not found",
            "status": status.HTTP_404_NOT_FOUND
        }), status.HTTP_404_NOT_FOUND
