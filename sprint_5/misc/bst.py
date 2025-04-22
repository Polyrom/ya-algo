from typing import Self
from collections import deque


class Node:
    def __init__(self, value: int, left: Self | None = None, right: Self | None = None):
        self.value = value
        self.right = right
        self.left = left


class BinarySearchTree:
    def __init__(self, values: list[int] | None = None):
        self.root = None
        if values:
            for val in values:
                self.root = self.push(val)

    def push(self, value: int) -> Node:
        def inner(root: Node | None, value: int) -> Node:
            if root is None:
                return Node(value)
            if value < root.value:
                root.left = inner(root.left, value)
            elif value >= root.value:
                root.right = inner(root.right, value)
            return root

        return inner(self.root, value)

    def nodes_count(self) -> int:
        def inner(root: Node | None) -> int:
            if not root:
                return 0
            return 1 + inner(root.left) + inner(root.right)

        return inner(self.root)

    def is_bst(self) -> bool:
        if not self.root:
            return True

        def inner(node: Node | None, min_val: float | int = float("-inf"), max_val: float | int = float("inf")) -> bool:
            if not node:
                return True
            if node.value < min_val or node.value > max_val:
                return False
            return inner(node.left, min_val, node.value - 1) and inner(node.right, node.value + 1, max_val)

        return inner(self.root)

    def find_dfs(self, value: int) -> bool:
        if not self.root:
            return False

        def inner(root: Node | None, value: int) -> bool:
            if not root:
                return False
            if root.value == value:
                return True
            is_in_left = inner(root.left, value)
            is_in_right = inner(root.right, value)
            return is_in_left or is_in_right

        return inner(self.root, value)

    def find_bfs(self, value: int) -> bool:
        if not self.root:
            return False
        stack = deque([self.root])
        while stack:
            node = stack.popleft()
            if node.value == value:
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False


def test():
    bst = BinarySearchTree([-1, 4, 3, 15, 8, 5])
    assert bst.nodes_count() == 6, "❌ nodes_num"
    print("✅ nodes_num")

    assert bst.is_bst(), "❌ is_bst"
    print("✅ is_bst")

    assert bst.find_dfs(3), "❌ find_dfs #1"
    print("✅ find_dfs #1")
    assert bst.find_dfs(5), "❌ find_dfs #2"
    print("✅ find_dfs #2")
    assert not bst.find_dfs(146), "❌ find_dfs #3"
    print("✅ find_dfs #3")

    assert bst.find_bfs(15), "❌ find_bfs #1"
    print("✅ find_bfs #1")
    assert bst.find_bfs(8), "❌ find_bfs #2"
    print("✅ find_bfs #2")
    assert not bst.find_bfs(14), "❌ find_bfs #3"
    print("✅ find_bfs #3")

    print("✅ all tests passed!")


if __name__ == "__main__":
    test()
