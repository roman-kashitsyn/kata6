def bellmanford(g, s):
    d = [float('inf') for _ in g]
    d[s] = 0
    p = [None for _ in g]
    for _ in range(len(g) - 1):
        for u, adj in enumerate(g):
            for v, w in adj:
                if d[u] + w < d[v]:
                    d[v] = d[u] + w
                    p[v] = u
    return (p, d)