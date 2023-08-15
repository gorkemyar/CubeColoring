def find_neighbours(edges):
    find_neighbours = {}
    for edge in edges:
        edge_neighbours = []
        for edge2 in edges:
            if edge[0] == edge2[0] or edge[0] == edge2[1] or edge[1] == edge2[0] or edge[1] == edge2[1]:
                if edge != edge2:
                    edge_neighbours.append(edge2)

        find_neighbours[edge] = edge_neighbours
                
    rmn = {}
    for key, value in find_neighbours.items():
        for key2, value2 in find_neighbours.items():
            if key == key2:
                continue
            tmp = [val for val in value if val in value2]
            if len(tmp) == 2 and key2 not in value:
                if key in rmn:
                    rmn[key].append(key2)
                else:
                    rmn[key] = [key2]

    for key, value in rmn.items():
        find_neighbours[key] += value

    return find_neighbours


    
