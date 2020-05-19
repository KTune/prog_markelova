
b = int(input())

k = 1

max = b

while b != 0:

    b = int(input())

    if b > max:

        max = b

        k = 1

    elif b == max:

        k += 1

print(k)
