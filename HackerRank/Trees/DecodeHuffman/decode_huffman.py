from HackerRank.Trees.tree_utils import Node

# The intuition behind huffman decoding is straightforward.
# Traverse to the maximum you can and then attach the value
# you find at the node. The important thing to remember is to
# reset the curr to the node and then move to either the right
# or left depending on which branch you're one.

def decode_huffman(root: Node, s: str) -> str:

    curr = root
    decoded = ""
    for i in s:
        if i == "0":
            if curr.left:
                curr = curr.left
            else:
                decoded += curr.info
                curr = root.left
        else:
            if curr.right:
                curr = curr.right
            else:
                decoded += curr.info
                curr = root.right

    decoded += curr.info
    return decoded








