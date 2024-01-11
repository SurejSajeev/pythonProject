from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


def depth_first_search(input_graph, root, visited=None):
    """Depth first search is used to traverse a graph and explore
    as far as possible before backtracking."""
    # set the visited nodes
    if not visited:
        visited = set()
    visited.add(root)
    print(f"Visited {root}")
    # Loop through the neighbours
    for node in input_graph[root]:
        if node not in visited:
            depth_first_search(input_graph, node, visited)


if __name__ == '__main__':
    depth_first_search(graph, 'A')
