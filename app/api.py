import requests
import backoff


@backoff.on_exception(backoff.expo,
                      (requests.exceptions.Timeout,
                       requests.exceptions.ConnectionError))
def census_api(url: str) -> dict:
    try:
        result = requests.get(url)
    except requests.exceptions.RequestException as error:
        # logging.error("Error in API call : %s", error)
        print(error)

    return {"json": result.json()["results"][0], "status_code": result.status_code}
