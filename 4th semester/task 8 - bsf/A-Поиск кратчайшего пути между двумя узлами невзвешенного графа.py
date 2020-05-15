"""
Дан невзвешенный связный граф. Вершины пронумерованы от 0. Трeбуется с помощью обхода в ширину найти расстояние
от одной указанной вершины до другой.

Формат входных данных
На вход программе в первой строке подаются через пробел четыре числа: n, m, x, y. Число n (2 <= n <= 1000) -
количество вершин в графе, m (1 <= m <= 20000) - количество ребер. x и y - начальная и конечная вершины соответственно
(0 <= x,y < n). В следующих m строках задаются ребра, по два числа в каждой строке - номера соединенных вершин.

Формат выходных данных
Требутеся распечатать одно число - расстояние от вершины x до вершины y .
"""
from collections import deque

vertexes, edges, start_x, end_x = map(int, input().split())  # подающиеся на вход параметры
graph = {x: set() for x in range(vertexes)}   # делаем словарь
for _ in range(edges):
    x1, x2 = map(int, input().split())
    graph[x1].add(x2)
    graph[x2].add(x1)

distances = [None] * vertexes
distances[start_x] = 0
queue = deque([start_x])

while queue:     # пока queue не равна 0
    cur_x = queue.popleft()
    for neighbour_x in graph[cur_x]:
        if distances[neighbour_x] is None:
            distances[neighbour_x] = distances[cur_x] + 1
            queue.append(neighbour_x)

print(distances[end_x])
