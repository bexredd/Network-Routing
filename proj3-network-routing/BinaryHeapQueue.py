from nodeWrapper import *
import math


class BinaryHeap:
    def __init__(self, nodes, src_index):
        self.dictionary = {}
        self.queue = self.init_queue(nodes, src_index)

    def init_queue(self, nodes, src_index):
        queue = list()
        for n in nodes:
            queue.append(NodeWrapper(n, math.inf))

        # set src node to the root of the binary heap
        root = queue[src_index]
        root.dist = 0
        del queue[src_index]
        queue.insert(0, root)

        for i in range(0, len(queue)-1):
            self.dictionary[queue[i].node.node_id] = i

        return queue

    def size(self):
        return len(self.queue)

    # if we needed this we would insert to the end of the array then bubble it up.
    def insert(self, node, distance):
        self.queue.append(NodeWrapper(node, distance))
        index = len(self.queue) - 1
        p_index = (index-1)//2
        while p_index >= 0 and self.queue[p_index].dist > self.queue[index].dist:
            self.bubble_up(index, p_index)

            index = p_index
            p_index = (index-1)//2

    # update the positions of the node in comparison to the parent and the sibling.
    def decrease_key(self, node_id, value):
        # index = next((i for i, n in enumerate(self.queue) if n.node.node_id == node_id), -1)
        index = self.dictionary[node_id]
        self.queue[index].dist = value
        p_index = (index-1)//2
        while p_index >= 0 and self.queue[p_index].dist > self.queue[index].dist:
            self.bubble_up(index, p_index)

            index = p_index
            p_index = (index-1)//2

    def delete_min(self):
        u = self.queue[0]
        last_node = self.queue[len(self.queue)-1]

        self.queue[0] = last_node
        self.dictionary[last_node.node.node_id] = 0

        self.queue.pop()
        del self.dictionary[u.node.node_id]

        self.bubble_down()
        return u

    def bubble_up(self, index, p_index):
            parent = self.queue[p_index]

            self.dictionary[self.queue[index].node.node_id] = p_index
            self.queue[p_index] = self.queue[index]

            self.dictionary[parent.node.node_id] = index
            self.queue[index] = parent

    def bubble_down(self,):
        index = 0
        while True:
            child1_idx = index*2+1
            child2_idx = index*2+2

            # if there is no child return
            if child1_idx >= len(self.queue) or child2_idx >= len(self.queue):
                return
            # if both children are smaller swap with the smaller of the 2
            elif self.queue[index].dist > self.queue[child1_idx].dist and self.queue[index].dist > self.queue[child2_idx].dist:
                if self.queue[child2_idx].dist < self.queue[child1_idx].dist:
                    curr = self.queue[index]

                    self.dictionary[self.queue[child2_idx].node.node_id] = index
                    self.queue[index] = self.queue[child2_idx]

                    self.dictionary[curr.node.node_id] = child2_idx
                    self.queue[child2_idx] = curr
                    index = child2_idx
                else:
                    curr = self.queue[index]

                    self.dictionary[self.queue[child1_idx].node.node_id] = index
                    self.queue[index] = self.queue[child1_idx]

                    self.dictionary[curr.node.node_id] = child1_idx
                    self.queue[child1_idx] = curr

                    index = child1_idx
            # if the left child is smaller swap with it
            elif self.queue[index].dist > self.queue[child1_idx].dist:
                curr = self.queue[index]

                self.dictionary[self.queue[child1_idx].node.node_id] = index
                self.queue[index] = self.queue[child1_idx]

                self.dictionary[curr.node.node_id] = child1_idx
                self.queue[child1_idx] = curr

                index = child1_idx
            # if the right child is smaller swap with it
            elif self.queue[index].dist > self.queue[child2_idx].dist:
                curr = self.queue[index]

                self.dictionary[self.queue[child2_idx].node.node_id] = index
                self.queue[index] = self.queue[child2_idx]

                self.dictionary[curr.node.node_id] = child2_idx
                self.queue[child2_idx] = curr
                index = child2_idx
            # if none of these are true, then return because its in the right spot.
            else:
                return

