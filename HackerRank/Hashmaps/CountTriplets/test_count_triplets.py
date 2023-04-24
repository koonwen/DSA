import unittest

from HackerRank.Hashmaps.CountTriplets.count_triplets import \
    count_triplets


def parse_input(filename: str):
    with open(filename) as f:
        n, r = (int(i) for i in f.readline().split())
        arr = [int(i) for i in f.readline().split()]
    return arr, r


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test1 = parse_input("test1.txt")
        self.test2 = parse_input("test2.txt")
        self.test3 = parse_input("test3.txt")
        self.test4 = parse_input("test4.txt")
        self.test5 = parse_input("test5.txt")

    def test_success(self):
        self.assertEqual(2, count_triplets(self.test1[0], self.test1[1]))
        self.assertEqual(6, count_triplets(self.test2[0], self.test2[1]))
        self.assertEqual(4, count_triplets(self.test3[0], self.test3[1]))
        self.assertEqual(4, count_triplets(self.test4[0], self.test4[1]))
        self.assertEqual(0, count_triplets(self.test5[0], self.test5[1]))


if __name__ == '__main__':
    unittest.main()
