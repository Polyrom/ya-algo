"""
У Риты была строка s, Гоша подарил ей на 8 марта ещё n других строк t_i, 1 ≤ i ≤ n.
Теперь Рита думает, куда их лучше поставить.
Один из вариантов —– расположить подаренные строки внутри имеющейся строки s, поставив строку t_i сразу
после символа строки s с номером k_i (в частности, если k_i=0, то строка вставляется в самое начало s).
Помогите Рите и определите, какая строка получится после вставки в s всех подаренных Гошей строк.

Формат ввода
В первой строке дана строка s. Строка состоит из строчных букв английского алфавита, не бывает пустой
и её длина не превышает 105 символов.
Во второй строке записано количество подаренных строк — натуральное число n, 1 ≤ n ≤ 105.
В каждой из следующих n строк через пробел записаны пары t_i и k_i.
Строка t_i состоит из маленьких латинских букв и не бывает пустой.
k_i — целое число, лежащее в диапазоне от 0 до |s|. Все числа k_i уникальны.
Гарантируется, что суммарная длина всех строк ti не превосходит 105.

Формат вывода
Выведите получившуюся в результате вставок строку.
"""

from collections import defaultdict

# Time: O(n) Space: O(n)
# Key approach: keep an insertions hash map to store arrays to be inserted, then iterate over the original string once
# and extend the string (stored as an array) with new arrays.
def solution(string: str, pairs: list[tuple[str, int]]) -> str:
    insertions = defaultdict(list)
    for t, k in pairs:
        insertions[k].append(t)

    result = []

    if 0 in insertions:
        result.extend(insertions[0])

    for i in range(len(string)):
        result.append(string[i])
        if i + 1 in insertions:
            result.extend(insertions[i + 1])

    return "".join(result)


def read_input() -> tuple[str, list[tuple[str, int]]]:
    string = input().strip()
    pairs_num = int(input())
    pairs = []
    for _ in range(pairs_num):
        pair = input().strip().split()
        pairs.append((pair[0], int(pair[1])))
    return string, pairs


if __name__ == "__main__":
    string, pairs = read_input()
    print(solution(string, pairs))
