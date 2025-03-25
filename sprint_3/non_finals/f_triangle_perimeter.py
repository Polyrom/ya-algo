"""
Перед сном Рита решила поиграть в игру на телефоне.
Дан массив целых чисел, в котором каждый элемент обозначает длину стороны треугольника.
Нужно определить максимально возможный периметр треугольника, составленного из сторон с длинами из заданного массива.
Помогите Рите скорее закончить игру и пойти спать.

Напомним, что из трёх отрезков с длинами a ≤ b ≤ c можно составить треугольник,
если выполнено неравенство треугольника: c < a + b

Разберём пример:
даны длины сторон 6, 3, 3, 2. Попробуем в качестве наибольшей стороны выбрать 6.
Неравенство треугольника не может выполниться, так как остались 3, 3, 2 —– максимальная сумма из них равна 6.

Без шестёрки оставшиеся три отрезка уже образуют треугольник со сторонами 3, 3, 2.
Неравенство выполняется: 3 < 3 + 2. Периметр равен 3 + 3 + 2 = 8.

Нужно вывести одно число —– наибольший периметр треугольника.
Гарантируется, что тройка чисел, которая может образовать треугольник, всегда есть.
"""

import os
from dataclasses import dataclass

ENVIRONMENT = "ENVIRONMENT"
TEST = "TEST"


def solution(sides: list[int]) -> int:
    sides.sort(reverse=True)
    for i in range(len(sides) - 2):
        if sides[i] < sides[i + 1] + sides[i + 2]:
            return sides[i] + sides[i + 1] + sides[i + 2]
    return -1


@dataclass
class TestData:
    sides: list[int]
    expected: int


def test():
    tds = [
        TestData([6, 3, 3, 2], 8),
        TestData([5, 3, 7, 2, 8, 3], 20),
    ]
    for td in tds:
        result = solution(td.sides)
        assert result == td.expected, f"expected {td.expected}, got {result}, inputs: {td.sides}"


def read_input() -> list[int]:
    _ = input()
    return list(map(int, input().strip().split()))


if __name__ == "__main__":
    environment = os.environ.get(ENVIRONMENT)
    if environment == TEST:
        test()
    else:
        sides = read_input()
        print(solution(sides))
