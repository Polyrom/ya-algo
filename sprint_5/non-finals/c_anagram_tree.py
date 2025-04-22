import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> bool:
    if not root:
        return True

    def is_anagram(left, right) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False

        if left.value != right.value:
            return False

        return is_anagram(left.left, right.right) and is_anagram(left.right, right.left)

    return is_anagram(root.left, root.right)


def test():
    node1 = Node(3, None, None)
    node2 = Node(4, None, None)
    node3 = Node(4, None, None)
    node4 = Node(3, None, None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert solution(node7)


if __name__ == "__main__":
    test()
