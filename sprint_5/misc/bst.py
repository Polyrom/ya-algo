from typing import Self


class Node:
    def __init__(self, value: int, left: Self | None = None, right: Self | None = None):
        self.value = value
        self.right = right
        self.left = left


def bst_push(root: Node | None, value: int) -> Node:
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = bst_push(root.left, value)
    elif value >= root.value:
        root.right = bst_push(root.right, value)
    return root


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)
    _ = bst_push(node5, 15)
    assert node5.right and node5.right.right and node5.right.right.value == 15


if __name__ == "__main__":
    test()
