
from CS312Graph import *

class NodeWrapper:
    def __init__(self, node, dist, prev):
        self.node = node
        self.dist = dist
        self.prev = prev

    def set_dist(self, dist):
        self.dist = dist
    def set_prev(self, prev):
        self.prev = prev

