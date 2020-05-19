
def hash_func(p,m,stroka):
    prom=0
    if len(stroka)==1:
        return (ord(stroka))%m
    elif len(stroka)==2:
        return (ord(stroka[0])*p+ord(stroka[1]))%m
    else:
        for i in range(len(stroka)):
            prom=prom*p
            prom+=ord(stroka[i])
        return prom%m


def check_key(table, key, hash_numb):
    hash_numb=int(hash_numb)
    for i in range(len(table[hash_numb])):
        if table[hash_numb][i][1]==key:
            return i
    return -1


def insert(table,key,value):
    if len(table[hash_func(91,100,key)%10])==0:
        table[hash_func(91,100,key)%10].append([hash_func(91,100,key), key, value])
    elif check_key(table,key, hash_func(91,100,key)%10)!=-1:
        table[hash_func(91,100,key)%10][check_key(table,key, hash_func(91,100,key)%10)][2]=value
    elif len(table[hash_func(91,100,key)%10])!=0:
        table[hash_func(91,100,key)%10].append([hash_func(91,100,key), key, value])


n=10
table=[[],[],[],[],[],[],[],[],[],[]]
amount=int(input())
for i in range(amount):
    chain=list(map(str,input().split()))
    insert(table,chain[0],chain[1])

# print(table)
for i in range(n):
    if len(table[i])!=0:
        print(i)
        for j in range(len(table[i])):
            print(table[i][j][0],table[i][j][1],table[i][j][2])
