
def F(f):
    if f == 0:
        return 1
    else:
        return (f - M(F(f - 1)))


def M(m):
    if m == 0:
        return 0
    else:
        return (m - F(M(m - 1)))
