"""
По заданной квадратной матрице n×n из нулей и единиц определите, может ли данная матрица быть матрицей смежности
простого неориентированного графа.

Формат входных данных
На вход программы поступает число n ( 1 <= n <= 100) – размер матрицы, а затем n строк по n чисел, каждое из которых
равно 0 или 1, – сама матрица.

Формат выходных данных
Выведите «YES», если приведенная матрица может быть матрицей смежности простого неориентированного графа,
и «NO» в противном случае.
"""
n = int(input())

matrix = [[] for _ in range(n)]
for i in range(n):
    matrix[i] = list(map(int, input().split()))

has_loop = True
for i in range(n):
    for j in range(n):
        if i == j and matrix[i][j] != 0:
            has_loop = False
            break
        elif matrix[i][j] != matrix[j][i]:
            has_loop = False
            break
if has_loop:
    print('YES')
else:
    print('NO')
