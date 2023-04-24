import unittest

from HackerRank.Graphs.ShortestReach.shortest_reach import shortest_reach


def parse_input(filename: str):
    input = []
    with open(filename) as f:
        q = int(f.readline())
        for _ in range(q):
            n, m = (int(i) for i in f.readline().split())
            edges = []
            for _ in range(m):
                u, v = (int(i) for i in f.readline().split())
                edges.append((u, v))
            s = int(f.readline())
            input.append((n, edges, s))
    return input


def evaluate(f, input):
    return [f(i[0], i[1], i[2]) for i in input]


class TestShortestReach(unittest.TestCase):
    def setUp(self) -> None:
        self.test1 = parse_input("test1.txt")
        self.test2 = parse_input("test2.txt")
        self.test3 = parse_input("test3.txt")
        self.test4 = parse_input("test4.txt")
        self.test5 = parse_input("test5.txt")

    def test_success(self):
        self.assertEqual([[6, 6, -1], [-1, 6]], evaluate(shortest_reach, self.test1))
        self.assertEqual([[6, 12, 18, 6, -1]], evaluate(shortest_reach, self.test2))
        self.assertEqual([[6, 12, 18, 6, -1, -1]], evaluate(shortest_reach, self.test3))
        self.assertEqual([[6, 12, 12, 6]], evaluate(shortest_reach, self.test4))
        self.assertEqual([], evaluate(shortest_reach, self.test5))


if __name__ == '__main__':
    unittest.main()
