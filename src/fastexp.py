def fastexp(x, n):
    if n < 0:
        raise ValueError("n must be non-negative")
    r = 1
    while n > 0:
        if n & 1:
            r *= x
        x = x * x
        n >>= 1
    return r
