"""
Merge sort.
Time: O(n log n). Space: O(n)
"""

from dataclasses import dataclass


def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    left = merge_sort(arr[0 : len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2 : len(arr)])
    result = [0] * len(arr)
    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    while l < len(left):
        result[k] = left[l]
        l += 1
        k += 1
    while r < len(right):
        result[k] = right[r]
        r += 1
        k += 1

    return result


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
        got = merge_sort(td.arr)
        assert got == td.expected, f"expected {td.expected}, got {got}, input {td.arr}"


if __name__ == "__main__":
    test()
