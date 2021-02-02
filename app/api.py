"""

"""
from typing import TypedDict

import requests
import backoff


class RestReponse(TypedDict):
    """
    Used to define the dict types in a strict way.
    """
    json: dict
    status_code: int


@backoff.on_exception(backoff.expo,
                      (requests.exceptions.Timeout,
                       requests.exceptions.ConnectionError))
def app_api(url: str) -> RestReponse:
    """

    :param url:
    :return:
    """
    try:
        result: requests.Response = requests.get(url)
    except requests.exceptions.RequestException as error:
        print(error)

    return {"json": result.json()["results"][0], "status_code": result.status_code}


class LamdaResponse(TypedDict):
    """
    Used to define the dict types in a strict way.
    """
    state: dict
    insert: dict
    delete: dict
    schema: dict
    has_more: dict


def create_response(json: dict) -> LamdaResponse:
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
