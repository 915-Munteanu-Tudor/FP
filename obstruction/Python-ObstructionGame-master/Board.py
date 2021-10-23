from Point import Point


class Board:
    def __init__(self, row=0, column=0):
        self.__row = row
        self.__column = column
        self.__board = []

    def get_row(self):
        return self.__row

    def get_column(self):
        return self.__column

    def set_row(self, row):
        self.__row = row

    def set_column(self, column):
        self.__column = column

    def available_move(self):
        """Function that returns the available moves"""
        move = []
        for x in range(self.get_row()):
            for y in range(self.get_column()):
                if self.__board[x][y] == 0:
                    move.append(Point(x, y))
        return move

    def board_move(self, point):
        """Function that borders all the existing neighbours of a point, if they exist and they are not bordered
        already"""
        x = point.get_x()
        y = point.get_y()
        if x - 1 >= 0 and y - 1 >= 0 and self.__board[x - 1][y - 1] == 0:
            self.__board[x - 1][y - 1] = -1
        if x - 1 >= 0 and self.__board[x - 1][y] == 0:
            self.__board[x - 1][y] = -1
        if x - 1 >= 0 and y + 1 < self.__column and self.__board[x - 1][y + 1] == 0:
            self.__board[x - 1][y + 1] = -1
        if y - 1 >= 0 and self.__board[x][y - 1] == 0:
            self.__board[x][y - 1] = -1
        if y + 1 < self.__column and self.__board[x][y + 1] == 0:
            self.__board[x][y + 1] = -1
        if x + 1 < self.__row and y + 1 < self.__column and self.__board[x + 1][y + 1] == 0:
            self.__board[x + 1][y + 1] = -1
        if x + 1 < self.__row and self.__board[x + 1][y] == 0:
            self.__board[x + 1][y] = -1
        if x + 1 < self.__row and y - 1 >= 0 and self.__board[x + 1][y - 1] == 0:
            self.__board[x + 1][y - 1] = -1

    def __len__(self):
        return len(self.__board)

    def __str__(self):
        """Overriding the str function"""
        string = "\n   "
        for x in range(self.__column):
            string += str(x) + '   '
        for x in range(self.__row):
            string += "\n "
            string += "-" * (4 * self.__column + 1)
            string += "\n"
            string += str(x) + '|'
            for y in range(self.__column):
                if self.__board[x][y] == 1:  # 1 = the player
                    string += ' ' + '0' + ' ' + "|"
                elif self.__board[x][y] == 2:  # 2 = the computer
                    string += ' ' + 'X' + ' ' + "|"
                elif self.__board[x][y] == -1:  # -1 = nonempty neighbours
                    string += '|||' + "|"
                else:
                    string += ' ' + ' ' + ' ' + "|"
        string += "\n "
        string += "-" * (4 * self.__column + 1) + "\n"
        return string

    def get_board(self):
        """Function that returns the board"""
        return self.__board

    def create_board(self):
        """
        The board will be a list of lists, each list will represent a row, and each element of these lists will
        represent a column.
        The board will have self.__row lists and each list will have self.__column elements.
        """
        for x in range(self.__row):
            array = []
            for y in range(self.__column):
                array.append(0)
            self.__board.append(array)

    def destroy_board(self):
        """Function that sets the board to the "default" size"""
        self.__board = []
        self.__row = 0
        self.__column = 0


