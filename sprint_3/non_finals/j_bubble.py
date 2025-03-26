def solution(array: list[int]):
    cur_arr_str = ""
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        arr_str = " ".join(list(map(str, array)))
        if arr_str != cur_arr_str:
            print(arr_str)
        cur_arr_str = arr_str


def read_input() -> list[int]:
    _ = input()
    return list(map(int, input().strip().split()))


if __name__ == "__main__":
    array = read_input()
    solution(array)
