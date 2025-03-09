from typing import List, Tuple


def moving_average(arr: List[int], window_size: int) -> List[float]:
    result = []
    current_sum = sum(arr[:window_size])
    result.append(current_sum / window_size)
    for i in range(len(arr) - window_size):
        current_sum -= arr[i]
        current_sum += arr[i + window_size]
        result.append(current_sum / window_size)
    return result


def read_input() -> Tuple[List[int], int]:
    _ = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size


arr, window_size = read_input()
print(" ".join(map(str, moving_average(arr, window_size))))
