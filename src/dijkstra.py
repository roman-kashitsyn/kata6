from heapq import heappop, heappush


def dijkstra(g, s):
    pq = []
    d = [float('inf') for _ in g]
    p = [None for _ in g]
    d[s] = 0
    heappush(pq, (0, s))

    while pq:
        w, u = heappop(pq)
        if w > d[u]:
            continue
        for v, w in g[u]:
            dist = d[u] + w
            if dist < d[v]:
                d[v] = dist
                p[v] = u
                heappush(pq, (dist, v))

    return (p, d)

