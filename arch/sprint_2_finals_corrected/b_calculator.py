# https://contest.yandex.ru/contest/22781/run-report/134902686/
#
# -- ПРИНЦИП РАБОТЫ --
# Задача реализована с использованием стека. Согласно описанию задачи, элементы выражения обрабатываются последовательно.
# Если элемент является операндом, он помещается в стек. Если элемент - оператор, из стека извлекаются элементы n - 2 
# (левый оператор) и n - 1 (правый оператор), к которым применяется текущий оператор. Результат выражения помещается в стек.
#
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# Стек - очередь LIFO. Т.к. по условию задачи нам гарантировано, что выражение всегда будет корректным
# и полным, а все операции, указанные в задаче, являются бинарными, то достаточно помещать операнды в стек, 
# и при встрече оператора применять его к двум элементам на вершине стека.
#
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# O(n), где n - количество элементов в выражении, поданном на вход. Каждый элемент обрабатывается один раз 
# в единственном цикле.
#
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Дополнительная память выделяется под стек, в котором хранятся операнды выражения.
# Т.о. пространственная сложность составляет O(n - k), где n - количество элементов в выражении, 
# а k - количество операторов в выражении. Т.е. общая пространственная сложность составляет O(n).


import operator

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}


class Stack:
    def __init__(self) -> None:
        self.items: list[int] = []
        self.size = 0

    def pop(self) -> int | None:
        if self.size == 0:
            return None
        item = self.items.pop()
        self.size -= 1
        return item

    def push(self, item: int) -> None:
        self.items.append(item)
        self.size += 1


def calculate(expr: list[str]) -> int | None:
    s = Stack()
    for op in expr:
        if op in OPERATORS:
            right = s.pop()
            left = s.pop()
            res = OPERATORS[op](left, right)
            s.push(res)
        else:
            s.push(int(op))
    return s.pop()


def read_input() -> list[str]:
    expr = input()
    return expr.strip().split()


if __name__ == "__main__":
    expr = read_input()
    print(calculate(expr))
