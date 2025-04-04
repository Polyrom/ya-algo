"""
Гоша написал программу, которая сравнивает строки исключительно по их хешам.
Если хеш равен, то и строки равны. Тимофей увидел это безобразие и поручил вам сломать программу Гоши,
чтобы остальным неповадно было.
В этой задаче вам надо будет лишь найти две различные строки, которые для заданной хеш-функции
будут давать одинаковое значение.
Гоша использует не Горнеровскую хеш-функцию c a = 1000 и m = 123987123.
В данной задаче необходимо использовать в качестве значений отдельных символов их коды в таблице ASCII.

Формат ввода
В задаче единственный тест без ввода.

Формат вывода
Отправьте две строки, по одной в строке. Строки могут состоять только из маленьких латинских букв
и не должны превышать в длину 1000 знаков каждая. Код отправлять не требуется.
Строки из примера использовать нельзя.
"""

import time
import string
import random

A_CONST = 1000
M_CONST = 123987123


def calculate_hash(a: int, m: int, s: str) -> int:
    """Horner's approach."""
    h = 0
    for c in s:
        h = (h * a + ord(c)) % m
    return h


def generate_breaking_strs(max_len=3) -> tuple[str, str, int, int, float]:
    """Brute force."""
    t0 = time.perf_counter()
    seen = {}
    i = 0
    while True:
        s = "".join(random.choices(string.ascii_lowercase, k=max_len))  # noqa: S311
        h = calculate_hash(A_CONST, M_CONST, s)
        if h in seen and seen[h] != s:
            return s, seen[h], h, i, time.perf_counter() - t0
        seen[h] = s
        i += 1
        if i % 1000 == 0:
            print(f"Checked {i} strings")


if __name__ == "__main__":
    s1, s2, h, i, elapsed = generate_breaking_strs(max_len=6)  # 6 is guaranteed to collide with these constants
    print(f"Colliding strings found: {s1} and {s2} hash to {h}. Confirming collision...")
    h1, h2 = (
        calculate_hash(
            A_CONST,
            M_CONST,
            s1,
        ),
        calculate_hash(
            A_CONST,
            M_CONST,
            s2,
        ),
    )
    assert h1 == h2
    print("Hash collision confirmed!")
    print(f"It took us {elapsed:.2f}s and {i} attempts to find colliding strings")
