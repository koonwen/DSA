
# This problem is somewhat of a more complex  dfs. The
# aim is to traverse all possible nodes and return the total
# reachable. But because it is a matrix, we have to check
# all six of it's boundaries that it can traverse to.

# TODO write tests

def max_region(grid):
    width = len(grid[0])
    height = len(grid)
    visited = set()

    def dfs(x, y):
        if (x, y) in visited:
            return 0
        if not (0 <= y < width and 0 <= x < height):
            return 0
        visited.add((x, y))
        if grid[x][y]:
            left = dfs(x - 1, y)
            top_left = dfs(x - 1, y - 1)
            bottom_left = dfs(x - 1, y + 1)
            top = dfs(x, y - 1)
            bottom = dfs(x, y + 1)
            top_right = dfs(x + 1, y - 1)
            right = dfs(x + 1, y)
            bottom_right = dfs(x + 1, y + 1)
            return left + top_left + bottom_left + top + bottom + top_right + right + bottom_right + 1
        return 0

    max_so_far = 0
    for y in range(width):
        for x in range(height):
            if (x, y) not in visited and grid[x][y] == 1:
                max_so_far = max(dfs(x, y), max_so_far)
    return max_so_far


if __name__ == '__main__':
    test = [[1, 0, 1, 1, 0],
            [1, 1, 0, 0, 1],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1],
            [1, 1, 1, 0, 0]]
    test2 = [[0, 0, 1, 1],
             [0, 0, 1, 0],
             [0, 1, 1, 0],
             [0, 1, 0, 0],
             [1, 1, 0, 0]]
    print(max_region(test2))
