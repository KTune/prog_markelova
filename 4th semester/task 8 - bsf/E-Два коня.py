"""
На стандартной шахматной доске (8х8) живут 2 шахматных коня: Красный и Зеленый. Обычно они беззаботно скачут по
просторам доски, пощипывая шахматную травку, но сегодня особенный день: у Зеленого коня День Рождения.
Зеленый конь решил отпраздновать это событие вместе с Красным. Но для осуществления этого прекрасного плана им нужно
оказаться на одной клетке. Заметим, что Красный и Зеленый шахматные кони сильно отличаются от черного с белым: они
ходят не по очереди, а одновременно,и если оказываются на одной клетке, никто никого не съедает. Сколько ходов им
потребуется, чтобы насладиться праздником?

Формат входных данных
На вход программы поступают координаты коней, записанные по стандартным шахматным правилам (т.е. двумя символами -
маленькая латинская буква (от a до h) и цифра (от 1 до 8), задающие столбец и строку соответственно).

Формат выходных данных
Требуется вывести наименьшее необходимое количество ходов, либо число -1, если кони не могут встретиться.
"""

from collections import deque

letters = 'abcdefgh'

numbers = '12345678'

graph = dict()

for l in letters:

    for n in numbers:
        graph[l + n] = set()


def add_edge(x1, x2):
    graph[x1].add(x2)

    graph[x2].add(x1)


for i in range(8):

    for j in range(8):

        x1 = letters[i] + numbers[j]

        if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
            x2 = letters[i + 2] + numbers[j + 1]

            add_edge(x1, x2)

        if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
            x2 = letters[i - 2] + numbers[j + 1]

            add_edge(x1, x2)

        if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
            x2 = letters[i + 1] + numbers[j + 2]

            add_edge(x1, x2)

        if 0 <= i - 1 < 8 and 0 <= j + 2 < 8:
            x2 = letters[i - 1] + numbers[j + 2]

            add_edge(x1, x2)

red, green = input().split()

distances_red = {x: None for x in graph}

distances_red[red] = 0

distances_green = {x: None for x in graph}

distances_green[green] = 0

queue_red = deque([red])

queue_green = deque([green])


def bfs(start_x, queue, distances):
    while queue:

        cur_x = queue.popleft()

        for neighbour_x in graph[cur_x]:

            if distances[neighbour_x] is None:
                distances[neighbour_x] = distances[cur_x] + 1

                queue.append(neighbour_x)


bfs(red, queue_red, distances_red)

bfs(green, queue_green, distances_green)

min_dist = []

for vertex in graph:

    if distances_green[vertex] == distances_red[vertex]:
        min_dist.append(distances_green[vertex])

if min_dist:

    print(min(min_dist))

else:

    print(-1)
