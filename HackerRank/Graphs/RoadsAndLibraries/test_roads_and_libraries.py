import unittest

from HackerRank.Graphs.RoadsAndLibraries.roads_and_libraries \
    import roads_and_libraries


def parse_input(filename: str):
    input_list = []
    with open(filename) as f:
        queries = int(f.readline())
        for _ in range(queries):
            n, m, c_lib, c_road = [int(i) for i in f.readline().split()]
            cities = []
            for _ in range(m):
                c1, c2 = [int(i) for i in f.readline().split()]
                cities.append((c1, c2))
            input_list.append((n, c_lib, c_road, cities))
    return input_list


def evaluate(f, input_list):
    result_list = []
    for n, c_lib, c_road, cities in input_list:
        result_list.append(f(n, c_lib, c_road, cities))
    return result_list


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test1 = parse_input("test1.txt")
        self.test2 = parse_input("test2.txt")
        self.test3 = parse_input("test3.txt")
        self.test4 = parse_input("test4.txt")
        self.test5 = parse_input("test5.txt")

    def test_success(self):
        self.assertEqual([4, 12], (evaluate(roads_and_libraries, self.test1)))
        self.assertEqual([12], (evaluate(roads_and_libraries, self.test2)))
        self.assertEqual([15], (evaluate(roads_and_libraries, self.test3)))
        self.assertEqual([10], (evaluate(roads_and_libraries, self.test4)))
        self.assertEqual([0], (evaluate(roads_and_libraries, self.test5)))


if __name__ == '__main__':
    unittest.main()
