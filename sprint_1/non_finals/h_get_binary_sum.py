from typing import Tuple


def decimal_to_binary(number: int) -> str:
    binary_digits = []
    while number > 0:
        quotinent, remainder = divmod(number, 2)
        binary_digits.append(str(remainder))
        number = quotinent
    return "".join(binary_digits[::-1]) if binary_digits else "0"


def binary_to_decimal(number: str) -> int:
    res = 0
    for i, d in enumerate(number[::-1]):
        res += int(d) * (2**i)
    return res


def get_sum(first_number: str, second_number: str) -> str:
    return decimal_to_binary(binary_to_decimal(first_number) + binary_to_decimal(second_number))


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
