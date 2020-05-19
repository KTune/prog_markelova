
def hash_func(x,m,stroka):

    prom = 0

    if len(stroka) == 1:

        return ord(stroka)

    elif len(stroka) == 2:

        return ord(stroka[0])*x+ord(stroka[1])

    else:

        for i in range(len(stroka)):

            prom = prom*x

            prom += ord(stroka[i])

        return prom % m


a = list(map(int,input().split()))
stroka = input()
print(hash_func(a[0], a[1], stroka))
