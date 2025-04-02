"""
Жители Алгосов любят устраивать турниры по спортивному программированию. Все участники разбиваются на пары
и соревнуются друг с другом.

А потом два самых сильных программиста встречаются в финальной схватке, которая состоит из нескольких раундов.
Если в очередном раунде выигрывает первый участник, в таблицу с результатами записывается 0, если второй, то 1.
Ничьей в раунде быть не может.

Нужно определить наибольший по длине непрерывный отрезок раундов, по результатам которого суммарно получается
ничья. Например, если дана последовательность 0 0 1 0 1 1 1 0 0 0, то раунды с 2-го по 9-й
(нумерация начинается с единицы) дают ничью.
"""

import os
from dataclasses import dataclass

ENVIRONMENT = "ENVIRONMENT"
TEST = "TEST"


def solution(rounds: list[int]) -> int:
    balances_map = {0: -1}
    max_length = 0
    balance = 0
 
    for i, r in enumerate(rounds):
        balance += 1 if r == 0 else -1

        if balance in balances_map:
            segment = i - balances_map[balance]
            if segment > max_length:
                max_length = segment
        else:
            balances_map[balance] = i

    return max_length


@dataclass
class TestData:
    rounds: list[int]
    expected: int


def test():
    tds = [
        TestData([0, 1, 0], 2),
        TestData([0, 1], 2),
    ]
    for td in tds:
        result = solution(td.rounds)
        assert result == td.expected, f"expected {td.expected}, got {result}, input {td.rounds}"


def read_input() -> list[int]:
    _ = input()
    return list(map(int, (input().strip().split())))


if __name__ == "__main__":
    environment = os.environ.get(ENVIRONMENT)
    if environment and environment.upper() == TEST:
        test()
    else:
        print(solution(read_input()))
