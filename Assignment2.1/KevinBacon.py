import GraphCreator
import DrawGraph
import networkx as nx
"""
The Six Degrees of Kevin Bacon script
Checks to see what the largest degree of separation is between two actors
Also calculates the average degree of separation
Outputs the actors with the largest degree of separation, as well as the average
Also shows a plot of the path between two actors
"""


g_big = GraphCreator.json_to_graph("data.json")
g_list = list(nx.connected_component_subgraphs(g_big))
g = g_list[0]

big = 0
actor1 = None
actor2 = None
count = 0
bacon_sum = 0

"""
Iterate over the nodes and find the shortest path between all the actors
Save the largest value, and also the number of comparisons as well as the sum of degree
This is to calculate the average
"""
for i in g.nodes(data=True):
    for j in g.nodes(data=True):
        if (i[1]['json_class'] == 'Actor') and (j[1]['json_class'] == 'Actor') and (i[0] is not j[0]):
            bacon_no = len(sorted(nx.shortest_path(g, i[0], j[0])))
            count += 1
            bacon_sum += (bacon_no - 2)
            if bacon_no > big:
                big = bacon_no
                actor1 = i
                actor2 = j

print("Actor 1: " + actor1[1]['name'])
print("Actor 2: " + actor2[1]['name'])
print("Degree of Separation: " + str(big - 2))
print("Average Degree of Separation: " + str(bacon_sum/count))

hub_list = nx.shortest_path(g, actor1[0], actor2[0])
for movie in nx.common_neighbors(g, actor1[0], actor2[0]):
    hub_list.append(movie)

g_small = g.subgraph(hub_list)
DrawGraph.draw_graph(g_small, True)