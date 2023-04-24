# The important thing to remember from this algorithm is that you need
# to keep track of the count by appending a tuple of the (node, cnt).
# The cnt is taking the last nodes cnt+1. Therefore the beginning entry
# must be queue = [(start_node, 0)]

# Consider dynamic programming
# The O(V+E) solution requires you to keep an array of distances [-1,-1,-1,-1,-1]
# which gets updates as you traverse throughout the graph by adding 6 each time
# when you pick your root node, you update the distance to 0 so [-1, -1, 0, -1, -1]
# (root node is 3) then as you traverse you update each distance by the previous +6
# At the end of the search, you remove the root node.


def shortest_reach(n, edges, s):

    g = {i: set() for i in range(1, n+1)}
    for u, v in edges:
        g[u].add(v)
        g[v].add(u)

    def bfs(start, end):
        visited = set()
        queue = [(start, 0)]
        while queue:
            curr, cnt = queue.pop(0)
            for neighbour in g[curr]:
                if neighbour not in visited:
                    if neighbour == end:
                        return cnt+1
                    visited.add(neighbour)
                    queue.append((neighbour, cnt+1))
        return -1

    res = []
    for node in range(1, n+1):
        if s == node:
            continue
        else:
            shortest = bfs(s, node)
            multiplier = 6*shortest if shortest != -1 else -1
            res.append(multiplier)

    return res
