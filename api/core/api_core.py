import json
from typing import Union, Dict

import requests


class BaseApi:

    def __init__(self):
        self.API_URL = 'http://demo8955896.mockable.io'
        self.headers = {
            'Content-Type': 'application/json'
        }

    def get(self, url: str, expected_statuscode=200, override_headers: dict = None) -> Union[Dict, str]:
        r = requests.get(self.API_URL + url, headers={**self.headers, **(override_headers if override_headers else {})})

        try:
            response = r.json()
        except json.JSONDecodeError:
            response = r.text

        assert expected_statuscode == r.status_code, json.dumps(
            {'status_code': r.status_code, 'error': response})

        return response
