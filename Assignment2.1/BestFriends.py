import GraphCreator
import DrawGraph
import networkx as nx
"""
This script analyzes the data to find who are best friends
It checks to see which two actors have done the most movies together
It outputs the names of the actors as well as the number of movies done together
It also displays a graph of the movies done in common
Note: Robin Wright and Robin Wright Penn are the same person, so I edited the JSON since they showed up as
common in all the movies she has done
"""


g = GraphCreator.json_to_graph("data.json")

big = 0
actor1 = None
actor2 = None

for i in g.nodes(data=True):
    for j in g.nodes(data=True):
        if (i[1]['json_class'] == 'Actor') and (j[1]['json_class'] == 'Actor') and (i[0] is not j[0]):
            hub_size = len(sorted(nx.common_neighbors(g, i[0], j[0])))
            if hub_size > big:
                big = hub_size
                actor1 = i
                actor2 = j

print("Actor 1: " + actor1[1]['name'])
print("Actor 2: " + actor2[1]['name'])
print("Count: " + str(big))

hub_list = [actor1[0], actor2[0]]
for movie in nx.common_neighbors(g, actor1[0], actor2[0]):
    hub_list.append(movie)

g_small = g.subgraph(hub_list)
DrawGraph.draw_graph(g_small, True)
