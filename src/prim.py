def prim(g):
    from heapq import heappop, heappush

    seen, mst = [False] * len(g), []
    for s in range(len(g)):
        if seen[s]:
            continue
        seen[s] = True
        pq = [(w, s, v) for v, w in g[s]]
        while pq:
            w, u, v = heappop(pq)
            if seen[v]:
                continue
            seen[v] = True
            mst.append((u, v, w))
            for nv, nw in g[v]:
                if not seen[nv]:
                    heappush(pq, (nw, v, nv))
    return mst
