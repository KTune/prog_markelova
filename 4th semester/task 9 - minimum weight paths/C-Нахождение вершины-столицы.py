"""
Некоторые из городов государства соединены дорогами. Жители этого государства просят вас помочь им с выбором
столицы: требуется, чтобы сумма расстояний от столицы до каждого из остальных городов была минимальна.

Для удобства города уже пронумерованы от 0 до n-1 .

Формат входных данных
На вход программе в первой строке подается два числа через пробел: n и m .

2 ≤ n ≤ 100 - число городов
1 ≤ m ≤ 500 - число дорог
В следующих m строках задаются дороги. Дорога задаётся тремя числами - два номера соединенных дорогой городов
и длина дороги.

Формат выходных данных
Выведите номер столицы. Если возможно несколько варинтов, выведете любой.
"""

n, m = input().split()
n, m = int(n), int(m)

gr = {}


def vvod(gr, a, b, ves):
    if a not in gr:
        gr[a] = {b: ves}
    else:
        gr[a][b] = ves


for i in range(m):
    inp_a, inp_b, inp_ves = input().split()
    inp_a = int(inp_a)
    inp_b = int(inp_b)
    inp_ves = int(inp_ves)
    vvod(gr, inp_a, inp_b, inp_ves)
    vvod(gr, inp_b, inp_a, inp_ves)


def dexter(gr, start):
    s = {}
    queue = []
    s[start] = 0
    queue.append(start)
    while queue:
        v = queue.pop(0)
        for u in gr[v]:
            if (u not in s) or (s[v] + gr[v][u]) < s[u]:
                s[u] = s[v] + gr[v][u]
                queue.append(u)

    return s


def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum


res = [[] for i in range(n)]
for i in range(n):
    s = dexter(gr, i)
    for item in s.values():
        res[i].append(item)
result = []
for el in res:
    result.append(listsum(el))


minimum = 10 ** 10
for el in result:
    if el < minimum:
        minimum = el
        prnt_result = result.index(el)
print(prnt_result)
