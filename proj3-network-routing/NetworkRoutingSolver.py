#!/usr/bin/python3


from CS312Graph import *
from ArrayQueue import *
from BinaryHeapQueue import *
import time
import math


class NetworkRoutingSolver:
    def __init__( self ):
        self.distances = []
        self.previous_nodes = []

    def initializeNetwork( self, network ):
        assert( type(network) == CS312Graph )
        self.network = network

    def getShortestPath( self, destIndex ):
        self.dest = destIndex

        # set up edges and length to return
        path_edges = []
        total_length = self.distances[destIndex]

        # start at the destination node and move through previous array.
        index = destIndex
        prev = self.previous_nodes[destIndex]

        while prev != math.inf:
            # get edge, add to path and add length to total length
            edge_index = next((i for i, n in enumerate(self.network.nodes[prev].neighbors) if n.dest.node_id == index), -1)
            edge = self.network.nodes[prev].neighbors[edge_index]
            path_edges.append((edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)))

            # move to prev node and repeat.
            index = prev
            prev = self.previous_nodes[index]


        # if you didn't get back to the source the node is unreachable
        if index != self.source:
            return {'cost': math.inf, 'path': []}
        return {'cost': total_length, 'path': path_edges}

    def computeShortestPaths( self, srcIndex, use_heap):
        self.source = srcIndex
        t1 = time.time()

        if use_heap:
            queue = BinaryHeap(self.network.nodes, srcIndex)
        else:
            queue = ArrayQueue(self.network.nodes, srcIndex)

        # create a list to hold the distances and set all to infinity. Also set source to 0
        # also create a list to hold the previous node index for each update.
        distances = [math.inf] * len(self.network.nodes)
        distances[srcIndex] = 0
        previous = [math.inf] * len(self.network.nodes)

        while queue.size() > 0:

            u = queue.delete_min()
            for n in u.node.neighbors:
                v = n.dest.node_id
                new_distance = distances[u.node.node_id] +n.length
                if distances[v] > new_distance:
                    distances[v] = new_distance
                    previous[v] = u.node.node_id
                    queue.decrease_key(v, new_distance)

        # set distance and previous nodes for use in get shortest path
        self.distances = distances
        self.previous_nodes = previous

        t2 = time.time()
        return t2-t1
