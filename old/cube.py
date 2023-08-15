import networkx as nx
import matplotlib.pyplot as plt

# Create a cube graph
G = nx.Graph()
G.add_edges_from([
    (0, 1), (1, 2), (2, 3), (0, 3),
    (4, 5), (5, 6), (6, 7), (4, 7),
    (0, 4), (1, 5), (2, 6), (3, 7)
])

# Draw the cube graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='gray')

# Customize node labels
node_labels = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7'}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12, font_color='black')

# Customize edge labels
edge_labels = {
    (0, 1): '1', (1, 2): '1', (2, 3): '1', (0, 3): '1',
    (4, 5): '1', (5, 6): '1', (6, 7): '1', (4, 7): '1',
    (0, 4): '1', (1, 5): '1', (2, 6): '1', (3, 7): '1'
}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

# Show the graph
plt.axis('off')
plt.show()
