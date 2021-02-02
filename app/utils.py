import os
from typing import TypedDict


class ConfigVars(TypedDict):
    """
    Used to define the dict types in a strict way.
    """
    url: str


def get_variables() -> ConfigVars:
    """
    get_variables is used to access environmental variables
    :return:
    """
    try:
        url: dict = os.environ['URL']
    except KeyError:
        raise KeyError("Please verify that the needed env variables are set")
    return {"url": url}
