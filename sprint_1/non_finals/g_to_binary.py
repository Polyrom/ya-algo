def to_binary(number: int) -> str:
    binary_digits = []
    while number > 0:
        quotinent, remainder = divmod(number, 2)
        binary_digits.append(str(remainder))
        number = quotinent
    return "".join(binary_digits[::-1]) if binary_digits else "0"


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
