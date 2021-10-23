from Point import Point,ValidatePoint
from random import randint


class AIController:
    def __init__(self, board):
        self.__board = board
        self.__valid = ValidatePoint()
        self.__startodd = False

    def get_board(self):
        return self.__board

    def set_row(self, row):
        self.__board.set_row(row)

    def set_column(self, column):
        self.__board.set_column(column)

    def create_board(self):
        self.__board.create_board()
        self.__startodd = False

    def destroy_board(self):
        self.__board.destroy_board()

    def make_move_player(self, x, y):
        """Function that validates the move the player wants to make.
        Raises exception if the move is invalid.
        Otherwise it records the move."""
        self.__valid.valid_point(x, y, self.__board)
        point = Point(x, y)
        self.__board.get_board()[point.get_x()][point.get_y()] = 1
        self.__board.board_move(point)


    def _decide_move(self, computer, row, column, moves):
        """Function that decides how will the AI make its next move based on some criteria"""

        # If the board is odd and AI started we continue with 1
        if self.__startodd is True and len(moves) != row * column:
            return 1

        # If the above criteria wasn't met, the AI will just make its move randomly
        return 2

    def _random_move(self, moves):
        """Function that makes AI move randomly"""
        move = randint(0, len(moves) - 1)
        self.__board.get_board()[moves[move].get_x()][moves[move].get_y()] = 2
        self.__board.board_move(moves[move])
        return moves[move]

    def make_move_ai(self, computer, x, y):
        """Function that makes the AI's move"""
        moves = self.__board.available_move()
        row = self.__board.get_row()
        column = self.__board.get_column()
        next_move = self._decide_move(computer, row, column, moves)

        if next_move == 2:
            # If the above criteria wasn't met, the AI will just make its move randomly
            return self._random_move(moves)

    def game_over(self):
        """Function that returns True if there are still available moves to be made and False otherwise"""
        if self.__board.available_move():
            return True
        return False
