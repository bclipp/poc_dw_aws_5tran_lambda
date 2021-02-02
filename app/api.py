"""

"""

import requests
import backoff


@backoff.on_exception(backoff.expo,
                      (requests.exceptions.Timeout,
                       requests.exceptions.ConnectionError))
def app_api(url: str) -> dict:
    """

    :param url:
    :return:
    """
    try:
        result: requests.Response = requests.get(url)
    except requests.exceptions.RequestException as error:
        print(error)

    return {"json": result.json()["results"][0], "status_code": result.status_code}


def create_response(json: dict) -> dict:
    """

    :return:
    """
    response: dict = dict()
    state = ""
    insert = ""
    delete = ""
    schema = ""
    has_more = ""
    return response
