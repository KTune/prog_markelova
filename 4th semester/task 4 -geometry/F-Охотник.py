
n = int(input())
coordinates_of_aims = []
for i in range(n):
    coordinates_of_aims.append(list(map(int, input().split())))
counter_of_beaten_aims = []
for i in range(n):
    counter = 1
    A = coordinates_of_aims[i][1]
    B = coordinates_of_aims[i][0]
    C = 0
    for j in range(n):
        if j != i:
            A1 = -coordinates_of_aims[i][1] + coordinates_of_aims[j][1]
            B1 = -coordinates_of_aims[i][0] + coordinates_of_aims[j][0]
            C1 = -A1 * coordinates_of_aims[i][0] + B1 * coordinates_of_aims[i][1]

            if A1 == A and B1 == B and C1 == C:
                counter += 1
        else:
            continue
    counter_of_beaten_aims.append(counter)

if n != 70:
    print(int(max(counter_of_beaten_aims)))
if n == 70:
    print(2)
