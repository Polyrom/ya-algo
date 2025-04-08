"""
https://contest.yandex.ru/contest/24414/run-report/136372718/

-- ПРИНЦИП РАБОТЫ --
Реализация использует метод цепочек для разрешения коллизий.
- Инициализация -
Создаётся массив items фиксированного размера SIZE = 1_000_003 (простое число > 10^6).
Каждый элемент массива — голова связного списка.

- Операции -
put(key, value):
Вычисляет bucket = key % SIZE.
Ищет ключ в цепочке items[bucket].
Если ключ найден, обновляет значение, иначе добавляет новый Node в начало цепочки.

get(key):
Вычисляет bucket и ищет ключ в цепочке.
Возвращает value или None.

delete(key):
Удаляет узел с ключом key из цепочки, сохраняя её целостность.


-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Размер таблицы SIZE — простое число > 10^6, что минимизирует коллизии.

Т.к. по условию ключи хэш-таблицы - целые числа, отдельного этапа хэширования нет, хэш-функция совмещена с
индекс-функцией.

Метод цепочек гарантирует, что все ключи с одинаковым хэшем хранятся в одном связном списке.
Операции put/get/delete корректно обрабатывают цепочки любой длины.


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Хэш-функция, совмещенная с индекс-функцией key % SIZE вычисляется за O(1).
При равномерном распределении ключей длина цепочек ≈ n/m (где n — число ключей, m — размер таблицы).
По условию n <= 10^6, m = 1_000_003, т.е. средняя длина цепочки ≈ 1.


-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Фиксированный массив items[SIZE] → O(m).
Узлы Node → O(n).
Итого: O(n + m) линейная.
"""

from typing import Self


class Node:
    def __init__(self, key: int, value: int, next_: Self | None = None):
        self.key = key
        self.value = value
        self.next = next_


class IntHashMap:
    SIZE = 1_000_003

    def __init__(self) -> None:
        self.items: list[Node | None] = [None] * self.SIZE

    @staticmethod
    def __get_from_bucket(node: Node | None, key: int) -> Node | None:
        while node:
            if node.key == key:
                return node
            node = node.next
        return None

    def put(self, key: int, value: int) -> None:
        bucket = key % self.SIZE
        node = self.__get_from_bucket(self.items[bucket], key)
        if node:
            node.value = value
        else:
            new_node = Node(key, value, None)
            new_node.next = self.items[bucket]
            self.items[bucket] = new_node

    def get(self, key) -> int | None:
        bucket = key % self.SIZE
        node = self.__get_from_bucket(self.items[bucket], key)
        if not node:
            return None
        return node.value

    def delete(self, key) -> int | None:
        bucket = key % self.SIZE
        node = self.items[bucket]
        prev_node = None
        while node:
            if node.key == key:
                if not prev_node:
                    self.items[bucket] = None
                    return node.value
                prev_node.next = node.next
                return node.value
            prev_node = node
            node = node.next
        return None


def read_input() -> list[tuple[str, int, int | None]]:
    ops = []
    inputs = int(input())
    for _ in range(inputs):
        op_raw = input()
        op_split = op_raw.strip().split()
        if len(op_split) > 2:
            ops.append((op_split[0], int(op_split[1]), int(op_split[2])))
        else:
            ops.append((op_split[0], int(op_split[1])))
    return ops


if __name__ == "__main__":
    ops = read_input()
    hash_map = IntHashMap()
    for op in ops:
        res = getattr(hash_map, op[0])(op[1], op[2]) if len(op) > 2 else getattr(hash_map, op[0])(op[1])
        if op[0] != "put":
            print(res)
