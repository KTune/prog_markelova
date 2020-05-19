
M = int(input())

b = []

b = input().split()

for j in range(M):

    b[j] = int(b[j])

k = ""

for j in range(1, M - 1):

    if ((b[j] > b[j - 1]) and (b[j] > b[j + 1])) or ((b[j] < b[j-1]) and (b[j] < b[j+1])):
        k += " " + str(j)

k = k[:0] + k[1:]

print(k)
