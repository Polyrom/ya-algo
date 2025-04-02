"""
На IT-конференции присутствовали студенты из разных вузов со всей страны.
Для каждого студента известен ID университета, в котором он учится.
Тимофей предложил Рите выяснить, из каких k вузов на конференцию пришло больше всего учащихся.

Формат ввода

В первой строке дано количество студентов в списке —– n (1 ≤ n ≤ 15 000).
Во второй строке через пробел записаны n целых чисел —– ID вуза каждого студента.
Каждое из чисел находится в диапазоне от 0 до 10 000.
В третьей строке записано одно число k.
"""

import os
from dataclasses import dataclass
from collections import Counter

ENVIRONMENT = "ENVIRONMENT"
TEST = "TEST"


def solution(students: list[int], show_num: int) -> list[int]:
    cnt = Counter(students)
    res = sorted(cnt.items(), key=lambda item: (-item[1], item[0]))
    return [uni for uni, _ in res[:show_num]]



@dataclass
class TestData:
    students: list[int]
    show_num: int
    expected: list[int]


def test():
    tds = [
        TestData([1, 2, 3, 1, 2, 3, 4], 3, [1, 2, 3]),
    ]
    for td in tds:
        result = solution(td.students, td.show_num)
        assert result == td.expected, f"expected {td.expected}, got {result}, input {td.show_num} {td.students}"


def read_input() -> tuple[list[int], int]:
    _ = input()
    students = list(map(int, (input().strip().split())))
    n = int(input())
    return students, n


if __name__ == "__main__":
    environment = os.environ.get(ENVIRONMENT)
    if environment and environment.upper() == TEST:
        test()
    else:
        result = solution(*read_input())
        print(" ".join(map(str, result)))
