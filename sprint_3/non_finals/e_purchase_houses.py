"""
Тимофей решил купить несколько домов на знаменитом среди разработчиков Алгосском архипелаге.
Он нашёл n объявлений о продаже, где указана стоимость каждого дома в алгосских франках. А у Тимофея есть k франков.
Помогите ему определить, какое наибольшее количество домов на Алгосах он сможет приобрести за эти деньги.
"""

import os
from dataclasses import dataclass

ENVIRONMENT = "ENVIRONMENT"
TEST = "TEST"


def solution(budget: int, prices: list[int]) -> int:
    res = 0
    prices.sort()
    for p in prices:
        budget -= p
        if budget < 0:
            return res
        res += 1
    return res


@dataclass
class TestData:
    budget: int
    prices: list[int]
    expected: int


def test():
    tds = [
        TestData(300, [999, 999, 999], 0),
        TestData(1000, [350, 999, 200], 2),
    ]
    for td in tds:
        result = solution(td.budget, td.prices)
        assert result == td.expected, f"expected {td.expected}, got {result}, inputs: {td.budget} {td.prices}"


def read_input() -> tuple[int, list[int]]:
    _, budget = tuple(map(int, input().strip().split()))
    prices = list(map(int, input().strip().split()))
    return budget, prices


if __name__ == "__main__":
    environment = os.environ.get(ENVIRONMENT)
    if environment == TEST:
        test()
    else:
        budget, prices = read_input()
        print(solution(budget, prices))
