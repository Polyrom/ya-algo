"""
Insertion sort.
Time: O(n**2). Space: O(1)
"""

from copy import deepcopy
from dataclasses import dataclass


def selection_sort(arr: list[int]) -> None:
    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        j = i
        while j > 0 and item_to_insert < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = item_to_insert
        print(f"step {i}, sorted {i + 1} elements, array {arr}")


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
        original_arr = deepcopy(td.arr)
        selection_sort(td.arr)
        assert td.arr == td.expected, f"expected {td.expected}, got {td.arr}, input: {original_arr}"


if __name__ == "__main__":
    test()
