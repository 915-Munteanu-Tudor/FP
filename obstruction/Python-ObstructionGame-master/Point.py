class Point:
    def __init__(self, x, y):
        self.__x = int(x)
        self.__y = int(y)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

class ValidatePoint:
    @staticmethod
    def valid_point(x, y, board):
        """Function that validates the coordinates of a point given"""
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            raise Exception("Please give integers!")
        if y < 0 or x < 0 or y >= board.get_column() or x >= board.get_row():
            raise Exception("Point out of border!")
        if board.get_board()[x][y] == -1 or board.get_board()[x][y] == 1 or board.get_board()[x][y] == 2:
            raise Exception("Square already taken!")