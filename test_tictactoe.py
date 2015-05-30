"""Test Tic Tac Toe."""
import unittest
from tictactoe import TicTacToe


class TestTicTacToe(unittest.TestCase):

    """Test Tic Tac Toe."""

    def setUp(self):
        """Create a new game for each test."""
        self.game = TicTacToe()

    def test_valid_range(self):
        """The player selects a space within 1-9."""
        self.assertFalse(self.game.validate_move(0))
        self.assertTrue(self.game.validate_move(1))
        self.assertTrue(self.game.validate_move(9))
        self.assertFalse(self.game.validate_move(10))
        self.assertFalse(self.game.validate_move('a'))

    def test_space_already_taken(self):
        """The space is already taken."""
        self.game.player1 = set([1, 2, 3])
        self.assertFalse(self.game.validate_move(1))

    def test_winning_board(self):
        """Any of the 8 possible winning boards should cause is_winning_board to return True."""
        self.assertFalse(self.game.is_there_a_winner())
        self.game.player1 = set([1, 2, 3])
        self.assertTrue(self.game.is_there_a_winner())

    def test_not_a_winning_board(self):
        """Any board that is not a winning board will cause is_winning_board to return False."""
        self.assertFalse(self.game.is_there_a_winner())
        self.game.player1 = set([1, 3, 5])
        self.game.player2 = set([2, 4])
        self.assertFalse(self.game.is_there_a_winner())

    def test_cats_game(self):
        """Any non-winning board that has no spaces left to play, is a cat's game."""
        self.assertFalse(self.game.is_there_a_winner())
        self.assertFalse(self.game.cats_game())
        self.game.player1 = set([1, 3, 5, 8])
        self.game.player2 = set([2, 4, 6, 7, 9])
        self.assertFalse(self.game.is_there_a_winner())
        for space in range(1, 10):
            self.assertFalse(self.game.validate_move(space))

        self.assertTrue(self.game.cats_game())

    def test_multiple_games(self):
        """Multiple games can occur at the same time."""
        pass

if __name__ == '__main__':
    unittest.main()
