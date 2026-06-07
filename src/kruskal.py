from unionfind import UnionFind


def kruskal(g):
    edges = [
        (w, u, v)
        for (u, adj) in enumerate(g)
        for (v, w) in adj
        if u < v
    ]
    uf, mst = UnionFind(len(g)), []
    for w, u, v in sorted(edges):
        if uf.union(u, v):
            mst.append((u, v, w))
    return mst
