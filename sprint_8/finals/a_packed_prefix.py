"""
Вам даны строки в запакованном виде. Определим запакованную строку (ЗС) рекурсивно.
Строка, состоящая только из строчных букв английского алфавита является ЗС.
Если A и B —– корректные ЗС, то и AB является ЗС.
Если A —– ЗС, а n — однозначное натуральное число, то n[A] тоже ЗС.
При этом запись n[A] означает, что при распаковке строка A записывается подряд n раз.
Найдите наибольший общий префикс распакованных строк и выведите его (в распакованном виде).

Формат ввода
В первой строке записано число n (1≤n≤1000) –— число строк.

Далее в n строках записаны запакованные строки. Гарантируется, что эти строки корректны,
то есть удовлетворяют указанному рекурсивному определению.
Длина строк после распаковки не превосходит 10^5.

Формат вывода
Выведите наибольший общий префикс распакованных строк.

Пример
3
2[a]2[ab]
3[a]2[r2[t]]
a2[aa3[b]]

aaa
"""

from enum import Enum
from typing import Generator


class SquareBrackets(str, Enum):
    OPEN = "["
    CLOSE = "]"


def unpack_string(s: str) -> Generator[str, None, None]:
    stack = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            stack.append((num, i))
        elif s[i] == SquareBrackets.OPEN:
            repeat, _ = stack.pop()
            stack.append((repeat, i + 1, []))
            i += 1
        elif s[i] == SquareBrackets.CLOSE:
            repeat, _, buf = stack.pop()
            expanded = buf * repeat
            if stack:
                stack[-1][2].extend(expanded)
            else:
                for c in expanded:
                    yield c
            i += 1
        else:
            if stack:
                stack[-1][2].append(s[i])
            else:
                yield s[i]
            i += 1


def longest_common_prefix_packed(strings: list[str]) -> str:
    iterators = [unpack_string(s) for s in strings]
    prefix = []
    prefix_found = False

    while not prefix_found:
        try:
            chars = [next(it) for it in iterators]
            if all(c == chars[0] for c in chars):
                prefix.append(chars[0])
            else:
                prefix_found = True
        except StopIteration:
            return "".join(prefix)

    return "".join(prefix)


def read_input() -> list[str]:
    str_count = int(input())
    return [input().strip() for _ in range(str_count)]


if __name__ == "__main__":
    strings = read_input()
    print(longest_common_prefix_packed(strings))
