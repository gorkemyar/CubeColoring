from vector_cube import *
from bitstring import BitArray
import matplotlib.pyplot as plt
import networkx as nx
import queue
from collections import deque

def find_neighbours(edges: list[Edge]):
    edge_dict = {}
    for e1 in edges:
        for e2 in edges:
            if e1 == e2:
                continue
            if e1.git(e2) or e1.is_parallel(e2):
                if e1 not in edge_dict:
                    edge_dict[e1] = []
                edge_dict[e1].append(e2)
    return edge_dict


def to_binary2(coordinates, dimension_count) -> int:
    coordinates_c = coordinates.copy()
    total = 0

    res = coordinates_c[0]*9 + coordinates_c[1]*3 + coordinates_c[2]

    return res

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
    colors = graph_coloring3(edges)
    edges_binary = []
    colors_binary = {}
    nodes = set()
    for e in edges:
        points = e.get_points()
        p1 = to_binary(points[0].coordinates, points[0].dimension_count)
        p2 = to_binary(points[1].coordinates, points[1].dimension_count)

        pair = (min(p1, p2), max(p1, p2))
        edges_binary.append(pair)
        colors_binary[pair] = color_switch(colors[e])
        nodes.add(p1)
        nodes.add(p2)

    print(colors_binary)
    print(edges_binary)
    G = nx.Graph()
    G.add_edges_from(edges_binary)
    pos = nx.spring_layout(G)
    nx.draw(G,pos, with_labels=True, node_color='skyblue', node_size=500, edge_color=[colors_binary[(min(e[0], e[1]), max(e[0],e[1]))] for e in G.edges()])
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
    
    stack = queue.deque()
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
    

def graph_coloring2(edges: list[Edge]) -> dict[Edge, int]:
    edge_neighbours = find_neighbours(edges)
    sorted_edges = sorted(edge_neighbours.keys(), key=lambda x: len(edge_neighbours[x]), reverse=True)
    
    colored_nodes = dict()
    for edge in sorted_edges:
        colored_nodes[edge] = -1
    
    llist = deque()
    llist.appendleft(sorted_edges[0])
    colored_nodes[sorted_edges[0]] = find_coloring(sorted_edges[0], edge_neighbours[sorted_edges[0]], colored_nodes, -1)

    while len(llist) > 0 and len(llist) < len(sorted_edges):
        current_edge = llist.popleft()
        llist.appendleft(current_edge)

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
                    llist.appendleft(adj)
                    anyAdjacentColored = True

        while (len(llist) != 0) and (not isPathAvailable):
            print("here")
            tmp_edge = llist.popleft()
            tmp_color = find_coloring(tmp_edge, edge_neighbours[tmp_edge], colored_nodes, colored_nodes[tmp_edge])
            if tmp_color is None:
                colored_nodes[tmp_edge] = -1
                continue
            else:
                colored_nodes[tmp_edge] = tmp_color
                llist.appendleft(tmp_edge)
                flag = True
                break
        if anyAdjacentColored == False:
            tmp = llist.popleft()
            llist.append(tmp)
         
    return colored_nodes

def color_switch(color:int) -> str :
    if color == 0:
        return "red"
    elif color == 1:
        return "green"
    elif color == 2:
        return "blue"
    elif color == 3:
        return "orange"
    else:
        return "black"

def is_safe(adj, color_dict, color):
    for a in adj:
        if color_dict[a] == color:
            return False
    return True

def graph_coloring_util(graph: dict, keys: list, idx: int, color_count, color_dict: dict):
    if idx == len(graph):
        return True

    for c in range(0, color_count):
        if is_safe(graph[keys[idx]], color_dict, c):
            color_dict[keys[idx]] = c
            if graph_coloring_util(graph, keys, idx + 1, color_count, color_dict):
                return True
            color_dict[keys[idx]] = -1

    return False

def graph_coloring3(edges: list[Edge]) -> dict[Edge, int]:
    graph = find_neighbours(edges)
    keys = sorted(graph.keys(), key=lambda x: len(graph[x]), reverse=True)
    colored_nodes = dict()
    for edge in graph:
        colored_nodes[edge] = -1

    num_of_colors = 4
    graph_coloring_util(graph, keys, 0, num_of_colors, colored_nodes)
    return colored_nodes