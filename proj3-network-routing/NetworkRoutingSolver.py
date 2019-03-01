#!/usr/bin/python3


from CS312Graph import *
from nodeWrapper import NodeWrapper
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

        # ****************Access source index through self.source
        # TODO: RETURN THE SHORTEST PATH FOR destIndex
        #       INSTEAD OF THE DUMMY SET OF EDGES BELOW
        #       IT'S JUST AN EXAMPLE OF THE FORMAT YOU'LL 
        #       NEED TO USE

        path_edges = []
        total_length = 0
        node = self.network.nodes[self.source]
        edges_left = 3
        while edges_left > 0:
            edge = node.neighbors[2]
            path_edges.append( (edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)) )
            total_length += edge.length
            node = edge.dest
            edges_left -= 1
        return {'cost':total_length, 'path':path_edges}

    def computeShortestPaths( self, srcIndex, use_heap=False ):
        self.source = srcIndex
        t1 = time.time()




        # create a list to hold the distances and set all to infinity. Also set source to 0
        # also create a list to hold the previous node index for each update.
        distances= [math.inf] * len(self.network.nodes)
        distances[srcIndex] = 0;
        previous= [math.inf] * len(self.network.nodes)
        nodes = list()
        for n in self.network.nodes:
            nodes.append(NodeWrapper(n, math.inf, None))
        nodes[srcIndex].dist = 0;

        # TODO: RUN DIJKSTRA'S TO DETERMINE SHORTEST PATHS.
        #       ALSO, STORE THE RESULTS FOR THE SUBSEQUENT
        #       CALL TO getShortestPath(dest_index)


        while len(nodes) != 0:
            u, nodes = self.array_delete_min(distances, nodes)

            for n in u.node.neighbors:
                v = n.dest.node_id
                if distances[v] > distances[u.node.node_id] + n.length:
                    n.dist = distances[u.node.node_id]+n.length
                    distances[v] = distances[u.node.node_id] + n.length
                    previous[v] = u.node.node_id

        self.distances = distances
        self.previous_nodes= previous
        t2 = time.time()
        return (t2-t1)

    def array_delete_min(self, distances, nodes):
            #id = distances.index(min(distances))
            index = nodes.index(min(nodes, key=lambda n: n.dist))
            u = nodes[index]
            del nodes[index]
            return u, nodes
            # u = self.network.nodes[id]
            # return node of smallest distance and updated node list.
