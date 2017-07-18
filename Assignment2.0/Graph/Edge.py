"""
Node class, contains connected nodes along with data
"""


class Edge(object):

    def __init__(self, movie, actor):
        """
        Basic constructor
        """
        self.movie = movie
        self.actor = actor
        self.weight = 0

