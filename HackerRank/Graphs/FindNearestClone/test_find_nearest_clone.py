import unittest

from HackerRank.Graphs.FindNearestClone.find_nearest_clone import find_nearest_clone


def parse_input(filename: str):
    with open(filename) as f:
        n, m = (int(num) for num in f.readline().split())
        g_from, g_to = [], []
        for _ in range(m):
            fst, snd = (int(num) for num in f.readline().split())
            g_from.append(fst)
            g_to.append(snd)
        ids = [int(num) for num in f.readline().split()]
        val = int(f.read())
    return n, g_from, g_to, ids, val


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test1 = parse_input("test1.txt")
        self.test2 = parse_input("test2.txt")
        self.test3 = parse_input("test3.txt")
        self.test4 = parse_input("test4.txt")
        self.test5 = parse_input("test5.txt")

    def test_find_nearest_clone(self):
        self.assertEqual(1, find_nearest_clone(self.test1[0],
                                               self.test1[1],
                                               self.test1[2],
                                               self.test1[3],
                                               self.test1[4]))
        self.assertEqual(-1, find_nearest_clone(self.test2[0],
                                                self.test2[1],
                                                self.test2[2],
                                                self.test2[3],
                                                self.test2[4]))
        self.assertEqual(3, find_nearest_clone(self.test3[0],
                                               self.test3[1],
                                               self.test3[2],
                                               self.test3[3],
                                               self.test3[4]))
        self.assertEqual(-1, find_nearest_clone(self.test4[0],
                                                self.test4[1],
                                                self.test4[2],
                                                self.test4[3],
                                                self.test4[4]))
        self.assertEqual(-1, find_nearest_clone(self.test5[0],
                                                self.test5[1],
                                                self.test5[2],
                                                self.test5[3],
                                                self.test5[4]))


if __name__ == '__main__':
    unittest.main()
