from collections import deque


def breadth_first_search(graph, root_node):
    """BFS explores all the neighbor nodes at the
    current level before moving to the next level.
    It explores a layer of nodes at a time."""
    # We create a deque with our starting node. Deque is a list like data type
    # which is faster than a list for appending and popping operations.
    visited, queue = set(), deque([root_node])
    # Add our root node to the visited set.
    visited.add(root_node)

    while queue:

        # Remove the visited node from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    breadth_first_search(graph, 0)
