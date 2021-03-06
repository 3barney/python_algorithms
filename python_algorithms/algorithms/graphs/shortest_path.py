graph = {
    "a": ["c", "d"],
    "b": ["d", "e"],
    "c": ["a", "e"],
    "d": ["a", "b"],
    "e": ["b", "c"],
}

# function to find the shortest path
def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


print("shortest path: ", find_shortest_path(graph, "a", "e"))
