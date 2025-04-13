from typing import Self, Callable


class Node:
    def __init__(self, value: int, children: list[Self] | None = None):
        self.value = value
        self.children = children

    def __str__(self) -> str:
        children_values = None
        if self.children:
            children_values = [f"Node({ch.value})" for ch in self.children]
        return f"Node(value={self.value}, children={children_values})"


def inorder(node: Node) -> None:
    print(node)
    if node.children:
        for child in node.children:
            inorder(child)


def reverse(node: Node) -> None:
    if node.children:
        for child in node.children:
            reverse(child)
    print(node)


def test(implementations: tuple[Callable]):
    """
            * 5
          /      \
        *3        *8
       /  \      /  \
     *1   *4   *6   *10
                      \
                       *11
    """
    node9 = Node(9, None)
    node8 = Node(11, None)
    node7 = Node(10, [node9, node8])
    node6 = Node(6, None)
    node1 = Node(1, None)
    node2 = Node(4, None)
    node3 = Node(3, [node1, node2])
    node4 = Node(8, [node6, node7])
    node5 = Node(5, [node3, node4])

    for impl in implementations:
        print("=== ===")
        impl(node5)


if __name__ == "__main__":
    test((inorder, reverse))
