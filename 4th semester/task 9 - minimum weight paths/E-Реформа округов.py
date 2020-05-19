"""
Правитель графландии решил провести реформу административных округов в своём государстве. Ему хочется, чтобы расстояние
от города до главного города его округа не превышало расстояния от данного города до главных городов других округов.
Главные города правитель уже выбрал, вам остаётся всего лишь разбить остальные города по округам. Если есть несколько
вариантов расстановки - подойдет любой. Если не справитесь, вам отрубят голову.

Формат входных данных
На вход программе в первой строке подается несколько (не менее трёх) чисел через пробел: n , m , a1 , a2 ,..

2 ≤ n ≤ 1000 - число городов
1 ≤ m ≤ 100000 - число дорог
ai - номера главных городов
В следующих m строках задаются дороги, по три числа в каждой строке - номера соединенных городов и длина дороги.
Города нумеруются с нуля.

Формат выходных данных
Для каждого города в отдельной строке выведите главный город его округа. Для 0го города - в первой строке, для 1го -
во второй,.. Если для данного города не достижим ни один из главных - выведите в соответствующей строке -1.
"""


def sift_up(heap,i):
    while i > 0 and d[heap[(i-1)//2]] > d[heap[i]]:
        v2h[heap[i]], v2h[heap[(i-1)//2]] = (i-1)//2, i
        heap[i], heap[(i-1)//2] = heap[(i-1)//2], heap[i]
        i = (i - 1) // 2


def sift_down(heap,i):
    n = len(heap)
    while i*2 + 1<n:
        j = i
        if (d[heap[i]] > d[heap[i * 2 + 1]]):
            j = i * 2 + 1
        if i * 2 + 2 < n and d[heap[j]] > d[heap[i * 2 + 2]]:
            j = i * 2 + 2
        if i == j:
            break
        v2h[heap[i]], v2h[heap[j]] = j, i
        heap[i], heap[j] = heap[j], heap[i]
        i = j


def extract_min(heap):
    x = heap[0]
    heap[0] = heap.pop()
    v2h[heap[0]] = 0
    sift_down(heap,0)
    return x


c = list(map(int,input().split()))
n = c.pop(0)
m = c.pop(0)
g = [[] for i in range(n)]
for edge in range(m):
    u, v, val = map(int, input().split())
    g[u].append((v, val))
    g[v].append((u, val))
d = [float("inf")]*n
result = [-1]*n
for i in range(len(c)):
    d[c[i]] = 0
    result[c[i]] = c[i]
heap = [i for i in c] + [i for i in range(n) if i not in c]
v2h = [0]*n
for i, j in enumerate(heap):
    v2h[j] = i
while heap:
    if len(heap) > 1:
        u = extract_min(heap)
    else:
        u = heap.pop()
    if d[u] == float("inf"):
        break
    for v, w in g[u]:
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            sift_up(heap, v2h[v])
            result[v] = result[u]
for i in range(len(result)):
    print(result[i])
