import unittest

from floydwarshall import floydwarshall


class TestFloydWarshall(unittest.TestCase):
    def test_wiki(self):
        """Tests the example from the Wikipedia: https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm#Example"""
        self.assertEqual(
            floydwarshall(
                [
                    [(0, 0), (2, -2)],
                    [(0, 4), (1, 0), (2, 3)],
                    [(2, 0), (3, 2)],
                    [(1, -1), (3, 0)],
                ]
            ),
            (
                [
                    [0, 3, 0, 2],
                    [1, 1, 0, 2],
                    [1, 3, 2, 2],
                    [1, 3, 0, 3],
                ],
                [
                    [0, -1, -2, 0],
                    [4, 0, 2, 4],
                    [5, 1, 0, 2],
                    [3, -1, 1, 0],
                ],
            ),
        )
