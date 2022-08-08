MAX_PLAYERS = 62
from copy import deepcopy

class Game:
    def __init__(self, w, h, n_players, n_npcs):
        self.empty_char = '.'
        if n_players > MAX_PLAYERS:
            raise RuntimeError("Too many players, " + str(n_players) + " is more than " + str(MAX_PLAYERS))
        self.width = w
        self.height = h
        self.board = []
        for x in range(w):
            self.board.append([])
            for y in range(h):
                self.board[-1].append(self.empty_char)

        # Initialize players
        # A player is represented as a list entry, with the list being composed of their character on the tic tac toe board
        self.next_player_turn = 0
        self.players = [chr(ord('0') + x) for x in range(10)]
        self.players.extend([chr(ord('a') + x) for x in range(26)])
        self.players.extend([chr(ord('A') + x) for x in range(26)])
        self.players = self.players[:n_players]

        self.n_npcs = n_npcs
    
    def step(self, player, x, y):
        '''Complete a single step in the game.
        
        Parameters:
            player: An integer representing the player number to complete a turn.
            x: The x value of the turn.
            y: The y value of the turn.
        
        Returns:
            Pair with (True if successful, False otherwise) and (return message)
        '''
        # Check correct turn
        if self.next_player_turn != player:
            return (False, "Not currently player " + str(player) + "'s turn, player " + str(self.next_player_turn) + " should go")

        # Check bounds of x and y
        if x < 0 or x >= self.width:
            return (False, "Specified x value " + str(x) + " too low or high, bounds are 0 <= x < " + str(self.width))

        if y < 0 or y >= self.height:
            return (False, "Specified y value " + str(y) + " too low or high, bounds are 0 <= y < " + str(self.height))

        # Check square empty
        if self.board[x][y] != self.empty_char:
            return (False, "Square (" + str(x) + ", " + str(y) + ") already occupied")

        # Change corresponding tile
        self.board[x][y] = self.players[player]

        # Progress the turn
        self.next_player_turn = (self.next_player_turn + 1) % len(self.players)

        return (True, "")
    
    def print_to_console(self):
        '''Print the board to the console
        '''
        for y in range(self.height):
            for x in range(self.width):
                print(self.board[x][y], end='')
            print()
    
    def check_helper(self, player, x, y, dx, dy):
        '''A recursive helper to check for a win.
        
        Parameters:
            player: An int representing the player to check
            x: The current x value to check
            y: The current y value to check
            dx: The direction to check in x-wise
            dy: The direction to check in y-wise
            
        Returns:
            The number of filled squares in a row in the given direction
        '''
        # Check bounds of x and y
        if x < 0 or x >= self.width:
            return 0

        if y < 0 or y >= self.height:
            return 0

        if self.board[x][y] != self.players[player]:
            return 0

        return self.check_helper(player, x+dx, y+dy, dx, dy) + 1

    def check_win(self, player):
        '''Check that a player has won or lost
        
        Parameters:
            player: The int representing the player to check
            
        Returns:
            True for win, False otherwise
        '''
        diffs = [-1, 0, 1]
        # Brute force iterate over every board square in every direction
        for x in range(self.width):
            for y in range(self.height):
                for diffx in diffs:
                    for diffy in diffs:
                        if (diffx or diffy) and self.check_helper(player, x, y, diffx, diffy) >= 3:
                            return True
        return False


#game = Game(5, 4, 0, 0)
#game.print_to_console()