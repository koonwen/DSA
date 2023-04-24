import unittest

from HackerRank.Hashmaps.FrequencyQueries.frequency_queries \
    import freq_query


def parse_input(filename):
    with open(filename, "r") as f:
        q = int(f.readline())
        queries = []
        for line in f:
            queries.append([int(x) for x in line.split()])
        return q, queries


class MyTestCase(unittest.TestCase):
    class TestFrequencyQueries(unittest.TestCase):

        def setUp(self) -> None:
            self.test1 = parse_input("test1.txt")
            self.test2 = parse_input("test2.txt")
            self.test3 = parse_input("test3.txt")
            self.test4 = parse_input("test4.txt")
            self.test5 = parse_input("test5.txt")

        def test_success(self):
            self.assertEqual([], freq_query(self.test1[1]))
            self.assertEqual([0, 1], freq_query(self.test2[1]))
            self.assertEqual([0, 1], freq_query(self.test3[1]))
            self.assertEqual([1], freq_query(self.test4[1]))
            self.assertEqual([0, 1, 1], freq_query(self.test5[1]))


if __name__ == '__main__':
    unittest.main()
