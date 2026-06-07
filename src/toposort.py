def toposort(g):
    r, state = [], ["w"] * len(g)

    def dfs(u):
        if state[u] == "b":
            return
        if state[u] == "g":
            raise ValueError("cycle")
        state[u] = "g"
        for v in g[u]:
            dfs(v)
        state[u] = "b"
        r.append(u)

    for s in range(len(g)):
        dfs(s)
    return r[::-1]
