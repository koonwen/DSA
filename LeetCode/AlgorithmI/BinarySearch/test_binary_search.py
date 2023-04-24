import unittest

from LeetCode.AlgorithmI.BinarySearch.binary_search import binary_search


def parse_input(filename: str):
    with open(filename) as f:
        n = int(f.readline())
        lst = [int(i) for i in f.readline().split()]
        find = int(f.readline())
        return lst, find


class TestBinarySearch(unittest.TestCase):
    def setUp(self) -> None:
        self.test1, self.find1 = parse_input("test1.txt")
        self.test2, self.find2 = parse_input("test2.txt")

    def test_success(self):
        self.assertEqual(4, binary_search(self.test1, self.find1))
        self.assertEqual(-1, binary_search(self.test2, self.find2))


if __name__ == '__main__':
    unittest.main()
