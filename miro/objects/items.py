from miro.base import BaseMiroObject


class Item(BaseMiroObject):
    def __init__(self, id: str = None,
                 endpoint='items'):
        super().__init__(id, endpoint)


class Connector(BaseMiroObject):

    def __init__(self, id: str = None,
                 endpoint='connectors'):
        super().__init__(id, endpoint)


class Card(BaseMiroObject):

    def __init__(self, id: str = None,
                 endpoint='cards'):
        super().__init__(id, endpoint)


class AppCard(BaseMiroObject):

    def __init__(self, id: str = None,
                 endpoint='app_cards'):
        super().__init__(id, endpoint)


class BoardMember(BaseMiroObject):

    def __init__(self, id: str = None,
                 endpoint='members'):
        super().__init__(id, endpoint)


class Document(BaseMiroObject):

    def __init__(self, id: str = None,
                 endpoint='documents'):
        super().__init__(id, endpoint)


class Image(BaseMiroObject):

    def __init__(self, id: str = None,
                 endpoint='images'):
        super().__init__(id, endpoint)


class Shape(BaseMiroObject):

    def __init__(self, id: str = None,
                 endpoint='shapes'):
        super().__init__(id, endpoint)


class StickyNote(BaseMiroObject):

    def __init__(self, id: str = None,
                 endpoint='sticky_notes'):
        super().__init__(id, endpoint)


class Text(BaseMiroObject):

    def __init__(self, id: str = None,
                 endpoint='texts'):
        super().__init__(id, endpoint)


class Embed(BaseMiroObject):

    def __init__(self, id: str = None,
                 endpoint='embeds'):
        super().__init__(id, endpoint)
