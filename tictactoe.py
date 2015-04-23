"""Tic Tac Toe.

A simple comman-line based game of tic-tac-toe.
"""


class TicTacToe(object):

    """TicTacToe game."""

    def __init__(self):
        """Setup the game.

        Each player has their own board which is represented as a bit array.
        """
        self.player1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.player2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def draw_board(self):
        """Draw the game board."""
        for i in range(9):
            if self.player1[i]:
                print(' x ', end='')
            elif self.player2[i]:
                print(' o ', end='')
            else:
                print('   ', end='')

            if i in [0, 1, 3, 4, 6, 7]:
                print('|', end='')
            if i in [2, 5]:
                print('\n' + '-'*10)

        print()

    def take_turn(self, player):
        """Player picks a location."""
        print("It's your turn, ", end='')
        if player is self.player1:
            print("PLAYER 1")
        else:
            print("PLAYER 2")

        print("""
        1 | 2 | 3
        ----------
        4 | 5 | 6
        ----------
        7 | 8 | 9
            """)

        good_move = False
        while not good_move:
            space = input("Choose a square to mark: ")
            try:
                space = space.strip()
                space = int(space)
            except:
                print("'{}' doesn't appear to be valid. Please enter a number between 1 and 9.".format(space))
                next  # try again

            if self.validate_move(space):
                # the game board spaces start at 1, but the index of the player's array starts at 0
                player[space - 1] = 1
                good_move = True

    def validate_move(self, space):
        """Check that the desired space is a valid move.

        Valid moves are ones that are not already occupied in the range of 1-9.
        """
        if space not in list(range(1, 10)):
            print('{} must be within the range 1-9'.format(space))
            return False
        # Remember that the player's array index starts at 0 but the human input starts at 1
        if (self.player1[space - 1] or self.player2[space - 1]):
            print('{} is already occupied.'.format(space))
            return False
        print('{} is a valid move'.format(space))
        return True

    def is_there_a_winner(self):
        """Check for a winner.

        There are only 8 possible winning boards. Compare each player's board to each winning board.
        """
        winning_boards = [
            [1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 1, 0, 1, 0, 0],
        ]

        for winning_board in winning_boards:
            # Use the winning board as a bit mask against the player's board.
            if winning_board == [x & y for x, y in zip(winning_board, self.player1)]:
                print("Player 1 is the WINNER")
                return True

            if winning_board == [x & y for x, y in zip(winning_board, self.player2)]:
                print("Player 2 is the WINNER")
                return True

        # no match
        return False

if __name__ == '__main__':
    GAME = TicTacToe()
    player = GAME.player1
    while (not GAME.is_there_a_winner()):
        GAME.draw_board()
        GAME.take_turn(player)
        player = GAME.player1 if player == GAME.player2 else GAME.player2
