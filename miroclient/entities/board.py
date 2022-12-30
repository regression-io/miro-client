from miroclient.base import BaseMiroObject
from miroclient.entities.items import Item, Connector, Card, BoardMember, AppCard, Document, Shape, Text, StickyNote, Image, Embed


class Board(BaseMiroObject):

    def __init__(self, id: str = None):
        super().__init__(id, 'boards')

    @property
    def items(self):
        return Item().all_by_board_id(self.id)

    @property
    def connectors(self):
        return Connector().all_by_board_id(self.id)

    def cards(self):
        return Card().all_by_board_id(self.id)

    @property
    def members(self):
        return BoardMember().all_by_board_id(self.id)

    def app_cards(self):
        return AppCard().all_by_board_id(self.id)

    def documents(self):
        return Document().all_by_board_id(self.id)

    def shapes(self):
        return Shape().all_by_board_id(self.id)

    def texts(self):
        return Text().all_by_board_id(self.id)

    def sticky_notes(self):
        return StickyNote().all_by_board_id(self.id)

    def embeds(self):
        return Embed().all_by_board_id(self.id)

    def images(self):
        return Image().all_by_board_id(self.id)

def get_board_id(name):
    return Board().get_by_name(name).id
