"""
Рита решила оставить у себя одежду только трёх цветов: розового, жёлтого и малинового.
После того как вещи других расцветок были убраны, Рита захотела отсортировать свой новый гардероб по цветам.
Сначала должны идти вещи розового цвета, потом —– жёлтого, и в конце —– малинового.
Помогите Рите справиться с этой задачей.

Примечание: попробуйте решить задачу за один проход по массиву!

В первой строке задано количество предметов в гардеробе: n –— оно не превосходит 1000000.
Во второй строке даётся массив, в котором указан цвет для каждого предмета.
Розовый цвет обозначен 0, жёлтый —– 1, малиновый –— 2.
"""

import os
import random
from enum import Enum
from dataclasses import dataclass


ENVIRONMENT = "ENVIRONMENT"
TEST = "TEST"


class Colors(int, Enum):
    ROSE = 0
    YELLOW = 1
    PURPLE = 2


def solution(nums: list[int]) -> list[int]:
    result = []
    colors_cnt = [0] * len(Colors)
    for n in nums:
        colors_cnt[n] += 1
    for i in range(len(colors_cnt)):
        result.extend([i] * colors_cnt[i])
    return result


@dataclass
class TestData:
    nums: list[int]
    expected: list[int]


def test():
    tds = [
        TestData([0, 2, 1, 2, 0, 0, 1], [0, 0, 0, 1, 1, 2, 2]),
    ]
    for td in tds:
        result = solution(td.nums)
        assert result == td.expected, f"expected {td.expected}, got {result}, input: {td.nums}"


def read_input() -> list[int]:
    _ = input()
    return list(map(int, input().strip().split()))


if __name__ == "__main__":
    environment = os.environ.get(ENVIRONMENT)
    if environment and environment.upper() == TEST:
        test()
    else:
        print(" ".join(list(map(str, solution(read_input())))))
