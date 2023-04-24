import unittest

from HackerRank.Trees.LowestCommonAncestor.lowest_common_ancestor import lca
from HackerRank.Trees.tree_utils import BinarySearchTree


def parse_input(filename: str):
    with open(filename) as f:
        tree = BinarySearchTree()
        n = int(f.readline())
        arr = [int(i) for i in f.readline().split()]
        v1, v2 = (int(i) for i in f.readline().split())
        for i in range(n):
            tree.create(arr[i])
        print(tree, v1, v2)
        return tree, v1, v2


class TestLowestCommonAncestor(unittest.TestCase):
    def setUp(self) -> None:
        self.test1 = parse_input("test1.txt")
        self.test2 = parse_input("test2.txt")
        self.test3 = parse_input("test3.txt")

    def test_success(self):
        self.assertEqual(4, lca(self.test1[0].root, self.test1[1], self.test1[2]).info)
        self.assertEqual(1, lca(self.test2[0].root, self.test2[1], self.test2[2]).info)
        self.assertEqual(5, lca(self.test3[0].root, self.test3[1], self.test3[2]).info)


if __name__ == '__main__':
    unittest.main()
