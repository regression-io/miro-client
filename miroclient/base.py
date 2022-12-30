import json

from miroclient.client import MiroApiClient
from miroclient.exceptions import UnexpectedResponseException


class BaseMiroObject(MiroApiClient):
    def __init__(self, id: str = None, endpoint: str = None):
        super().__init__()
        self.id = id
        self.endpoint = endpoint
        self._client = None

    def get(self):
        json = self._get(f'{self.endpoint}/{self.id}')
        return self.to_entity(json)

    def get_by_name(self, name: str):
        json = self._get(f'{self.endpoint}?name={name}')
        if 'data' in json and len(json['data']) > 0:
            self.to_entity(json['data'][0])
            return self

    def create(self, name, desc):
        board_data = {
            'name': name,
            'description': desc
        }

        json = self._post(self.endpoint, board_data)
        return self.to_entity(json)

    def update(self, id, board_data):
        json = self._update(f'{self.endpoint}/{id}', board_data)
        return self.to_entity(json)

    def delete(self, id):
        json = self._delete(f'{self.endpoint}/{id}')
        return self.to_entity(json)

    def to_entity(self, json):
        self.__dict__.update(json)
        return self

    def __repr__(self) -> str:
        return json.dumps(self.__dict__, default=str)

    def all_by_board_id(self, board_id: str):
        items_json = self._get(f'boards/{board_id}/{self.endpoint}')
        items_json = items_json['data']

        items = []
        try:
            for w in items_json:
                if 'type' in w:
                    item = self.get_one(w['type'])
                else:
                    item = self.__class__()
                items.append(item.to_entity(w))
        except Exception as e:
            raise UnexpectedResponseException(cause=e)

        return items

    def capcase(self, s):
        return ''.join(x for x in s.title() if x != '_')

    def get_one(self, typ: str):
        import importlib
        module = importlib.import_module('miroclient.entities.items')
        class_ = getattr(module, self.capcase(typ))
        return class_()
