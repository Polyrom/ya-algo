"""
Ребятам стало интересно, сколько может быть различных деревьев поиска, содержащих в своих узлах все уникальные
числа от 1 до n. Помогите им найти ответ на этот вопрос.

Формат ввода
В единственной строке задано число n. Оно не превосходит 15.

Формат вывода
Нужно вывести число, равное количеству различных деревьев поиска,
в узлах которых могут быть размещены числа от 1 до n включительно.
"""

import os
import math
from dataclasses import dataclass

ENVIRONMENT = "ENVIRONMENT"
TEST = "TEST"


def solution(n: int) -> int:
    """Catalan number Cn = (2n)! / (n+1)! * n!"""
    return math.comb(2*n, n) // (n + 1)


@dataclass
class TestData:
    num: int
    expected: int


def test():
    tds = [
        TestData(2, 2),
        TestData(3, 5),
        TestData(4, 14),
    ]
    for td in tds:
        result = solution(td.num)
        assert result == td.expected, f"expected {td.expected}, got {result}, input {td.num}"


if __name__ == "__main__":
    environment = os.environ.get(ENVIRONMENT)
    if environment and environment.upper() == TEST:
        test()
    else:
        print(solution(int(input())))
