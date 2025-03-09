def eratosthenes(n: int) -> list[int | bool]:
    "Memory: O(n log(log n))"
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for i in range(2, n):
        if numbers[i]:
            for j in range(i * i, n + 1, i):
                numbers[j] = False
    return numbers


def get_least_prime_linear(n: int) -> tuple(list[int], list[int]):
    return 0


if __name__ == "__main__":
    print(eratosthenes(25))
    print(get_least_prime_linear(25))
