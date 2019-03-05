from nodeWrapper import *
import math


class ArrayQueue:
        def __init__(self, nodes, src_index):
            self.queue = self.init_queue(nodes, src_index)

        def init_queue(self, nodes, src):
            dict = {}
            for n in nodes:
                dict[n.node_id] = NodeWrapper(n, math.inf)
            dict[src].dist = 0
            return dict

        def size(self):
            #return len(self.queue)
            return len(self.queue)

        # if we needed this we would insert to the end of the array
        def insert(self):
            pass

        # update the distance of the node.
        def decrease_key(self, node_id, value):
            self.queue[node_id].dist = value

        # get the smallest distance node, delete it from the queue and return.
        def delete_min(self):
            # return node of smallest distance and updated node list. Then delete the node from the queue
            index = min(self.queue, key=lambda n:self.queue[n].dist)
            u = self.queue[index]
            del self.queue[index]
            return u
