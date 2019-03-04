#!/usr/bin/python3


from CS312Graph import *
from nodeWrapper import NodeWrapper
from ArrayQueue import *
from BinaryHeapQueue import *
import time
import math
import copy


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
        total_length = 0

        # start at the destination node and move through previous array.
        index = destIndex
        prev = self.previous_nodes[destIndex]

        total_length = self.distances[index];

        while prev != math.inf:
            # get edge, add to path and add length to total length
            edge_index = next((i for i, n in enumerate(self.network.nodes[prev].neighbors) if n.dest.node_id == index), -1)
            edge = self.network.nodes[prev].neighbors[edge_index]
            path_edges.append( (edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)) )

            # move to prev node and repeat.
            index = prev
            prev = self.previous_nodes[index]


        # if you didn't get back to the source the node is unreachable
        if index != self.source:
            return {'cost': math.inf, 'path': path_edges}
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
                v = n.dest.node_id;
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


    # def array_delete_min(self, nodes):
    #         # return node of smallest distance and updated node list. Then delete the node from the queue
    #         index = nodes.index(min(nodes, key=lambda n: n.dist))
    #         u = nodes[index]
    #         del nodes[index]
    #         return u, nodes

    # def array_shortest_paths(self, srcIndex):
    #             # create a list to hold the distances and set all to infinity. Also set source to 0
    #     # also create a list to hold the previous node index for each update.
    #     distances= [math.inf] * len(self.network.nodes)
    #     distances[srcIndex] = 0
    #     previous = [math.inf] * len(self.network.nodes)
    #
    #     # unordered array queue, set all nodes and set distance to infinity, set source distance to 0
    #     nodes = list()
    #     for n in self.network.nodes:
    #         nodes.append(NodeWrapper(n, math.inf))
    #     nodes[srcIndex].dist = 0
    #
    #     # while there are still nodes in the queue
    #     while len(nodes) != 0:
    #         # get the node with the smallest distance and update queue
    #         u, nodes = self.array_delete_min(nodes)
    #
    #         # visit each neighbor and update distance
    #         for n in u.node.neighbors:
    #             v = n.dest.node_id
    #             if distances[v] > distances[u.node.node_id] + n.length:
    #                 # if still in queue update distance..
    #                 x = next((i for i, n in enumerate(nodes) if n.node.node_id == v), -1)
    #                 if x != -1:
    #                     nodes[x].dist = distances[u.node.node_id]+n.length
    #                 distances[v] = distances[u.node.node_id] + n.length
    #                 previous[v] = u.node.node_id
    #
    #     # set distance and previous nodes for use in get shortest path
    #     self.distances = distances
    #     self.previous_nodes = previous
