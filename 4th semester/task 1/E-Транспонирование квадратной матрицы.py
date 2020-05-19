
M = int(input())

b = [[0] * M for i in range(M)]

for j in range(M):

    b[j] = input().split()

otv = []

for j in range(M):

    c = []

    for l in range(M):

        c += [b[l][j]]

    otv += [c]

for j in range(M):

    print(*otv[j])
