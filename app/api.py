"""

"""
from typing import TypedDict
import time

import requests
import backoff
import datetime


class RestResponse(TypedDict):
    """
    Used to define the dict types in a strict way.
    """
    json: dict
    status_code: int


@backoff.on_exception(backoff.expo,
                      (requests.exceptions.Timeout,
                       requests.exceptions.ConnectionError))
def app_api(url: str = "https://my.api.mockaroo.com/fake_data_poc.json",
            headers: dict = {'X-API-Key': '56c5cc10'}) -> RestResponse:
    """

    :param url:
    :param headers:
    :return:
    """
    try:
        result: requests.Response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as error:
        print(error)

    return {"json": result.json(), "status_code": result.status_code}


class LambdaResponse(TypedDict):
    """
    Used to define the dict types in a strict way.
    """
    state: dict
    insert: dict
    delete: dict
    schema: dict
    has_more: dict


def create_response(response_json: list) -> LambdaResponse:
    """

    :return:
    """
    timestamp: str = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    result = {'state': {timestamp: timestamp},
              'insert': {'students': response_json}}
    return result
