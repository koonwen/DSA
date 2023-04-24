from typing import List, Tuple


def topsort(nodes: int, edges: List[Tuple[int, int]]) -> List[int]:
    g = {i: set() for i in range(0, nodes + 1)}
    for fr, to in edges:
        g[fr].add(to)

    visited = set()
    stack = list()

    def dfs(node):
        if node in visited:
            return
        else:
            visited.add(node)
            for neighbour in g[node]:
                dfs(neighbour)

            stack.append(node)

    for i in range(1,nodes+1):
        dfs(i)
    stack.reverse()
    return stack



if __name__ == '__main__':
    test = [(1, 2), (2, 3), (2, 4), (4, 5), (6, 2), (6, 7)]
    print(topsort(7, test))