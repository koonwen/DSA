# To solve the problem, we take note that if the cost of building
# the library is cheaper than repair the road then we build the
# library in every city. Else we need to perform DFS on each node
# to identify the total number of "areas" that we can cover by
# repairing roads. We note that within each area, the number of
# roads we must repair is (n - 1) cities. Hence we can find the
# total number of roads needed to repaired as
# r = (totol_cities - areas)
# finally our cost is then the (r * c_roads + areas * c_lib)

def roads_and_libraries(n, c_lib, c_road, cities):
    """
    Calculate the minimum cost required to have
    every city either be connected to a city that has a library
    or has a library itself.
    :param n:
    :param c_lib:
    :param c_road:
    :param cities:
    :return: Minimum cost to build
    """
    graph = {i: set() for i in range(1, n+1)}
    for c1, c2 in cities:
        graph[c1].add(c2)
        graph[c2].add(c1)

    if c_lib < c_road:
        return c_lib * n

    visited = set()
    def dfs(city):
        if city not in visited:
            visited.add(city)
            for neighbour in graph[city]:
                dfs(neighbour)

    cnt = 0
    for city in graph.keys():
        if city not in visited:
            cnt += 1
            dfs(city)

    return cnt*c_lib + (n-cnt)*c_road
