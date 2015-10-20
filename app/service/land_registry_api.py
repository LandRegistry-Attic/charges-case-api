from app import config
import requests


def submit_helper(payload):
    url = "{base}/landregistry/submit".format(
        base=config.CASE_API_BASE_HOST
    )

    response = requests.post(url, data={"payload": payload})

    return response
