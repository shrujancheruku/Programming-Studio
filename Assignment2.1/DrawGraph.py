import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt


"""
The Draw Graph class
This class takes in the graph from GraphCreator and plots it using NetworkX's draw functionality
"""


def draw_graph(g, big=False, pos=None):

    plt.figure(figsize=(17, 6))
    plt.axis('off')

    color_map = {'Actor': '#ff0000', 'Movie': '#0000ff'}

    l_size = 6 if big else 4

    """
    If layout isn't specified, use graphviz
    """
    if pos is None:
        pos = graphviz_layout(g, prog='dot')

    labels = {}
    for i in g.nodes(data=True):
        if i[1]['json_class'] == 'Actor':
            labels[i[0]] = str(i[1]['name']) + "\n" + "Age: " + str(i[1]['age'])
        else:
            labels[i[0]] = str(i[1]['name']) + "\n" + "Gross:" + str(i[1]['box_office'])

    nx.draw_networkx_labels(g, pos, labels, font_size=l_size)

    nx.draw_networkx_nodes(g, pos, show_label=False, node_color=[color_map[g.node[node]['json_class']] for node in g],
                           node_size=200, font_size=l_size, alpha=0.3)
    nx.draw_networkx_edges(g, pos)

    plt.show()
