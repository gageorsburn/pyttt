# pylint: disable=C0103
# pylint: disable=C0111

from tkinter import Canvas, Tk
from functools import partial

CLEAR = 0
X = 1
O = 2
SIZE = 100


#This is a prototype so I'm using globals. Will refactor out later.
turn = 0
win = False

STATE = [
    [CLEAR, CLEAR, CLEAR],
    [CLEAR, CLEAR, CLEAR],
    [CLEAR, CLEAR, CLEAR]
]

def click_event(canvas, event):
    (x, y) = (int(event.x / 100), int(event.y / 100))

    if not win and STATE[x][y] == CLEAR:
        global turn
        STATE[x][y] = X if turn % 2 == 0 else O

        (x1, y1, x2, y2) = (SIZE*x,
                            SIZE*y,
                            SIZE*x+SIZE,
                            SIZE*y+SIZE)

        canvas.create_rectangle(x1, y1, x2, y2, fill='red' if turn % 2 == 0 else 'blue')
        turn += 1

        check()

def collection_equal(c):
    return CLEAR not in c and c[1:] == c[:-1]

def check():
    global win

    #vertical
    for a in range(3):
        if collection_equal(STATE[a]):
            win = True

    #horizontal
    for a in zip(STATE[0], STATE[1], STATE[2]):
        if collection_equal(a):
            win = True

    #diagonal 1
    if collection_equal([STATE[a][a] for a in range(3)]):
        win = True

    #diagonal 2
    if collection_equal([STATE[a][2-a] for a in range(3)]):
        win = True

    #check turn count for draws

    if win:
        print('winner')

if __name__ == "__main__":
    window = Tk()

    canvas = Canvas(window, width=300, height=300)
    canvas.pack()

    #vertical lines
    canvas.create_line(100, 0, 100, 300)
    canvas.create_line(200, 0, 200, 300)
    #horizontal lines
    canvas.create_line(300, 100, 0, 100)
    canvas.create_line(300, 200, 0, 200)

    canvas.bind('<Button-1>', partial(click_event, canvas))

    window.mainloop()
