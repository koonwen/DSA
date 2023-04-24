
def lca(root, v1, v2):

    def find_path(node, v1, path):

        path.append(node)

        if node.info == v1:
            return path

        if v1 < node.info:
            return find_path(node.left, v1, path)
        else:
            return find_path(node.right, v1, path)

    path1 = find_path(root, v1, [])
    path2 = find_path(root, v2, [])

    lowest = root
    for n1, n2 in zip(path1, path2):
        if n1 != n2:
            break
        else:
            lowest = n1

    return lowest
