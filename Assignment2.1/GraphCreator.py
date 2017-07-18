import JSONHandler
import networkx as nx
"""
The Graph Creator
This class uses JSON Handler to get the lists and creates a NetworkX Undirected Graph
It returns the created graph
"""


def json_to_graph(data):
    lists = JSONHandler.parse_json(data)
    actor_list = lists[0]
    movie_list = lists[1]

    actor_name_list = []
    for i in actor_list:
        actor_name_list.append(i)

    movie_name_list = []
    for i in movie_list:
        movie_name_list.append(i)

    """
    Iterate through actors, and add their movies one by one
    Add edge weight based on the number of movies the actor has done
    """
    g = nx.Graph()
    for actor in actor_name_list:
        g.add_node(actor, actor_list[actor])
        for movie in actor_list[actor]['movies']:
            if movie in movie_name_list:
                g.add_node(movie, movie_list[movie])

                if len(actor_list[actor]['movies']) == 0:
                    actor_gross = 0
                else:
                    actor_gross = (actor_list[actor]['total_gross'] / len(actor_list[actor]['movies']))

                g.add_edge(actor, movie, weight=actor_gross)

    """
    Iterate through movies and add any movies we might have missed
    """
    for movie in movie_name_list:
        g.add_node(movie, movie_list[movie])
        for actor in movie_list[movie]['actors']:
            if actor in actor_name_list:
                g.add_node(actor, actor_list[actor])

                if len(movie_list[movie]['actors']) == 0:
                    actor_gross = 0
                else:
                    actor_gross = (movie_list[movie]['box_office'] / len(movie_list[movie]['actors']))

                g.add_edge(movie, actor, weight=actor_gross)

    return g
