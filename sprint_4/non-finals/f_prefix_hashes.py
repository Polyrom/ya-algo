"""
Алла не остановилась на достигнутом –— теперь она хочет научиться быстро вычислять хеши произвольных подстрок данной
строки. Помогите ей!
На вход поступают запросы на подсчёт хешей разных подстрок. Ответ на каждый запрос должен выполняться за O(1).
Допустимо в начале работы программы сделать предподсчёт для дальнейшей работы со строкой.
В данной задаче необходимо использовать в качестве значений отдельных символов их коды в таблице ASCII.

Формат ввода

В первой строке дано число a (1 <= a <= 1000) –— основание, по которому считается хеш.
Во второй строке дано число m (1 <= m <= 10^7) -- модуль.
В третьей строке дана строка s (0 <= |s| <= 10^6), состоящая из больших и маленьких латинских букв.
В четвертой строке дано число запросов t –— натуральное число от 1 до 10^5.
В каждой из следующих t строк записаны через пробел два числа l и r –— индексы начала и конца очередной подстроки
(1 <= l <= r <= |s|).

Формат вывода

Для каждого запроса выведите на отдельной строке хеш заданной в запросе подстроки.
"""

from collections import namedtuple
import os
from dataclasses import dataclass

ENVIRONMENT = "ENVIRONMENT"
TEST = "TEST"

Range = namedtuple("Range", "left, right")


def solution(a: int, m: int, s: str, ranges: list[Range]) -> list[int]:
    prefix_hashes = [0] * (len(s) + 1)
    powers = [1] * (len(s) + 1)
    for i in range(1, len(s) + 1):
        prefix_hashes[i] = (prefix_hashes[i - 1] * a + ord(s[i - 1])) % m
        powers[i] = (powers[i - 1] * a) % m

    return [(prefix_hashes[right] - prefix_hashes[left - 1] * powers[right - (left - 1)]) % m for left, right in ranges]


@dataclass
class TestData:
    a: int
    m: int
    s: str
    ranges: list[Range]
    expected: list[int]


def test():
    tds = [
        TestData(100, 10, "a", [Range(1, 1)], [7]),
        TestData(
            1000,
            1000009,
            "abcdefgh",
            [
                Range(1, 1),
                Range(1, 5),
                Range(2, 3),
                Range(3, 4),
                Range(4, 4),
                Range(1, 8),
                Range(5, 8),
            ],
            [
                97,
                225076,
                98099,
                99100,
                100,
                436420,
                193195,
            ],
        ),
    ]
    for td in tds:
        result = solution(td.a, td.m, td.s, td.ranges)
        args = f"input=(a={td.a} m={td.m}, s={td.s} ranges={td.ranges})"
        assert result == td.expected, f"expected={td.expected}, got={result}, {args}"
        print(f"test for params {args} passed!")


def read_input() -> tuple[int, int, str, list[Range]]:
    a = int(input())
    m = int(input())
    s = input()
    n = int(input())
    ranges = []
    for _ in range(n):
        pair = tuple(map(int, input().strip().split()))
        ranges.append(Range(left=pair[0], right=pair[1]))
    return a, m, s, ranges


if __name__ == "__main__":
    environment = os.environ.get(ENVIRONMENT)
    if environment and environment.upper() == TEST:
        test()
    else:
        a, m, s, ranges = read_input()
        res = solution(a, m, s, ranges)
        for r in res:
            print(r)
