# pylint: disable=C0103
# pylint: disable=C0111

from tkinter import Canvas, Tk
from functools import partial

SQUARE_SIZE = 100

class View:
    def __init__(self):
        self.window = Tk()
        self.turn = 0
        self.win = False

        canvas = Canvas(self.window, width=300, height=300)
        canvas.pack()

        #vertical lines
        canvas.create_line(100, 0, 100, 300)
        canvas.create_line(200, 0, 200, 300)
        #horizontal lines
        canvas.create_line(300, 100, 0, 100)
        canvas.create_line(300, 200, 0, 200)

        canvas.bind('<Button-1>', partial(self.click_event, canvas))

    def click_event(self, canvas, event):
        (x, y) = (int(event.x / 100), int(event.y / 100))

        if not self.win and self.is_clear(x, y):

            self.set_state(x, y, 1 if self.get_turn() % 2 == 0 else 2)

            (x1, y1, x2, y2) = (SQUARE_SIZE*x,
                                SQUARE_SIZE*y,
                                SQUARE_SIZE*x+SQUARE_SIZE,
                                SQUARE_SIZE*y+SQUARE_SIZE)

            canvas.create_rectangle(x1, y1, x2, y2, fill='red' if
                                    self.get_turn() % 2 == 0 else 'blue')

            self.increment_turn()

    def loop(self):
        self.window.mainloop()
