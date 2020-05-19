
pord = int(input())
razmer = int(input())

graph_normal = {x: set() for x in range(pord)}
graph_reversed = {x: set() for x in range(pord)}

for i in range(razmer):
    x1, x2 = map(int, input().split())
    graph_normal[x1].add(x2)
    graph_reversed[x2].add(x1)


def dfs(vertex, graph, used):
    used.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs(neighbour, graph, used)


used = set()
used_inv = set()
dfs(0, graph_normal, used)
dfs(0, graph_reversed, used_inv)

if (used == set(graph_normal.keys())
        and
        used_inv == set(graph_reversed.keys())
):
    print('YES')
else:
    print('NO')
    