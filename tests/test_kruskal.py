from graphs import DIJKSTRA_WIKI
from kruskal import kruskal


def test_wiki():
    assert kruskal(DIJKSTRA_WIKI) == [
        (2, 5, 2),
        (3, 4, 6),
        (0, 1, 7),
        (0, 2, 9),
        (4, 5, 9),
    ]


def test_single_vertex():
    assert kruskal([[]]) == []


def test_two_vertices():
    assert kruskal([[(1, 5)], [(0, 5)]]) == [(0, 1, 5)]


def test_disconnected():
    # Two disjoint edges 0-1 (w=3) and 2-3 (w=4): Kruskal returns
    # a minimum spanning forest with total weight 7.
    assert kruskal([[(1, 3)], [(0, 3)], [(3, 4)], [(2, 4)]]) == [
        (0, 1, 3),
        (2, 3, 4),
    ]
