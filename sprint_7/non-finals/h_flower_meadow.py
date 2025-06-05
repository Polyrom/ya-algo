"""
Черепаха Кондратина путешествует по клетчатому полю из n строк и m столбцов. В каждой клетке либо растёт цветочек,
либо не растёт. Кондратине надо добраться из левого нижнего в правый верхний угол и собрать как можно больше цветочков.
Помогите ей с этой сложной задачей и определите, какое наибольшее число цветочков она сможет собрать при условии,
что Кондратина умеет передвигаться только на одну клетку вверх или на одну клетку вправо за ход.

Формат ввода
В первой строке даны размеры поля n и m (через пробел). Оба числа лежат в диапазоне от 1 до 1000.
В следующих n строках задано поле. Каждая строка состоит из m символов 0 или 1, записанных подряд без пробелов,
и завершается переводом строки. Если в клетке записана единица, то в ней растёт цветочек.

Формат вывода
Выведите единственное число — максимальное количество цветочков, которое сможет собрать Кондратина.
"""


def print_matrix(m):
    for i in range(len(m)):
        print(" ".join(map(str, m[i])))
    print()


def solution(meadow: list[list[int]], rows: int, cols: int) -> int:
    # construct frame
    dp = [[0] * (cols + 2) for _ in range(rows + 2)]
    dp[rows][1] = meadow[rows - 1][0]
    for i in range(rows + 2):
        dp[i][0] = -1
        dp[i][cols + 1] = -1
    for j in range(cols + 2):
        dp[0][j] = -1
        dp[rows + 1][j] = -1

    # actual dp
    for i in range(rows, 0, -1):
        range_start = 1 if i != rows else 2
        for j in range(range_start, cols + 1):
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) + meadow[i - 1][j - 1]

    return dp[1][cols]


def read_input() -> tuple[list[list[int]], int, int]:
    rows, cols = tuple(map(int, input().strip().split()))
    meadow = []
    for _ in range(rows):
        meadow.append(list(map(int, list(input().strip()))))
    return meadow, rows, cols


if __name__ == "__main__":
    meadow, rows, cols = read_input()
    print(solution(meadow, rows, cols))
