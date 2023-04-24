# This problem is solved with a breadth first search algorithm
# We iterate over all nodes in the graph with the color we are
# interested in and see what is the shortest distance for each traversal.
# Because we know that the graph is undirected, we can have a global set
# to mark nodes visited previously and will not need to revisit them
# even when starting the BFS on a new node.

def find_nearest_clone(g_nodes, g_from, g_to, ids, val):
    """
    Find shortest path between nodes of the same id. Return -1 if not found
    :param g_nodes:
    :param g_from:
    :param g_to:
    :param ids:
    :param val:
    :return: shortest path
    """
    g = {i: set() for i in range(1, g_nodes + 1)}
    for to, fr in zip(g_from, g_to):
        g[to].add(fr)
        g[fr].add(to)

    visited = set()

    def bfs(start_node):
        col = ids[start_node - 1]
        queue = [(start_node, 1)]
        visited.add(start_node)
        cnt = 1
        while queue:
            cnt += 1
            curr, n = queue.pop(0)
            for neighbour in g[curr]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    if col == ids[neighbour - 1]:
                        return n
                    else:
                        queue.append((neighbour, cnt))
        return -1

    shortest_path_list = [bfs(node) for node in g.keys() if ids[node - 1] == val]
    shortest_path_list = list(filter(lambda x: x > 0, shortest_path_list))
    return min(shortest_path_list) if shortest_path_list else -1
