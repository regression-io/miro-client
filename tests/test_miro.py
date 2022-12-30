from miroclient.entities.board import Board


# def test_create_board():
#     board = Board().create('test-board', 'this is a test board')
#     print(board)

def test_get_board():
    board = Board().get_by_name('test-board')
    print(board)

def test_get_board_items():
    board = Board().get_by_name('test-board')
    print(board.items)

def test_get_board_connectors():
    board = Board().get_by_name('test-board')
    print(board.connectors)

def test_get_board_cards():
    board = Board().get_by_name('test-board')
    print(board.cards)

if __name__ == '__main__':
    test_get_board()
