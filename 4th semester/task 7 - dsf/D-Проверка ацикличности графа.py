
por, razmer = map(int, input().split())

graph = {z: set() for z in range(por)}

for _ in range(razmer):
    z1, z2 = map(int, input().split())
    graph[z1].add(z2)


def dfs_stack(vertex, graph, stack, colour):
    colour[vertex] = 1
    for neighbour in graph[vertex]:
        if colour[neighbour] == 0:
            stack[neighbour] = vertex
            if dfs_stack(neighbour, graph, stack, colour):
                return True
        elif colour[neighbour] == 1:
            loop.append(neighbour)
            loop.append(vertex)
            return True
    colour[vertex] = 2
    return False


stack = [-1] * por
colour = [0] * por
loop = []

for vertex in graph:
    if dfs_stack(vertex, graph, stack, colour):
        break

cycle = []
if loop:
    current = loop[1]
    while current != loop[0]:
        cycle.append(current)
        current = stack[current]
    cycle.append(loop[0])
    cycle.reverse()
    print(*cycle)
else:
    print('YES')
