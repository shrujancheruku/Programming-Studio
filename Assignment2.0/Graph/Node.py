"""
Node class, contains list of edges along with data
"""


class Node(object):

    def __init__(self, url, name, type, old):
        """
        Basic constructor
        """
        self.edges = []
        self.url = url
        self.name = name
        self.old = old
        self.type = type

