"""
Гоша измерял температуру воздуха n дней подряд. В результате у него получился некоторый временной ряд.
Теперь он хочет посмотреть, как часто встречается некоторый шаблон в получившейся последовательности.
Однако температура — вещь относительная, поэтому Гоша решил, что при поиске шаблона длины m (a1, a2, ..., am)
стоит также рассматривать сдвинутые на константу вхождения.
Это значит, что если для некоторого числа c в исходной последовательности нашёлся
участок вида (a1 + c, a2 + c, ... , am + c), то он тоже считается вхождением шаблона (a1, a2, ..., am).

По заданной последовательности измерений X и шаблону A=(a1, a2, ..., am) определите все вхождения A в X,
допускающие сдвиг на константу.

Формат ввода

В первой строке дано количество сделанных измерений n — натуральное число, не превышающее 104.
Во второй строке через пробел записаны n целых чисел xi, 0 ≤ xi ≤ 103 –— результаты измерений.
В третьей строке дано натуральное число m –— длина искомого шаблона, 1≤ m ≤ n.
В четвёртой строке даны m целых чисел ai — элементы шаблона, 0 ≤ ai ≤ 103.

Формат вывода
Выведите через пробел в порядке возрастания все позиции, на которых начинаются вхождения
шаблона A в последовательность X. Нумерация позиций начинается с единицы.

Примеры:
9
3 9 1 2 5 10 9 1 7
2
4 10

1 8
"""


def find(orig: list[int], pattern: list[int], start: int = 0) -> int | None:
    if len(orig) < len(pattern):
        return None
    for pos in range(start, len(orig) - len(pattern) + 1):
        match = True
        for offset in range(len(pattern) - 1):
            diff_pattern = pattern[offset + 1] - pattern[offset]
            diff_orig = orig[pos + offset + 1] - orig[pos + offset]
            if diff_pattern != diff_orig:
                match = False
                break
        if match:
            return pos
    return None


def solution(temps: list[int], seq: list[int]) -> list[int]:
    occurs = []
    start = 0
    while len(temps) - start >= len(seq):
        pos = find(temps, seq, start)
        if pos is not None:
            occurs.append(pos + 1)
            start = pos + 1
            continue
        start += 1

    return occurs


if __name__ == "__main__":
    _ = input()
    temps = list(map(int, input().strip().split()))
    _ = input()
    seq = list(map(int, input().strip().split()))
    res = solution(temps, seq)
    print(" ".join(map(str, res)))
