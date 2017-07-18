import GraphCreator
import DrawGraph
import networkx as nx
"""
This script analyzes the data to find who the hub actors are
It checks to see which actors have done the most movies with others
It outputs the name of the actor as well as the number connections
It also displays a graph of connections
"""


g = GraphCreator.json_to_graph("data.json")

big = 0
hub_actor = None

for i in g.nodes(data=True):
        if i[1]['json_class'] == 'Actor':
            hub_size = len(sorted(nx.neighbors(g, i[0])))
            if hub_size > big:
                big = hub_size
                hub_actor = i

print("Actor: " + hub_actor[1]['name'])
print("Count: " + str(big))

actor_name = hub_actor[1]['name']

g = GraphCreator.json_to_graph("data.json")

hub_list = [actor_name]
for movie in nx.neighbors(g, actor_name):
    hub_list.append(movie)
    for actor in nx.neighbors(g, movie):
        hub_list.append(actor)

g_small = g.subgraph(hub_list)
DrawGraph.draw_graph(g_small, True)
