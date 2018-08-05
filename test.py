def gen(a, b = None):
    yield a
    if b:
        yield from b



b = gen(1)
c = gen(2, b)
d = gen(3, c)
print([i for i in d])
print([i for i in c])
