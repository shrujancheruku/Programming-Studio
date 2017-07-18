import GraphCreator
import DrawGraph
import networkx as nx
"""
This script is meant to draw the specified actor, as well as all the actors they've worked with
"""

"""
Specify actor name here
"""
actor_name = 'Tom Hanks'

g = GraphCreator.json_to_graph("data.json")

hub_list = [actor_name]
for movie in nx.neighbors(g, actor_name):
    hub_list.append(movie)
    for actor in nx.neighbors(g, movie):
        hub_list.append(actor)

g_small = g.subgraph(hub_list)
DrawGraph.draw_graph(g_small, True)
