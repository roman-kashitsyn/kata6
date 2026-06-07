from unionfind import UnionFind


def test_unionfind():
    ds = UnionFind(8)
    for i in range(8):
        assert ds.find(i) == i
    for x, y in [(0, 1), (4, 5), (0, 4), (5, 7), (2, 3)]:
        ds.union(x, y)
    for x in [0, 1, 4, 5, 7]:
        assert ds.find(0) == ds.find(x)
    for x in [2, 3]:
        assert ds.find(0) != ds.find(x)
        assert ds.find(2) == ds.find(x)
    assert ds.find(6) == 6
