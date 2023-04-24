# We return -1 because if the root is not even defined, then we can signal an error.

def height(root):
    if not root:
        return -1
    else:
        return max(height(root.left)+1,
                   height(root.right)+1)
