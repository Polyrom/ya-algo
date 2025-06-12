"""
Prefix functions
"""

from dataclasses import dataclass

# Time: O(n^3)
def prefix_naive(s: str) -> list[int]:
    n = len(s)
    # Создадим массив π, состоящий из N нулей.
    π = [0] * n

    for i in range(1, n + 1):
        # i — длина подстроки-префикса.
        substring = s[0:i]
        # Проверяем, перекрывается ли подстрока substring с собой по k символам.
        for k in range(i - 1, 0, -1):
            # Для этого сравним префикс и суффикс соответствующих длин.
            prefix = substring[0:k]
            suffix = substring[i - k : i]
            if prefix == suffix:
                π[i - 1] = k  # Запишем значение π-функции.
                break  # Дальше не проверяем — k идёт в порядке уменьшения.
    return π


# DP approach
# Time: O(n)
def prefix(s: str) -> list[int]:
    # Функция возвращает массив длины |s|
    n = len(s)
    π = [-1] * n
    π[0] = 0
    for i in range(1, n):
        k = π[i - 1]
        while k > 0 and s[k] != s[i]:
            k = π[k - 1]
        if s[k] == s[i]:
            k += 1
        π[i] = k
    return π


@dataclass
class TestString:
    s: str
    expected: list[int]


if __name__ == "__main__":
    test_strings = [
        TestString(s="ahaha", expected=[0, 0, 1, 2, 3]),
        TestString(s="gogol", expected=[0, 0, 1, 2, 0]),
        TestString(s="bubble", expected=[0, 0, 1, 1, 0, 0]),
        TestString(s="freewill", expected=[0, 0, 0, 0, 0, 0, 0, 0]),
    ]
    for ts in test_strings:
        print(f'⚙️ Testing naive prefix function for string "{ts.s}"...')
        assert prefix_naive(ts.s) == ts.expected, f"actual={prefix_naive(ts.s)}, expected={ts.expected}"
        print(f'✅ Naive prefix function test for string "{ts.s}" passed!')
        print(f'⚙️ Testing DP prefix function for string "{ts.s}"...')
        assert prefix(ts.s) == ts.expected, f"actual={prefix_naive(ts.s)}, expected={ts.expected}"
        print(f'✅ DP prefix function test for string "{ts.s}" passed!\n')
    print("🏆 All tests passed!")
