from tkinter import *
from tkinter import messagebox
from SixSixBoard import SixSIxBoard
from EightEightBoard import EightEightBoard


class GameGUI:
    def __init__(self, ai):
        self.__ai = ai
        self.tk = Tk()
        self.tk.geometry("500x400+0+0")
        self.tk.title("Obstruction game")

        # Creating the base frame that we will use for the rest of the frames;
        # every frame will have its own class defined
        all_frames = Frame(self.tk)
        all_frames.pack()

        # Creating a dictionary of frames, key = the class name of that frame
        self.frames = {}

        # Creating the starting frame which will contain the game title, the start game button, the exit button and info
        # about the game (rules)
        for frame in (StartGame, SixSIxBoard, EightEightBoard):
            fr = frame(all_frames, self, self.__ai)
            self.frames[frame] = fr
            fr.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartGame)

        self.tk.mainloop()

    def show_frame(self, name):
        """Function which will show the current frame the user is on"""
        frame = name
        name = self.frames[name]
        if frame != StartGame:
            name.create_board()
            result = messagebox.askyesno("?", "Do you want to be the one who starts the game?")
            if result is not True:
                name.first_ai()
        name.tkraise()

    def quit_frame(self):
        self.show_frame(StartGame)


class StartGame(Frame):
    def __init__(self, parent, controller, nothing):
        Frame.__init__(self, parent)
        self.game = ""
        self.__ctr = controller

        # Creating the title
        lblInfo = Label(self, font=('harrington', 20, 'bold'), text="The Obstruction game", fg="green", bd=25,
                        anchor='w')
        lblInfo.grid(row=0, column=0)

        # adding a fill label to put a space between title and the next widgets
        fill_label = Label(self)
        fill_label.grid(row=1)

        # Creating the radio buttons and the buttons for the game
        lbl = Label(self, font=('arial', 10), text="Grid sizes:", bd=1, anchor='e', fg="steel blue")
        lbl.grid(row=1, column=0)
        self.set(SixSIxBoard)

        # 2 radio buttons, one for each grid size
        radio_six = Radiobutton(self, text="6x6 Grid", value=1, command=lambda: self.set(SixSIxBoard))
        radio_six.deselect()
        radio_six.grid(row=2)
        radio_eight = Radiobutton(self, text="8x8 Grid", value=4, command=lambda: self.set(EightEightBoard))
        radio_eight.grid(row=3)
        radio_eight.deselect()

        # the buttons for start, description and quit
        self.start = Button(self, text="Start", bg="yellow", height=2, width=10, command=lambda: self.start_game())
        self.start.grid(row=4)
        self.ButtonQuit = Button(self, background="#DA2C43", text="Quit", bg='orange', height=2, width=10, command=lambda: Frame.quit(self))
        self.ButtonQuit.grid(row=5)

    def set(self, game_frame):
        self.game = game_frame


    def start_game(self):
        self.__ctr.show_frame(self.game)
