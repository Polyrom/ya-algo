from typing import Callable, Self


class Node:
    def __init__(self, value: int, left: Self | None = None, right: Self | None = None):
        self.value = value
        self.right = right
        self.left = left


def is_bst_recursive(root: Node) -> bool:
    def validate(node: Node, low=float("-inf"), high=float("inf")) -> bool:
        if not node:
            return True
        if not (low < node.value < high):
            return False
        return validate(node.left, low, node.value) and validate(node.right, node.value, high)

    return validate(root)


def is_bst_iterative(root: Node) -> bool:
    stack = [(root, float("-inf"), float("inf"))]
    while stack:
        node, low, high = stack.pop()
        if not (low < node.value < high):
            return False
        if node.left:
            stack.append((node.left, low, node.value))
        if node.right:
            stack.append((node.right, node.value, high))
    return True


def is_bst_inorder(root: Node) -> bool:
    prev = float("-inf")
    stack = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        if node.value <= prev:
            return False
        prev = node.value
        node = node.right
    return True


def test(implementations: tuple[Callable]):
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    for i, impl in enumerate(implementations, 1):
        assert impl(node5)
        print(f"test {i}.1 passed!")
        node2.value = 5
        assert not impl(node5)
        print(f"test {i}.2 passed!")
        node2.value = 4


if __name__ == "__main__":
    test((is_bst_recursive, is_bst_iterative, is_bst_inorder))
