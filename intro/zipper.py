from typing import List, Tuple


def zipper(a: List[int], b: List[int]) -> List[int]:
    result = []
    for i in range(len(a)):
        result.append(a[i])
        result.append(b[i])
    return result


def prepare_output(output: List[int]) -> str:
    return " ".join(map(str, output))


def read_input() -> Tuple[List[int], List[int]]:
    _ = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b


a, b = read_input()
result = zipper(a, b)
output = prepare_output(result)
print(output)
