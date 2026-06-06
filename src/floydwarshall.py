def floydwarshall(g):
    d = [[float('inf') for _ in g] for _ in g]
    p = [[None for _ in g] for _ in g]
    for u, adj in enumerate(g):
        d[u][u] = 0
        p[u][u] = u
        for v, w in adj:
            d[u][v] = w
            p[u][v] = u
    for k in range(len(d)):
        for i in range(len(d)):
            for j in range(len(d)):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    p[i][j] = p[k][j]
    return (p, d)