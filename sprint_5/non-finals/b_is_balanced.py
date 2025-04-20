"""
Гоше очень понравилось слушать рассказ Тимофея про деревья. Особенно часть про сбалансированные деревья.
Он решил написать функцию, которая определяет, сбалансировано ли дерево.

Дерево считается сбалансированным, если левое и правое поддеревья каждой вершины отличаются по высоте не больше, чем на единицу.
Реализуйте функцию, определяющую, является ли дерево сбалансированным.
"""

import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> bool:
    def inner(root) -> tuple[bool, int]:
        if root is None:
            return True, 0

        is_left_balanced, height_left = inner(root.left)
        is_right_balanced, height_right = inner(root.right)
        height = 1 + max(height_left, height_right)
        is_current_balanced = abs(height_left - height_right) <= 1
        return is_left_balanced and is_right_balanced and is_current_balanced, height

    is_balanced, _ = inner(root)
    return is_balanced


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == "__main__":
    test()
