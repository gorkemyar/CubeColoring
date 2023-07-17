from vector_cube import *
from bitstring import BitArray
import matplotlib.pyplot as plt
import networkx as nx
import queue
def find_neighbours(edges: list[Edge]):
    edge_dict = {}
    for e1 in edges:
        for e2 in edges:
            if e1 == e2:
                continue
            if e1.is_perpendicular(e2) or e1.is_parallel(e2):
                if e1 not in edge_dict:
                    edge_dict[e1] = []
                edge_dict[e1].append(e2)
    return edge_dict


def to_binary(coordinates, dimension_count) -> int:
    coordinates_c = coordinates.copy()
    total = 0
    for i in range(dimension_count):
        if not (coordinates_c[i] == 0 or coordinates_c[i] == 1):
            size = dimension_count - i 
            arr = [0] * size
            arr[0] = coordinates_c[i]-1
            total += to_binary(arr, size)
            coordinates_c[i] = 1

    b = "".join([str(coordinates_c[i]) for i in range(dimension_count)])
    total 
    return BitArray(bin=b).uint + total

def vector_graph_to_nx_graph(edges: list[Edge]):
    colors = graph_coloring(edges)
    edges_binary = []
    colors_binary = {}
    nodes = set()
    for e in edges:
        points = e.get_points()
        p1 = to_binary(points[0].coordinates, points[0].dimension_count)
        p2 = to_binary(points[1].coordinates, points[1].dimension_count)
        edges_binary.append((p1, p2))
        colors_binary[(p1, p2)] = color_switch(colors[e])
        nodes.add(p1)
        nodes.add(p2)

    print(colors_binary)
    G = nx.Graph()
    G.add_edges_from(edges_binary)
    pos = nx.spring_layout(G)
    nx.draw(G,pos, with_labels=True, node_color='skyblue', node_size=500, edge_color=[colors_binary[e] for e in G.edges()])
    plt.axis('off')
    plt.show()


def find_coloring(edge: Edge, adjs: list[Edge], color_dict:dict[Edge, int]  ,current_color: int) -> int:
    colors = [i for i in range(current_color+1, 4)]
    for adj in adjs:
        if color_dict[adj] in colors:
            colors.remove(color_dict[adj])
    
    if len(colors) == 0:
        return None
    
    return colors[0]


def graph_coloring(edges: list[Edge]) -> dict[Edge, int]:
    edge_neighbours = find_neighbours(edges)
    sorted_edges = sorted(edge_neighbours.keys(), key=lambda x: len(edge_neighbours[x]), reverse=True)
    
    colored_nodes = dict()
    for edge in sorted_edges:
        colored_nodes[edge] = -1
    
    stack = queue.LifoQueue()
    stack.put(sorted_edges[0])
    colored_nodes[sorted_edges[0]] = find_coloring(sorted_edges[0], edge_neighbours[sorted_edges[0]], colored_nodes, -1)

    while not stack.empty() and stack.qsize() < len(sorted_edges):
        print(len(sorted_edges), "\t", stack.qsize())
        current_edge = stack.get()
        stack.put(current_edge)
        isPathAvailable = True
        anyAdjacentColored = False
        for adj in edge_neighbours[current_edge]:
            if colored_nodes[adj] == -1:
                color_current_edge = find_coloring(adj, edge_neighbours[adj], colored_nodes, -1)
                if color_current_edge is None:
                    isPathAvailable = False
                    break
                else:
                    colored_nodes[adj] = color_current_edge
                    stack.put(adj)
                    anyAdjacentColored = True

        while (not stack.empty()) and (not isPathAvailable):
            print("here")
            tmp_edge = stack.get()
            tmp_color = find_coloring(tmp_edge, edge_neighbours[tmp_edge], colored_nodes, colored_nodes[tmp_edge])
            if tmp_color is None:
                colored_nodes[tmp_edge] = -1
                continue
            else:
                colored_nodes[tmp_edge] = tmp_color
                stack.put(tmp_edge)
                flag = True
                break
        if anyAdjacentColored == False:
            stack.get()

         
    return colored_nodes
    
def color_switch(color:int) -> str :
    if color == 0:
        return "red"
    elif color == 1:
        return "green"
    elif color == 2:
        return "blue"
    elif color == 3:
        return "yellow"
    else:
        return "black"

    