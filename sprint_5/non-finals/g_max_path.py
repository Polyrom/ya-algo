"""
Тимофей устраивает соревнования по спортивному ориентированию в своём офисе. Схема офиса представлена в виде дерева.
Посещая каждый пункт, можно зарабатывать или терять очки. Если в узле записано положительное число,
это значение добавляется к текущему количеству очков участника. Если отрицательное —– очки вычитаются.
Если 0 –— их количество не меняется. Нужно определить, какое максимальное число очков можно заработать,
пройдя по пути из какого-то пункта A в какой-то (возможно, тот же) пункт B .

Путь не обязательно должен проходить через корень или содержать лист. Путь должен содержать по крайней мере один узел.
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
    max_sum = float("-inf")

    def dfs(node) -> int:
        nonlocal max_sum
        if not node:
            return 0
        max_left = max(dfs(node.left), 0)
        max_right = max(dfs(node.right), 0)
        current_sum = node.value + max_left + max_right
        max_sum = max(max_sum, current_sum)

        return node.value + max(max_left, max_right)

    dfs(root)
    return max_sum



def test():
    node1 = Node(5, None, None)
    node2 = Node(1, None, None)
    node3 = Node(-3, node2, node1)
    node4 = Node(2, None, None)
    node5 = Node(2, node4, node3)
    assert solution(node5) == 6


if __name__ == "__main__":
    test()
