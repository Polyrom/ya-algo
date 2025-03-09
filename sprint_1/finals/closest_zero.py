# https://contest.yandex.ru/contest/22450/run-report/134044702/

from typing import List


def get_closest_zero(arr: List[int]) -> List[int]:
    result = [0] * len(arr)
    counter = 1
    prev_zero_index = -1
    for i in range(len(arr)):
        if arr[i] == 0:
            counter = 1
            mid = (i - prev_zero_index) // 2
            if prev_zero_index == -1 and i != 0:
                mid = i
            prev_zero_index = i
            for j in range(1, mid + 1):
                result[i - j] = j
        else:
            result[i] = counter
            counter += 1
    return result


def read_input() -> List[int]:
    _ = int(input())
    return list(map(int, input().strip().split()))


arr = read_input()
print(" ".join(map(str, get_closest_zero(arr))))
