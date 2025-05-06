def eratosthenes(n: int) -> list[int | bool]:
    "Memory: O(n log(log n))"
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for i in range(2, n):
        if numbers[i]:
            for j in range(i * i, n + 1, i):
                numbers[j] = False
    return numbers


if __name__ == "__main__":
    print(eratosthenes(25))
