import unittest

from HackerRank.Trees.ValidBinarySearchTreee.valid_bst import checkBST
from HackerRank.Trees.tree_utils import BinarySearchTree

# TODO
def parse_input(filename: str):
    with open(filename) as f:
        tree = BinarySearchTree()
        n = int(f.readline())
        arr = [int(i) for i in f.readline().split()]
        for i in range(n):
            tree.create(arr[i])
        return tree


class TestHeightOfBinaryTree(unittest.TestCase):
    def setUp(self) -> None:
        self.test1 = parse_input("test1.txt")
        self.test2 = parse_input("test2.txt")
        self.test3 = parse_input("test3.txt")
        self.test4 = parse_input("test4.txt")
        self.test5 = parse_input("test5.txt")

    def test_success(self):
        self.assertEqual(True, checkBST(self.test1.root))
        self.assertEqual(True, checkBST(self.test2.root))
        self.assertEqual(True, checkBST(self.test3.root))
        self.assertEqual(False, checkBST(self.test4.root))
        self.assertEqual(False, checkBST(self.test5.root))


if __name__ == '__main__':
    unittest.main()