from Graph import Node
from Graph import Edge
import jsonpickle
import sys
import resource

sys.setrecursionlimit(8000)

# max_rec = 0x100000
#
# # May segfault without this line. 0x100 is a guess at the size of each stack frame.
# resource.setrlimit(resource.RLIMIT_STACK, [0x100 * max_rec, resource.RLIM_INFINITY])
# sys.setrecursionlimit(max_rec)

"""
Graph class, allows user to create a graph and add nodes and edges
"""


class Graph(object):
    def __init__(self):
        """
        Basic constructor
        """
        self.movie_list = []
        self.actor_list = []
        self.edge_list = []

    def get_actors(self):
        return self.actor_list

    def get_movies(self):
        return self.movie_list

    def get_edges(self):
        return self.edge_list

    def create_node(self, url, name, type, old):
        """
        Adds a node given the relevant data
        """
        node = Node.Node(url, name, type, old)
        if (node not in self.actor_list) and (node not in self.movie_list):

            if node.type == "actor":
                self.actor_list.append(node)
            if node.type == "movie":
                self.movie_list.append(node)

        return node

    def create_edge(self, movie, actor):
        """
        Adds an edge given the relevant data
        """
        edge = Edge.Edge(movie, actor)
        if edge not in self.edge_list:
            self.edge_list.append(edge)

            movie.edges.append(edge)
            actor.edges.append(edge)

    def store_json(self):
        """
        Dumps the lists in a json
        """
        with open('movie.json', 'w') as f:
            json_obj = jsonpickle.encode(self.movie_list)
            f.write(json_obj)

        with open('actor.json', 'w') as f:
            json_obj = jsonpickle.encode(self.actor_list)
            f.write(json_obj)

        with open('edge.json', 'w') as f:
            json_obj = jsonpickle.encode(self.edge_list)
            f.write(json_obj)

    def load_json(self, movie_json, actor_json, edge_json):
        """
        Loads the lists from a json
        """
        with open(movie_json, 'w') as f:
            json_str = f.read()
            self.movie_list = jsonpickle.decode(json_str)

        with open(actor_json, 'w') as f:
            json_str = f.read()
            self.actor_list = jsonpickle.decode(json_str)

        with open(edge_json, 'w') as f:
            json_str = f.read()
            self.edge_list = jsonpickle.decode(json_str)
