from nodeWrapper import *
import math

class ArrayQueue:
        def __init__(self, nodes, src_index):
            self.queue = self.init_queue(nodes,src_index)  # list of nodes that will be edited

        def init_queue(self,nodes, src_index):
            queue = list()
            for n in nodes:
                queue.append(NodeWrapper(n, math.inf))
            queue[src_index].dist = 0
            return queue

        # if we needed this we would insert to the end of the array
        def insert(self):
            pass

        # update the distance of the node.
        def decrease_key(self, node_id, value):
            x = next((i for i, n in enumerate(self.queue) if n.node.node_id == node_id), -1)
            if x != -1:
                self.queue[x].dist = value

        # get the smallest distance node, delete it from the queue and return.
        def delete_min(self):
            # return node of smallest distance and updated node list. Then delete the node from the queue
            index = self.queue.index(min(self.queue, key=lambda n: n.dist))
            u = self.queue[index]
            del self.queue[index]
            return u

        def size(self):
            return len(self.queue)
