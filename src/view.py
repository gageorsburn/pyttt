# pylint: disable=C0103
# pylint: disable=C0111

from tkinter import Canvas, Tk
from functools import partial

SQUARE_SIZE = 100

class View:
    def __init__(self, grid_size):
        self.window = Tk()
        self.turn = 0
        self.grid_size = grid_size
        self.win = False

        canvas = Canvas(self.window, width=SQUARE_SIZE*grid_size, height=SQUARE_SIZE*grid_size)
        canvas.pack()

        #vertical
        for line in range(grid_size - 1):
            x, y = (SQUARE_SIZE * (line + 1),
                    grid_size * SQUARE_SIZE)
            canvas.create_line(x, 0, x, y)

        #horizontal
        for line in range(grid_size - 1):
            x, y = (SQUARE_SIZE * grid_size,
                    SQUARE_SIZE * (line + 1))
            canvas.create_line(x, y, 0, y)

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
