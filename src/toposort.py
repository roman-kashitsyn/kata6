def toposort(g):
    r, state = [], ["w"] * len(g)

    def dfs(s):
        if state[s] == "b":
            return
        if state[s] == "g":
            raise ValueError("cycle")
        state[s] = "g"
        for u in g[s]:
            dfs(u)
        state[s] = "b"
        r.append(s)

    for s in range(len(g)):
        dfs(s)
    return r[::-1]
