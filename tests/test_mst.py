import pytest

from graphs import DIJKSTRA_WIKI
from kruskal import kruskal
from prim import prim


def canon(edges):
    # Orient each edge as (min, max, weight) and sort, so two MSTs
    # are comparable regardless of how the algorithm orients edges.
    return sorted(
        (min(u, v), max(u, v), w) for u, v, w in edges
    )


CASES = [
    pytest.param(
        DIJKSTRA_WIKI,
        [
            (0, 1, 7),
            (0, 2, 9),
            (2, 5, 2),
            (3, 4, 6),
            (4, 5, 9),
        ],
        id="wiki",
    ),
    pytest.param([[]], [], id="single_vertex"),
    pytest.param(
        [[(1, 5)], [(0, 5)]], [(0, 1, 5)], id="two_vertices"
    ),
    pytest.param(
        [[(1, 3)], [(0, 3)], [(3, 4)], [(2, 4)]],
        [(0, 1, 3), (2, 3, 4)],
        id="disconnected_forest",
    ),
    # Vertex 0 lists its heavy edge 0-1 (w=10) before the light
    # edge 0-2 (w=1). If Prim forgets to heapify the initial pq,
    # heappop returns pq[0] = (10, 0, 1) and the MST is wrong.
    pytest.param(
        [
            [(1, 10), (2, 1)],
            [(0, 10), (2, 5)],
            [(0, 1), (1, 5)],
        ],
        [(0, 2, 1), (1, 2, 5)],
        id="unordered_adjacency",
    ),
]


@pytest.mark.parametrize("graph,expected", CASES)
@pytest.mark.parametrize(
    "algo", [kruskal, prim], ids=["kruskal", "prim"]
)
def test_mst(algo, graph, expected):
    assert canon(algo(graph)) == canon(expected)
