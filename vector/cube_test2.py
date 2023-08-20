from vector_cube import *
from vector_graph_functions import *


points = [Point(3, [(i // 9) % 3, (i // 3) % 3, i % 3]) for i in range(27)]

edges = []

print(points)


for i in range(len(points)):
    for j in range(i+1, len(points)):
        if points[i].distance(points[j]) == 1:
            edges.append(Edge(points[i], points[j]))


print(len(edges))
print(graph_coloring3(edges))
vector_graph_to_nx_graph(edges)