
def is_loop(graph):
    def dfs_stack(vertex, graph, stack, color):
        color[vertex] = 1
        for neighbour in graph[vertex]:
            if color[neighbour] == 0:
                stack[neighbour] = vertex
                if dfs_stack(neighbour, graph, stack, color):
                    return True
            elif color[neighbour] == 1:
                loop.append(neighbour)
                loop.append(vertex)
                return True
        color[vertex] = 2
        return False

    stack = [-1] * order
    color = [0] * order
    loop = []

    for vertex in graph:
        if dfs_stack(vertex, graph, stack, color):
            break

    cycle = []
    if loop:
        return True
    else:
        return False


def dfs_topological(vertex, graph, used, ans):
    used.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs_topological(neighbour, graph, used, ans)
    ans.append(vertex)


order, size = map(int, input().split())

graph = {v: set() for v in range(order)}

for _ in range(size):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)

if is_loop(graph):
    print('NO')
    exit(0)

used = set()
ans = []

for vertex in graph:
    if vertex not in used:
        dfs_topological(vertex, graph, used, ans)
print(*ans[::-1])
