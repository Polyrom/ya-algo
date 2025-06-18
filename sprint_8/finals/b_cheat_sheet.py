"""
Вася готовится к экзамену по алгоритмам и на всякий случай пишет шпаргалки.
Чтобы уместить на них как можно больше информации, он не разделяет слова пробелами.
В итоге получается одна очень длинная строка. Чтобы на самом экзамене из-за нервов не запутаться в прочитанном,
он просит вас написать программу, которая по этой длинной строке и набору допустимых слов определит,
можно ли разбить текст на отдельные слова из набора.

Более формально: дан текст T и набор строк s_1, ..., s_n.
Надо определить, представим ли T как s_k1 s_k2...s_kr, где k_i — индексы строк. Индексы могут повторяться.
Строка s_i может встречаться в разбиении текста T произвольное число раз. Можно использовать не все строки для разбиения.
Строки могут идти в любом порядке.

Формат ввода
В первой строке дан текст T, который надо разбить на слова. Длина T не превосходит 100100.
Текст состоит из строчных букв английского алфавита.
Во второй строке записано число допустимых к использованию слов 1 ≤ n ≤ 100.
В последующих n строках даны сами слова, состоящие из маленьких латинских букв. Длина каждого слова не превосходит 100.

Формат вывода
Выведите «YES», если текст можно разбить на слова из данного словаря, или «NO» в ином случае.

Пример
examiwillpasstheexam
5
will
pass
the
exam
i

YES
"""

from enum import Enum


class Result(Enum):
    YES = "YES"
    NO = "NO"


class Trie:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def insert(self, word: str):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.is_end_of_word = True


def can_segment_text(text: str, words: list[str]) -> bool:
    trie = Trie()
    for word in words:
        trie.insert(word)

    n = len(text)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(n):
        node = trie
        j = i
        while j < n and text[j] in node.children:
            node = node.children[text[j]]
            j += 1
            if node.is_end_of_word and dp[i]:
                dp[j] = True

    return dp[n]


if __name__ == "__main__":
    text = input().strip()
    words_num = int(input())
    words = [input().strip() for _ in range(words_num)]
    is_possible_to_segment = can_segment_text(text, words)
    print(Result.YES.value if is_possible_to_segment else Result.NO.value)
