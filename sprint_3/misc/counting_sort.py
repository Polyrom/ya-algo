"""
Counting sort.
Time: O(n). Space: O(n).
Suitable only for arrays with known elements range.
(This example is for arrays, whose elements <= 12).
"""

from dataclasses import dataclass


MONTHS_NUM = 12


def counting_sort(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr
    met_count = [0] * MONTHS_NUM
    result = []
    for n in arr:
        met_count[n - 1] += 1
    for i in range(len(met_count)):
        result.extend([i + 1] * met_count[i])
    return result


@dataclass
class TestData:
    arr: list[int]
    expected: list[int]


def test():
    tds = [
        TestData([], []),
        TestData([12, 8, 9, 6], [6, 8, 9, 12]),
        TestData([12, 11, 8, 11, 4, 2, 3, 3, 3, 3, 9, 1, 6], [1, 2, 3, 3, 3, 3, 4, 6, 8, 9, 11, 11, 12]),
    ]
    for td in tds:
        got = counting_sort(td.arr)
        assert got == td.expected, f"expected {td.expected}, got {got}, input: {td.arr}"


if __name__ == "__main__":
    test()
