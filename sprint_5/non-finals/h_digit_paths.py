"""
Вася и его друзья решили поиграть в игру. Дано дерево, в узлах которого записаны цифры от 0 до 9.
Таким образом, каждый путь от корня до листа содержит число, получившееся конкатенацией цифр пути.
Нужно найти сумму всех таких чисел в дереве.

Гарантируется, что ответ не превосходит 20 000.
"""

import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> int:
    total = 0

    if not root:
        return total

    def sum_paths(node, current_path) -> None:
        nonlocal total
        if not node:
            return
        current_path += str(node.value)
        if not node.left and not node.right:
            total += int(current_path)
            return
        sum_paths(node.left, current_path)
        sum_paths(node.right, current_path)


    sum_paths(root, "")
    return total


def test():
    node1 = Node(2, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(2, None, None)
    node5 = Node(1, node4, node3)

    assert solution(node5) == 275



if __name__ == "__main__":
    test()
