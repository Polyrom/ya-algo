# https://contest.yandex.ru/contest/22450/run-report/134089635/

from collections import defaultdict
from typing import List, Tuple

ROW_LEN = 4
DOT = "."


def get_max_points(k: int, field: List[str]) -> int:
    result = 0

    m = defaultdict(int)
    for i in range(ROW_LEN):
        for j in range(ROW_LEN):
            val = field[i][j]
            if val != DOT:
                m[field[i][j]] += 1

    max_taps = k * 2
    for v in m.values():
        if v <= max_taps:
            result += 1
    return result


def read_input() -> Tuple[int, List[str]]:
    k = int(input())
    field = []
    for i in range(4):
        field.append(input().strip())
    return k, field


k, field = read_input()
print(get_max_points(k, field))
