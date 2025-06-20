"""
В некоторых языках предложения пишутся и читаются не слева направо, а справа налево.
Вам под руку попался странный текст –— в нём обычный (слева направо) порядок букв в словах.
А вот сами слова идут в противоположном направлении.
Вам надо преобразовать текст так, чтобы слова в нём были написаны слева направо.

Формат ввода
На ввод подаётся строка, состоящая из слов, разделённых пробелами (один пробел между соседними словами).
Всего слов не более 1000, длина каждого из них —– от 1 до 100 символов.
Слова состоят из строчных букв английского алфавита.

Формат вывода
Выведите строку с обратным порядком слов в ней.
"""


def solution(text: str) -> str:
    return " ".join(text.split()[::-1])


if __name__ == "__main__":
    text = input()
    print(solution(text))
