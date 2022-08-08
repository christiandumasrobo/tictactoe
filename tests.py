from game import Game

def test_win():
    game = Game(5, 6, 2, 0)
    game.board[0][0] = '0'
    game.board[1][1] = '0'
    game.board[2][2] = '0'
    game.print_to_console()
    print(game.check_win(0))
    print(game.check_win(1))

def test_turns():
    game = Game(5, 6, 2, 0)
    result = game.step(1, 0, 0)
    if not result[0]:
        print("Correct response: " + result[1])

test_turns()
