"""
Неориентированный граф называется регулярным, если все его вершины имеют одинаковую степень.
Для заданного списком ребер графа проверьте, является ли он регулярным.

Формат входных данных
Сначала вводятся числа n ( 1 ≤ n ≤ 100) – количество вершин в графе и m ( 0 ≤ m ≤ n(n - 1)/2) – количество ребер.
Затем следует m пар чисел – ребра графа. Нумерация вершин с 0.

Формат выходных данных
Выведите «YES», если граф является регулярным, и «NO» в противном случае.
"""
vertexes, edges = map(int, input().split())
# vertexes, edges = int(vertexes), int(edges)
# for i in range(edges)
gr = [ [] for x in range(vertexes)]

for i in range(edges):
    x1, x2 = map(int, input().split())
    gr.append(x1)
    gr.append(x2)

pa = gr.count(0)

for v in range(vertexes):
    st = gr.count(v)
    if pa != st:
        break

if pa == st:
    print("YES")
else:
    print("NO")
