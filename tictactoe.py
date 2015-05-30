"""Tic Tac Toe.

A simple comman-line based game of tic-tac-toe.
"""


class TicTacToe(object):

    """TicTacToe game."""

    def __init__(self):
        """Setup the game.

        Each player has their own board which is represented as a bit array. A 1 means they are in that
        position on the board, a 0 means they are not.
        """
        self.player1 = set()
        self.player2 = set()

    def draw_board(self):
        """Draw the game board. Player1 is x, Player2 is o."""
        for i in range(1, 10):
            if i in self.player1:
                print(' x ', end='')
            elif i in self.player2:
                print(' o ', end='')
            else:
                print('   ', end='')

            if i in [1, 2, 4, 5, 7, 8]:
                print('|', end='')
            if i in [3, 6]:
                print('\n' + '-'*10)

        print()

    def take_turn(self, player):
        """Player picks a location."""
        print("It's your turn, ", end='')
        if player is self.player1:
            print("PLAYER 1")
        else:
            print("PLAYER 2")
            return self.computer_turn()

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
                player.add(space)
                good_move = True

    def computer_turn(self):
        for space in range(1, 10):
            if(self.validate_move(space)):
                self.player2.add(space)
                return

    def validate_move(self, space):
        """Check that the desired space is a valid move.

        Valid moves are ones that are not already occupied in the range of 1-9.
        """
        if space not in list(range(1, 10)):
            print('{} must be within the range 1-9'.format(space))
            return False
        if ((space in self.player1) or (space in self.player2)):
            print('{} is already occupied.'.format(space))
            return False
        print('{} is a valid move'.format(space))
        return True

    def cats_game(self):
        """Return true if this is a cats game and there are no more moves to play."""
        if set([1, 2, 3, 4, 5, 6, 7, 8, 9]) == self.player1.union(self.player2):
            print("CATS GAME! Please play again...")
            return True
        return False

    def is_there_a_winner(self):
        """Check for a winner.

        There are only 8 possible winning boards. Compare each player's board to each winning board.
        """
        winning_boards = [
            set([1, 2, 3]),
            set([4, 5, 6]),
            set([7, 8, 9]),
            set([1, 4, 7]),
            set([2, 5, 8]),
            set([3, 6, 9]),
            set([1, 5, 9]),
            set([3, 5, 7])
        ]

        for winning_board in winning_boards:
            # Use the winning board as a bit mask against the player's board.
            if winning_board <= self.player1:
                print("Player 1 is the WINNER")
                return True

            if winning_board <= self.player2:
                print("Player 2 is the WINNER")
                return True

        # no match
        return False

if __name__ == '__main__':
    GAME = TicTacToe()
    player = GAME.player1
    while (not GAME.is_there_a_winner() and not GAME.cats_game()):
        GAME.draw_board()
        GAME.take_turn(player)
        player = GAME.player1 if player == GAME.player2 else GAME.player2

    GAME.draw_board()
