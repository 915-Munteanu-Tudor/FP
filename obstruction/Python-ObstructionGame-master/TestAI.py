import unittest
from Board import Board
from AI import AIController


class MyTestCase(unittest.TestCase):
    def test_ai(self):
        board = Board(3, 7)
        self.bo = AIController(board)
        self.bo.create_board()
        self.assertNotEqual(self.bo.get_board(), None)
        self.assertEqual(str(board), str(self.bo.get_board()))

        self.assertEqual(self.bo.destroy_board(), None)

        self.assertFalse(self.bo.game_over())

        self.bo = AIController(Board(1, 3))
        self.bo.create_board()
        self.bo.make_move_player(0, 1)

        try:
            self.bo.make_move_player(0, 1)
            self.bo.make_move_player(0, 2)
            self.bo.make_move_player(0, 0)
        except Exception:
            pass

        self.assertFalse(self.bo.game_over())

        self.bo = AIController(Board(3, 5))
        self.bo.create_board()
        self.bo.make_move_ai(True, 0, 0)

        try:
            self.bo.make_move_player(1, 3)
            self.bo.make_move_player(0, 3)
            self.bo.make_move_player(0, 2)
            self.bo.make_move_player(0, 1)
            self.bo.make_move_player(1, 2)
            self.bo.make_move_player(1, 1)
            self.bo.make_move_player(2, 3)
            self.bo.make_move_player(2, 1)
            self.bo.make_move_player(2, 2)
        except Exception:
            pass

        self.assertTrue(self.bo.game_over())
        self.bo.make_move_player(1, 0)
        self.assertTrue(self.bo.game_over())
        self.bo.make_move_ai(True, 1, 0)
        self.assertFalse(self.bo.game_over())



if __name__ == '__main__':
    unittest.main()
