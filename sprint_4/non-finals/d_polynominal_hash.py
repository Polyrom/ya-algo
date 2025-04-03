""" """

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
