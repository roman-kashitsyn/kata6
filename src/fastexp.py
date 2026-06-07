def fastexp(x, n):
    r = 1
    while n > 0:
        if n & 1:
            r *= x
        x *= x
        n = n >> 1
    return r
