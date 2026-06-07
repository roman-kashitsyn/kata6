class UnionFind:
    def __init__(self, n: int):
        self.p, self.r = list(range(n)), n * [0]

    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.r[x] < self.r[y]:
            x, y = y, x
        self.p[y] = x
        if self.r[x] == self.r[y]:
            self.r[x] += 1
        return True
