
from collections import deque


order, size = map(int, input().split())

graph = {x : set() for x in range(order)}

for _ in range(size):

    x1, x2 = map(int, input().split())

    graph[x1].add(x2)


def bfs(start_x):

    if graph[start_x]:

        parents = [None] * order

        distances = [None] * order

        distances[start_x] = 0

        queue = deque([start_x])

        while queue:

            cur_x = queue.popleft()

            for neighbour_x in graph[cur_x]:

                if distances[neighbour_x] is None:

                    distances[neighbour_x] = distances[cur_x] + 1

                    parents[neighbour_x] = cur_x

                    queue.append(neighbour_x)

                elif neighbour_x == start_x:

                    path = [cur_x]

                    parent = parents[cur_x]

                    while not parent is None:

                        path.append(parent)

                        parent = parents[parent]

                    return path[::-1]

    return []


cycles = []

for start_x in graph:

    cycle = bfs(start_x)

    if cycle:

        cycles.append(cycle)


if not cycles:

    print('NO CYCLES')

    exit(0)

else:

    cycles.sort(key=len)

    print(*cycles[0])
