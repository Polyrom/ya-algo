"""
Теперь черепашке Кондратине надо узнать не только, сколько цветочков она может собрать, но и как ей построить свой
маршрут для этого. Помогите ей!
Напомним, что Кондратине надо дойти от левого нижнего до правого верхнего угла,
а передвигаться она умеет только вверх и вправо.

Формат ввода
В первой строке даны размеры поля n и m (через пробел). Оба числа лежат в диапазоне от 1 до 1000.
В следующих n строках задано поле. Каждая строка состоит из m символов 0 или 1 и завершается переводом строки.
Если в клетке записана единица, то в ней растет цветочек.

Формат вывода
Выведите в первой строке максимальное количество цветочков, которое сможет собрать Кондратина.
Во второй строке выведите маршрут в виде последовательности символов «U» и «R», где «U» означает передвижение вверх,
а «R» – передвижение вправо.
Если возможных оптимальных путей несколько, то выведите любой.
"""


class Direction:
    RIGHT = "R"
    UP = "U"


def solution(meadow: list[list[int]], rows: int, cols: int) -> tuple[int, list[str]]:
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

    # backtrack steps
    path = []
    i, j = 1, cols
    while not (i == rows and j == 1):
        if dp[i + 1][j] > dp[i][j - 1]:
            path.append(Direction.UP)
            i += 1
        else:
            path.append(Direction.RIGHT)
            j -= 1

    return dp[1][cols], path[::-1]


def read_input() -> tuple[list[list[int]], int, int]:
    rows, cols = tuple(map(int, input().strip().split()))
    meadow = []
    for _ in range(rows):
        meadow.append(list(map(int, list(input().strip()))))
    return meadow, rows, cols


if __name__ == "__main__":
    meadow, rows, cols = read_input()
    max_flowers, path = solution(meadow, rows, cols)
    print(max_flowers)
    print("".join(path))
