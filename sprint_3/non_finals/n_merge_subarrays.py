"""
Алла захотела, чтобы у неё под окном были узкие клумбы с тюльпанам.
На схеме земельного участка клумбы обозначаются просто горизонтальными отрезками, лежащими на одной прямой.
Для ландшафтных работ было нанято n садовников. Каждый из них обрабатывал какой-то отрезок на схеме.
Процесс был организован не очень хорошо, иногда один и тот же отрезок или его часть могли быть обработаны
сразу несколькими садовниками.

Таким образом, отрезки, обрабатываемые двумя разными садовниками, сливаются в один.
Непрерывный обработанный отрезок затем станет клумбой. Нужно определить границы будущих клумб.

Рассмотрим примеры.
Пример 1:
Даны 4 отрезка: [7, 8], [7, 8], [2, 3], [6, 10].
Два одинаковых отрезка [7, 8] и [7, 8] сливаются в один, но потом их накрывает отрезок [6, 10].
Таким образом, имеем две клумбы с координатами [2, 3] и [6, 10].
"""

import os
from dataclasses import dataclass

ENVIRONMENT = "ENVIRONMENT"
TEST = "TEST"


def solution(nums: list[list[int]]) -> list[list[int]]:
    if len(nums) <= 1:
        return nums
    nums.sort(key=lambda x: x[0])
    result = [nums[0]]
    for n in nums[1:]:
        last = result[-1]
        if n[0] <= last[1]:
            last[1] = max(last[1], n[1])
        else:
            result.append(n)
    return result


@dataclass
class TestData:
    nums: list[list[int]]
    expected: list[list[int]]


def test():
    tds = [
        TestData(
            [[7, 8], [7, 8], [2, 3], [6, 10]],
            [[2, 3], [6, 10]],
        ),
        TestData(
            [[2, 3], [5, 6], [3, 4], [3, 4]],
            [[2, 4], [5, 6]],
        ),
    ]
    for td in tds:
        result = solution(td.nums)
        assert result == td.expected, f"expected {td.expected}, got {result}, input {td.nums}"


def read_input() -> list[list[int]]:
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, (input().strip().split()))))
    return data


if __name__ == "__main__":
    environment = os.environ.get(ENVIRONMENT)
    if environment and environment.upper() == TEST:
        test()
    else:
        result = solution(read_input())
        for n in result:
            print(n[0], n[1])
