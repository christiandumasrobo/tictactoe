from game import Game

w = int(input("How wide should the board be? "))
h = int(input("How tall should the board be? "))
n_players = int(input("How many players should there be? "))
game = Game(w, h, n_players, 0)

current_turn = game.next_player_turn
while True:
    game.print_to_console()
    print("Player " + str(current_turn) + "'s turn")
    x = int(input("Please enter the x coordinate for your turn: "))
    y = int(input("Please enter the y coordinate for your turn: "))
    turn_result = game.step(current_turn, x, y)
    if not turn_result[0]:
        print(turn_result[1])
        continue

    if game.check_win(current_turn):
        print("Congrats player " + str(current_turn) + ", you win!")
        break

    current_turn = (current_turn + 1) % len(game.players)