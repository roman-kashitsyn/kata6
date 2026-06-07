import pytest

from toposort import toposort


def is_topo_order(g, order):
    # Valid topological order: a permutation of [0, n) where
    # every edge u -> v places u before v.
    if sorted(order) != list(range(len(g))):
        return False
    pos = {v: i for i, v in enumerate(order)}
    return all(
        pos[u] < pos[v]
        for u, adj in enumerate(g)
        for v in adj
    )


CASES = [
    pytest.param([], id="empty"),
    pytest.param([[]], id="single_vertex"),
    pytest.param([[], []], id="two_disconnected"),
    # Forward chain 0 -> 1 -> 2.
    pytest.param([[1], [2], []], id="chain_forward"),
    # Reverse-indexed chain 2 -> 1 -> 0: catches outer loops
    # that visit nodes in index order without an unseen check
    # (every node looks "already done" by the time it sinks).
    pytest.param([[], [0], [1]], id="chain_reverse"),
    # Diamond: 0 -> {1, 2} -> 3.
    pytest.param([[1, 2], [3], [3], []], id="diamond"),
    # Two roots converging on a single sink.
    pytest.param([[2], [2], []], id="two_roots"),
    # Two independent DAGs in one adjacency list.
    pytest.param(
        [[1], [], [3], []], id="disconnected_dags"
    ),
    # Cormen Fig. 22.7 "dressing" DAG. Vertices:
    # 0=undershorts, 1=pants, 2=belt, 3=shirt, 4=tie,
    # 5=jacket, 6=socks, 7=shoes, 8=watch.
    pytest.param(
        [
            [1, 7],  # undershorts -> pants, shoes
            [2, 7],  # pants -> belt, shoes
            [5],  # belt -> jacket
            [4, 2],  # shirt -> tie, belt
            [5],  # tie -> jacket
            [],  # jacket
            [7],  # socks -> shoes
            [],  # shoes
            [],  # watch
        ],
        id="cormen_dressing",
    ),
]


@pytest.mark.parametrize("graph", CASES)
def test_toposort(graph):
    assert is_topo_order(graph, toposort(graph))


def test_output_is_permutation():
    # Independent of edge ordering: every vertex appears
    # exactly once.
    g = [[1, 2], [3], [3], []]
    assert sorted(toposort(g)) == [0, 1, 2, 3]


CYCLES = [
    pytest.param([[0]], id="self_loop"),
    pytest.param([[1], [0]], id="two_node_cycle"),
    pytest.param([[1], [2], [0]], id="three_node_cycle"),
    # Cycle 1 <-> 2 sits inside a larger graph; 0 is a
    # legitimate root and 3 is an isolated sink.
    pytest.param(
        [[1], [2], [1], []], id="cycle_inside_graph"
    ),
    # Cycle is only reachable through a chain; entry node
    # itself is not on the cycle.
    pytest.param(
        [[1], [2], [3], [1]], id="cycle_after_chain"
    ),
]


@pytest.mark.parametrize("graph", CYCLES)
def test_toposort_detects_cycle(graph):
    with pytest.raises(ValueError, match="cycle"):
        toposort(graph)
