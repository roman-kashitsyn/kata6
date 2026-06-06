def floydwarshall(g):
    n = len(g)
    d = [[float("inf")] * n for _ in range(n)]
    p = [[None] * n for _ in range(n)]
    for u, adj in enumerate(g):
        d[u][u] = 0
        p[u][u] = u
        for v, w in adj:
            d[u][v] = w
            p[u][v] = u
    for k in range(n):
        for i in range(n):
            for j in range(n):
                nd = d[i][k] + d[k][j]
                if nd < d[i][j]:
                    d[i][j] = nd
                    p[i][j] = p[k][j]
    return (p, d)
