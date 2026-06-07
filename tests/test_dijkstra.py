from dijkstra import dijkstra
from graphs import DIJKSTRA_WIKI


def test_wiki():
    assert dijkstra(DIJKSTRA_WIKI, 0) == (
        [None, 0, 0, 2, 5, 2],
        [0, 7, 9, 20, 20, 11],
    )
