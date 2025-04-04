"""
Алле очень понравился алгоритм вычисления полиномиального хеша. Помогите ей написать функцию, вычисляющую хеш строки s.
В данной задаче необходимо использовать в качестве значений отдельных символов их коды в таблице ASCII.
Формат ввода

В первой строке дано число a (1 <= a <= 1000) –— основание, по которому считается хеш.
Во второй строке дано число m (1 <= m <= 10^9) -- модуль.
В третьей строке дана строка s (0 <= |s| <= 10^6), состоящая из больших и маленьких латинских букв.

Формат вывода

Выведите целое неотрицательное число –— хеш заданной строки.
"""

import os
from dataclasses import dataclass
from functools import reduce

ENVIRONMENT = "ENVIRONMENT"
TEST = "TEST"


def solution_non_horner(a: int, m: int, s: str) -> int:
    """Non-Horner approach."""
    acc = reduce(lambda x, iv: x + (ord(iv[1]) * (a ** ((len(s) - 1) - iv[0]))), enumerate(s), 0)
    return acc % m


def solution(a: int, m: int, s: str) -> int:
    """Horner approach."""
    return reduce(lambda acc, char: (acc * a + ord(char)) % m, s, 0)


@dataclass
class TestData:
    a: int
    m: int
    s: str
    expected: int


def test():
    tds = [
        TestData(123, 100003, "a", 97),
        TestData(123, 100003, "hash", 6080),
        TestData(123, 100003, "HaSH", 56156),
    ]
    for td in tds:
        result = solution(td.a, td.m, td.s)
        assert result == td.expected, f"expected={td.expected}, got={result}, input=(a={td.a} m={td.m}, s={td.s})"


def read_input() -> tuple[int, int, str]:
    a = int(input())
    m = int(input())
    s = input()
    return a, m, s


if __name__ == "__main__":
    environment = os.environ.get(ENVIRONMENT)
    if environment and environment.upper() == TEST:
        test()
    else:
        a, m, s = read_input()
        print(solution(a, m, s))
