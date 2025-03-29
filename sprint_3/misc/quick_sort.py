"""
Quick sort.
Time: O(n log n)* (worst case O(n**2)). Space: O(n)
"""

import random
from dataclasses import dataclass


def partition(array: list[int], pivot: int) -> tuple[list[int], list[int], list[int]]:
    left = [x for x in array if x < pivot]
    right = [x for x in array if x > pivot]
    mid = [x for x in array if x == pivot]
    return left, mid, right


def quick_sort(array: list[int]) -> list[int]:
    if len(array) < 2:
        return array
    pivot = random.choice(array)
    left, mid, right = partition(array, pivot)
    return quick_sort(left) + mid + quick_sort(right)


@dataclass
class TestData:
    arr: list[int]
    expected: list[int]


def test():
    tds = [
        TestData([], []),
        TestData([-1, -4, 0, -2], [-4, -2, -1, 0]),
        TestData([89, 4, 11, -8, 14], [-8, 4, 11, 14, 89]),
        TestData([4, 89, 11, -8, 14, -22, -8, 0], [-22, -8, -8, 0, 4, 11, 14, 89]),
    ]
    for td in tds:
        got = quick_sort(td.arr)
        assert got == td.expected, f"expected {td.expected}, got {got}, input {td.arr}"


if __name__ == "__main__":
    test()
