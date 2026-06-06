def bellmanford(g, s):
    d = [float("inf")] * len(g)
    p = [None] * len(g)
    d[s] = 0
    for _ in range(len(g) - 1):
        for u, adj in enumerate(g):
            for v, w in adj:
                if d[u] + w < d[v]:
                    d[v] = d[u] + w
                    p[v] = u
    return (p, d)
