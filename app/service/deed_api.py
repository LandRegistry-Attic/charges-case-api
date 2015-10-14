from flask_api import request
from app import config


class DeedApi(object):
    DEED_API_BASE_HOST = config.DEED_API_BASE_HOST

    def __init__(self):
        pass




    def get(self, deed_id):
        url = "{base}/deed/{deed_id}".format(
            base=self.DEED_API_BASE_HOST,
            deed_id=str(deed_id)
        )
        return request.get(url)

