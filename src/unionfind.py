class UnionFind:
    def __init__(self, n):
        self.n, self.p, self.r = n, list(range(n)), n*[0]

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return
        if self.r[x] < self.r[y]:  x, y = y, x
        self.p[y] = x
        if self.r[x] == self.r[y]:
            self.r[x] += 1
