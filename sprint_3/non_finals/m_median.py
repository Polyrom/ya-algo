"""
Задача повышенной сложности

На каждом острове в архипелаге Алгосы живёт какое-то количество людей или же остров необитаем
(тогда на острове живёт 0 людей). Пусть на i-м острове численность населения составляет ai.
Тимофей захотел найти медиану среди всех значений численности населения.

Определение: Медиана массива чисел a_i —– это такое число, что половина чисел из массива не больше него,
а другая половина не меньше. В общем случае медиану массива можно найти, отсортировав числа и взяв среднее из них.
Если количество чисел чётно, то возьмём в качестве медианы полусумму соседних средних чисел,
(a[n/2] + a[n/2 + 1])/2.

У Тимофея уже есть отдельно данные по северной части архипелага и по южной, причём значения
численности населения в каждой группе отсортированы по неубыванию.

Определите медианную численность населения по всем островам Алгосов.

Формат ввода

В первой строке записано натуральное число n, во второй —– натуральное число m. Они не превосходят 10 000.

Далее в строку через пробел записаны n целых неотрицательных чисел, каждое из которых не превосходит 10 000,
–— значения численности населения в северной части Алгосов.

В последней строке через пробел записаны m целых неотрицательных чисел, каждое из которых не превосходит 10 000
–— значения численности населения в южной части Алгосов.

Значения в третьей и четвёртой строках упорядочены по неубыванию.
"""

import os
from dataclasses import dataclass

ENVIRONMENT = "ENVIRONMENT"
TEST = "TEST"


def solution(north: list[int], south: list[int]) -> float:
    if len(north) > len(south):
        north, south = south, north

    m, n = len(north), len(south)
    total = m + n
    half = (total + 1) // 2

    left, right = 0, m

    while left <= right:
        i = (left + right) // 2
        j = half - i

        north_left = north[i - 1] if i > 0 else float("-inf")
        north_right = north[i] if i < m else float("inf")
        south_left = south[j - 1] if j > 0 else float("-inf")
        south_right = south[j] if j < n else float("inf")

        if north_left <= south_right and south_left <= north_right:
            if total % 2 == 0:
                return (max(north_left, south_left) + min(north_right, south_right)) / 2
            return max(north_left, south_left)
        if north_left > south_right:
            right = i - 1
        else:
            left = i + 1

    return -1


@dataclass
class TestData:
    north: list[int]
    south: list[int]
    expected: float


def test():
    tds = [
        TestData([1, 3], [2], 2),
        TestData([1, 2], [3, 4], 2.5),
        TestData([0, 0, 0, 1, 3, 3, 5, 10], [4, 4, 5, 7, 7, 7, 8, 9, 9, 10], 5),
    ]
    for td in tds:
        result = solution(td.north, td.south)
        assert result == td.expected, f"expected {td.expected}, got {result}, input n: {td.north} s: {td.south}"


def read_input() -> tuple[list[int], list[int]]:
    _ = input()
    _ = input()
    north = list(map(int, (input().strip().split())))
    south = list(map(int, (input().strip().split())))
    return north, south


if __name__ == "__main__":
    environment = os.environ.get(ENVIRONMENT)
    if environment and environment.upper() == TEST:
        test()
    else:
        print(solution(*read_input()))
