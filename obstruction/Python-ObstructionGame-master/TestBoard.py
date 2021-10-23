import unittest
from Board import Board
from Point import Point


class MyTestCase(unittest.TestCase):
    def test_board(self):
        board = '[[0, 0, 0, 0, 0]]'
        self.bo = Board(1, 5)
        self.bo.create_board()
        self.assertNotEqual(self.bo.get_board(), None)
        self.assertEqual(board, str(self.bo.get_board()))

        self.bo.destroy_board()
        self.assertEqual(self.bo.destroy_board(), None)

        self.bo = Board(7, 8)
        self.bo.create_board()
        moves = self.bo.available_move()
        self.assertEqual(len(moves), 56)

        self.bo.set_column(7)
        self.bo.create_board()
        moves = self.bo.available_move()
        self.assertEqual(len(moves), 49)

        self.bo.set_column(5)
        self.bo.create_board()
        moves = self.bo.available_move()
        self.assertEqual(len(moves), 35)

        self.assertEqual(self.bo.get_column(), 5)
        self.assertEqual(self.bo.get_row(), 7)

        self.bo.board_move(Point(2, 3))
        moves = self.bo.available_move()
        self.assertEqual(len(moves), 27)


if __name__ == '__main__':
    unittest.main()
