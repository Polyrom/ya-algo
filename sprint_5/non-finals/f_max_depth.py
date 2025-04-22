"""
Алла хочет побывать на разных островах архипелага Алгосы. Она составила карту.
Карта представлена в виде дерева: корень обозначает центр архипелага, узлы –— другие острова.
А листья —– это дальние острова, на которые Алла хочет попасть.

Помогите Алле определить максимальное число островов, через которые ей нужно пройти для совершения
одной поездки от стартового острова до места назначения, включая начальный и конечный пункты.
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
    if not root:
        return 0
    left_depth = solution(root.left)
    right_depth = solution(root.right)
    return max(left_depth, right_depth) + 1


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5) == 3


if __name__ == "__main__":
    test()
