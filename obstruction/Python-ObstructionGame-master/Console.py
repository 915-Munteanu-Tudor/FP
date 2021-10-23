class Console:
    def __init__(self, ai_controller):
        self.__game = ai_controller
        self.__startwithai = False
        self.__in_turn = 1

    def start(self):
        continue_game = True
        while continue_game:
            try:
                x = int(input("\nGive the dimension of the board: \nheight = "))
                y = int(input("width = "))

                if x < 1 or y < 1:
                    raise ValueError
                set_player = input("\nDo you want to be the one that starts the game?\n a) Yes\n b) No\n ")
                # Settind the size of the board
                self.__game.set_row(x)
                self.__game.set_column(y)
                self.__game.create_board()

                if set_player == 'a':
                    self.__in_turn = 1  # 1 will be the player
                    self.__startwithai = False
                elif set_player == 'b':
                    self.__in_turn = 2  # 2 will be the computer
                    self.__startwithai = True
                while self.__game.game_over() is True:
                    if self.__in_turn == 1:
                        try:
                            print(str(self.__game.get_board()))
                            x = input("x = ")
                            y = input("y = ")
                            self.__game.make_move_player(x, y)
                            self.__in_turn = 2
                        except Exception as error:
                            print(error)
                    elif self.__in_turn == 2:
                        self.__game.make_move_ai(self.__startwithai, x, y)
                        self.__in_turn = 1
                print(str(self.__game.get_board()))
                if self.__in_turn == 2:
                    print("Player has won!")
                else:
                    print("Computer has won!")

                cont = input("\n Do you wish to play again?\n a) Yes\n b) No\n")
                if cont == 'a':
                    self.__game.destroy_board()
                elif cont == 'b':
                    continue_game = False
                else:
                    print("Invalid option!")
            except ValueError:
                print("Invalid coordinates!")
