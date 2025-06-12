"""
Алла придумала новый способ сравнивать две строки: чтобы сравнить строки a и b, в них надо оставить только те буквы,
которые в английском алфавите стоят на четных позициях. Затем полученные строки сравниваются по обычным правилам.
Помогите Алле реализовать новое сравнение строк.

Формат ввода
На вход подаются строки a и b по одной в строке. Обе строки состоят из маленьких латинских букв, не бывают пустыми
и не превосходят 105 символов в длину.

Формат вывода
Выведите -1, если a < b, 0, если a = b, и 1, если a > b.
"""

import string
from enum import Enum


class Comparison(Enum):
    LESS = -1
    EQUAL = 0
    GREATER = 1


def weird_str_compare(a: str, b: str) -> int:
    lower_ascii = {string.ascii_lowercase[i] for i in range(len(string.ascii_lowercase)) if (i + 1) % 2 == 0}
    trimmed_a = "".join(char for char in a if char in lower_ascii)
    trimmed_b = "".join(char for char in b if char in lower_ascii)
    if trimmed_a > trimmed_b:
        return Comparison.GREATER.value
    if trimmed_a < trimmed_b:
        return Comparison.LESS.value
    return Comparison.EQUAL.value


if __name__ == "__main__":
    a = input().strip()
    b = input().strip()
    print(weird_str_compare(a, b))
