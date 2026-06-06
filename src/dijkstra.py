from heapq import heappop, heappush


def dijkstra(g, s):
    d = [float("inf")] * len(g)
    p = [None] * len(g)
    d[s] = 0
    pq = [(0, s)]

    while pq:
        du, u = heappop(pq)
        if du > d[u]:
            continue
        for v, w in g[u]:
            dist = du + w
            if dist < d[v]:
                d[v] = dist
                p[v] = u
                heappush(pq, (dist, v))
    return (p, d)
