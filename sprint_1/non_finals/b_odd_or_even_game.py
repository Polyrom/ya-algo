def is_even(x: int) -> bool:
    return x % 2 == 0


def check_parity(a: int, b: int, c: int) -> bool:
    winning_parity = is_even(a)
    return all(is_even(val) == winning_parity for val in (b, c))


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
