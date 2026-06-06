import unittest

from unionfind import UnionFind


class UnionFindTest(unittest.TestCase):
    def test_unionfind(self):
        ds = UnionFind(8)
        for i in range(8):
            self.assertEqual(i, ds.find(i))
        for x, y in [
            (0, 1),
            (4, 5),
            (0, 4),
            (5, 7),
            (2, 3),
        ]:
            ds.union(x, y)
        for x in [0, 1, 4, 5, 7]:
            self.assertEqual(ds.find(0), ds.find(x))
        for x in [2, 3]:
            self.assertNotEqual(ds.find(0), ds.find(x))
            self.assertEqual(ds.find(2), ds.find(x))
        self.assertEqual(ds.find(6), 6)
