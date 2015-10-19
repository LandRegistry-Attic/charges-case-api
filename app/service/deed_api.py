from app import config
import requests
from flask.ext.api import status



def get_deed_helper(deed_id):
    result = None
    url = "{base}/deed/{deed_id}".format(
        base=config.DEED_API_BASE_HOST,
        deed_id=str(deed_id)
    )
    response = requests.get(url)

    if response.status_code == status.HTTP_200_OK:
        result = response.content.decode()

    return result



