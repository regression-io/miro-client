import json
import os

import requests

from miro.utils import (get_json_or_raise_exception)

BASE_URL = 'https://api.miro.com'


class MiroApiClient:

    def _get(self, id: str) -> dict:
        url = f'{BASE_URL}/v2/{id}'
        response = requests.get(url, headers=self._auth_header())
        return get_json_or_raise_exception(response)

    def _post(self, collection: str, data: dict) -> dict:
        url = f'{BASE_URL}/v2/{collection}/'
        response = requests.post(url, headers=self._auth_header(), json=data)
        return get_json_or_raise_exception(response)

    def _update(self, id: str, data: dict) -> dict:
        url = f'{BASE_URL}/v2/{id}'
        response = requests.put(url, headers=self._auth_header(), json=data)
        return get_json_or_raise_exception(response)

    def _delete(self, id: str) -> dict:
        url = f'{BASE_URL}/v2/{id}'
        response = requests.delete(url, headers=self._auth_header())
        return get_json_or_raise_exception(response)

    def _auth_header(self):
        return {
            'Authorization': f'Bearer: {self._auth_token_from_env()}'
        }

    def _auth_token_from_env(self) -> str:
        return os.environ.get('MIRO_AUTH_TOKEN', '')
