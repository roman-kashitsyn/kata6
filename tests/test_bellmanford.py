import unittest

from bellmanford import bellmanford


class BellmanFordTest(unittest.TestCase):
    def test_wiki(self):
        """Test the example from the Wikipedia article on Dijkstra
        https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif
        """
        self.assertEqual(
            bellmanford(
                [
                    [(1, 7), (2, 9), (5, 14)],
                    [(0, 7), (2, 10), (3, 15)],
                    [(0, 9), (1, 10), (3, 11), (5, 2)],
                    [(1, 15), (2, 11), (4, 6)],
                    [(3, 6), (5, 9)],
                    [(0, 14), (2, 2), (4, 9)],
                ],
                0,
            ),
            ([None, 0, 0, 2, 5, 2], [0, 7, 9, 20, 20, 11]),
        )
