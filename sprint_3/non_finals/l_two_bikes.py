NOT_FOUND = -1


def bin_search_rec(target, arr: list[int], left: int, right: int, result=NOT_FOUND) -> int:
    if right < left:
        return result
    mid = (right + left) // 2
    if arr[mid] >= target:
        return bin_search_rec(target, arr, left, mid - 1, mid)
    return bin_search_rec(target, arr, mid + 1, right, result)


def solution(target: int, arr: list[int]) -> tuple[int, int]:
    one_bike = bin_search_rec(target, arr, 0, len(arr) - 1)
    two_bikes = bin_search_rec(target * 2, arr, 0, len(arr) - 1)
    return one_bike + 1 if one_bike != NOT_FOUND else one_bike, two_bikes + 1 if two_bikes != NOT_FOUND else two_bikes


def read_input() -> tuple[int, list[int]]:
    _ = input()
    vals = list(map(int, input().strip().split()))
    target = input()
    return int(target), vals


target, arr = read_input()
print(" ".join(list(map(str, solution(target, arr)))))
