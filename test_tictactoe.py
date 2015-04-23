"""Test Tic Tac Toe."""
import unittest
from tictactoe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    """Test Tic Tac Toe."""

    def setUp(self):
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
        self.game.player1 = [1, 1, 1, 0, 0, 0, 0, 0, 0]
        self.assertFalse(self.game.validate_move(1))

    def test_winning_board(self):
        """Any of the 8 possible winning boards should cause is_winning_board to return True."""
        self.assertFalse(self.game.is_there_a_winner())
        self.game.player1 = [1, 1, 1, 0, 0, 0, 0, 0, 0]
        self.assertTrue(self.game.is_there_a_winner())

    def test_not_a_winning_board(self):
        """Any board that is not a winning board will cause is_winning_board to return False."""
        self.assertFalse(self.game.is_there_a_winner())
        self.game.player1 = [1, 0, 1, 0, 1, 0, 0, 0, 0]
        self.game.player2 = [0, 1, 0, 1, 0, 0, 0, 0, 0]
        self.assertFalse(self.game.is_there_a_winner())

    def test_cats_game(self):
        """Any non-winning board that has no spaces left to play, is a cat's game."""
        self.assertFalse(self.game.is_there_a_winner())
        self.game.player1 = [1, 0, 1,
                             0, 1, 0,
                             0, 1, 0]
        self.game.player2 = [0, 1, 0,
                             1, 0, 1,
                             1, 0, 1]
        self.assertFalse(self.game.is_there_a_winner())
        for space in range(1, 10):
            self.assertFalse(self.game.validate_move(space))


if __name__ == '__main__':
    unittest.main()
