def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def factorial_iter(n: int) -> int:
    acc = 1
    while n > 1:
        acc *= n
        n -= 1
    return acc

