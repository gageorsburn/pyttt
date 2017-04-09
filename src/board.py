# pylint: disable=C0103
# pylint: disable=C0111
# pylint: disable=E1101

CLEAR = 0
X = 1
O = 2

def collection_equal(c):
    return CLEAR not in c and c[1:] == c[:-1]

class Board:

    def __init__(self):
        self.state = [
            [CLEAR, CLEAR, CLEAR],
            [CLEAR, CLEAR, CLEAR],
            [CLEAR, CLEAR, CLEAR]
        ]

    #def __init(self, state):
    #    self.state = state

    def check(self):
        win = False

        for a in range(3):
            if collection_equal(self.state[a]):
                win = True

        for a in zip(self.state[0], self.state[1], self.state[2]):
            if collection_equal(a):
                win = True

        if collection_equal([self.state[a][a] for a in range(3)]):
            win = True

        if collection_equal([self.state[a][2-a] for a in range(3)]):
            win = True

        if win:
            self.alert_win()

    def set_state(self, x, y, v):
        self.state[x][y] = v
        #self = Board(self.state)
        self.check()

    def is_clear(self, x, y):
        return self.state[x][y] == CLEAR
    