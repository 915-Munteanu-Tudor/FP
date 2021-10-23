from Board import Board
from AI import AIController

game = AIController(Board())

from Console import Console
from GUI import GameGUI
# ui = Console(game)
# ui.start()

ui = GameGUI(game)
