def fibo(n: int, k: int) -> int:
    if n <= 1:
        return 1
    tmp = [0] * (n + 1)
    tmp[0] = 1
    tmp[1] = 1
    for i in range(2, n + 1):
        tmp[i] = (fibo(i - 2, k) + fibo(i - 1, k)) % (10**k)
    return tmp[n]


def read_input() -> tuple[int, int]:
    inp = input()
    return tuple(map(int, inp.strip().split()))


if __name__ == "__main__":
    n, k = read_input()
    print(fibo(n, k))
