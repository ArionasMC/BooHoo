import numpy as np

class Space:
    def __init__(self, dim):
        self.dim = dim
        self.space = np.zeros(shape=dim, dtype=int)

    def insert(self, pos, item):
        self.space[pos[0], pos[1], pos[2]] = item

    def read(self, pos):
        return self.space[pos[0], pos[1], pos[2]]

    def increase(self, pos, inc):
        self.space[pos[0], pos[1], pos[2]] += inc
