
def dot_product(N, s1, s2):
    s = 0
    for i in range(N):
        s += s1[i] * s2[i]
    return s
