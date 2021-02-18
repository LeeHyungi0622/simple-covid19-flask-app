import requests

URL = "https://apiv2.corona-live.com/updates.json?timestamp=1613547340934"


def get_json_data():
    return requests.get(URL).json()
