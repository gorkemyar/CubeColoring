import networkx as nx
import matplotlib.pyplot as plt
from graph_functions import *

# number of cubes to generate
N = 2

# number of vertices and edges
vertex_count = N * 4 + 4
edge_count = N * 8 + 4

node_labels = {i: str(i) for i in range(vertex_count)}
edges = [(i, i + 1) if (i + 1) % 4 != 0 else (i-3, i)  for i in range(0, vertex_count)]
edges += [(i, i + 4) for i in range(0, edge_count-vertex_count)]
edge_labels = { i: '1' for i in edges}
edge_colors = { i: 'gray' for i in edges}


colors = {"r" : "red", "g" : "green", "b" : "blue", "y" : "yellow"}



neighbours_dict = find_neighbours(edges)
for key, value in neighbours_dict.items():
    print(key, ": ", value, sep="")
    print("Length: ", len(value), sep="")

# Draw the cube graph
G = nx.Graph()
G.add_edges_from(edges)

# Draw the cube graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color=[edge_colors[e] for e in G.edges()])

# Customize node labels
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12, font_color='black')

# Customize edge labels
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

# Show the graph
plt.axis('off')
plt.show()





