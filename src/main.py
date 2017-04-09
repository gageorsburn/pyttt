# pylint: disable=C0103
# pylint: disable=C0111

from board import Board
from view import View

turn = 0

def get_turn():
    return turn

def increment_turn():
    global turn
    turn += 1

if __name__ == "__main__":
    board = Board()
    view = View()

    view.set_state = board.set_state
    view.is_clear = board.is_clear
    view.get_turn = get_turn
    view.increment_turn = increment_turn

    def dispatch_win():
        view.win = True

        print('winner!')

    board.alert_win = dispatch_win

    view.loop()
