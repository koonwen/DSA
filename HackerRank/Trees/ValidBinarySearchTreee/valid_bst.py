import sys

from HackerRank.Trees.tree_utils import Node

# Can be difficult to get the intuition for recursive problems.
# However this problem requires that you pass down the ranges
# to help you check if the node is within the valid range
# then we perform the recursion on the left and right subtrees,
# finally we need to bubble up the results so we return if both
# the left and right are True.

# True and True : True
# True and False : False
# False and False : False

# True or True : True
# True or False : True
# False or False : False

def checkBST(root: Node):

    def rec_check(node: Node, lo: int, hi: int) -> bool:
        if not node:
            return True
        if lo < node.info < hi:
            left = rec_check(node.left, lo, node.info)
            right = rec_check(node.right, node.info, hi)
            return left and right
        return False

    return rec_check(root, -sys.maxsize, sys.maxsize)

