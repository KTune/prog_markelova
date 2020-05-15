"""
Дан невзвешенный неориентированный связный граф. Вершины пронумерованы от 0. Требуется с помощью обхода в ширину
построить остовное дерево.

Формат входных данных
На вход программе в первой строке подаются через пробел два числа: n (2 <= n <= 1000) — число вершин в графе и
 m (1 <= m <= 20000) — число рёбер. В следующих m строках задаются ребра: по два числа в каждой строке —
номера соединённых вершин.

Формат выходных данных
Требуется распечатать n-1 пару чисел, каждyю на новой строке. Каждая пара задаёт ребро в остовном дереве.
"""
from collections import deque

vertexes, edges = map(int, input().split())
graph = {x: set() for x in range(vertexes)}
for _ in range(edges):
    x1, x2 = map(int, input().split())
    graph[x1].add(x2)
    graph[x2].add(x1)

distances = [None] * vertexes
parents = {x: set() for x in range(vertexes)}
start_x = max(graph.keys(), key=lambda k: len(graph[k]))
distances[start_x] = 0
queue = deque([start_x])

while queue:
    cur_x = queue.popleft()
    for neighbour_x in graph[cur_x]:
        if distances[neighbour_x] is None:
            distances[neighbour_x] = distances[cur_x] + 1
            parents[neighbour_x].add(cur_x)
            queue.append(neighbour_x)

for par in parents:
    if parents[par]:
        for child in parents[par]:
            print(child, par)
