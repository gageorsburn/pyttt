# pylint: disable=C0103
# pylint: disable=C0111
# pylint: disable=E1101

CLEAR = 0
X = 1
O = 2

def collection_equal(c):
    return CLEAR not in c and c[1:] == c[:-1]

class Board:

    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.state = [[CLEAR] * grid_size for size in range(grid_size)]

    def check(self):

        if any(collection_equal(s) for s in self.state):
            self.alert_win()

        if any(collection_equal(s) for s in zip(*self.state)):
            self.alert_win()

        if collection_equal([self.state[a][a] for a in range(self.grid_size)]):
            self.alert_win()

        if collection_equal([self.state[a][self.grid_size-1-a] for a in range(self.grid_size)]):
            self.alert_win()

    def set_state(self, x, y, v):
        self.state[x][y] = v
        self.check()

    def is_clear(self, x, y):
        return self.state[x][y] == CLEAR
    