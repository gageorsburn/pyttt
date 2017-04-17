# pylint: disable=C0103
# pylint: disable=C0111
# pylint: disable=W0104

from tkinter import *
from functools import partial

SQUARE_SIZE = 100

class LabelEntry(Frame):
    def __init__(self, parent, text):
        super().__init__(parent)

        self.label = Label(self, text=text)
        self.entry = Entry(self)

        self.label.pack(side=LEFT)
        self.entry.pack(side=RIGHT)

    def get(self):
        return self.entry.get()


class OptionFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent.window)

        self.btnHostGame = Button(self, text="Host Game", command=parent.host)
        self.btnJoinGame = Button(self, text="Join Game", command=parent.join)

        self.btnHostGame.pack(side=TOP)
        self.btnJoinGame.pack(side=BOTTOM)


class HostOptionFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent.window)

        self.btnBack = Button(self, text="Back", command=partial(parent.back, self))
        self.leGridSize = LabelEntry(self, "Grid Size")
        self.btnStart = Button(self, text="Start", command=partial(parent.start_host, self))

        self.btnBack.pack()
        self.leGridSize.pack()
        self.btnStart.pack()

    def get_grid_size(self):
        return int(self.leGridSize.get())


class JoinOptionFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent.window)

        self.btnBack = Button(self, text="Back", command=partial(parent.back, self))
        #other widgets will go here
        self.btnStart = Button(self, text="Start", command=partial(parent.start_join, self))

        self.btnBack.pack()
        #other widget packs will go here
        self.btnStart.pack()

class GameFrame(Frame):
    def __init__(self, parent, grid_size):
        super().__init__(parent.window)

        canvas = Canvas(parent.window, width=SQUARE_SIZE*grid_size, height=SQUARE_SIZE*grid_size)
        canvas.pack(side=RIGHT)

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

        canvas.bind('<Button-1>', partial(parent.canvas_click, canvas))

class SideFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent.window, width=200, background='red')

class View:
    def __init__(self):
        self.window = Tk()

        self.window.title('Ultimate Tic Tac Toe')
        self.window.minsize(width=500, height=300)
        self.window.resizable(width=False, height=False)

        self.optionFrame = OptionFrame(self)
        self.hostOptionFrame = HostOptionFrame(self)
        self.joinOptionFrame = JoinOptionFrame(self)

        self.optionFrame.pack(pady=150)

    def host(self):
        self.optionFrame.pack_forget()
        self.hostOptionFrame.pack()

    def join(self):
        self.optionFrame.pack_forget()
        self.joinOptionFrame.pack()

    def back(self, caller):
        caller.pack_forget()
        self.optionFrame.pack(pady=150)

    def start_host(self, caller):
        caller.pack_forget()

        self.sideFrame = SideFrame(self)
        self.gameFrame = GameFrame(self, self.hostOptionFrame.get_grid_size())

        self.sideFrame.pack(side=LEFT, fill='both', expand='True')
        self.gameFrame.pack()

    def start_join(self, caller):
        caller.pack_forget()

        self.sideFrame = SideFrame(self)
        self.gameFrame = GameFrame(self, 3)

        self.sideFrame.pack(side=LEFT, fill='both')
        self.gameFrame.pack()

    def canvas_click(self, canvas, event):

        #temp hacks to work on view
        self.win = False
        self.is_clear = lambda x, y: True
        self.set_state = lambda x, y, z: None
        self.get_turn = lambda: 1
        #end temp hacks

        (x, y) = (int(event.x / 100), int(event.y / 100))

        if not self.win and self.is_clear(x, y):

            self.set_state(x, y, 1 if self.get_turn() % 2 == 0 else 2)

            (x1, y1, x2, y2) = (SQUARE_SIZE*x,
                                SQUARE_SIZE*y,
                                SQUARE_SIZE*x+SQUARE_SIZE,
                                SQUARE_SIZE*y+SQUARE_SIZE)

            canvas.create_rectangle(x1, y1, x2, y2, fill='red' if
                                    self.get_turn() % 2 == 0 else 'blue')

    def loop(self):
        self.window.mainloop()
