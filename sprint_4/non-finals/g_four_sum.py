"""
У Гоши есть любимое число S. Помогите ему найти все уникальные четвёрки чисел в массиве,
которые в сумме дают заданное число S.

Формат ввода
В первой строке дано общее количество элементов массива (0<=n<=1000).
Во второй строке дано целое число S|S|<=10^9.
В третьей строке задан сам массив. Каждое число является целым и не превосходит по модулю 10^10.

Формат вывода
В первой строке выведите количество найденных четвёрок чисел.
В последующих строках выведите найденные четвёрки. Числа внутри одной четверки должны быть упорядочены по возрастанию.
Между собой четвёрки упорядочены лексикографически. Выводить только уникальные четвёрки.
"""

import os
from dataclasses import dataclass
from collections import defaultdict

ENVIRONMENT = "ENVIRONMENT"
TEST = "TEST"

Four = tuple[int, int, int, int]


def solution(target: int, array: list[int]) -> list[Four]:
    array.sort()
    n = len(array)
    pairs = defaultdict(list)
    fours = set()
    for i in range(n):
        for j in range(i + 1, n):
            pairs[array[i] + array[j]].append((i, j))
    for k in range(n):
        for v in range(k + 1, n):
            diff = target - (array[k] + array[v])
            if diff in pairs:
                for i, j in pairs[diff]:
                    if k != i and k != j and v != i and v != j:
                        fours.add(tuple(sorted([array[i], array[j], array[k], array[v]])))
    return sorted(fours)


@dataclass
class TestData:
    target: int
    array: list[int]
    expected: list[Four]


def test():
    tds = [
        TestData(10, [2, 3, 2, 4, 1, 10, 3, 0], [(0, 3, 3, 4), (1, 2, 3, 4), (2, 2, 3, 3)]),
        TestData(0, [1, 0, -1, 0, 2, -2], [(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)]),
    ]
    for td in tds:
        result = solution(td.target, td.array)
        assert result == td.expected, f"expected={td.expected}, got={result}, input=(t={td.target} a={td.array})"


def read_input() -> tuple[int, list[int]]:
    _ = input()
    target = int(input())
    array = list(map(int, input().strip().split()))
    return target, array


if __name__ == "__main__":
    environment = os.environ.get(ENVIRONMENT)
    if environment and environment.upper() == TEST:
        test()
    else:
        result = solution(*read_input())
        print(len(result))
        for four in result:
            print(" ".join(list(map(str, four))))
