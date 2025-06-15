"""
Напишите программу, которая будет заменять в тексте все вхождения строки s на строку t.
Гарантируется, что никакие два вхождения шаблона s не пересекаются друг с другом.

Формат ввода
В первой строке дан текст —– это строка из строчных букв английского алфавита, длина которой не превышает 10^6.
Во второй строке записан шаблон s, вхождения которого будут заменены.
В третьей строке дана строка t, которая будет заменять вхождения.
Обе строки s и t состоят из строчных букв английского алфавита, длина каждой строки не превосходит 10^5.
Размер итоговой строки не превосходит 2 * 10^6.

Формат вывода
В единственной строке выведите результат всех замен — текст, в котором все вхождения s заменены на t.

Пример
pingpong
ng
mpi

pimpipompi

aaa
a
ab

ababab
"""

SENTINEL = "#"


def prefix(s: str) -> list[int]:
    n = len(s)
    pr = [0] * n
    pr[0] = 0
    for i in range(1, n):
        k = pr[i - 1]
        while k > 0 and s[i] != s[k]:
            k = pr[k - 1]
        if s[i] == s[k]:
            k += 1
        pr[i] = k
    return pr


def search_and_replace(text: str, search: str, replace: str) -> str:
    pattern = search + SENTINEL + text
    prefix_vals = prefix(pattern)

    matches = []
    pattern_len = len(search)
    i = pattern_len + 1

    while i < len(pattern):
        if prefix_vals[i] == pattern_len:
            orig_pos = i - 2 * pattern_len
            matches.append(orig_pos)
        i += 1

    if not matches:
        return text

    result = []
    last_pos = 0
    for match_pos in matches:
        result.append(text[last_pos:match_pos])
        result.append(replace)
        last_pos = match_pos + pattern_len

    result.append(text[last_pos:])
    return "".join(result)


if __name__ == "__main__":
    text = input().strip()
    search = input().strip()
    replace = input().strip()

    print(search_and_replace(text, search, replace))
