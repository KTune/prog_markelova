"""
Дан взвешенный связный граф. Вершины нумеруются с нуля. Трeбуется с помощью алгоритма Дейкстры восстановить
кратчайший путь от вершины s до вершины f.

Формат входных данных
На вход программе в первой строке подается четыре числа через пробел: n , m , s , f .

2 ≤ n ≤ 1000 - число вершин в графе
1 ≤ m ≤ 20000 - число ребер
s и f - номера начальной и конечной вершин, соответственно
В следующих m строках задаются ребра, по три числа в каждой строке - номера соединенных вершин и вес ребра.

Формат выходных данных
Кратчайший путь между вершинами s и f.
"""
n, m, s, f = input().split()
n = int(n)
m = int(m)
s = int(s)
f = int(f)

graph = {}


def vvod(graph, a, b, ves):
    if a not in graph:
        graph[a] = {b: ves}
    else:
        graph[a][b] = ves


for i in range(m):
    a, b, ves = input().split()
    a, b, ves = int(a), int(b), int(ves)
    vvod(graph, a, b, ves)
    vvod(graph, b, a, ves)


p = [-1 for i in range(n)]


def dexter(graph, start):
    s = {}
    queue = []
    s[start] = 0
    queue.append(start)
    while queue:
        v = queue.pop(0)
        for u in graph[v]:
            if (u not in s) or (s[v] + graph[v][u]) < s[u]:
                s[u] = s[v] + graph[v][u]
                p[u] = v
                queue.append(u)


dexter(graph, s)
res = []
while f != s:
    res.append(f)
    f = p[f]
res.append(s)
res.reverse()
print(*res)
