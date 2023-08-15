from vector_cube import *
from vector_graph_functions import *
# number of cubes to generate
N = 1

# number of vertices and edges
vertex_count = 16


#points = [Point(3, [i // 4, (i // 2) % 2, i % 2]) for i in range(vertex_count)]

# 0 => 0, 0, 0, 0
# 1 => 0, 0, 0, 1
# 2 => 0, 0, 1, 1
# 3 => 0, 0, 1, 0

# 4 => 0, 1, 0, 0
# 5 => 0, 1, 0, 1
# 6 => 0, 1, 1, 1
# 7 => 0, 1, 1, 0

# 8 => 1, 0, 0, 0
# 9 => 1, 0, 0, 1
# 10 => 1, 0, 1, 1
# 11 => 1, 0, 1, 0

# 12 => 1, 1, 0, 0
# 13 => 1, 1, 0, 1
# 14 => 1, 1, 1, 1
# 15 => 1, 1, 1, 0


# 0, 1, 2, 3, 4, .... 15
# i // 8, (i % 8) // 4, (i % 4) // 2, 1 if (i % 4) in [1,2] else 0



points = [Point(4, [i // 8, (i % 8) // 4, (i % 4) // 2, 1 if (i % 4) in [1,2] else 0]) for i in range(vertex_count)]
edges = []

for i in range(len(points)):
    for j in range(i+1, len(points)):
        if points[i].distance(points[j]) == 1:
            edges.append(Edge(points[i], points[j]))




#edges = [Edge(points[i], points[i + 1]) if (i + 1) % 4 != 0 else Edge(points[i-3], points[i])  for i in range(0, vertex_count)]
#edges += [Edge(points[i], points[i + 4]) for i in range(0, edge_count-vertex_count)]


#print(graph_coloring3(edges))

vector_graph_to_nx_graph(edges)



# for key in sorted_edges:
#     print(key, edge_neighbours[key])
#     print("Length: ", len(edge_neighbours[key]))

#vector_graph_to_nx_graph(edges)