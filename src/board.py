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
        
    def check(self):

        if any(collection_equal(s) for s in self.state):
            self.alert_win()

        if any(collection_equal(s) for s in zip(*self.state)):
            self.alert_win()

        if collection_equal([self.state[a][a] for a in range(3)]):
            self.alert_win()

        if collection_equal([self.state[a][2-a] for a in range(3)]):
            self.alert_win()

    def set_state(self, x, y, v):
        self.state[x][y] = v
        self.check()

    def is_clear(self, x, y):
        return self.state[x][y] == CLEAR
    