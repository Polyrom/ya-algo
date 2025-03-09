from typing import List


def get_next_divider(num: int) -> int:
    for d in range(2, round((num**0.5)) + 1):
        q, r = divmod(num, d)
        if r == 0:
            return d
    return num


def factorize(number: int) -> List[int]:
    result = []
    while True:
        div = get_next_divider(number)
        result.append(div)
        if div == number:
            break
        number //= div

    return sorted(result)


result = factorize(int(input()))
print(" ".join(map(str, result)))
