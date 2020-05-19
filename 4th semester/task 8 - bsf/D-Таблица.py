"""
Дана таблица, состоящая из N строк и M столбцов. В каждой клетке таблицы записано одно из чисел: 0 или 1.

Расстоянием между клетками cell_1 = (x1, y1) и cell_2 = (x2, y2) назовём:

расстояние(cell_1, cell_2) = |x1 - x2| + |y1 - y2|.
Вам необходимо построить таблицу расстояний, в (i, j)-клетке которой будет записано минимальное расстояние между
клеткой (i, j) начальной таблицы и клеткой, в которой записана единица. Гарантируется, что хотя бы одна единица
в исходной таблице есть.

Формат входных данных
В первой строке вводятся два натуральных числа N и M, не превосходящих 300. Далее идут N строк. Каждая строка содержит
M чисел, разделённых пробелом - элементы исходной таблицы.

Формат выходных данных
Требуется вывести N строк по M чисел - элементы таблицы расстояний.
"""
import itertools
from collections import deque


def bfs(start_x):
    distances[start_x[0]][start_x[1]] = 0
    queue = deque([start_x])
    while queue:
        cur_x = queue.popleft()
        for neighbour_x in graph[cur_x]:

            if (distances[neighbour_x[0]][neighbour_x[1]] is None
                    or
                    distances[cur_x[0]][cur_x[1]] + 1 < distances[neighbour_x[0]][neighbour_x[1]]
            ):
                distances[neighbour_x[0]][neighbour_x[1]] = distances[cur_x[0]][cur_x[1]] + 1
                queue.append(neighbour_x)


N, M = map(int, input().split())

table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

graph = {x: set() for x in itertools.product(range(N), range(M))}

for i in range(N):
    for j in range(M):
        if i - 1 >= 0:
            graph[(i, j)].add((i - 1, j))
        if i + 1 < N:
            graph[(i, j)].add((i + 1, j))
        if j - 1 >= 0:
            graph[(i, j)].add((i, j - 1))
        if j + 1 < M:
            graph[(i, j)].add((i, j + 1))

distances = [[None for _ in range(M)] for _ in range(N)]

for vertex in graph:
    if table[vertex[0]][vertex[1]] == 1:
        bfs(vertex)

for i in range(N):
    print(*distances[i])
