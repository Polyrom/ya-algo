"""
Вечером ребята решили поиграть в игру «Большое число».
Даны числа. Нужно определить, какое самое большое число можно из них составить.

В первой строке записано n — количество чисел. Оно не превосходит 100.
Во второй строке через пробел записаны n неотрицательных чисел, каждое из которых не превосходит 1000.

Нужно вывести самое большое число, которое можно составить из данных чисел.
"""

import os
from dataclasses import dataclass

ENVIRONMENT = "ENVIRONMENT"
TEST = "TEST"

MAX_LEN = 1000


def sort_key(n: str):
    return tuple(int(x) for x in n) + (float("inf"),) * (MAX_LEN - len(n))


# 6 68 6 should be 68 6 6


def solution(nums: list[str]) -> str:
    nums.sort(key=sort_key, reverse=True)
    print(nums)
    return "".join(nums)


@dataclass
class TestData:
    nums: list[str]
    expected: str


def test():
    tds = [
        # TestData(["15", "56", "2"], "56215"),
        # TestData(["1", "783", "2"], "78321"),
        # TestData(["2", "4", "5", "2", "10"], "542210"),
        # TestData(["4", "3", "42"], "4423"),
        # TestData(["9", "10", "1", "1", "1", "6"], "9611110"),
        TestData(
            [
                "9",
                "6",
                "43",
                "81",
                "66",
                "69",
                "15",
                "33",
                "6",
                "53",
                "93",
                "64",
                "33",
                "88",
                "39",
                "34",
                "57",
                "23",
                "42",
                "44",
                "79",
                "25",
            ],
            "99388817969666664575344434239343333252315",
        ),
    ]
    for td in tds:
        result = solution(td.nums)
        assert result == td.expected, f"expected {td.expected}, got {result}, input: {td.nums}"


def read_input() -> list[str]:
    _ = input()
    return input().strip().split()


if __name__ == "__main__":
    environment = os.environ.get(ENVIRONMENT)
    if environment and environment.upper() == TEST:
        test()
    else:
        print(solution(read_input()))
